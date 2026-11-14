---
title: Úloha 5
year: 2013
round: DK
roundName: Domáce kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú5
weight: 3005
hasSolution: true
source: ZAO:I_Zadania/02_GmtrCas/02_SS_DK.tex
years:
- '2013'
rounds:
- Domáce kolo
categories:
- SŠ
types:
- Teória
topics:
- Geometria a čas
collection: ZAO
---

## Zadanie

Okolo hviezdy 58Tuc (spektrálna trieda A0V s hmotnosťou $2\,\mathit{M}_\Sun$) obieha planéta ADAM (obiehajúca retrográdne vo vzdialenosti $0{,}7\,\mathrm{au}$ so siderickou rotačnou dobou iba 6 hodín). Vypočítajte, koľko trvá solárny deň na planéte ADAM s hmotnosťou 2x väčšou, ako má Jupiter, za predpokladu, že planéta rotuje retrográdne. Koľko by trval, ak by rotácia planéty bola prográdna?

<details class="solution">
<summary>Riešenie</summary>

Obežná doba planéty je 

$$
P^2=\frac{4\pi^2a^3}{G(M+m)} \, , \tag{1}
$$

 

$$
P=2\pi \sqrt{\frac{(0,7\cdot1{,}496 \cdot 10^{11})^3}{6{,}67 \cdot 10^{-11}\cdot2\cdot1{,}9891 \cdot 10^{30}}}=1{,}31 \cdot 10^{7}\,\mathrm{s}=3631\,\mathrm{h} \, . \tag{2}
$$

 Planéta obieha okolo hviezdy retrográdne, to znamená, že obieha v opačnom zmysle ako rotuje hviezda. V zadaní sa nás najskôr pýtajú na dĺžku trvania solárneho dňa v prípade retrográdnej rotácie, teda keď planéta nielen obieha, ale aj rotuje v opačnom zmysle ako hviezda. To ale znamená, že planéta rotuje v rovnakom zmysle ako obieha okolo hviezdy a preto môžeme na výpočet synodickej rotačnej doby použiť vzorec, ktorý sa bežne používa pre prográdnu rotáciu a obeh.\
Siderická rotačná perióda je $T=6\,\mathrm{h}$. Synodická rotačná doba v prípade retrográdnej rotácie je 

$$
S_\textrm{R}=\frac{1}{\frac{1}{T}+\frac{1}{P}}=\frac{1}{\frac{1}{6}+\frac{1}{3631}}=5^{\mathrm{h}}\,59^{\mathrm{min}}\,25^{\mathrm{s}} \, . \tag{3}
$$

 Na výpočet synodickej doby v prípade prográdnej rotácie zase použijeme vzorec, ktorý sa bežne využíva pre prográdny obeh a retrográdnu rotáciu. Dostaneme 

$$
S_\textrm{P}=\frac{1}{\frac{1}{T}-\frac{1}{P}}=\frac{1}{\frac{1}{6}-\frac{1}{3631}}=6^{\mathrm{h}}\,0^{\mathrm{min}}\,36^{\mathrm{s}} \, . \tag{4}
$$

</details>
