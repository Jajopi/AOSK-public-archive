---
title: Úloha 6
year: 2007
round: CK
roundName: Celoštátne kolo
category: ZŠ
type: teoria
typeName: Teória
label: Ú6
weight: 2006
hasSolution: true
source: ZAO:I_Zadania/05_OptikDek/05_ZS_FI.tex
years:
- '2007'
rounds:
- Celoštátne kolo
categories:
- ZŠ
types:
- Teória
topics:
- Optika a detektory
collection: ZAO
---

## Zadanie

<ol type="a">

<li>

Aký veľký by musel byť priemer objektívu ďalekohľadu, aby v ňom bol v čase perigea na Mesiaci viditeľný kráter o priemere $3{,}6\,\mathrm{km}$. Využite poznatok, že $1\,\mathrm{m}$ vidíme voľným okom pod uhlom $1^{\circ}$ zo vzdialenosti $57{,}3\,\mathrm{m}$ a vzdialenosť Mesiaca v perigeu je $360\,000\,\mathrm{km}$.

</li>

<li>

Aké má ďalekohľad zorné pole, ak pri montáži bez pohonu možno vidieť v zornom poli celý Mesiac počas 4 minút. Počítajte s uhlovým priemerom Mesiaca $30'$ a zanedbajte vlastný pohyb Mesiaca.

</li>

</ol>

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Najmenší možný uhlový priemer kráteru sa rovná rozlišovacej schopnosti.

</li>

</ol>

<ol type="a" start="2">

<li>

V zadaní chýba údaj o deklinácii Mesiaca, ktorý je pre výpočet zorného poľa ďalekohľadu potrebný. Maximálna veľkosť zorného poľa nám vyjde, ak uvažujeme, že sa Mesiac práve nachádza na rovníku. V tomto prípade sa za 4 minúty Mesiac pohne o uhol

</li>

</ol>

$$
\alpha=\frac{4}{24\cdot60}\cdot360^{\circ}=1^{\circ}=60' \, . \tag{1}
$$

 Počas 4 minút pozorujeme celý Mesiac, za tú dobu sa ľavý okraj Mesiaca pohne o $60'$, pravý okraj bude ešte o $30'$ ďalej, zorné pole ďalekohľadu bude preto $\rm FOV = 90'=1^{\circ}\,30'$. Toto je najväčšia možná hodnota.\
Najmenšiu možnú hodnotu získame, ak budeme uvažovať Mesiac s čo najväčšou deklináciou (alebo najmenšou, vyjde to rovnako). Dráha Mesiaca je voči rovine ekliptiky sklonená o $5{,}14^{\circ}$, maximálna možná deklinácia je preto $\delta_{\Mo}=\varepsilon+i=23^{\circ}\,26'+5{,}14^{\circ}=28{,}57^{\circ}$. Za 4 minúty sa kotúčik Mesiaca pohne o uhol $\beta= 1^{\circ} \cdot \cos (28{,}57^{\circ})=53'$. Zorné pole ďalekohľadu je v tomto prípade $\rm FOV = 53'+30'=83'=1^{\circ}\,23'$ .

</details>
