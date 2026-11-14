---
title: Vek vesmíru
year: 2026
round: RK
roundName: Regionálne kolo
category: ZŠ
type: teoria
typeName: Teória
label: T1
weight: 1001
points: '50'
authors:
- Samuel Amrich
- 'opravuje: R. Lascsák'
hasSolution: true
source: 2026:-ZS/.RK/Vek-vesmiru.tex
rocniky:
- '2026'
kola:
- Regionálne kolo
kategorie:
- ZŠ
typy:
- Teória
tagy:
- Nezaradené
---

## Zadanie

V kozmológii je známy *Hubblov-Lemaîtrov zákon*, ktorý určuje, ako rýchlo sa vesmír rozpína. To sa dá zapísať ako 

$$
v = H \cdot d \,, \tag{1}
$$

 kde $v$ je rýchlosť, s akou sa vzdialené objekty (napríklad galaxie) od nás vzďaľujú, $d$ je ich vzdialenosť od nás a $H$ je *Hubblova konštanta*, ktorú vieme z astronomických meraní zistiť. Ako prvý tak učinil Edwin Hubble a získal hodnotu $H=500\,\mathrm{km}\,{\mathrm{s}}^{-1}\,{\mathrm{Mpc}}^{-1}$, čo je výrazne odlišné číslo ako súčasné merania. Zaujímavosťou je, že znalosť $H$ nám dovoľuje odhadnúť vek vesmíru. Na pochopenie toho, ako to funguje, si skúsme rovnicu vyššie upraviť na tvar 

$$
\frac{1}{H} \cdot v = d \,. \tag{2}
$$

 Ak sa zamyslíte, toto je veľmi podobné rovnici pre rovnomerný pohyb: $t \cdot v = d$. Uvažujeme, že počiatok vesmíru je moment, v ktorom boli všetky pozorované objekty vesmíru v jednom, nekonečne malom bode na jednom mieste. S týmito znalosťami a hodnotou $H$ od Edwina Hubbla určte vek vesmíru v *rokoch*. Uvažujte, že Hubblova konštanta je v čase konštantná.

<details class="solution">
<summary>Riešenie</summary>

Ako prvé si pod seba napíšeme 2 rovnice, ktoré máme poskytnuté v zadaní: rovnicu pre rovnomerný pohyb a rovnicu pre Hubblov-Lemaîtrov zákon v upravenom tvare: 

$$
\begin{align*}
    t \cdot v = d \,, \tag{3}\\
    \frac{1}{H} \cdot v = d \,. \tag{4}\end{align*}
$$

 Preto vidíme, že $\frac{1}{H}$ v druhej rovnici prislúcha času $t$ v prvej rovnici, pričom čas $t$ predstavuje vek vesmíru. To znamená, že môžeme písať 

$$
t = \frac{1}{H} \,.
    \qquad\textit{[20\,b]} \tag{5}
$$

Hodnotu Hubblovej konštanty neberieme z konštantovníka, ale ako hovorí zadanie, vezmeme hodnotu, ktorú nameral Edwin Hubble: 

$$
H = 500\,\mathrm{km}\,{\mathrm{s}}^{-1}\,{\mathrm{Mpc}}^{-1} \,.
    \qquad\textit{[5\,b]} \tag{6}
$$

 Čo vieme dosadiť do vyjadrenia pre čas (5) 

$$
t = \frac{1}{500\,\mathrm{km}\,{\mathrm{s}}^{-1}\,{\mathrm{Mpc}}^{-1}} \,.
    \qquad\textit{[5\,b]} \tag{7}
$$

Ďalej sa potrebujeme pohrať s jednotkami. Využijeme nasledovné prepočty do základných jednotiek sústavy SI: 

$$
\mathrm{km} = 1000\,\mathrm{m} \a
    {\mathrm{s}}^{-1} = \frac{1}{\mathrm{s}} \,, \tag{8}
$$

 

$$
{\mathrm{Mpc}}^{-1} = \frac{1}{10^{6}\,\mathrm{pc}} = \frac{1}{10^6 \cdot 3{,}262 \cdot 63\,241 \cdot 149\,597\,870\,700\,\mathrm{m}} = \frac{1}{3{,}086 \cdot 10^{22}\,\mathrm{m}} \,.
    \qquad\textit{[10\,b]} \tag{9}
$$

Pri prevode megaparseku ($\mathrm{Mpc}$) na metre ($\mathrm{m}$) sme využili hodnoty z konštantovníka, konkrétne postupne: prevod z parsekov na svetelné roky ($1\,\mathrm{pc} = 3{,}262\,\mathrm{ly}$), prevod zo svetelných rokov na astronomické jednotky ($1\,\mathrm{ly} = 63\,241\,\mathrm{au}$) a prevod z astronomických jednotiek na metre ($1\,\mathrm{au} = 149\,597\,870\,700\,\mathrm{m}$).

Dosadením všetkých prevodov do rovnice (7) dostaneme 

$$
t = \frac{1}{500\,\cdot 1000\,\mathrm{m} \cdot \cfrac{1}{\mathrm{s}} \cdot \cfrac{1}{3{,}086 \cdot 10^{22}\,\mathrm{m}}} =
    \frac{1}{\cfrac{500 \cdot 1000\,\cancel{{\mathrm{m}}}}{\mathrm{s} \cdot 3{,}086 \cdot 10^{22}\,\cancel{\mathrm{m}}}} =
    \frac{\mathrm{s} \cdot 3{,}086 \cdot 10^{22}}{500\,000} \doteq 6{,}172 \cdot 10^{16}\,\mathrm{s} \,.
    \qquad\textit{[5\,b]} \tag{10}
$$

Nakoniec ostáva previesť sekundy na roky. Využijeme, že: 

$$
\begin{align*}
    1\,\mathrm{rok} &= 365{,}25\,\mathrm{dňa} \,, \tag{11}\\
    1\,\mathrm{deň} &= 24\,\mathrm{h} \,, \tag{12}\\
    1\,\mathrm{h} &= 60\,\mathrm{min} \,, \tag{13}\\
    1\,\mathrm{min} &= 60\,\mathrm{s} \,. \tag{14}\end{align*}
$$

 Čiže 

$$
1\,\mathrm{rok} = 365{,}25 \cdot 24 \cdot 60 \cdot 60\,\mathrm{s} = 31\,557\,600\,\mathrm{s}  \,, \tag{15}
$$

čo je pre zaujímavosť približne rovné $\pi\cdot 10^7$. Ako vek vesmíru v rokoch preto dostávame 

$$
t = \frac{6{,}172 \cdot 10^{16}}{31\,557\,600} \, \mathrm{rokov} \doteq
    \boxed{2 \cdot 10^{9}\,\mathrm{rokov}}\,.
    \qquad\textit{[5\,b]} \tag{16}
$$

Dostali sme vek vesmíru približne 2 miliardy rokov. Súčasné kozmologické modely vesmíru odhadujú vek vesmíru na 14 miliárd rokov, teda 7-krát viac ako z meraní Edwina Hubbla.

</details>

## Komentár autora

Túto úlohu sme do Astronomickej olympiády zaradili na počesť nášho organizátora Samuela Amricha. Samo v roku 2024 navrhoval do súťaže toľko úloh, že mohol sám poskladať celý ročník. V našich archívoch sa preto stále nachádzajú úlohy s jeho menom a rozhodli sme sa dve z nich spracovať, jednu v základoškolskej a druhú v stredoškolskej kategórii.
