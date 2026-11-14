---
title: Metón z Atén
year: 2026
round: DK
roundName: Domáce kolo
category: ZŠ
type: teoria
typeName: Teória
label: T3
weight: 3
points: '50'
authors:
- Radovan Lascsák
hasSolution: true
source: 2026:-ZS/-DK/Meton-z-Aten.tex
rocniky:
- '2026'
kola:
- Domáce kolo
kategorie:
- ZŠ
typy:
- Teória
tagy:
- Nezaradené
---

## Zadanie

Metón z Atén bol grécky astronóm a matematik, ktorý žil v piatom storočí pred našim letopočtom. V roku 432 p. n. l. bol prijatý jeho kalendárny systém, ktorý bol založený na takzvanom Metónovom cykle. Dĺžka Metónovho cyklu je $6940\,\mathrm{dní}$, čo je približne 19 rokov. Metón pozoroval, že toto časové obdobie je možné takmer presne rozdeliť na istý počet po sebe idúcich synodických mesiacov, teda časových úsekov od splnu po spln.

<ol type="a">

<li>

<span class="body">[20 b]</span> Koľko synodických mesiacov napočítal Metón počas jedného Metónovho cyklu? Využite hodnotu synodickej obežnej doby Mesiaca v konštantovníku. Váš výsledok zaokrúhlite na celé číslo.

</li>

</ol>

Na základe dĺžky synodického mesiaca odvodil Metón dĺžky kalendárnych mesiacov. Na to, aby počet dní v každom kalendárnom mesiaci bol celé číslo (nie desatinné), Metón volil pre niektoré mesiace dĺžku 29 dní a pre iné 30 dní. Zároveň Metón chcel, aby bol počet kalendárnych mesiacov rovnaký ako počet synodických mesiacov, teda, aby 29-dňových mesiacov spolu s tými 30-dňovými bolo dokopy toľko, koľko ste zistili v úlohe (a).

<ol type="a" start="2">

<li>

<span class="body">[30 b]</span> Koľko 29-dňových a koľko 30-dňových kalendárnych mesiacov je potrebných na to, aby presne vyplnili jeden Metónov cyklus?

</li>

</ol>

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Z konštantovníka zistíme, že dĺžka synodického mesiaca je $S_\Mo = 29{,}53\,\mathrm{dňa}$. <span class="subbody">[5 b]</span> Toľko dní ubehne medzi dvoma po sebe idúcimi splnmi, alebo inými rovnakými fázami Mesiaca. Na zistenie, koľko synodických mesiacov ubehne počas Metónovho cyklu ($6940\,\mathrm{dní}$), nám stačí jednoduché vydelenie. Rozdeľujeme $6940\,\mathrm{dní}$ medzi úseky o dĺžke $29{,}53\,\mathrm{dňa}$, čiže vydelíme nasledovne 

$$
6940\,\mathrm{dní} : 29{,}53\,\mathrm{dňa} = 235,015 \doteq 235 \,. \qquad\textit{[15\,b]} \tag{1}
$$

Počas jedného Metónovho cyklu Metón napočítal 235 synodických mesiacov. Ako skúšku správnosti vypočítame koľko dní napočítame počas 235 synodických mesiacov 

$$
\underbrace{29{,}53\,\mathrm{dňa} + 29{,}53\,\mathrm{dňa} + \cdots + 29{,}53\,\mathrm{dňa}}_{\text{235-krát}}
    =
    235 \cdot 29{,}53\,\mathrm{dňa} = 6939{,}55\,\mathrm{dňa} \doteq 6940\,\mathrm{dní} \,. \tag{2}
$$

 Po zaokrúhlení dostávame $6940\,\mathrm{dní}$, čo je práve jeden Metónov cyklus.

</li>

<li>

Ak by všetkých 235 kalendárnych mesiacov malo $29\,\mathrm{dní}$, potom by sa dokopy poskladali na $235\cdot 29\,\mathrm{dní} = 6815\,\mathrm{dní}$, čo je menej ako Metónov cyklus. Do požadovanej dĺžky $6940\,\mathrm{dní}$ chýba 

$$
6940\,\mathrm{dní} - 6815\,\mathrm{dní} = 125\,\mathrm{dní} \,, \tag{3}
$$

 čiže potrebujeme predĺžiť súčet dní o 125. To spravíme nahradením 125 kratších (29-dňových) kalendárnych mesiacov za dlhšie (30-dňové). Takto dostaneme $235 - 125 = 110$ kratších a $125$ dlhších mesiacov. Celkový súčet dní bude 

$$
\underbrace{110 \cdot 29\,\mathrm{dní}}_{krat\check{s}ie~mesiace} + 
    \underbrace{125 \cdot 30\,\mathrm{dní}}_{dlh\check{s}ie~mesiace} =
    6940\,\mathrm{dní} \,, \qquad\textit{[30\,b]} \tag{4}
$$

 čo odpovedá požadovanej dĺžke Metónovho cyklu.

K výsledku sa vieme dopracovať aj riešením rovnice. Označme $x$ ako počet kratších mesiacov. Počet dlhších mesiacov potom bude $235 - x$. Podmienku dĺžky Metónovho cyklu zapíšeme rovnicou ako 

$$
x \cdot 29\,\mathrm{dní} +
    (235-x) \cdot 30\,\mathrm{dní} =
    6940\,\mathrm{dní} \,. \qquad\textit{[15\,b]} \tag{5}
$$

Z tejto rovnice potrebujeme vyjadriť a vypočítať $x$. Začneme roznásobením zátvorky: 

$$
x \cdot 29\,\mathrm{dní} +
    235 \cdot 30\,\mathrm{dní} -
    x \cdot 30\,\mathrm{dní} =
    6940\,\mathrm{dní} \,. \tag{6}
$$

 Ďalej preusporiadame rovnicu: 

$$
x \cdot 29\,\mathrm{dní} -
    x \cdot 30\,\mathrm{dní} =
    6940\,\mathrm{dní} - 235 \cdot 30\,\mathrm{dní} \,. \tag{7}
$$

 Vyberieme $x$ pred zátvorku a na pravej strane vypočítame násobenie: 

$$
x \cdot (29\,\mathrm{dní} - 30\,\mathrm{dní}) =
    6940\,\mathrm{dní} - 7050\,\mathrm{dní} \,. \tag{8}
$$

 Na oboch stranách vypočítame odčítanie: 

$$
- x \cdot 1\,\mathrm{deň} =
    - 110\,\mathrm{dní} \,. \tag{9}
$$

 Z oboch strán odstránime znamienko mínus: 

$$
x \cdot 1\,\mathrm{deň} =
    110\,\mathrm{dní} \,. \tag{10}
$$

 Na záver rovnicu vydelíme jednotkou $1\,\mathrm{deň}$, čím dostaneme 

$$
x  = 110 \,. \qquad\textit{[10\,b]} \tag{11}
$$

Teda kratších (29-dňových) kalendárnych mesiacov je 110 a dlhších (30-dňových) kalendárnych mesiacov je $235-110 = 125$. <span class="subbody">[5 b]</span>

</li>

</ol>

</details>
