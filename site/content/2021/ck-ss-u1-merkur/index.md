---
title: Merkúr
year: 2021
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
- '2021'
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

Merkúr je najbližšia planéta k Slnku zaujímavá pomalou rotáciou a tým, že jeho rotačná os je kolmá na rovinu obehu. Predstavme si, že bývame na rovníku Merkúra.

<ol type="a">

<li>

Ako najvyššie nad obzor sa môže dostať Slnko?

</li>

<li>

Ako dlho je stred Slnka nad obzorom?

</li>

<li>

Ako dlho vychádza Slnko nad obzor?

</li>

</ol>

Uvažujte že Merkúr obieha okolo Slnka po kruhovej dráhe s periódou obehu $P = 88\,\mathrm{dní}$ a okolo vlastnej osi sa otočí (prográdne) za $t = 59\,\mathrm{dní}$.\
V skutočnosti však Merkúr obieha po eliptickej dráhe s pomerne veľkou excentricitou $e = 0{,}2$.

<ol type="a" start="4">

<li>

Ako dlho vychádza Slnko nad obzor v aféliu? Môžete použiť informáciu, že v perihéliu sa Merkúr pohybuje rýchlosťou $v_\mathrm{P} = 59\,\mathrm{km}\,{\mathrm{s}}^{-1}$ (vzhľadom na Slnko).

</li>

<li>

V istom momente sa Slnko na oblohe zastaví a začne sa hýbať opačným smerom. V akej vzdialenosti od Slnka sa vtedy nachádza Merkúr? Pomôcka: Finálnu rovnicu môžete riešiť numericky, napríklad iteračnou metódou.

</li>

</ol>

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Na úvod je dôležité si uvedomiť, že keďže je rotačná os kolmá na rovinu obehu, tak nebeský rovník je zhodný s ekliptikou, čo znamená, že Slnko sa hýbe po nebeskom rovníku. Ak sa nachádzame na rovníku Merkúra, tak máme nebeský rovník priamo nad sebou, teda kolmo nad obzorom. Najvyšší bod kam sa môže Slnko dostať je tým pádom zenit.

</li>

<li>

To, že je nebeský rovník kolmý na obzor nám výrazne zjednodušuje situáciu, keďže Slnko musí prejsť presne polovicu kružnice, čo je $180^{\circ}$. Musíme teda zrátať uhlovú rýchlosť Slnka na oblohe. Na tento pohyb vplýva rotácia Merkúra a jeho pohyb okolo Slnka. Merkúr rotuje v rovnakom smere ako obieha, teda synodický deň trvá na ňom dlhšie ako siderický – podobné ako na Zemi. Výsledná uhlová rýchlosť bude teda

</li>

</ol>

$$
\omega=\omega_\textrm{R}-\omega_\textrm{O} \, . \tag{1}
$$

 kde $\omega_\textrm{R}$ je uhlová rýchlosť rotácie a $\omega_\textrm{O}$ uhlová rýchlosť obehu. $\omega_\textrm{R}$ zistíme z doby otočenia okolo vlastnej osi 

$$
\omega_\textrm{R}=\frac{360^{\circ}}{t}=\frac{360}{59}=6{,}10^{\circ}\textrm{/deň} \, , \tag{2}
$$

 a $\omega_\textrm{O}$ z periódy obehu 

$$
\omega_\textrm{O}=\frac{360^{\circ}}{P}=\frac{360}{88}=4{,}09^{\circ}\textrm{/deň} \, . \tag{3}
$$

 Výsledná uhlová rýchlosť 

$$
\omega=\omega_\textrm{R}-\omega_\textrm{O}=6,10-4,09=2{,}01^{\circ}\textrm{/deň} \, . \tag{4}
$$

 Slnko nad obzorom prejde $180^{\circ}$, teda tam strávi dobu rovnú 

$$
T=\frac{180^{\circ}}{\omega}=\frac{0,5}{\frac{1}{t}-\frac{1}{P}}=\frac{Pt}{2(P-t)}=\frac{88\cdot59}{2\cdot(88-59)}=89{,}55\,\mathrm{dní} \, . \tag{5}
$$

 Tento vzorec sa tiež dal získať zo vzťahu na výpočet dĺžky synodického dňa.

<ol type="a" start="3">

<li>

Ako prvé potrebujeme vedieť ako ďaleko je Merkúr od Slnka. Keďže uvažujeme, že obieha po kruhovej dráhe, táto vzdialenosť je stále rovnaká, konkrétne ju vieme zistiť z 3. Keplerovho zákona platného pre veľkú polos v au a obežnú dobu v rokoch. Teda

</li>

</ol>

$$
a=\sqrt[3]{P^2}=\left(\frac{88}{365,25}\right)^{2/3}=0{,}387\,\mathrm{au}=5{,}8 \cdot 10^{10}\,\mathrm{m} \, . \tag{6}
$$

 Východ Slnka sa začína v momente, kedy sa jeho horný okraj dotkne horizontu a skončí, keď sa horizontu dotkne jeho dolný okraj. Slnko nad obzor vychádza kolmo, to znamená, že počas jeho východu sa pohne presne o svoj uhlový priemer. Ak by Slnko vychádzalo voči horizontu pod iným uhlom ako $90^{\circ}$, muselo by počas svojho východu prejsť dlhšiu uhlovú dráhu. Uhlový priemer Slnka vypočítame pomocou trigonometrie 

$$
\theta_\Sun =\frac{2R_\Sun}{a}=\frac{2\cdot6{,}955 \cdot 10^{8}}{5{,}8 \cdot 10^{10}}=0{,}024\,\mathrm{rad}=1{,}374^{\circ} \, . \tag{7}
$$

 Tým pádom čas potrebný na východ Slnka je 

$$
T_\textrm{V}=\frac{\theta_\Sun}{\omega}=\frac{1,374}{2,01}=0{,}684\,\mathrm{dňa}=16\,\mathrm{h}\;24\,\min \, . \tag{8}
$$

<ol type="a" start="4">

<li>

Slnko vychádza pomerne dlho, avšak v pomere k celému obehu je to málo. Preto môžeme aproximovať pohyb v aféliu na obeh po kružnici s polomerom rovným aféliovej vzdialenosti. Potrebujeme totižto zrátať novú uhlovú rýchlosť Slnka po oblohe $\omega_\textrm{A}$ a jeho uhlový priemer $\theta_\textrm{A}$

</li>

</ol>

$$
\omega_\textrm{A}=\omega_\textrm{R}-\omega_\textrm{O,A} \, , \tag{9}
$$

 

$$
\omega_\textrm{O,A}=\frac{v_\textrm{A}}{Q} \, . \tag{10}
$$

 $v_\textrm{A}$ je rýchlosť Merkúra v aféliu, ktorú vieme zistiť zo zákona zachovania momentu hybnosti 

$$
mv_\textrm{P}q=mv_\textrm{A}Q  \, , \tag{11}
$$

 

$$
v_\textrm{A}=v_\textrm{P}\frac{q}{Q} \, , \tag{12}
$$

 

$$
\omega_\textrm{O,A}=\frac{v_\textrm{P}q}{Q^2} \, . \tag{13}
$$

 kde $q$ je perihéliová a $Q$ aféliová vzdialenosť. Tie môžeme určiť pomocou excentricity 

$$
q=a(1-e) \, , \tag{14}
$$

 

$$
Q=a(1+e) \, . \tag{15}
$$

 Po dosadení je uhlová obežná rýchlosť 

$$
\omega_\textrm{O,A}=\frac{v_\textrm{P}}{a}\frac{1-e}{(1+e)^2}=\frac{59\,000}{5{,}8 \cdot 10^{10}}\cdot\frac{0,8}{1,2^2}=5{,}64 \cdot 10^{-7}\,\mathrm{rad}\,{\mathrm{s}}^{-1}=2{,}80^{\circ}\textrm{/deň} \, . \tag{16}
$$

 Veľkú poloos sme už vyrátali v minulom podzadaní a $v_\textrm{P}$, $e$ máme zadané. Posledná vec čo vplýva na dĺžku západu Slnka je jeho uhlová veľkosť 

$$
\theta_\textrm{A}=\frac{2R_\Sun}{Q}=\frac{2R_\Sun}{a(1+e)}=\frac{2\cdot6{,}955 \cdot 10^{8}}{5{,}8 \cdot 10^{10}\cdot1,2}=0{,}02\,\mathrm{rad}=1{,}145^{\circ} \, . \tag{17}
$$

 Finálne, trvanie východu Slnka bude teda trvať 

$$
T_\textrm{V,A}=\frac{\theta_\textrm{A}}{\omega_\textrm{A}}=\frac{\theta_\textrm{A}}{\omega_\textrm{R}-\omega_\textrm{O,A}}=\frac{1,145}{6,1-2,8}=0{,}347\,\mathrm{dní}=8\,\mathrm{h}\;20\,\min \, . \tag{18}
$$

<ol type="a" start="5">

<li>

Na to aby sa zastavil pohyb Slnka sa musia vyrovnať uhlové rýchlosti

</li>

</ol>

$$
\omega_\textrm{O,r}=\omega_\textrm{R} \, . \tag{19}
$$

 kde $\omega_\textrm{O,r}$ je obežná uhlová rýchlosť v mieste dráhy so vzdialenosťou $r$ od Slnka. Potrebujeme teda určiť obežnú uhlovú rýchlosť vo všeobecnom mieste dráhy. Podobne ako v (d) platí 

$$
\omega_\textrm{O,r}=\frac{v}{r} \, . \tag{20}
$$

 Rýchlosť $v$ vo vzdialenosti $r$ určíme pomocou rovnice vis-viva 

$$
v^2=GM_\Sun\left(\frac{2}{r}-\frac{1}{a}\right) \, . \tag{21}
$$

 Z čoho dostávame rovnicu pre vzdialenosť $r$ 

$$
\frac{\sqrt{GM_\Sun\left(\frac{2}{r}-\frac{1}{a}\right)}}{r}=\omega_\textrm{R}=\frac{2\pi}{t} \, . \tag{22}
$$

 Táto rovnica je kubická, preto je ju najjednoduchšie riešiť numericky iteračnou metódou. Ako prvé si vyjadríme $r$ pomocou $r$. Potom za $r$ na pravej strane dosadíme náš úvod odhad $r_0$ a dostaneme nasledujúce priblíženie $r_1$. Takto pokračujeme až kým nie je presnosť dostačujúca. Vyjadrenie pre $r$ je nasledujúce 

$$
r=\frac{t}{2\pi}\sqrt{GM_\Sun\left(\frac{2}{r}-\frac{1}{a}\right)} \, . \tag{23}
$$

 Ako $r_0$ zoberieme veľkú polos $a=5{,}8 \cdot 10^{10}\,\mathrm{m}$. Po asi 30-tich iteráciách dôjdeme ku výsledku 

$$
r=4{,}7 \cdot 10^{10}\,\mathrm{m}=0{,}314\,\mathrm{au} \, . \tag{24}
$$

 Vzdialenosť $r$ je možné vypočítať aj analyticky, je to ale veľmi náročné.

</details>
