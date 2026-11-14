---
title: Úloha 5
year: 2007
round: DK
roundName: Domáce kolo
category: ZŠ
type: teoria
typeName: Teória
label: Ú5
weight: 5
hasSolution: true
source: ZAO:I_Zadania/08_Rozsiahle/08_ZS_DK.tex
years:
- '2007'
rounds:
- Domáce kolo
categories:
- ZŠ
types:
- Teória
topics:
- Rozsiahle príklady
collection: ZAO
---

## Zadanie

Na obrazovku monitora pri rozlíšení 800 x 600 pixelov chceme zobraziť jednoduchú mapku oblohy, ktorá by zobrazovala hviezdy do 5. magnitúdy tak, aby svetový rovník prechádzal vodorovne stredom monitora. Zobrazenie, ktoré použijeme je tzv. štvorcové a teda rektascenzia na mapke narastá zľava doprava tak, že na jeden stupeň pripadá $k$ pixelov a deklinácia narastá zdola nahor s tou istou mierkou $k$.

<ol type="a">

<li>

Akú veľkosť konštanty k zvolíme, aby v mapka obsahovala hviezdy s rektascenziou od $140^{\circ}$ do $220^{\circ}$?

</li>

<li>

Aká hodnota deklinácie bude pri spodnom okraji obrazovky a aká pri hornom okraji?

</li>

<li>

Odvoďte vzorec na výpočet súradnice $x$ hviezdy v závislosti na rektascenzii $\alpha$ a vzorec na výpočet súradnice $y$ z deklinácie $\delta$, ak sa obidve veličiny sa zadávajú v stupňoch a ľavý dolný roh monitora má súradnice $(0, 0)$.

</li>

<li>

Aké budú súradnice $(x, y)$ obrazu hviezdy Regulus ($\alpha = 10^{\mathrm{h}}\,08^{\mathrm{min}}$, $\delta = -11^{\circ}\,58'$)?

</li>

<li>

Ak budeme hviezdy 5. magnitúdy zobrazovať ako body pozostávajúce z jedného pixela, aký priemer kotúčika (v pixloch) by mal mať obraz hviezdy 0. magnitúdy? Vychádzajte z požiadavky, aby plochy kotúčikov obrazov hviezd rôznych jasností boli úmerné osvetleniu týchto hviezd.

</li>

</ol>

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Celkovo potrebujeme 800 pixelmi pokryť rektascenziu v rozsahu $220^{\circ}-140^{\circ}=80^{\circ}$. Na jeden stupeň pripadá $k=10$ pixelov.

</li>

<li>

Na výšku máme 600 pixelov, dokážeme pokryť deklináciu s rozsahom $\frac{600}{k}=\frac{600}{10}=60^{\circ}$. Keďže rovník má prechádzať stredom, pri dolnom okraji musí byť deklinácia $-30^{\circ}$ a pri hornom okraji deklinácia $30^{\circ}$.

</li>

<li>

V bode v ľavom dolnom rohu so súradnicami $(x,y)=(0,0)$ musia byť rektascenzia a deklinácia $(\alpha,\delta)=(140^{\circ},-30^{\circ})$. Súradnice $x$ a $y$ sú lineárne závislé na $\alpha$ a $\delta$, preto pre ne musia platiť rovnice

</li>

</ol>

$$
x=k\alpha+a \, , \tag{1}
$$

 

$$
y=k\delta+d \, . \tag{2}
$$

 Dosadením požadovaných hodnôt v ľavom dolnom rohu dostaneme $a$ a $d$ 

$$
0=10\cdot140^{\circ}+a \, , \tag{3}
$$

 

$$
0=10\cdot(-30^{\circ})+d \, . \tag{4}
$$

 Vyjdú hodnoty $a=-1400$ a $d=300$.

<ol type="a" start="4">

<li>

Rektascenzia hviezdy Regulus prepočítaná na stupne je $\alpha=152^{\circ}$, deklinácia je $\delta=-11{,}97^{\circ}$. Dosadíme ich do rovníc odvodených v časti c), $x=10\cdot152^{\circ}-1400=120$, $y=-10\cdot11{,}97^{\circ}+300=180,3$. Hviezda Regulus bude mať súradnice $(x,y)=(120,180)$.

</li>

<li>

Hviezda 0. magnitúdy je 100-krát jasnejšia ako hviezda 5. magnitúdy.

</li>

</ol>

$$
\frac{I_0}{I_5}=100=\frac{D_0^2}{D_5^2}=\frac{D_0^2}{1} \, . \tag{5}
$$

 Priemer kotúčika hviezdy 0. magnitúdy bude $D_0=10$ pixelov.

</details>
