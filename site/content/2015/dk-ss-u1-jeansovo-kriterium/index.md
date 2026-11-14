---
title: Jeansovo kritérium
year: 2015
round: DK
roundName: Domáce kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú1
weight: 3001
hasSolution: true
source: ZAO:I_Zadania/06_FyzHaP/06_SS_DK.tex
years:
- '2015'
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

Odvoďte tzv. „Jeansovo“ kritérium – t.j. kritickú hmotnosť hmloviny potrebnú pre vznik hviezd. Hmlovinu považujte za nerotujúcu a sféricky symetrickú. Pomôcka: vychádzajte z rovnosti kinetickej a potenciálnej energie plynu. Potenciálna energia gule je daná vzťahom: $E_\textrm{P} = -\frac{3}{5}\frac{GM^2}{R}$, kde $M$ je hmotnosť, $R$ polomer hmloviny, $G$ gravitačná konštanta.

<details class="solution">
<summary>Riešenie</summary>

Pre systém v rovnováhe platí viriálová veta 

$$
2E_\textrm{k}+E_\textrm{p}=0 \tag{1}
$$

 V prípade, že prevládne gravitačná potenciálna energia, dôjde ku kolapsu, ak prevládne kinetická energia, oblak sa rozplynie. Rovnica vyššie popisuje hraničný stav.\
Využijeme vzťah pre potenciálnu energiu zo zadania. Celkovú kinetickú energiu oblaku odhadneme ako kinetickú energiu ideálneho plynu s teplotou $T$ 

$$
E_\textrm{k}=\frac{3}{2}Nk_\textrm{B}T \, , \tag{2}
$$

 

$$
2\cdot\frac{3}{2}Nk_\textrm{B}T-\frac{3}{5}\frac{GM^2}{R}=0 \, . \tag{3}
$$

 Celková hmotnosť oblaku je $M=Nm$, kde $N$ je počet častíc a $m$ je hmotnosť jednej častice 

$$
R^3=\frac{3M}{4\pi\rho} \, , \tag{4}
$$

 

$$
\frac{k_\textrm{B}T}{m}=\frac{GM}{5R} \, , \tag{5}
$$

 

$$
\left(\frac{k_\textrm{B}T}{m}\right)^3=\frac{G^3M^3}{5^3R^3} \, , \tag{6}
$$

 

$$
\left(\frac{k_\textrm{B}T}{m}\right)^3=\frac{G^3M^3}{5^3}\frac{4\pi\rho}{3M} \, . \tag{7}
$$

 Ak hmotnosť oblaku presiahne kritickú Jeansovu hmotnosť $M_\textrm{J}$, tak dôjde ku kolapsu 

$$
M_\textrm{J}=\left(\frac{k_\textrm{B}T}{m}\right)^{3/2}\sqrt{\frac{375}{4\pi G^3 \rho}} \, . \tag{8}
$$

</details>
