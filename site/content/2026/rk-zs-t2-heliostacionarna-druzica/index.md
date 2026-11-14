---
title: Heliostacionárna družica
year: 2026
round: RK
roundName: Regionálne kolo
category: ZŠ
type: teoria
typeName: Teória
label: T2
weight: 1002
points: '60'
authors:
- Samuel Buranský
hasSolution: true
source: 2026:-ZS/.RK/Heliostacionarna-druzica.tex
rocniky:
- '2026'
kola:
- Regionálne kolo
kategorie:
- ZŠ
typy:
- Teória
tagy:
- Nezaradené
---

## Zadanie

Geostacionárna družica je družica, ktorá obieha okolo Zeme takým spôsobom, aby bola neustále nad jedným miestom na Zemi. Najčastejším využitím geostacionárnych družíc je telekomunikácia, prenos dát, meteorológia, navigácia alebo sledovanie Zeme. Predstavme si na výskumné účely takzvanú heliostacionárnu družicu, teda družicu, ktorá obieha v rovine slnečného rovníka a neustále sleduje jedno jeho miesto. Vypočítajte, ako ďaleko od povrchu Slnka by bola heliostacionárna družica sledujúca rovník Slnka.

Slnko je zaujímavé tým, že nerotuje ako tuhé teleso, ale má takzvanú diferenciálnu rotáciu, čo znamená, že rôzne časti Slnka rotujú rôzne rýchlo. Rotačná perióda na slnečnom rovníku je $25{,}67\,\mathrm{dní}$ a napríklad na $75^{\circ}$ heliografickej šírky je rotačná perióda $33{,}40\,\mathrm{dní}$.

<details class="solution">
<summary>Riešenie</summary>

Stacionárna dráha je charakteristická tým, že obežná doba satelitu je zhodná s rotačnou<span class="subbody">[15 b]</span> periódou centrálneho telesa a zároveň ide o kruhovú dráhu. Na výpočet vzdialenosti od povrchu Slnka môžeme využiť jednoducho 3. Keplerov zákon a vypočítať veľkú polos jeho dráhy. Môžeme využiť tvar 3. Keplerovho zákona pre slnečnú sústavu 

$$
a^3 = P^2 \qquad\textit{[15\,b]}\,, \tag{1}
$$

 kde veľká polos $a$ je v astronomických jednotkách a obežná perióda $P$ v rokoch. Z rovnice si vyjadríme veľkú polos 

$$
a = \sqrt[3]{P^2} \qquad\textit{[15\,b]}\,. \tag{2}
$$

 Obežnú periódu premeníme na roky: $25{,}67\,\mathrm{dní} = 0{,}07028\,\mathrm{roka}$.<span class="subbody">[5 b]</span> Po dosadení do rovnice dostaneme veľkú polos ako $a \doteq 0{,}1703\,\mathrm{au}$. Po premene na kilometre dostaneme $a \doteq 2{,}548 \cdot 10^{7}\,\mathrm{km}$.<span class="subbody">[5 b]</span> Na zistenie výšky nad povrchom len odpočítame polomer Slnka a družica bude nad povrchom približne $\boxed{2{,}478 \cdot 10^{7}\,\mathrm{km}}$.<span class="subbody">[5 b]</span>

Uvedieme ešte alternatívnu časť riešenia na výpočet veľkej polosi dráhy. Namiesto použitia rokov a astronomických jednotiek by bolo možné použiť 3. Keplerov zákon v plnom znení 

$$
\frac{a^3}{P^2} = \frac{G(M+m)}{4\pi^2} \qquad\textit{[15\,b]}\,, \tag{3}
$$

 kde $a$ je veľká polos v metroch, $P$ obežná perióda v sekundách, $G = 6{,}674 \cdot 10^{-11}\,{\mathrm{m}}^{3}\,{\mathrm{kg}}^{-1}\,{\mathrm{s}}^{-2}$ je gravitačná konštanta, $M = 1{,}989 \cdot 10^{30}\,\mathrm{kg}$ je hmotnosť Slnka a $m$ je hmotnosť družice, ktorú môžeme zanedbať, keďže je oveľa menšia než hmotnosť Slnka.<span class="subbody">[5 b]</span>

Ak v rovnici (3) zanedbáme $m$ a vyjadríme veľkú polos, dostaneme výraz 

$$
a = \sqrt[3]{\frac{G M P^2}{4 \pi^2}} \qquad\textit{[10\,b]}\,, \tag{4}
$$

 kam dosadíme konštanty a periódu v základných jednotkách $P = 2{,}218 \cdot 10^{6}\,\mathrm{s}$ a dostaneme veľkú polos $\boxed{a \doteq 2{,}548 \cdot 10^{10}\,\mathrm{m} = 2{,}548 \cdot 10^{7}\,\mathrm{km}}$, čo je rovnaký výsledok ako v prvej časti.<span class="subbody">[10 b]</span>

</details>
