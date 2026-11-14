---
title: Galaxie
year: 2015
round: DK
roundName: Domáce kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú4
weight: 3004
hasSolution: true
source: ZAO:I_Zadania/07_Kozmo/07_SS_DK.tex
years:
- '2015'
rounds:
- Domáce kolo
categories:
- SŠ
types:
- Teória
topics:
- Kozmológia
collection: ZAO
---

## Zadanie

Základným predpokladom kozmologických modelov je, že vesmír je homogénny, t.j. obsahuje všade rovnaké množstvo hmoty (galaxií). Tento fakt sa dá overiť pozorovaním magnitúdového rozdelenia galaxií. Vypočítajte pomer počtu galaxií $m+1$ magnitúdy $N_{m+1}$ k počtu galaxií $m$ magnitúdy $N_m$ za týchto predpokladov:

<ol type="a">

<li>

Skúmané galaxie sú rozložené v celom vesmíre homogénne s koncentráciou $\rho$.

</li>

<li>

Absolútna jasnosť všetkých skúmaných galaxií je rovnaká.

</li>

</ol>

<details class="solution">
<summary>Riešenie</summary>

Pre absolútnu magnitúdu platí vzorec 

$$
M=m+5-5\log r \, . \tag{1}
$$

 Galaxie so zdanlivou magnitúdou $m$ sa nachádzajú vo sférickej vrstve s polomerom $r_\textrm{m}$ a hrúbkou $dr$. Objem takejto vrstvy je 

$$
V=4\pi r_\textrm{m}^2 dr \, . \tag{2}
$$

 Polomer $r_m$ vyjadríme zo vzorca pre absolútnu magnitúdu 

$$
r_\textrm{m}=10^{\frac{m+5-M}{5}} \, . \tag{3}
$$

 Počet galaxií vo vrstve je 

$$
N_\textrm{m}=4\pi r_\textrm{m}^2 \rho dr \, . \tag{4}
$$

 Podobne, galaxie s rovnakou absolútnou magnitúdou $M$ a zdanlivou magnitúdou $m$+1 sa nachádzajú v guľovej vrstve s polomerom $r_\textrm{m+1}$ a ich počet je 

$$
N_\textrm{m+1}=4\pi r_{m+1}^2 \rho dr \, . \tag{5}
$$

 Pre polomer vrstvy platí 

$$
r_\textrm{m+1}=10^{\frac{m+1+5-M}{5}} \, . \tag{6}
$$

 Pomer počtu galaxií je 

$$
\frac{N_\textrm{m+1}}{N_\textrm{m}}=\frac{r_\textrm{m+1}^2}{r_\textrm{m}^2}=10^{2\cdot\frac{m+1+5-M}{5}-2\cdot\frac{m+5-M}{5}}=10^{\frac{2}{5}} \, . \tag{7}
$$

</details>
