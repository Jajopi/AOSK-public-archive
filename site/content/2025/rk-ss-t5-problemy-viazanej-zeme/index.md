---
title: Problémy viazanej Zeme
year: 2025
round: RK
roundName: Regionálne kolo
category: SŠ
type: teoria
typeName: Teória
label: T5
weight: 1305
points: '60'
authors:
- Samuel Amrich
hasSolution: true
source: 2025:2-RK/1-SS/01-Problemy-viazanej-Zeme/00-zadanie.tex
rocniky:
- '2025'
kola:
- Regionálne kolo
kategorie:
- SŠ
typy:
- Teória
tagy:
- Nezaradené
---

## Zadanie

Jeden z možných pohľadov na to, prečo si Zem stále drží atmosféru, je, že typická rýchlosť molekúl $\Bar{v}$ v atmosfére je menšia ako druhá kozmická rýchlosť. Typická rýchlosť molekuly plynu je daná Maxwellovým-Boltzmanovým rozdelením ako 

$$
\Bar{v}=\sqrt{\frac{2RT}{M}} \, , \tag{1}
$$

 kde $R$ je univerzálna plynová konštanta, $T$ je teplota a $M$ je hmotnosť molekuly. Pre molekulu dusíka $\textrm{N}_{2}$ pri teplote $T_0=20\,^{\circ}\mathrm{C}$ máme $\Bar{v_0}=422\,\mathrm{m}\,{\mathrm{s}}^{-1}$, čo je výrazne menej ako druhá kozmická rýchlosť $v_{II}$. Druhá kozmická rýchlosť je najmenšia potrebná rýchlosť na opustenie gravitačného poľa Zeme.

Čo by sa ale stalo, keby Zem získala voči Slnku viazanú rotáciu a tým by sa teplota na jej privrátenej strane ku Slnku zvýšila? Uvažujte, že Zem vyžaruje ako absolútne čierne teleso s emisivitou $1$. Zanedbajte prenos tepla na odvrátenú stranu.

<ol type="a">

<li>

<span class="body">[25 b]</span> Vypočítajte novú teplotu na privrátenej strane Zeme.

</li>

<li>

<span class="body">[25 b]</span> Vypočítajte novú typickú rýchlosť molekuly $\textrm{N}_{2}$ pri novej teplote na privrátenej strane. Postačuje takáto rýchlosť na únik z povrchu Zeme?

</li>

<li>

<span class="body">[10 b]</span> Ak ste odpovedali v časti b) záporne. Akú teplotu musí dosiahnuť privrátená strana Zeme, aby molekuly $\textrm{N}_{2}$ unikli z povrchu Zeme?

</li>

</ol>

Budete potrebovať veľkosť slnečnej konštanty $\mathit{k}_\Sun = 1361\,\mathrm{W} \cdot \mathrm{m}^{-2}$, ktorá udáva koľko energie za sekundu dopadá kolmo na meter štvorcový plochy zo Slnka v blízkosti Zeme. Druhá podstatná informácia je vzorec na výpočet druhej kozmickej rýchlosti 

$$
v_{II}=\sqrt{\frac{2GM_{\Ze}}{R_{\Ze}}} \approx 11{,}2\,\mathrm{km}\cdot\mathrm{s}^{-1}  \, . \tag{2}
$$

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Riešenie prvej podúlohy leží v pochopení toho, že Zem nejaký príkon prijíma zo Slnka a nejaký výkon vyžaruje do okolitého vesmíru. Prijímaná energia za sekundu $P_{in}$ je daná $\mathit{k}_\Sun$ (tokom zo Slnka) na prierez Zeme $S_{in}=\pi R_{\Ze}^2$.

Vyžiarená energia za sekundu $P_{out}$ je typicky z celého povrchu Zeme, ale naše zadanie nám prikazuje vyžarovať iba z privrátenej polovice o ploche $S_{out}=2\pi R_{\Ze}^2$. Vyžarovanie z povrchu o teplote $T$ je dané Stefanovým-Boltzmannovým zákonom, teda pre prijatý a vyžiarený výkon platí 

$$
P_{in} = k_\Sun S_{in} = k_\Sun \pi R_\Ze^2 \,, \tag{3}
$$

 

$$
P_{out} = S_{out}\sigma T^4 = 2\pi R_{\Ze}^2 \sigma T^4 \,, \tag{4}
$$

kde $\sigma$ označuje Stefanovou-Boltzmannovu konštantu.

Teplotu $T$ na ktorej sa ustáli privrátená strana Zeme označíme $T\equiv T_a$. Z rovnosti prijatého a vyžiareného výkonu $P_{in} = P_{out}$ dostávame 

$$
\begin{align*}
    k_\Sun \pi R_\Ze^2 &= \sigma 2\pi R_{\Ze}^2 \sigma T_a^4 \,, \tag{5}\\
    \mathit{k}_\Sun &= 2\sigma T_a^4 \,, \tag{6}\end{align*}
$$

 z čoho vyjadríme hľadanú teplotu 

$$
T_a = \sqrt[4]{\frac{\mathit{k}_\Sun}{2\sigma}}\approx 331\,\mathrm{K} \doteq 58\,^{\circ}\mathrm{C} \,. \tag{7}
$$

</li>

<li>

Na vyriešenie druhej úlohy si najprv musíme zistiť hmotnosť $M$ molekuly dusíku $\textrm{N}_{2}$. Na to využijeme znalosť typickej rýchlosti molekúl $\Bar{v_0}$ pri laboratórnej teplote $T_0$. 

$$
\Bar{v_0}=\sqrt{\frac{2RT_0}{M}} \ztv
    M = \frac{2RT_0}{\Bar{v_0}^2}\, . \tag{8}
$$

 Čo ani len nemusíme vyčísľovať. Keď nás teda zaujíma akú priemernú rýchlosť $\Bar{v_b}$ budeme mať pri novej teplote $T_a$, stačí len do všeobecnej rovnice zo zadania (1) dosadiť vyjadrenú hmotnosť molekuly dusíku (8). 

$$
\Bar{v_b}=\sqrt{\frac{2RT_a}{\cfrac{2RT_0}{\Bar{v_0}^2}}} = \sqrt{\Bar{v_0}^2 \frac{T_a}{T_0}}= \Bar{v_0}\sqrt{\frac{T_a}{T_0}} \approx 449\,\mathrm{m}\,{\mathrm{s}}^{-1}\,. \tag{9}
$$

 Táto hodnota taktiež nie je väčšia ako druhá kozmická $v_{II}\approx 11{,}2\,\mathrm{km}\,{\mathrm{s}}^{-1}$, a tak ani viazaná Zem nie je zbavená svojej atmosféry.

</li>

<li>

Pristúpme teda k tretej podúlohe, a teda k určeniu potrebnej teploty $T_c$, aby sa priemerná teplota molekúl vyrovnala druhej kozmickej rýchlosti. Môžeme poľahky vychádzať už zo známeho výrazu (9) s prepísaním veličín, 

$$
v_{II} = \Bar{v_0}\sqrt{\frac{T_c}{T_0}} \,. \tag{10}
$$

 Po jednoduchom preusporiadaní získavame 

$$
T_c = T_0 \left( \frac{v_{II}}{v_o} \right)^2 \approx 200\,000\,\mathrm{K}\,. \tag{11}
$$

Hoci sa môže táto hodnota zdať nehorázne vysoká, v skutočnosti by začala Zem strácať atmosféru už pri násobne nižšej teplote, pretože hoci priemerná rýchlosť nebude dostačovať, stále sa nájdu molekuly s vyššou rýchlosťou. Zároveň stačí, aby sa molekuly dostali dostatočne vysoko, do riedkeho prostredia, a tam už budú urýchlené slnečným vetrom, a unesené do vesmíru.

</li>

</ol>

</details>

## Komentár autora

Celá podstata úlohy je dostať do Astronomickej olympiády úlohu z molekulovej fyziky. No i tak môže názorne ukázať, ako je možné, že si planéty dokážu udržať stabilné atmosféry.
