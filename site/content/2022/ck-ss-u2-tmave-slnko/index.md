---
title: Tmavé Slnko
year: 2022
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú2
weight: 5002
hasSolution: true
source: ZAO:I_Zadania/01_NebMech/01_SS_FI.tex
years:
- '2022'
rounds:
- Celoštátne kolo
categories:
- SŠ
types:
- Teória
topics:
- Nebeská mechanika
collection: ZAO
---

## Zadanie

Tmavá hmota je hypotetická látka, ktorá takmer neinteraguje s normálnom hmotou. Jediný spôsob interakcie je gravitácia (podľa klasického Newtonovho gravitačného zákona). Predstavme si, že by bolo naše Slnko z tmavej hmoty. Uvažujme guľu (tmavé Slnko) kompletne vyrobenú z tmavej hmoty v ktorej je hmotnosť rozložená podľa funkcie 

$$
M(r)=M_\Sun\frac{r}{R_\Sun} \,,
$$

 kde $M(r)$ je hmotnosť koncentrickej gule s polomerom $r$ (guľa, ktorá má stred v strede tmavého Slnka). Keďže rozloženie hmoty je sféricky symetrické, tak (podľa Gaussovho zákona) na objekt vnútri tmavého Slnka ($r<R_\Sun$) pôsobí gravitácia ekvivalentná gravitácii hmoty uloženej vo sfére pod objektom, teda gravitácia gule s polomerom $r$.

Predstavme si, že vnútri tmavého Slnka obieha sonda na kruhovej dráhe s polomerom $r=R_\Sun /2$.

**Úlohy:**

<ol type="a">

<li>

Aká je obehová rýchlosť $v$ sondy?

</li>

<li>

Aká je perióda $T$ obehu sondy?

</li>

<li>

Prežil by človek zdanlivé zrýchlenie $a$ na palube sondy?

</li>

</ol>

Teraz si predstavme, že sonda zapla motory v radiálnom smere, a začala sa postupným špirálovaním hýbať k povrchu Slnka. Pri tom si udržiavala konštantnú radiálnu rýchlosť $v_\mathrm{R}=1\,\mathrm{km}\,{\mathrm{s}}^{-1}$.

<ol type="a" start="4">

<li>

Ako dlho (čas $t$) bude sonda putovať k povrchu?

</li>

<li>

Akú rýchlosť $v_\mathrm{p}$ bude mať sonda v momente kedy dosiahne povrch?

</li>

</ol>

V momente ako sonda dosiahla povrch Slnka, tak vypla motory. Stále jej však ostala radiálna rýchlosť $v_\mathrm{R}$, takže vyletela nad povrch, chvíľu letela nad ním, a potom bola gravitáciou stiahnutá naspäť do Tmavého Slnka.

<ol type="a" start="6">

<li>

Aká je maximálna výška $h$ nad povrchom, ktorú sonda dosiahne?

</li>

<li>

Ako dlho (čas $\Delta t$) sa sonda udrží nad povrchom?

</li>

</ol>

**Pomôcka:**

Všimnite si, že výška $h\ll R$, teda gravitačnú silu nad povrchom môžete aproximovať konštantnou hodnotou $F_\mathrm{g} (r=R)$ pre $r \in (R, R+h)$.

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Na kruhovej dráhe musí platiť rovnosť gravitačnej sily $F_\textrm{g}$ a odstredivej sily $F_\textrm{o}$. Zadanie nám napovedá dôležitú vec: na objekt vnútri tmavého Slnka ($r < R_\Sun$) pôsobí gravitácia ekvivalentná gravitácii hmoty uloženej vo sfére pod objektom, teda gravitácia gule s polomerom $r$. Preto 

$$
F_\textrm{g}=\frac{GmM(r)}{r^2}=\frac{GmM_\Sun \frac{r}{R_\Sun}}{r^2}=\frac{GmM_\Sun}{rR_\Sun} \, , \tag{1}
$$

 

$$
F_\textrm{o}=\frac{mv^2}{r} \, . \tag{2}
$$

 Z rovnosti gravitačnej a odstredivej sily dostávame vyjadrenie pre rýchlosť $v$ 

$$
F_\textrm{g}=F_\textrm{o} \, , \tag{3}
$$

 

$$
\frac{GmM_\Sun}{rR_\Sun}=\frac{mv^2}{r} \, , \tag{4}
$$

 

$$
v=\sqrt{\frac{GM_\Sun}{R_\Sun}}=\sqrt{\frac{6{,}673 \cdot 10^{-11}\cdot1{,}9891 \cdot 10^{30}}{6{,}955 \cdot 10^{8}}}=4{,}37 \cdot 10^{5}\,\mathrm{m}\,{\mathrm{s}}^{-1}=437\,\mathrm{km}\,{\mathrm{s}}^{-1} \, . \tag{5}
$$

 Všimnime si, že táto rýchlosť nie je závislá na vzdialenosti $r$. Toto bude dôležité neskôr.

</li>

<li>

Perióda obehu je čas za ktorý sonda prejde kruhovú dráhu o dĺžke $2\pi r$, kde $r=R_\Sun /2$

</li>

</ol>

$$
T=\frac{\pi R_\Sun}{v}=\frac{\pi R_\Sun}{\sqrt{\frac{GM_\Sun}{R_\Sun}}}=\pi \sqrt{\frac{R_\Sun ^3}{GM_\Sun}}=\pi\cdot\sqrt{\frac{(6{,}955 \cdot 10^{8})^3}{6{,}673 \cdot 10^{-11}\cdot1{,}9891 \cdot 10^{30}}}=5003\,\mathrm{s}=1{,}39\,\mathrm{h} \, . \tag{6}
$$

<ol type="a" start="3">

<li>

V zadaní (a) sme vraveli, že platí rovnosť gravitačnej a odstredivej sily. To znamená, že výslednica síl pôsobiaca na sondu (a človeka v nej) je nulová. No a keďže je nulová sila, tak aj zrýchlenie 

$$
a=0\,\mathrm{m}\,{\mathrm{s}}^{-2} \, . \tag{7}
$$

 Je to obdobná situácia ako na medzinárodnej vesmírnej stanici – na sonde panuje stav beztiaže. A ten (ako je všeobecne známe) ľudia prežiť vedia.

</li>

<li>

Sonda si udržiava konštantnú rýchlosť $v_\mathrm{R}$ v radiálnom smere. K povrchu potrebuje precestovať vzdialenosť $R_\Sun/2$, čo jej bude trvať čas 

$$
t = \frac{R_\Sun/2}{v_\mathrm{R}} = \frac{R_\Sun}{2 v_\mathrm{R}} = \frac{6{,}955 \cdot 10^{5}}{2\cdot 1}=348\,000\,\mathrm{s}=4{,}03\,\mathrm{dňa} \, . \tag{8}
$$

</li>

<li>

V (a) sme zistili, že obehová, respektíve tangenciálna, rýchlosť sondy je konštantná. To znamená, že na povrchu bude stále rovná $v=437\,\mathrm{km}\,{\mathrm{s}}^{-1}$. V radiálnom smere motory zabezpečujú konštantnú rýchlosť $v_\mathrm{R} = 1\,\mathrm{km}\,{\mathrm{s}}^{-1}$. Výsledná rýchlosť $v_\textrm{p}$ je zložením $v$ a $v_\textrm{R}$ podľa Pytagorovej vety (keďže rýchlosti sú na seba kolmé). Avšak vidíme, že $v\gg v_\textrm{R}$, a preto v rámci presnosti na 3 platné číslice 

$$
v_\textrm{p}=\sqrt{v^2+v_\textrm{R}^2}\approx v =437\,\mathrm{km}\,{\mathrm{s}}^{-1} \, . \tag{9}
$$

</li>

<li>

Keďže už ďalej nepôsobia motory, tak môžeme využiť zákon zachovania energie (takisto by sme to vedeli rátať pomocou zákonu zachovania momentu hybnosti). Energia sondy na povrchu musí byť rovná energii sondy v jej najvyššom bode dráhy nad tmavým Slnkom. Dôležité je si uvedomiť, že počas pohybu sondy nad povrchom sa nemení tangenciálna zložka (keďže v tomto smere nepôsobí gravitačná sila). Preto rýchlosť sondy vo výške $h$ nad povrchom je rovná $v$. Rýchlosť na povrchu $v_\textrm{p}$ sme už zrátali (treba si dať pozor, že v tomto prípade nemôžeme aproximovať $v_\textrm{p}\approx v$, keďže by sme dostali $h=0$). Zákon zachovania energie nám hovorí 

$$
\frac{1}{2}mv_\textrm{p}^2-\frac{GmM_\Sun}{R_\Sun}=\frac{1}{2}mv^2-\frac{GmM_\Sun}{R_\Sun+h} \, . \tag{10}
$$

Po dosadení $v_\textrm{p}^2=v^2+v_\textrm{R}^2$ a úprave získame $h$. 

$$
\begin{align*}
\frac{1}{2}mv^2+\frac{1}{2}v_\textrm{R}^2-\frac{GM_\Sun}{R_\Sun} &= \frac{1}{2}mv^2-\frac{GM_\Sun}{R_\Sun+h} \, , \tag{11}\\
\frac{v_\textrm{R}^2R_\Sun-2GM_\Sun}{2R_\Sun} &= -\frac{GM_\Sun}{R_\Sun+h} \, , \tag{12}\\
R_\Sun+h &= \frac{2GM_\Sun R_\Sun}{2GM_\Sun - v_\textrm{R}^2R_\Sun} \, , \tag{13}\\
h &= \frac{2GM_\Sun }{2GM_\Sun/R_\Sun - v_\textrm{R}^2} - R_\Sun \, . \tag{14}\end{align*}
$$

Po dosadení číselných hodnôt dostávame výsledok 

$$
h = \frac{2 \cdot 6{,}674 \cdot 10^{-11} \cdot 1{,}989 \cdot 10^{30}}{2 \cdot 6{,}674 \cdot 10^{-11} \cdot 1{,}989 \cdot 10^{30} / 6{,}955 \cdot 10^{8} - 1000^2 \cdot } - 6{,}955 \cdot 10^{8} = 1{,}82\,\mathrm{km} \, . \tag{15}
$$

**Poznámka:**\
Všeobecné vyjadrenia môžeme skrášliť využitím aproximácie $v \gg v_\textrm{R}$, keďže $437\,\mathrm{km}\,{\mathrm{s}}^{-1} \gg 1\,\mathrm{km}\,{\mathrm{s}}^{-1}$. Ak si spomenieme na vyjadrenie $v=\sqrt{GM_\Sun / R_\Sun}$ z (a), tak 

$$
v^2 = \frac{GM_\Sun}{R_\Sun} \gg v_\mathrm{R}^2 \, . \tag{16}
$$

 Nemôžeme však len hneď zjednodušiť menovateľ rovnice (14) ako 

$$
\frac{2GM_\Sun}{R_\Sun} - v_\textrm{R}^2 \approx \frac{2GM_\Sun}{R_\Sun} \, , \tag{17}
$$

 pretože by to bola príliš veľká aproximácia a dostali by sme 

$$
h \approx \frac{2GM_\Sun }{2GM_\Sun/R_\Sun} - R_\Sun = R_\Sun - R_\Sun = 0 \, , \tag{18}
$$

 teda nulovú výšku.

Namiesto toho dáme najskôr v rovnici (14) dokopy zlomok a mínus $R_\Sun$ a potom aproximujeme. 

$$
\begin{align*}
    h &= \frac{2GM_\Sun }{2GM_\Sun/R_\Sun - v_\textrm{R}^2} - R_\Sun =
    \frac{2GM_\Sun - \left( 2GM_\Sun/R_\Sun - v_\textrm{R}^2 \right) R_\Sun }{2GM_\Sun/R_\Sun - v_\textrm{R}^2} = \tag{19}\\
    &= \frac{2GM_\Sun - 2GM_\Sun + v_\textrm{R}^2 R_\Sun }{2GM_\Sun/R_\Sun - v_\textrm{R}^2} = 
    \frac{v_\textrm{R}^2 R_\Sun }{2GM_\Sun/R_\Sun - v_\textrm{R}^2} \approx
    \frac{v_\textrm{R}^2 R_\Sun }{2GM_\Sun/R_\Sun}
    = \frac{v_\textrm{R}^2 R_\Sun^2 }{2GM_\Sun} \, . \tag{20}\end{align*}
$$

 Výsledok sa líši o $1\,\mathrm{m}\,{\mathrm{s}}^{-1}$, čo je mimo presnosti na 3 platné cifry.

</li>

<li>

Ako pomôcka napovedá, všimnime si že výška $h\ll R$, teda sonda vyletí nad povrch iba nepatrne a takmer okamžite sa ponorí naspäť do tmavého Slnka. To znamená, že gravitačnú silu môžeme aproximovať ako konštantnú, pretože z pohľadu sondy blízko povrchu sa tmavé Slnko javí ako nekonečná rovina (obdobne sa nám na povrchu Zeme (a tesne nad ním) javí, že sme v homogénnom gravitačnom poli). Počas pohybu sondy sa nezmení tangenciálna zložka rýchlosti, a preto stačí vyšetriť pohyb v radiálnom smere.

No a to nie je nič iné ako zvislý vrh so zrýchlením $a = F_\mathrm{g} / m$

</li>

</ol>

$$
h=\frac{1}{2}a\left(\frac{\Delta t}{2}\right)^2 = \frac{1}{2} \frac{F_\mathrm{g}}{m} \left(\frac{\Delta t}{2}\right)^2 = \frac{1}{2} \frac{G M_\Sun}{R_\Sun^2} \left(\frac{\Delta t}{2}\right)^2 \, . \tag{21}
$$

 Vyjadríme $\Delta t$ a dopočítame (využijeme hodnotu výšky $h$ z (f)) 

$$
\Delta t = 2R_\Sun\sqrt{\frac{2h}{GM_\Sun}} = 2 \cdot 6{,}955 \cdot 10^{8} \sqrt{ \frac{2 \cdot 1820}{6{,}674 \cdot 10^{-11} \cdot 1{,}989 \cdot 10^{30}} } = 7{,}28\,\mathrm{s} \, . \tag{22}
$$

**Poznámka:**\
Využitím vzťahu pre $h$ odvodeného v minulej poznámke vieme approximovať (22) ako 

$$
\Delta t = 2R_\Sun\sqrt{\frac{2h}{GM_\Sun}} \approx
    \Delta t = 2R_\Sun\sqrt{\frac{2\frac{v_\textrm{R}^2 R_\Sun^2 }{2GM_\Sun}}{GM_\Sun}} =
    \Delta t = 2R_\Sun\sqrt{\frac{v_\textrm{R}^2 R_\Sun^2 }{G^2 M_\Sun^2}} =
    \Delta t = 2 \frac{v_\textrm{R} R_\Sun^2}{G M_\Sun} \, . \tag{23}
$$

 Výsledok sa líši o $0{,}01\,\mathrm{s}$, čo je prijateľná presnosť.

</details>
