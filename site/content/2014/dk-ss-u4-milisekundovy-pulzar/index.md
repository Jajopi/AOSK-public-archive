---
title: Milisekundový pulzar
year: 2014
round: DK
roundName: Domáce kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú4
weight: 3004
hasSolution: true
source: ZAO:I_Zadania/08_Rozsiahle/08_SS_DK.tex
years:
- '2014'
rounds:
- Domáce kolo
categories:
- SŠ
types:
- Teória
topics:
- Rozsiahle príklady
collection: ZAO
---

## Zadanie

V súhvezdí Veľryba vybuchla supernova SN 2019A. Astronómovia zistili, že po výbuchu supernovy ostal milisekundový pulzar, ktorého frekvencia sa menila v rozsahu od $699{,}650175\,\mathrm{Hz}$ do $700{,}350175\,\mathrm{Hz}$ s periódou 4,5 dňa. Presné fotometrické a spektroskopické pozorovania ukázali, že sa jedná o zákrytový systém, v ktorom pulzar obieha okolo červeného obra po kruhovej dráhe a že spektrálna čiara ionizovaného vápnika s vlnovou dĺžkou $3933{,}66\,\mathring{A}$ mení svoju polohu o $\pm$ $0{,}63\,\mathring{A}$. Pomocou strednopásmovej (Strömgrenovej) fotometrie určili hmotnosť červeného obra na $5\,\mathit{M}_\Sun$. Vypočítajte polos dráhy dvojhviezdy.

<details class="solution">
<summary>Riešenie</summary>

Dopplerov posun vo frekvencii pulzaru aj vo vlnovej dĺžke čiary vápnika nastáva kvôli vzájomnému obehu pulzaru a hviezdy. Ak predpokladáme sklon dráhy $90^{\circ}$, ich obežné rýchlosti vieme dopočítať priamo zo vzorca pre Dopplerov jav 

$$
\frac{v_\textrm{p}}{c}=\frac{\lambda-\lambda_0}{\lambda_0}=\frac{\frac{c}{f}-\frac{c}{f_0}}{\frac{c}{f_0}}=\frac{f_0-f}{f} \, . \tag{1}
$$

 Vlastná frekvencia pulzaru je priemerom jej krajných nameraných hodnôt 

$$
f_0=\frac{699,650175+700,350175}{2}=700{,}000175\,\mathrm{Hz} \, , \tag{2}
$$

 

$$
v_\textrm{p}=\frac{f_0-f_1}{f_1}c=\frac{700,000175-699,650175}{699,650175}\cdot2{,}9979 \cdot 10^{8}=150\,\mathrm{km}\,{\mathrm{s}}^{-1} \, . \tag{3}
$$

 Rýchlosť hviezdy je 

$$
v_\textrm{h}=\frac{\Delta \lambda}{\lambda_0}c=\frac{0,63}{3933,66}\cdot2{,}9979 \cdot 10^{8}=48\,\mathrm{km}\,{\mathrm{s}}^{-1} \, . \tag{4}
$$

 Veľká polos vzájomnej dráhy dvojhviezdy je súčtom veľkých polosí jednotlivých zložiek 

$$
a=a_\textrm{p}+a_\textrm{h}=\frac{Pv_\textrm{p}}{2\pi}+\frac{Pv_\textrm{h}}{2\pi}=\frac{P}{2\pi}(v_\textrm{p}+v_\textrm{h}) \, , \tag{5}
$$

 

$$
\frac{4,5\cdot86400}{2\pi}\cdot(150+48)\cdot10^3=1{,}23 \cdot 10^{10}\,\mathrm{m}=0{,}08\,\mathrm{au} \, . \tag{6}
$$

</details>
