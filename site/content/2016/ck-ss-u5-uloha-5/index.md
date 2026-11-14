---
title: Úloha 5
year: 2016
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú5
weight: 5005
hasSolution: true
source: ZAO:I_Zadania/01_NebMech/01_SS_FI.tex
years:
- '2016'
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

Predpokladáme, že prachové zrnká sú absolútne čierne telesá. Určite priemer prachového zrnka guľového tvaru, ktoré vo vzdialenosti $1\,\mathrm{au}$ od Slnka je v rovnováhe medzi silou tlaku žiarenia a gravitačnou silou Slnka. Počítajte s hustotou prachového zrnka $\rho=10^{3}\,\mathrm{kg}\,{\mathrm{m}}^{-3}$.

<details class="solution">
<summary>Riešenie</summary>

Tlak žiarenia je spôsobený prenosom hybnosti fotónov na zrnko prachu. Fotón s energiou $E$ má hybnosť 

$$
p=\frac{E}{c} \, . \tag{1}
$$

 Podľa 2. Newtonovho zákonu sa sila rovná zmene hybnosti za čas. Pre tlakovú silu žiarenia potom platí 

$$
F_\textrm{p}=\frac{\Delta p}{\Delta t}=\frac{\Delta E}{c\Delta t} \, . \tag{2}
$$

 Na zrnko prachu dopadá tok žiarenia od Slnka 

$$
F=\frac{L_\Sun}{4\pi r^2} \, . \tag{3}
$$

 Celková energia, ktorá dopadne na zrnko s polomerom $R$ za 1 sekundu je 

$$
\frac{\Delta E}{\Delta t} = FS=\frac{L_\Sun}{4\pi r^2} \pi R^2 \, . \tag{4}
$$

 Dosadíme to do vzorca pre silu a dostaneme celkovú silu na zrnko spôsobenú tlakom žiarenia 

$$
F_\textrm{p}=\frac{L_\Sun\pi R^2}{4\pi r^2 c} \, . \tag{5}
$$

 Gravitačná sila pôsobiaca na prachové zrnko je 

$$
F_\textrm{g}=\frac{GM_\Sun m}{r^2}=\frac{4\pi G \rho M_\Sun R^3}{3r^2} \, . \tag{6}
$$

 Gravitačná a tlaková sila sú v rovnováhe 

$$
F_\textrm{p}=F_\textrm{g} \, , \tag{7}
$$

 

$$
\frac{L_\Sun R^2}{4 r^2 c}=\frac{4\pi G \rho M_\Sun R^3}{3r^2} \, . \tag{8}
$$

 Z rovnosti vyjadríme polomer zrnka 

$$
R=\frac{3L_\Sun}{16\pi G \rho M_\Sun c} \, . \tag{9}
$$

 V zadaní sa nás pýtajú na priemer zrnka, ktorý je 

$$
D=2R=\frac{3L_\Sun}{8\pi G \rho M_\Sun c} \, . \tag{10}
$$

 

$$
D=\frac{3\cdot3{,}826 \cdot 10^{26}}{8\pi6{,}673 \cdot 10^{-11}\cdot10^3\cdot1{,}9891 \cdot 10^{30}\cdot2{,}9979 \cdot 10^{8}}=1{,}15 \cdot 10^{-6}\,\mathrm{m}=1{,}15\,\mu\mathrm{m} \, . \tag{11}
$$

</details>
