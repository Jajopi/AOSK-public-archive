---
title: Úloha 1
year: 2007
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú1
weight: 5001
hasSolution: true
source: ZAO:I_Zadania/04_FotoSpek/04_SS_FI.tex
years:
- '2007'
rounds:
- Celoštátne kolo
categories:
- SŠ
types:
- Teória
topics:
- Fotometria a spektroskopia
collection: ZAO
---

## Zadanie

Moderná pozorovacia technika umožnila objavy planét obiehajúcich okolo iných hviezd našej Galaxie – exoplanét, ktorých v súčasnosti poznáme už vyše 200[^1]. Niektoré z nich by mohli mať vlastnosti podobné Zemi, potenciálnym kandidátom je napríklad objekt Gliese 581c. Exoplanéta obieha okolo trpasličej materskej hviezdy Gliese 581[^2] s polomerom približne $0{,}38\,\mathit{R}_\Sun$ a teplotou $2500\,\mathrm{K}$ v strednej vzdialenosti $0{,}073\,\mathrm{au}$. Úlohy:

<ol type="a">

<li>

Vypočítajte žiarivý výkon hviezdy Gliese 581 (t. j. množstvo energie vyžiarenej z celého povrchu hviezdy za sekundu), porovnajte ho so žiarivým výkonom Slnka.

</li>

<li>

Určte, aký žiarivý výkon dopadá kolmo na meter štvorcový povrchu planéty Gliese 581c z jej materskej hviezdy, porovnajte túto hodnotu s množstvom energie, ktorá dopadá na meter štvorcový povrchu Zeme zo Slnka (tzv. slnečná konštanta).

</li>

</ol>

[^1]: Ku dňu 26. 10. 2022 bolo potvrdených už vyše 5000 exoplanét.

[^2]: V roku 2008 bola vyslaná zo Zeme správa, ktorá by mala doraziť ku exoplanéte v roku 2029.

<details class="solution">
<summary>Riešenie</summary>

\(a\) Žiarivý výkon hviezdy je 

$$
L=4\pi R^2 \sigma T^4 \, , \tag{1}
$$

 

$$
L=4\pi \cdot 0,38^2\cdot(6{,}955 \cdot 10^{8})^2\cdot5{,}67 \cdot 10^{-8}\cdot2500^4=1{,}94 \cdot 10^{24}\,\mathrm{W} \, , \tag{2}
$$

 

$$
\frac{L}{L_\Sun}=0,38^2\cdot\left(\frac{2500}{5778}\right)^4=5{,}06 \cdot 10^{-3} \, . \tag{3}
$$

 (b) Tok žiarenia dopadajúci na exoplanétu je 

$$
F=\frac{L}{4\pi a^2} \, , \tag{4}
$$

 

$$
F=\frac{1{,}94 \cdot 10^{24}}{4\pi \cdot0,073^2\cdot(1{,}496 \cdot 10^{11})^2} = 1294\,\mathrm{W}\,{\mathrm{m}}^{-2} \, . \tag{5}
$$

 Porovnanie so slnečnou konštantou 

$$
\frac{F}{S}=\frac{L}{L_\Sun}\frac{a_\Ea^2}{a^2} \, , \tag{6}
$$

 

$$
\frac{F}{S}=5{,}06 \cdot 10^{-3}\cdot\frac{1}{0,073^2}=0,95 \, . \tag{7}
$$

</details>
