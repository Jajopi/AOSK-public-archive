-- Pandoc Lua filter: make GitHub-flavoured Markdown output keep what plain Markdown cannot express.
-- Lists keep their (a)/(i)/1. labels and start numbers, figures keep captions and widths.
-- Math never reaches pandoc (it is replaced by placeholders before and restored after).

local function raw(s) return pandoc.RawBlock('html', s) end

local level = 0
local function list_type(style, lvl)
  if style == 'LowerAlpha' or style == 'UpperAlpha' then return style == 'LowerAlpha' and 'a' or 'A' end
  if style == 'LowerRoman' or style == 'UpperRoman' then return style == 'LowerRoman' and 'i' or 'I' end
  if style == 'Decimal' then return '1' end
  -- DefaultStyle: (a) at top level, i. nested, 1. deeper (AO convention)
  if lvl == 1 then return 'a' elseif lvl == 2 then return 'i' end
  return '1'
end

local function walk_list(el)
  level = level + 1
  local items = {}
  for i, item in ipairs(el.content) do
    items[i] = pandoc.walk_block(pandoc.Div(item), { traverse = 'topdown', OrderedList = function(e) local r = walk_list(e); return r, false end }).content
  end
  local t = list_type(el.listAttributes.style, level)
  local start = el.listAttributes.start or 1
  level = level - 1
  local out = { raw(string.format('<ol type="%s"%s>', t, start ~= 1 and (' start="' .. start .. '"') or '')) }
  for _, blocks in ipairs(items) do
    table.insert(out, raw('<li>'))
    for _, b in ipairs(blocks) do table.insert(out, b) end
    table.insert(out, raw('</li>'))
  end
  table.insert(out, raw('</ol>'))
  return out, false
end

local function img_html(img)
  local style = ''
  local w, h = img.attributes['width'], img.attributes['height']
  if w then style = string.format(' style="width:%s"', w)
  elseif h then style = string.format(' style="height:%s;width:auto"', h) end
  return string.format('<img src="%s" alt="obrázok" loading="lazy"%s>', img.src, style)
end

local function collect_images(blocks)
  local imgs = {}
  pandoc.walk_block(pandoc.Div(blocks), { Image = function(i) table.insert(imgs, i) end })
  return imgs
end

function Figure(el)
  local out = { raw('<figure>') }
  local html = {}
  for _, i in ipairs(collect_images(el.content)) do table.insert(html, img_html(i)) end
  table.insert(out, raw('<div class="fig-images">' .. table.concat(html, '') .. '</div>'))
  local cap = el.caption and el.caption.long or {}
  if #cap > 0 then
    table.insert(out, raw('<figcaption>'))
    for _, b in ipairs(cap) do table.insert(out, b) end
    table.insert(out, raw('</figcaption>'))
  end
  table.insert(out, raw('</figure>'))
  return out
end

function Table(el)
  -- caption as a paragraph above the table (GFM tables have no captions)
  local cap = el.caption and el.caption.long or {}
  if #cap == 0 then return el end
  local out = { raw('<div class="table-caption">') }
  for _, b in ipairs(cap) do table.insert(out, b) end
  table.insert(out, raw('</div>'))
  el.caption = pandoc.Caption({})
  table.insert(out, el)
  return out
end

function Header(el)
  -- headings inside problem text become small run-in titles
  return pandoc.Para({ pandoc.Strong(el.content) })
end

function Div(el)
  return el.content
end

return {
  { Figure = Figure, Table = Table, Header = Header, Div = Div },
  { traverse = 'topdown', OrderedList = walk_list },
}
