---
title: Pulzar
year: 2008
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú1
weight: 5001
hasSolution: true
source: ZAO:I_Zadania/06_FyzHaP/06_SS_FI.tex
years:
- '2008'
rounds:
- Celoštátne kolo
categories:
- SŠ
types:
- Teória
topics:
- Fyzika hviezd a planét
collection: ZAO
---

## Zadanie

Pulzar v Krabej hmlovine je neutrónová hviezda s hmotnosťou $2{,}8 \cdot 10^{30}\,\mathrm{kg}$ a polomerom $10\,\mathrm{km}$, ktorá rotuje s periódou $30\,\mathrm{ms}$. Od doby jej vzniku keď rotovala s oveľa kratšou periódou, sa spomaľovala tempom, pri ktorom pokles rotačnej kinetickej energie je nepriamo úmerný štvrtej mocnine periódy.\
Vypočítajte približne pred akou dobou vybuchla supernova, pri ktorej vznikla táto neutrónová hviezda ak vieme, že súčasná pozorovaná časová derivácia periódy je $5 \cdot 10^{-13}$.

<details class="solution">
<summary>Riešenie</summary>

Úloha sa dá vyriešiť dvomi spôsobmi. Na presnejší výpočet je potrebné použiť integrály a derivácie. Najskôr vypočítame časovú deriváciu kinetickej energie. 

$$
E_\textrm{k}=\frac{1}{2}I\omega^2=\frac{1}{2}I\frac{4\pi^2}{P^2}=\frac{2\pi^2I}{P^2} \, , \tag{1}
$$

 

$$
\frac{dE_\textrm{k}}{dt}=-4\pi^2I\frac{1}{P^3}\frac{dP}{dt} \, . \tag{2}
$$

 Zo zadania vieme, že derivácia kinetickej energie je nepriamo úmerná štvrtej mocnine periódy, teda platí 

$$
\frac{dE_\textrm{k}}{dt}=\frac{C}{P^4} \, . \tag{3}
$$

 $C$ je konštanta úmernosti. Celkovo dostaneme rovnosť 

$$
\frac{C}{P^4}=-4\pi^2I\frac{1}{P^3}\frac{dP}{dt} \, . \tag{4}
$$

 Všetky konštanty presunieme na ľavú stranu rovnice a dostaneme nasledujúcu diferenciálnu rovnicu 

$$
\frac{C}{-4\pi^2 I}=P\frac{dP}{dt}=K \, . \tag{5}
$$

 Ľavá strana rovnice je konštanta, jej hodnota je 

$$
K=P\frac{dP}{dt}=0,03\cdot5 \cdot 10^{-13}=1{,}5 \cdot 10^{-14}\,\mathrm{s} \, . \tag{6}
$$

 Diferenciálnu rovnicu vyriešime separáciou premenných 

$$
\int_0^TKdt=\int_0^P P'dP' \, . \tag{7}
$$

 Integračné medze sme vybrali nasledujúcim spôsobom: v čase $t=0$ vybuchla supernova a vznikla neutrónová hviezda, čas $t=T$ je súčasnosť a teda zároveň aj vek neutrónovej hviezdy. Na začiatku bola rotačná perióda veľmi malá oproti súčasnej, zobrali sme limitný prípad, kedy by na začiatku existencie bola $P=0$, teraz je perióda rotácie $P=30\,\mathrm{ms}$. Po integrovaní dostaneme rovnosť 

$$
KT=\frac{P^2}{2} \, , \tag{8}
$$

 

$$
T=\frac{P^2}{2K}=\frac{0,03^2}{2\cdot1{,}5 \cdot 10^{-14}}=3 \cdot 10^{10}\,\mathrm{s}=950\,\mathrm{rokov} \, . \tag{9}
$$

 Supernova vybuchla pred približne 950 rokmi. Úlohu je možné riešiť aj bez použitia integrálov a derivácií, ak predpokladáme, že zmena periódy v čase bola konštantná. V tom prípade sa rotačná perióda zmenila z hodnoty blízkej 0 na dnešnú periódu $P=30\,\mathrm{ms}$. Týmto spôsobom dostaneme horný odhad veku pulzaru $T$ 

$$
\frac{P}{T}\approx 5 \cdot 10^{-13} \, , \tag{10}
$$

 

$$
T=\frac{P}{5 \cdot 10^{-13}}=\frac{0,03}{5 \cdot 10^{-13}}=6 \cdot 10^{10}\,\mathrm{s}=1900\,\mathrm{rokov} \, . \tag{11}
$$

 Týmto spôsobom nám vyšiel aspoň horný odhad veku pulzaru, ktorý je zhruba 2-krát väčší ako skutočný vek.

</details>
