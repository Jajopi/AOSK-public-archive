---
title: Nočný snack
year: 2026
round: RK
roundName: Regionálne kolo
category: SŠ
type: teoria
typeName: Teória
label: T2
weight: 1302
points: '80'
authors:
- Jana Švrčková
hasSolution: true
source: 2026:.SS/.RK/Nocny-snack.tex
rocniky:
- '2026'
kola:
- Regionálne kolo
kategorie:
- SŠ
typy:
- Teória
tagy:
- Nezaradené
---

## Zadanie

Je možné uvariť hrniec ryže v ohnisku Nordic Optical Telescope (NOT), ak ho namierime na Mesiac v splne? Aj nad takýmito filozofickými otázkami sa zamýšľala estónska astronómka Anni počas dlhých nocí na observatóriu. V tomto príklade z tejto filozofickej otázky spravíte fyzikálnu a pokúsite sa zistiť, či si astronómovia naozaj v prípade núdze môžu v ďalekohľade pripraviť večeru.

Vyriešte nasledujúcu sériu podúloh, ktorá vás privedie k vytúženej odpovedi:

<ol type="a">

<li>

<span class="body">[15 b]</span> Vypočítajte, aký tok dopadá z Mesiaca v splne na vrchol zemskej atmosféry vo $V$ filtri. Jasnosti objektov v tomto filtri môžete považovať za rovnaké, aké zodpovedajú vizuálnej jasnosti. Zo Slnka dopadá na zemskú atmosféru vo $V$ filtri tok $F_\Sun = 1240\,\mathrm{W}{\mathrm{m}}^{-2}$.

</li>

<li>

<span class="body">[20 b]</span> Kvôli prechodu svetla zemskou atmosférou sa zoslabuje svetlo objektov. Čím hrubšou vrstvou atmosféry svetlo prechádza, tým viac sa zoslabí. Z toho dôvodu si na varenie ryže vyberieme noc, kedy sa Mesiac nachádza v najbližšej možnej polohe k zenitu. Vypočítajte minimálnu možnú zenitovú vzdialenosť Mesiaca z pohľadu pozorovateľa nachádzajúceho sa v budove NOT.

</li>

<li>

<span class="body">[15 b]</span> Magnitúda objektu na oblohe sa kvôli prechodu cez atmosféru zvýši o 

$$
\Delta m = \frac{k}{\cos z}, \tag{1}
$$

 kde $k=0,2$ je koeficient extinkcie a $z$ je zenitová vzdialenosť. Vypočítajte tok žiarenia Mesiaca, ktorý po prechode atmosférou dopadá na povrch ďalekohľadu.

</li>

<li>

<span class="body">[15 b]</span> Vypočítajte, aký výkon dokáže Nordic Optical Telescope sústrediť do svojho ohniska za predpokladu, že sa 12 % svetla stratí pri odrazoch. Predpokladajte, že ďalekohľad pracuje vo $V$ filtri a svetlo iných vlnových dĺžok sa do ohniska nedostane.

</li>

<li>

<span class="body">[10 b]</span> Ryžu skúsite uvariť v jednom litri vody s počiatočnou teplotou $20\,^{\circ}\mathrm{C}$. Určte energiu potrebnú na zohriatie vody na teplotu varu, ktorá je v nadmorskej výške NOT asi $92\,^{\circ}\mathrm{C}$. Hmotnostná tepelná kapacita vody je $c_{H_2O} = 4180\,\mathrm{J}\,{\mathrm{kg}}^{-1}\,{\mathrm{K}}^{-1}$.

</li>

<li>

<span class="body">[5 b]</span> Zistite, za akú dobu sa voda v ohnisku zohreje dostatočne na to, aby začala vrieť. Rozhodnite, či je realistické stihnúť vodu zohriať na požadovanú teplotu v priebehu jednej noci. Pre jednoduchosť môžete zanedbať pohyb Mesiaca po oblohe a predpokladajte, že zostane celú dobu v blízkosti zenitu (je to síce veľmi odvážny predpoklad, ale pre náš jednoduchý odhad nám bohate stačí).

</li>

</ol>

Pri výpočte môžu byť užitočné nasledujúce informácie o NOT:

- priemer primárneho zrkadla: $D=2{,}56\,\mathrm{m}$,

- ohnisková vzdialenosť primárneho\
  zrkadla: $f=28{,}160\,\mathrm{m}$,

<!-- -->

- zemepisná šírka: $\varphi = 28^{\circ}\,45'$N,

- zemepisná dĺžka: $\lambda = 17^{\circ}\,53'$W,

- nadmorská výška: $H = 2382\,\mathrm{m}$.

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Využijeme Pogsonovu rovnicu, v ktorej porovnáme žiarenie vo viditeľnom svetle pochádzajúce priamo zo Slnka a žiarenie odrazené od Mesiaca. Z rovnice si vyjadríme tok mesačného svetla 

$$
\begin{align*}
    m_\Sun - m_\Mo &= 2,5 \log \left(\frac{F_\Mo}{F_\Sun}\right) , \tag{2}\\
    \frac{F_\Mo}{F_\Sun} &= 10^{0,4(m_\Sun-m_\Mo)} \, , \tag{3}\\
    F_\Mo &= F_\Sun \cdot 10^{0,4(m_\Sun-m_\Mo)} \, ,\qquad\textit{[13\,b]} \tag{4}\end{align*}
$$

 po dosadení 

$$
F_\Mo = 1240\,\mathrm{W}\,{\mathrm{m}}^{-2} \cdot 10^{0,4\cdot(-26,74+12,74)} \doteq \boxed{3{,}11\,\mathrm{mW}\,{\mathrm{m}}^{-2}}\, . \qquad\textit{[2\,b]} \tag{5}
$$

</li>

<li>

Najskôr určíme, do akej maximálnej výšky nad južným horizontom sa Mesiac môže dostať. Ak by sa pohyboval po rovníku, bolo by to maximálne $90^{\circ} - \varphi$. V prípade, že by bol vždy na ekliptike (ako Slnko), mohol by sa dostať ešte o $\varepsilon = 23^{\circ}\,26'$ vyššie (kvôli vzájomnému sklonu rovín ekliptiky a rovníka). Rovina dráhy Mesiaca je ale voči ekliptike naklonená ešte o ďalších $i_\Mo = 5{,}14^{\circ}$, čiže Mesiac sa dokáže dostať ešte o niečo vyššie. Sčítaním týchto uhlov dostaneme maximálnu možnú výšku Mesiaca nad horizontom 

$$
h_{max} = 90^{\circ} -\varphi +\varepsilon + i_\Mo \, , \qquad\textit{[15\,b]} \tag{6}
$$

 

$$
h_{max} = 90^{\circ} - 28^{\circ}\,45' +23^{\circ}\,26' + 5^{\circ}\,8' = 89^{\circ}\,49'\, . \qquad\textit{[2\,b]} \tag{7}
$$

Minimálna zenitová vzdialenosť Mesiaca je doplnkom do $90^{\circ}$, teda $\boxed{z_{min} = 0^{\circ}\,11'}$. <span class="subbody">[3 b]</span>

</li>

<li>

Pretože uhol $z_{min}$ je veľmi blízky nule, môžeme použiť aproximáciu $\cos z_{min} \approx 1$. Tok mesačného svetla, ktorý dopadne na zemský povrch, je v tom prípade 

$$
F_\Mo' = F_\Mo \cdot 10^{-0,4\Delta m} = F_\Mo \cdot 10^{-0,4k} \, ,\qquad\textit{[13\,b]} \tag{8}
$$

 

$$
F_\Mo' = 3{,}11\,\mathrm{mW}\,{\mathrm{m}}^{-2} \cdot 10^{-0,4 \,\cdot \,0,2} \doteq \boxed{2{,}59\,\mathrm{mW}\,{\mathrm{m}}^{-2}} \, .\qquad\textit{[2\,b]} \tag{9}
$$

</li>

<li>

Ďalekohľad zachytáva svetlo celou plochou svojho primárneho zrkadla, pričom efektivita prenosu energie až do ohniska je $\eta = 1-0,12 = 0,88$. Do ohniska sa tak dostane výkon 

$$
P = \eta \frac{\pi D^2}{4}F_\Mo'\, , \qquad\textit{[13\,b]} \tag{10}
$$

 

$$
P = 0,88 \cdot\frac{\pi \cdot (2{,}56\,\mathrm{m})^2}{4}\cdot 2{,}59\,\mathrm{mW}\,{\mathrm{m}}^{-2} \doteq \boxed{11{,}7\,\mathrm{mW}}\, . \qquad\textit{[2\,b]} \tag{11}
$$

</li>

<li>

Energiu vypočítame zo vzorca 

$$
E = c_{H_2O} \,m \,\Delta T\, , \qquad\textit{[8\,b]} \tag{12}
$$

 pričom využijeme fakt, že 1 liter vody váži zhruba $1\,\mathrm{kg}$. Číselný výsledok je 

$$
E = 4180\,\mathrm{J}\,{\mathrm{kg}}^{-1}\,{\mathrm{K}}^{-1} \cdot 1\,\mathrm{kg} \cdot (92-20) \mathrm{K} \doteq \boxed{3{,}01 \cdot 10^{5}\,\mathrm{J}}\, . \qquad\textit{[2\,b]} \tag{13}
$$

</li>

<li>

Čas potrebný na zohriatie vody vypočítame jednoducho ako 

$$
t = \frac{E}{P} = \frac{3{,}01 \cdot 10^{5}\,\mathrm{J}}{11{,}7 \cdot 10^{-3}\,\mathrm{W}} \doteq \boxed{2{,}57 \cdot 10^{7}\,\mathrm{s}}\, . \qquad\textit{[4\,b]} \tag{14}
$$

Po prepočte na dni nám vyjde až $t=298\,\mathrm{dní}$, je teda jasné, že za jednu noc je nemožné vodu zohriať na bod varu. Astronómovia preto musia používať bežnejšie metódy varenia večere. <span class="subbody">[1 b]</span>

</li>

</ol>

</details>

## Komentár autora

Za nápad na úlohu ďakujem Anni Kasikov, ktorá sa pri nočných pozorovaniach s NOT zamýšľala nad naozaj podstatnými vecami.
