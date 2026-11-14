---
title: Úloha 2
year: 2007
round: DK
roundName: Domáce kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú2
weight: 302
hasSolution: true
source: ZAO:I_Zadania/02_GmtrCas/02_SS_DK.tex
rocniky:
- '2007'
kola:
- Domáce kolo
kategorie:
- SŠ
typy:
- Teória
tagy:
- Geometria a čas
collection: ZAO
---

## Zadanie

Jupiter a jeho štyri najväčšie mesiace zohrali v histórii vedy významné úlohy. Ich objav, ktorý uskutočnil Galileo Galilei v roku 1609, predstavoval významný argument pre heliocentrické učenie. Koncom 17. storočia sa Olaf Rőmer pokúsil určiť rýchlosť svetla s využitím výsledkov pozorovania zatmení týchto satelitov. Sledovanie týchto úkazov sa uplatnilo aj pri určovaní zemepisnej dĺžky v námornej doprave. Zaujímavými javmi tejto kategórie sú aj prechody mesiacov resp. ich tieňov popred kotúčik Jupitera. Samotný mesiac je síce pred diskom Jupitera vďaka nízkemu kontrastu ťažko pozorovateľný, ale jeho tieň sa javí ako výrazná čierna škvrnka, ktorú za priaznivých podmienok zbadáme už pri 100-násobnom zväčšení. Dokonca nastávajú aj také situácie, že tieň opúšťa disk materskej planéty, ale mesiac samotný sa ešte nedotkol okraja Jupitera. Pri riešení nasledovných úloh využijeme určité zjednodušenia, ktoré však výsledok nezaťažia veľkou nepresnosťou. Zanedbáme sklon obežnej roviny mesiaca Io voči rovníku Jupitera, budeme uvažovať, že táto rovina zároveň prechádza stredom Zeme. Dráhy všetkých telies (Zem, Jupiter, mesiac Io) okolo Slnka resp. Jupitera považujeme za kružnice. Veľká polos Io je $a_{\rm{Io}}=4{,}217 \cdot 10^{5}\,\mathrm{km}$, a siderická obežná doba $P_{\rm{Io}}=42{,}5\,\mathrm{h}$.

<ol type="a">

<li>

Načrtnite polohy Jupitera a Zeme voči Slnku, pri ktorej sú mesiac Io a jeho tieň v projekcii na disk Jupitera od seba najvzdialenejšie. Ako tieto aspekty Jupitera z hľadiska pozorovateľa na Zemi nazývame?

</li>

<li>

Určte vzdialenosť mesiaca Io a jeho tieňa v projekcii na kotúč Jupitera z predošlej úlohy v jednotkách polomerov planéty Jupiter.

</li>

<li>

V akom poradí nastáva vstup mesiaca a jeho tieňa pri zmieňovaných aspektoch? Vypočítajte časový interval medzi nimi.

</li>

</ol>

<details class="solution">
<summary>Riešenie</summary>

<figure>

<div class="fig-images"><img class="invert" src="AO2007_SS_DK_2_1.svg" alt="obrázok" loading="lazy" style="width:60%"></div>

</figure>

<ol type="a">

<li>

Ide o aspekty nazývané kvadratúry (pozícia Zeme Z1 – západná kvadratúra Jupitera, viditeľný je na rannej oblohe, Z2 – východná kvadratúra Jupitera, planéta je viditeľná na večernej oblohe).

</li>

</ol>

<ol type="a" start="2">

<li>

Uhol $\phi$ vyrátame s využitím pravouhlého trojuholníka S – Z1 – J.

</li>

</ol>

$$
\sin \phi=\frac{r_{\Ea}}{r_{\Ju}}=\frac{1}{5,204}=0,192 \, , \tag{1}
$$

$$
\phi=11{,}1^{\circ} \, . \tag{2}
$$

Vo vzorci je $r_{\Ea}$ vzdialenosť SZ, $r_{\Ju}$ je vzdialenosť SJ. Ten istý uhol zvierajú aj spojnice Jupitera so Slnkom resp. Zemou na ďalšom obrázku. Vzdialenosť priemetov Io a jeho tieňa do roviny kolmej na spojnicu Zem - Jupiter určíme ($r_{\textrm{I}{\Ju}}$ je vzdialenosť stredov Io a Jupitera, $r_\textrm{I,p}$ je vzdialenosť Io od povrchu Jupitera, $R_{\Ju}$ je polomer Jupitera) 

$$
d=r_\textrm{I,p}\sin \phi = (r_{\textrm{I}\Ju}-R_{\Ju})\sin \phi = (421700-69911)\cdot0,192=67{,}5 \cdot 10^{3}\,\mathrm{km}=0{,}97\,\mathit{R}_\Ju \, . \tag{3}
$$

<figure>

<div class="fig-images"><img class="invert" src="AO2007_SS_DK_2_2.svg" alt="obrázok" loading="lazy" style="width:80%"></div>

</figure>

<ol type="a" start="3">

<li>

V prípade mesiaca Io je rozdiel medzi synodickou a siderickou obežnou dobou minimálny, môžeme použiť hodnotu $T=42{,}5\,\mathrm{h}$. Za túto dobu opíše mesiac uhol $360^{\circ}$. Interval medzi vstupom mesiaca a tieňa na disk Jupitera potom predstavuje dobu, za ktorý opíše Io spomínaný uhol $\phi = 11{,}1^{\circ}$. Použitím priamej úmery tak vychádza časový interval

</li>

</ol>

$$
t=\frac{11,1}{360}\cdot42,5=1{,}31\,\mathrm{h} \, . \tag{4}
$$

Ak sa Jupiter nachádza v blízkosti západnej kvadratúry so Slnkom, nastáva najskôr vstup tieňa, až potom samotného mesiaca. Pre východnú kvadratúru je poradie úkazov opačné.

</details>
