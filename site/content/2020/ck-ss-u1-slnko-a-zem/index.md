---
title: Slnko a Zem
year: 2020
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú1
weight: 5001
hasSolution: true
source: ZAO:I_Zadania/08_Rozsiahle/08_SS_FI.tex
years:
- '2020'
rounds:
- Celoštátne kolo
categories:
- SŠ
types:
- Teória
topics:
- Rozsiahle príklady
collection: ZAO
---

## Zadanie

Uvažujme hypotetický prípad, kedy sa Zem začne otáčať okolo svojej osi tak, aby mala so Slnkom viazanú rotáciu (pod. ako má Mesiac so Zemou). V takomto prípade je vždy jedna celá pologuľa Zeme natočená k Slnku a druhá je od neho vždy odvrátená. Teraz ale Zem rozdelíme (cez celú planétu) dokonale izolujúcou stenou ktorá izoluje privrátenú a odvrátenú stranu Zeme. Teda sa neprenáša žiadne teplo z osvetlenej strany na neosvetlenú. Známe veličiny:

- $a_{\Ea}$ vzdialenosť Zeme od Slnka,

- $R_{\Ea}$, $R_{\Sun}$ polomer Zeme, Slnka,

- $\lambda_{\Sun}$ vlnová dĺžka na ktorej Slnko vyžaruje najintenzívnejšie,

- všetky fundamentálne konštanty.

<ol type="a">

<li>

Aká je perióda otáčania sa Zeme okolo vlastnej osi keď má viazanú rotáciu? Aký je smer otáčania? Situáciu nakreslite.

</li>

<li>

Aká je teplota povrchu na privrátenej strane Zeme k Slnku? Uvažujte, že Zem aj Slnko sa správajú ako absolútne čierne teleso. Viete, že všetka energia ktorá dopadá na privrátenú stranu je iba zo Slnka?

</li>

<li>

Aká je teplota na odvrátenej strane Zeme, na ktorú nedopadá absolútne žiadna energia zo Slnka?

</li>

</ol>

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Keďže Zem bude mať viazanú rotáciu, tak na jeden obeh okolo Slnka požadujeme aby sa Zem taktiež otočila presne o $360^{\circ}$. Takže jeden deň bude trvať rovnako ako siderický rok, tj. 365,256 stredných slnečných dní.

</li>

<li>

Keďže poznáme iba vlnovú dĺžku na ktorej Slnko vyžaruje najintenzívnejšie, tak je potrebné, aby sme si ju previedli na teplotu povrchu (fakticky na efektívnu teplotu, ale tú môžeme aproximovať na reálnu teplotu)

</li>

</ol>

$$
T_{\Sun}=\frac{b}{\lambda_{\Sun}} \, . \tag{1}
$$

 Vyžarovaný výkon z celého povrchu Slnka je 

$$
L=4\pi R_{\Sun}^2\sigma T_{\Sun}^4 \, . \tag{2}
$$

 Teplotu Slnka si vyjadríme cez vlnovú dĺžku žiarenia 

$$
L=4\pi R_{\Sun}^2\sigma \left(\frac{b}{\lambda_{\Sun}}\right)^4 \, . \tag{3}
$$

 Pri Zemi je žiarivý tok rovný 

$$
F=\frac{L}{4\pi a_{\Ea}^2}=\frac{4\pi R_{\Sun}^2\sigma \left(\frac{b}{\lambda_{\Sun}}\right)^4}{4\pi a_{\Ea}^2}=\frac{R_{\Sun}^2\sigma b^4}{a_{\Ea}^2\lambda_{\Sun}^4} \, . \tag{4}
$$

 Vieme, že príkon zo Slnka na Zem a výkon s akým Zem vyžaruje sa musia rovnať 

$$
P_{\Sun}=P_{\Ea} \, . \tag{5}
$$

 Príkon zo Slnka na Zem je rovný žiarivému toku zachytenému privrátenou pologuľou Zeme. Zem efektívne zachytáva žiarenie ako kruh s polomerom $R_{\Ea}$. 

$$
P_{\Sun}=F\pi R_{\Ea}^2=\frac{R_{\Sun}^2\sigma b^4}{a_{\Ea}^2\lambda_{\Sun}^4}\pi R_{\Ea}^2 \, . \tag{6}
$$

 Zem vyžaruje ako absolútne čierne teleso z celého povrchu pologule 

$$
P_{\Ea}=L_{\Ea}=2\pi R_{\Ea}^2\sigma T_{\Ea}^4 \, , \tag{7}
$$

 

$$
\frac{R_{\Sun}^2\sigma b^4}{a_{\Ea}^2\lambda_{\Sun}^4}\pi R_{\Ea}^2=2\pi R_{\Ea}^2\sigma T_{\Ea}^4 \, , \tag{8}
$$

 

$$
\frac{R_{\Sun}^2 b^4}{a_{\Ea}^2\lambda_{\Sun}^4}=2T_{\Ea}^4 \, , \tag{9}
$$

 

$$
T_{\Ea}^4=\frac{R_{\Sun}^2 b^4}{2a_{\Ea}^2\lambda_{\Sun}^4} \, , \tag{10}
$$

 

$$
T_{\Ea}=\sqrt[4]{\frac{1}{2}}\frac{b}{\lambda_{\Sun}}\sqrt{\frac{R_{\Sun}}{a_\Ea}} \, . \tag{11}
$$

<ol type="a" start="3">

<li>

Keďže jediná energia pochádza z mikrovlnného kozmického pozadia (CMB), tak teplota sa ustáli približne na hodnote teploty CMB, to je $2{,}73\,\mathrm{K}$.

</li>

</ol>

</details>
