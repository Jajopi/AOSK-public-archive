---
title: Zem pri pohľade z družice
year: 2014
round: DK
roundName: Domáce kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú2
weight: 302
hasSolution: true
source: ZAO:I_Zadania/02_GmtrCas/02_SS_DK.tex
rocniky:
- '2014'
kola:
- Domáce kolo
kategorie:
- SŠ
typy:
- Teória
tagy:
- Geometria a čas
collection: ZAO
---

## Zadanie

Z akej výšky $h$ (v km) nad povrchom môže umelá družica Zeme zobraziť presne polovicu povrchu plochy privrátenej pologule našej planéty? Zem považujte za dokonalú guľu bez atmosféry s polomerom $6378\,\mathrm{km}$.

<details class="solution">
<summary>Riešenie</summary>

Povrch plochy privrátenej pologule Zeme je $S=2\pi R_{\Ea}^2$, plocha povrchu guľového vrchlíka je $S_\textrm{V}=2\pi R_{\Ea}v$. Požadujeme, aby družica mohla zobraziť polovicu privrátenej pologule, teda musí platiť $S_\textrm{V}=\frac{1}{2}S$. Z toho dostaneme $v=\frac{1}{2}R_{\Ea}$, hraničná zemepisná šírka, ktorú bude družica pozorovať bude teda 

$$
\sin{\varphi}=\frac{R_{\Ea}-v}{R_{\Ea}}=\frac{1}{2} \, , \tag{1}
$$

 

$$
\varphi=30^{\circ} \, . \tag{2}
$$

 Pre túto zemepisnú šírku zároveň platí vzťah 

$$
\sin{\varphi}=\frac{R_{\Ea}}{R_{\Ea}+h} \, . \tag{3}
$$

 Požadovaná výška družice nad povrchom Zeme je 

$$
h=\frac{6378}{\sin{30^{\circ}}}-6378=6378\,\mathrm{km} \, . \tag{4}
$$

<figure>

<div class="fig-images"><img class="invert" src="AO2014_SS_DK_2.svg" alt="obrázok" loading="lazy" style="width:50%"></div>

</figure>

</details>
