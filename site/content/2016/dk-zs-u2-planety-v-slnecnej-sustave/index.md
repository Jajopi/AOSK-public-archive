---
title: Planéty v Slnečnej sústave
year: 2016
round: DK
roundName: Domáce kolo
category: ZŠ
type: teoria
typeName: Teória
label: Ú2
weight: 2
hasSolution: true
source: ZAO:I_Zadania/02_GmtrCas/02_ZS_DK.tex
years:
- '2016'
rounds:
- Domáce kolo
categories:
- ZŠ
types:
- Teória
topics:
- Geometria a čas
collection: ZAO
---

## Zadanie

Vypočítajte vzájomnú vzdialenosť Venuše a Marsu, ak je Venuša (pri pohľade zo Zeme) v najväčšej západnej elongácii (od Slnka) a Mars je v západnej kvadratúre. Uvažujte, že planéty obiehajú v jednej rovine po kruhových dráhach.

<details class="solution">
<summary>Riešenie</summary>

Spojnice Venuše a Marsu so Zemou a Slnkom vytvárajú v danej chvíli pravouhlé trojuholníky.

<figure>

<div class="fig-images"><img class="invert" src="AO2016_ZS_DK_2.svg" alt="obrázok" loading="lazy" style="width:50%"></div>

</figure>

Vzdialenosti Venuše aj Marsu od Zeme vypočítame z Pytagorovej vety 

$$
d_\textrm{ZV}=\sqrt{a_{\Ea}^2-a_{\Ve}^2}=\sqrt{1^2-0,723^2}=0{,}691\,\mathrm{au} \, , \tag{1}
$$

 

$$
d_\textrm{ZM}=\sqrt{a_{\Ma}^2-a_{\Ea}^2}=\sqrt{1,524^2-1^2}=1{,}15\,\mathrm{au} \, . \tag{2}
$$

 Pre uhol $\alpha$ platí 

$$
\alpha=\arcsin{\frac{a_{\Ve}}{a_{\Ea}}}=\arcsin{\frac{0,723}{1}}=46{,}3^{\circ} \, . \tag{3}
$$

 Uhol $\beta$ je jeho doplnkom do $90^{\circ}$, teda $\beta=90^{\circ}-\alpha=43{,}7^{\circ}$. Vzdialenosť Marsu od Venuše vypočítame z kosínusovej vety 

$$
d_\textrm{VM}^2=d_\textrm{ZV}^2+d_\textrm{ZM}^2+2d_\textrm{ZV}d_\textrm{ZM}\cos{\beta} \, , \tag{4}
$$

 

$$
d_\textrm{VM}=\sqrt{0,691^2+1,15^2-2\cdot0,691\cdot1,15\cdot\cos{46{,}3^{\circ}}}=0{,}84\,\mathrm{au} \, . \tag{5}
$$

</details>
