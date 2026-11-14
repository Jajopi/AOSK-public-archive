---
title: Liptovská Mara II
year: 2024
round: RK
roundName: Regionálne kolo
category: SŠ
type: teoria
typeName: Teória
label: T4
weight: 4004
points: '100'
authors:
- Samuel Buranský
hasSolution: true
source: 2024:RK/SS/aTeoria/Solarna-(ne)konstanta-II.tex
years:
- '2024'
rounds:
- Regionálne kolo
categories:
- SŠ
types:
- Teória
topics:
- Nezaradené
---

## Zadanie

Počas roka dochádza na Zemi k striedaniu ročných období. Dôvodom je naklonenie roviny zemského rovníka o uhol $\varepsilon = 23{,}4^{\circ}$ voči rovine ekliptiky. Zem zároveň obieha okolo Slnka na eliptickej dráhe, to znamená, že raz je k Slnku bližšie, inokedy ďalej. To spôsobuje, že na dané miesto na Zemi dopadá v rôzne dni rôzne množstvo žiarivej energie zo Slnka. Vypočítajte pomer žiarivých energií zo Slnka, ktoré dopadnú na celú plochu Liptovskej Mary za $1\,\mathrm{s}$ na pravé poludnie v deň letného (20. 6. 2024) a zimného slnovratu (21. 12. 2024). Poloha Liptovskej Mary je $49{,}1^{\circ}$ N, $19{,}5^{\circ}$ E a plocha $A$ = $27\,{\mathrm{km}}^{2}$.

Zem obieha okolo Slnka po eliptickej dráhe. Prechod perihéliom tento rok nastáva 3. 1. 2024 a prechod aféliom 5. 7. 2024. Pre prípadné medzivýpočty môžete využiť slnečnú konštantu, ktorej hodnota je uvedená v zozname konštánt. Slnečná konštanta predstavuje množstvo energie, ktoré prejde za $1\,\mathrm{s}$ plochou $1\,{\mathrm{m}}^{2}$ orientovanou kolmo na slnečné lúče vo vzdialenosti $1\,\mathrm{au}$ od Slnka bez extinkcie (absorpcie). Pri výpočte zanedbajte vplyv atmosféry. V dni slnovratov považujte deklináciu Slnka za konštantnú.

Vzdialenosť Zeme od Slnka môžete vypočítať podľa vzťahu 

$$
r = a (1 - e \cos{E}) \,, \tag{1}
$$

 kde $a$ je veľká polos dráhy, $e$ je excentricita a $E$ je excentrická anomália, pre ktorú platí Keplerova rovnica 

$$
M = E - e \sin{E} \,, \tag{2}
$$

 kde $M$ je stredná anomália definovaná vzťahom 

$$
M = n (t - T) \,, \tag{3}
$$

 kde $n=2\pi/P$ je stredný denný pohyb v radiánoch za deň, $P$ je perióda obehu, $t$ je aktuálny čas a $T$ je čas prechodu perihéliom. Na výpočet excentrickej anomálie je nutné použiť iteračnú metódu, kde ako prvý odhad pre $E$ použite $M$.

<details class="solution">
<summary>Riešenie</summary>

Pre pomer slnečných energií využijeme upravenú rovnicu z domáceho kola 

$$
\frac{\mathcal{E}_{\textrm{LS}}}{\mathcal{E}_{\textrm{ZS}}} = \frac{A t}{A t} \frac{\sin{(90^{\circ} - \varphi + \delta_{\Sun(LS)})}}{\sin{(90^{\circ}} - \varphi + \delta_{\Sun(ZS)})} \cdot \frac{\cfrac{L_\Sun}{4 \pi r_{LS}^2}}{\cfrac{L_\Sun}{4 \pi r_{ZS}^2}} \,, \tag{4}
$$

 kde člen $\frac{L_\Sun}{4 \pi r^2}$ vyjadruje energiu dopadajúcu na jednotku povrchu gule s polomerom $r$, ktorá sa líši v závislosti na vzdialenosti. Pre slnovraty platí $\delta_{\Sun(LS)} = \varepsilon$ a $\delta_{\Sun(ZS)} = -\varepsilon$. Po zjednodušení z výrazu dostaneme 

$$
\frac{\mathcal{E}_{\textrm{LS}}}{\mathcal{E}_{\textrm{ZS}}} = \frac{\sin{(90^{\circ} - \varphi + \varepsilon)}}{\sin{(90^{\circ}} - \varphi - \varepsilon)} \frac{r_{ZS}^2}{r_{LS}^2} \,. \tag{5}
$$

Vzdialenosť Zeme od Slnka spočítame pomocou vzťahov pre anomálie. Začneme výpočtom $t - T = \Delta t$, čiže časového rozdielu od prechodu perihéliom. 

$$
\Delta t(LS) = 169\,\mathrm{dní} \a
    \Delta t(ZS) = 353\,\mathrm{dní} \,. \tag{6}
$$

 Ďalej vypočítame stredný denný pohyb, kde použijeme ako periódu $P$ anomalistický rok (čas medzi dvoma po sebe idúcimi prechodmi Zeme perihéliom) 

$$
n = \frac{360^{\circ}}{365{,}2596\,\mathrm{dní}} = 0{,}9856004\,^{\circ}/\mathrm{deň} = 0{,}01720197171\,\mathrm{rad}/\mathrm{deň}\,. \tag{7}
$$

 Pre stredné anomálie teda platí 

$$
\begin{align*}
    M_{LS} &= 166{,}566464^{\circ} = 2{,}90713322\,\mathrm{rad}\,, \tag{8}\\
    M_{ZS} &= 347{,}9169336^{\circ} = 6{,}072296015\,\mathrm{rad}\,. \tag{9}\end{align*}
$$

Na výpočet excentrickej anomálie použijeme iteračnú metódu kde si Keplerovu rovnicu (do ktorej musíme dosádzať radiány) upravíme do tvaru 

$$
E = M + e \sin{E} \, \tag{10}
$$

 a iterovať budeme podľa predpisu 

$$
E_n = M + e \sin{E_{n-1}} \,, \tag{11}
$$

 kde zvolíme $E_0 = M$. Po pár iteráciách dostaneme 

$$
\begin{align*}
    E_{LS} &= 2{,}910950879\,\mathrm{rad} = 166{,}7851997^{\circ} \,, \tag{12}\\
    E_{ZS} &= 6{,}068742199\,\mathrm{rad} = 347{,}713315^{\circ} \,. \tag{13}\end{align*}
$$

Môžme prejsť k záverečnému výpočtu pomeru, kedy do rovnice (5) dosadíme za vzdialenosti výrazy z pomocnej rovnice a pokrátime veľkú polos a dosadíme číselné hodnoty 

$$
\frac{\mathcal{E}_{\textrm{LS}}}{\mathcal{E}_{\textrm{ZS}}} = \frac{\sin{(90^{\circ} - \varphi + \varepsilon)}}{\sin{(90^{\circ}} - \varphi - \varepsilon)} \frac{(1-e\cos{E_{ZS}})^2}{(1-e\cos{E_{LS}})^2} = 2{,}807525469 \doteq 2{,}81 \,. \tag{14}
$$

</details>
