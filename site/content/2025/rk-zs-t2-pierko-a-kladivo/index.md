---
title: Pierko a kladivo
year: 2025
round: RK
roundName: Regionálne kolo
category: ZŠ
type: teoria
typeName: Teória
label: T2
weight: 1002
points: '70'
authors:
- Terézia Hanáková
hasSolution: true
source: 2025:2-RK/0-ZS/01-Pierko-a-kladivo/00-zadanie.tex
years:
- '2025'
rounds:
- Regionálne kolo
categories:
- ZŠ
types:
- Teória
topics:
- Nezaradené
---

## Zadanie

Uvažujte, že na Mesiaci sa nenachádza vzduch a že tiažové zrýchlenie na jeho povrchu je rovné gravitačnému zrýchleniu, ktoré má hodnotu $1{,}6\,\mathrm{m}\,{\mathrm{s}}^{-2}$. Astronauti na Mesiaci spravili experiment, pri ktorom naraz pustili z rovnakej výšky $1{,}6\,\mathrm{m}$ pierko a kladivo. Viete, že hmotnosť pierka je $30\,\mathrm{g}$, hmotnosť kladiva $1{,}3\,\mathrm{kg}$ a hmotnosť Mesiaca $7{,}3 \cdot 10^{22}\,\mathrm{kg}$.

<ol type="a">

<li>

<span class="body">[15 b]</span> Aká gravitačná sila pôsobila na pierko a aká na kladivo?

</li>

<li>

<span class="body">[55 b]</span> Ktoré teleso dopadlo skôr? Vypočítajte číselne pre pierko i kladivo.

</li>

</ol>

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Sily, ktoré pôsobia na pierko a kladivo si vieme vypočítať pomocou gravitačného zákona 

$$
F_g = G \frac{mM}{r^2} \,. \tag{1}
$$

 Napíšeme si ho pre pierko a kladivo 

$$
F_{g,p} = G \frac{M_\Mo m_p}{r^2} \a
F_{g,k} = G \frac{M_\Mo m_k}{r^2} \,. \tag{2}
$$

 A dosadíme hodnoty 

$$
\begin{align*}
F_{g,p} &= G \frac{M_\Mo m_p}{(R_\Mo + h)^2} = 6{,}674 \cdot 10^{-11}\,{\mathrm{m}}^{3}\,{\mathrm{kg}}^{-1}\,{\mathrm{s}}^{-2} \cdot \frac{7{,}3 \cdot 10^{22}\,\mathrm{kg} \cdot 0{,}03\,\mathrm{kg}}{(1\,737\,000\,\mathrm{m}+1{,}6\,\mathrm{m})^2} \approx 0{,}048\,\mathrm{N}\,, \tag{3}\\
F_{g,k} &= G \frac{M_\Mo m_k}{(R_\Mo + h)^2} = 6{,}674 \cdot 10^{-11}\,{\mathrm{m}}^{3}\,{\mathrm{kg}}^{-1}\,{\mathrm{s}}^{-2} \cdot \frac{7{,}3 \cdot 10^{22}\,\mathrm{kg} \cdot 1{,}3\,\mathrm{kg}}{(1\,737\,000\,\mathrm{m}+1{,}6\,\mathrm{m})^2} \approx 2{,}1\,\mathrm{N} \,. \tag{4}\end{align*}
$$

</li>

<li>

To, ako sú pierko a kladivo urýchľované zistíme pomocou zrýchlenia $g$, ktoré vystupuje v Newtonovom zákone sily 

$$
F_g = mg \,, \tag{5}
$$

 v ktorom sa gravitačná sila môže zapísať aj gravitačným zákonom 

$$
F_g = G \frac{mM}{r^2} \,. \tag{6}
$$

Tieto vzťahy (5) a (6) si napíšeme pre pierko a kladivo 

$$
\begin{align*} 
F_{g,p} = m_p g_p &\a
F_{g,k} = m_k g_k \,, \tag{7}\\
F_{g,p} = G \frac{M_\Mo m_p}{r^2} &\a
F_{g,k} = G \frac{M_\Mo m_k}{r^2} \,. \tag{8}\end{align*}
$$

Ak teraz spojíme tieto rovnice, dostávame 

$$
m_p g_p = G \frac{M_\Mo m_p}{r^2} \a
    m_k g_k = G \frac{M_\Mo m_k}{r^2} \,. \tag{9}
$$

Z oboch rovníc sa vykrátia hmotnosti pierka a kladiva, čím dostávame vzťah pre gravitačné zrýchlenie na Mesiaci 

$$
g_p = G \frac{M_\Mo}{r^2} \a
g_k = G \frac{M_\Mo}{r^2} \,. \tag{10}
$$

Z týchto rovníc už vidíme, že sa rovnajú, pretože výška h, z ktorej púšťame pierko aj kladivo je rovnaká. Platí, že $r = R_\Mo + h$, kde h = $1{,}6\,\mathrm{m}$. Môžeme si dosadiť a získame hodnotu 

$$
g_p = g_k = g = G \frac{M_\Mo}{(R_\Mo + h)^2} \,, \tag{11}
$$

 

$$
g = 6{,}674 \cdot 10^{-11}\,{\mathrm{m}}^{3}\,{\mathrm{kg}}^{-1}\,{\mathrm{s}}^{-2} \cdot \frac{7{,}3 \cdot 10^{22}\,\mathrm{kg}}{(1\,737\,000\,\mathrm{m} +1{,}6\,\mathrm{m})^2} \approx 1{,}6\,\mathrm{m}\,{\mathrm{s}}^{-2} \,. \tag{12}
$$

To je tiež hodnota v zadaní. Platí teda, že pierko aj kladivo sú urýchľované rovnakým zrýchlením, a tým pádom padajú na povrch Mesiaca voľným pádom, ktorého dráha má vzťah 

$$
h = \frac{1}{2}gt^2 \,. \tag{13}
$$

Pre pierko a kladivo 

$$
h_p = \frac{1}{2}gt_p^2 \a
    h_k = \frac{1}{2}gt_k^2 \,. \tag{14}
$$

Ak výška $h_p = h_k = h$, vieme si vyjadriť čas t 

$$
t_p = \sqrt{\frac{2h}{g}} \a
    t_k = \sqrt{\frac{2h}{g}} \,. \tag{15}
$$

Vidíme, že $t_p = t_k$, čím sme aj matematicky dokázali, že dopadnú v rovnakom čase, a to konkrétne za 

$$
t = \sqrt{\frac{2 \cdot 1{,}6\,\mathrm{m}}{1{,}6\,\mathrm{m}\,{\mathrm{s}}^{-2}}} \approx 1{,}4\,\mathrm{s} \tag{16}
$$

Keby bol na Mesiaci vzduch, pôsobilo by medzi pierkom a kladivom trenie, kvôli čomu by kladivo dopadlo na zem skôr ako pierko, no vo vákuu trenie neexistuje, a preto sú všetky telesá priťahované k zemi rovnakým gravitačným zrýchlením, ktoré nezávisí na ich hmotnosti.

</li>

</ol>

</details>

## Komentár autora

Experiment vykonal astronaut David Scott na Mesiaci počas misie Apollo 15.
