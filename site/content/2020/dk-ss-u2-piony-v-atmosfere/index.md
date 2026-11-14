---
title: Pióny v atmosfére
year: 2020
round: DK
roundName: Domáce kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú2
weight: 3002
hasSolution: true
source: ZAO:I_Zadania/06_FyzHaP/06_SS_DK.tex
years:
- '2020'
rounds:
- Domáce kolo
categories:
- SŠ
types:
- Teória
topics:
- Fyzika hviezd a planét
collection: ZAO
---

## Zadanie

Neutrálny pión $\pi^0$ je nestabilná častica s pokojovou hmotnosťou $m_0 = 135{,}0\,\mathrm{MeV}\,{\mathit{c}}^{-2}$ a so strednou dobou života $\tau = 8{,}4 \cdot 10^{-17}\,\mathrm{s}$. Rozpadáva sa na dva fotóny $\pi^0 \rightarrow \gamma + \gamma$. Uvažujme jeden pión, ktorý vznikol ako výsledok interakcie kozmického žiarenia s atómami hornej atmosféry. Voči pozemskému pozorovateľovi má tento pión energiu $E = 1\,\mathrm{GeV}$. Musíme zanedbať interakcie piónu s atómami atmosféry.

<ol type="a">

<li>

Určte rýchlosť v piónu voči pozemskému pozorovateľovi a dráhu $l$ ktorú prešiel až kým sa nerozpadol.

</li>

<li>

Určte maximálny možný rozdiel energií $\Delta E$ dvoch fotónov, ktoré vznikajú uvedeným rozpadom voči danému pozorovateľovi.

</li>

</ol>

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Vzťah medzi celkovou energiou a pokojovou hmotnosťou piónu je

</li>

</ol>

$$
E=\gamma m_0c^2 \, . \tag{1}
$$

 Faktor $\gamma$ sa nazýva Lorentzov faktor a má hodnotu 

$$
\gamma=\frac{E}{m_0c^2}=\frac{1000}{135}=7,41 \, . \tag{2}
$$

 Lorentzov faktor je definovaný pomocou rýchlosti $v$ 

$$
\gamma=\frac{1}{\sqrt{1-\frac{v^2}{c^2}}} \, . \tag{3}
$$

 Vyjadríme si z toho rýchlosť piónu 

$$
1-\frac{v^2}{c^2} \, , \tag{4}
$$

 

$$
\frac{v^2}{c^2}=1-\frac{1}{\gamma^2} \, , \tag{5}
$$

 

$$
v=\sqrt{1-\frac{1}{\gamma^2}}c=\sqrt{1-\frac{1}{7,41^2}}\cdot2{,}9979 \cdot 10^{8}=2{,}97 \cdot 10^{8}\,\mathrm{m}\,{\mathrm{s}}^{-1} \, . \tag{6}
$$

 Doba života $\tau$ uvedená v zadaní je z pohľadu piónu. Vďaka dilatácii času bude z pohľadu pozorovateľa trvať dlhšiu dobu $(t=\gamma \tau)$, než sa pión rozpadne. Za tento čas prejde pión dráhu 

$$
l=vt=v\gamma \tau=7,41\cdot2{,}97 \cdot 10^{8}\cdot8{,}4 \cdot 10^{-17}=1{,}85 \cdot 10^{-7}\,\mathrm{m}=185\,\mathrm{nm} \, . \tag{7}
$$

<ol type="a" start="2">

<li>

Rozdiel energií fotónov bude najväčší v prípade, že poletia presne opačnými smermi, jeden presne v smere pohybu pôvodného piónu a druhý presne proti tomuto smeru. Zo zákonu zachovanie energie dostaneme, že súčet energií fotónov sa musí rovnať energii piónu, z ktorého vznikli

</li>

</ol>

$$
E_1+E_2=E \, . \tag{8}
$$

 Zo zákonu zachovania hybnosti zase dostaneme, že vektorový súčet hybností fotónov sa musí rovnať hybnosti piónu. Pretože sa všetky 3 častice pohybujú po jednej priamke, namiesto vektorového zápisu môžeme rovno použiť rozdiel číselných hodnôt hybností fotónov 

$$
p_1-p_2=p \, . \tag{9}
$$

 Hybnosť a energia fotónu pohybujúceho sa v smere piónu sú označené indexom 1, druhého fotónu indexom 2, veličiny bez indexu popisujú pión. Pre hybnosť a energiu fotónu platí jednoduchý vzťah (pretože majú nulovú pokojovú hmotnosť) 

$$
p=\frac{E}{c} \, . \tag{10}
$$

 Dosadíme to do zákonu zachovania hybnosti a dostaneme 

$$
p_1-p_2=\frac{E_1-E_2}{c}=p \, , \tag{11}
$$

 

$$
E_1-E_2=cp \, . \tag{12}
$$

 Pión má na rozdiel od fotónov nenulovú pokojovú hmotnosť, preto medzi jeho hybnosťou a energiou platí zložitejší vzťah 

$$
E^2=m_0^2c^4+p^2c^2 \, . \tag{13}
$$

 Sčítaním a odčítaním rovníc zákonov zachovania dostaneme výrazy pre energie obidvoch fotónov 

$$
E_1+E_1+E_1-E_2=E+cp \, , \tag{14}
$$

 

$$
E_1=\frac{E+cp}{2} \, , \tag{15}
$$

 

$$
E_2=\frac{E-cp}{2} \, . \tag{16}
$$

 Rozdiel energií je 

$$
\Delta E =E_1-E_2=\frac{2cp}{2}=cp=c\frac{\sqrt{E^2-m_0^2c^4}}{c}=\sqrt{(1000)^2+135^2}=991\,\mathrm{MeV} \, . \tag{17}
$$

</details>
