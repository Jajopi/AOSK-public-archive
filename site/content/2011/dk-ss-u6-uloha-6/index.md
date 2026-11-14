---
title: Úloha 6
year: 2011
round: DK
roundName: Domáce kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú6
weight: 3006
hasSolution: true
source: ZAO:I_Zadania/06_FyzHaP/06_SS_DK.tex
years:
- '2011'
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

Ľad s teplotou $-10\,^{\circ}\mathrm{C}$ a plochou $50 \times 50\,\mathrm{cm}$ je vystavený v čiernej tepelne izolovanej nádobe slnečnému žiareniu, ktoré dopadá naň kolmo za normálneho atmosférického tlaku. Hrúbka ľadu je $1\,\mathrm{cm}$. Ľad sa rozpustí za $58\,\min$.

Užitočné konštanty:\
Hustota ľadu: $\rho_\textrm{ľad}=917\,\mathrm{kg}\,{\mathrm{m}}^{-3}$\
Merná tepelná kapacita vody: $c_\mathrm{H_2O}=4180\,\mathrm{J}\,{\mathrm{kg}}^{-1}\,{\mathrm{K}}^{-1}$\
Skupenské teplo topenia ľadu: $L_\textrm{t,ľad}=334\,000\,\mathrm{J}\,{\mathrm{kg}}^{-1}$

<ol type="a">

<li>

Vypočítajte celkový žiarivý výkon Slnka. Porovnajte s tabuľkovými hodnotami, určte rozdiel v percentách a zdôvodnite.

</li>

<li>

Ako dlho by sa rozpúšťal rovnako veľký ľad na Marse, ak by sme uvažovali rovnaké podmienky jeho uloženia, za akých sa rozpúšťal na Zemi?

</li>

</ol>

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Celková energia potrebná na roztopenie ľadu sa rozdelí na dve časti. Prvá sa spotrebuje na zohriatie ľadu na teplotu topenia, teda $0^{\circ}$C ($273\,\mathrm{K}$) a druhá sa spotrebuje na skupenskú premenu ľadu na vodu. Predpokladáme, že všetka potrebná energia je ľadu dodaná vo forme slnečného žiarenia

</li>

</ol>

$$
E=\frac{L_{\Sun}}{4\pi a_{\Ea}^2}St \, , \tag{1}
$$

 

$$
E=Sh\rho_\textrm{ľad}[c_{\textrm{H}_2\textrm{O}}\Delta T+L_\textrm{t,ľad}] \, . \tag{2}
$$

 Plochu ľadu, ktorou absorbuje žiarenie sme označili $S$, hrúbku ľadu $h$. Žiarivý výkon Slnka je 

$$
L_{\Sun}=4\pi a_{\Ea}^2h\rho_\textrm{ľad}\frac{1}{t}[c_{\textrm{H}_2\textrm{O}}\Delta T+L_\textrm{t,ľad}] \, , \tag{3}
$$

 

$$
L_{\Sun}=\frac{4\pi \cdot(1{,}496 \cdot 10^{11})^2\cdot0,01\cdot917}{58\cdot60}\cdot(4180\cdot10+334\,000)=2{,}78 \cdot 10^{26}\,\mathrm{W} \, . \tag{4}
$$

 Tabuľková hodnota je $L_{\Sun,\textrm{tab}}=3{,}826 \cdot 10^{26}\,\mathrm{W}$, nami vypočítaná hodnota z nej tvorí iba 73%. Pri výpočte sme zanedbali albedo zemskej atmosféry i ľadu ako aj fakt, že Slnko nie je jediným zdrojom tepla, ktoré je použité na topenie ľadu.

<ol type="a" start="2">

<li>

Energia potrebná na roztopenie ľadu je stále rovnaká. Čas topenia preto závisí iba na príkone energie od Slnka. Keďže plocha ľadu sa nemení, príkon závisí iba na toku žiarenia od Slnka, ktorý je nepriamo úmerný druhej mocnine vzdialenosti od Slnka. Na základe týchto úvah vidíme, že pre pomer časov topenia na Marse a na Zemi platí

</li>

</ol>

$$
\frac{t_{\Ma}}{t_{\Ea}}=\frac{F_{\Ma}}{F_{\Ea}}=\frac{a_{\Ma}^2}{a_{\Ea}^2} \, . \tag{5}
$$

 Na Marse sa ľad roztopí za čas 

$$
t_{\Ma}=\frac{1,524^2}{1^2}\cdot58=135\,\min=2\,\mathrm{h}\ 15\,\min \, . \tag{6}
$$

</details>
