---
title: Úloha 4
year: 2015
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú4
weight: 2304
hasSolution: true
source: ZAO:I_Zadania/04_FotoSpek/04_SS_FI.tex
rocniky:
- '2015'
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

Žiarenie prichádzajúce zo Slnka na Zem musí najprv prekonať atmosféru Zeme, kým dopadne na jej povrch. Zem tiež uvoľňuje žiarenie do priestoru a toto žiarenie musí tiež prechádzať atmosférou do kozmického priestoru. Je známe, že prestupnosť slnečného žiarenia cez atmosféru počas prechodu ($t_1$) je vyššia ako prestupnosť žiarenia zo Zeme von ($t_2$). Nech $T_{\Sun}$ je efektívna teplota Slnka, $R_\Sun$ je polomer Slnka, $R_\Ea$ je polomer Zeme a $x$ je vzdialenosť Zeme od Slnka. Odvoďte teplotu zemského povrchu ako funkciu vyššie uvedených parametrov, pričom je isté, že množstvo prijatého a vyžiareného žiarenia Zemou je rovnaké (Zem je v tepelnej rovnováhe).

<details class="solution">
<summary>Riešenie</summary>

Svietivosť Slnka je 

$$
L_{\Sun}=4\pi R_{\Sun}^2\sigma T_{\Sun}^4 \, . \tag{1}
$$

 Do vzdialenosti $1\,\mathrm{au}$ od Slnka dopadá tok 

$$
F=\frac{4\pi R_{\Sun}^2\sigma T_{\Sun}^4}{4\pi x^2} \, . \tag{2}
$$

 Výkon, ktorý zachytí Zem je 

$$
P_1=t_1 \pi R_{\Ea}^2 F=\frac{R_{\Sun}^2\sigma T_{\Sun}^4}{x^2}t_1 \pi R_{\Ea}^2 \, . \tag{3}
$$

 Výkon, ktorý Zem vyžiari je 

$$
P_2= t_2 4\pi R_{\Ea}^2\sigma T_{\Ea}^4 \, . \tag{4}
$$

 Teplotu Zeme zistíme z rovnosti prijatého a vyžiareného množstva energie $P_1=P_2$ 

$$
\frac{R_{\Sun}^2\sigma T_{\Sun}^4}{x^2}t_1 \pi R_{\Ea}^2=t_2 4\pi R_{\Ea}^2\sigma T_{\Ea}^4 \, , \tag{5}
$$

 

$$
T_{\Ea}^4=\frac{R_{\Sun}^2T_{\Sun}^4t_1}{4t_2x^2} \, , \tag{6}
$$

 

$$
T_{\Ea}=\sqrt{\frac{R_{\Sun}}{2x}\sqrt{\frac{t_1}{t_2}}}T_{\Sun} \, . \tag{7}
$$

</details>
