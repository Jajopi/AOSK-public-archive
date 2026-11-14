---
title: Úloha 2
year: 2019
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú2
weight: 2302
hasSolution: true
source: ZAO:I_Zadania/04_FotoSpek/04_SS_FI.tex
rocniky:
- '2019'
kola:
- Celoštátne kolo
kategorie:
- SŠ
typy:
- Teória
tagy:
- Fotometria a spektroskopia
collection: ZAO
---

## Zadanie

<ol type="a">

<li>

Stefanov-Boltzmannov zákon nám hovorí, ako závisí intenzita vyžarovania hviezdy od jej teploty

</li>

</ol>

$$
I=\sigma T^4\, ,
$$

 kde $\sigma$ je Stefanova-Boltzmanova konštanta. $\sigma$ sa dá vyjadriť pomocou iných konštánt ako 

$$
\sigma=A\frac{k_\textrm{B}^\alpha}{h^\beta c^\gamma}\, ,
$$

 kde $k_\textrm{B}$ je Boltzmannova konštanta, $h$ je Planckova konštanta, $c$ je rýchlosť svetla a $A$ je bezrozmerná konštanta. Určte pomocou rozmerovej analýzy hodnoty koeficientov $\alpha$, $\beta$, $\gamma$ a hodnotu konštanty $A$.

<ol type="a" start="2">

<li>

Rádioteleskop s priemerom $D = 200\,\mathrm{m}$ pozoroval po celú noc pulzar. Spektrálna intenzita žiarenia pulzaru na frekvencii $1660\,\mathrm{MHz}$ bola $S_{1660} = 0{,}21\,\mathrm{Jy}$. Aké množstvo energie zachytí rádioteleskop počas osemhodinového pozorovania pulzaru na frekvencii $1660\,\mathrm{MHz}$ so šírkou pásma $100\,\mathrm{MHz}$?

</li>

</ol>

Pre vyžarovanie rádiových vĺn sa Planckov zákon dá zjednodušiť na Rayleighov-Jeansov zákon 

$$
B_\textrm{f}=\frac{2k_\textrm{B}Tf^2}{c^2} \, ,
$$

 kde $B_\textrm{f}$ je výkon pulzaru prerátaný na meter štvorcový na steradián na Hertz.

<ol type="a" start="3">

<li>

Porovnajte túto energiu s energiou zachytenou počas 5 minút solárnym panelom s plochou $1\,{\mathrm{m}}^{2}$ a účinnosťou 5,4%. Koľkokrát je menšia/väčšia energia zachytená solárnym panelom?

</li>

</ol>

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Najskôr si vypíšeme základné fyzikálne jednotky, v ktorých sú jednotlivé konštanty vyjadrené. Podľa nich si potom vytvoríme sústavu lineárnych rovníc

</li>

</ol>

$$
[\sigma]=1\,\mathrm{J}\,{\mathrm{s}}^{-1}\,{\mathrm{m}}^{-2}\,{\mathrm{K}}^{4}=1\,\mathrm{kg}\,{\mathrm{s}}^{-3}\,{\mathrm{K}}^{4} \, , \tag{1}
$$

 

$$
[k_\textrm{B}]=1\,\mathrm{J}\,{\mathrm{K}}^{-1}=1\,\mathrm{kg}\,{\mathrm{m}}^{2}\,{\mathrm{s}}^{-2}\,{\mathrm{K}}^{-1} \, , \tag{2}
$$

 

$$
[h]=1\,\mathrm{J}\,\mathrm{s}=1\,\mathrm{kg}\,{\mathrm{m}}^{2}\,{\mathrm{s}}^{-1} \, , \tag{3}
$$

 

$$
[c]=1\,\mathrm{m}\,{\mathrm{s}}^{-1} \, . \tag{4}
$$

 Využili sme, že pre jednotku 1 J platí 

$$
1\,\mathrm{J}=1\,\mathrm{kg}\,{\mathrm{m}}^{2}\,{\mathrm{s}}^{-2} \, . \tag{5}
$$

 Toto tvrdenie sa dá jednoducho overiť, ak sa pozrieme na vzorec pre kinetickú energiu $E_\textrm{k}=\frac{1}{2}mv^2$, kde vľavo je energia v jouloch a vpravo je hmotnosť v kilogramoch a rýchlosť v metroch za sekundu umocnená na druhú. Sústava lineárnych rovníc je 

$$
\rm kg: \ 1=\alpha-\beta \, , \tag{6}
$$

 

$$
\rm m: \ 0=2\alpha-2\beta-\gamma \, , \tag{7}
$$

 

$$
\rm s: \ -3=-2\alpha+\beta+\gamma \, , \tag{8}
$$

 

$$
\rm K: \  -4=-\alpha \, . \tag{9}
$$

 Riešením sústavy sú koeficienty $\alpha=4$, $\beta=3$ a $\gamma=2$. Vzorec pre Stefanovu-Boltzmanovu konštantu je 

$$
\sigma=A\frac{k_\textrm{B}^4}{h^3 c^2} \, . \tag{10}
$$

 Hodnota bezrozmernej konštanty $A$ je 

$$
A=\frac{\sigma h^3c^2}{k_\textrm{B}^4}=\frac{5{,}67 \cdot 10^{-8}\cdot(6{,}626 \cdot 10^{-34})^3\cdot(2{,}998 \cdot 10^{8})^2}{(1{,}381 \cdot 10^{-23})^4}=40,76 \, . \tag{11}
$$

<ol type="a" start="2">

<li>

Rayleighov-Jeansov bol v zadaní zámerne napísaný navyše a pri riešení úlohy nebol potrebný. Zachytená energia sa dá jednoducho odhadnúť ako

</li>

</ol>

$$
E_1=S_{1660}\pi \frac{D^2}{4}t\Delta f \, , \tag{12}
$$

 

$$
E_1=0{,}21 \cdot 10^{-26}\cdot\pi \cdot \frac{200^2}{4}\cdot8\cdot3600\cdot 100 \cdot 10^{6} = 1{,}9 \cdot 10^{-10}\,\mathrm{J} \, . \tag{13}
$$

<ol type="a" start="2">

<li>

Solárny panel zachytí energiu

</li>

</ol>

$$
E_2=\frac{L_{\Sun}}{4\pi a_{\Ea}^2}\eta S\Delta t \, , \tag{14}
$$

 

$$
E_2=\frac{3{,}826 \cdot 10^{26}}{4\pi\cdot (1{,}496 \cdot 10^{11})^2}\cdot0,054\cdot1\cdot5\cdot60=22\,000\,\mathrm{J} \, . \tag{15}
$$

 Pomer energií je 

$$
\frac{E_2}{E_1}=\frac{22\,000}{1{,}9 \cdot 10^{-10}}=1{,}2 \cdot 10^{14} \, . \tag{16}
$$

 Solárny panel teda zachytí $1{,}2 \cdot 10^{14}$-krát viac energie ako rádioteleskop.

</details>
