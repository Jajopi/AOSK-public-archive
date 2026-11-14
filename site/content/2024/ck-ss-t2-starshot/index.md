---
title: Starshot
year: 2024
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: T2
weight: 2302
points: '60'
authors:
- Samuel Amrich
hasSolution: true
source: 2024:zCK/SS/aTeoria/StarShot.tex
rocniky:
- '2024'
kola:
- Celoštátne kolo
kategorie:
- SŠ
typy:
- Teória
tagy:
- Nezaradené
---

## Zadanie

Jeden z konceptov ako preskúmať iné hviezdne systémy je projekt `Breakthrough Starshot`, ktorý využíva veľmi malé sondy so solárnymi plachtami, urýchľované pomocou laseru. Typicky sa so sondami vo vesmíre komunikujeme pomocou rádiového žiarenia, i keď v prípade Starshotu to bude pravdepodobne pomocou optického laseru.

V reálnom svete je množstvo prenesenej informácie pomocou elektromagnetického žiarenia závislé od použitej frekvencie. K výpočtu sa používa Nyquistov teorém, podľa ktorého maximálne množstvo prenesenej informácie za sekundu je rovné polovici použitej frekvencie (ak $f=100\,\mathrm{MHz}$, potom maximálny tok informácií je $\mu=50\,\mathrm{Mbit}/\mathrm{s}$).

Predstavte si, že Starshot urýchlená na rýchlosť $v=0{,}2\,\mathrm{c}$ vysiela na frekvencií $f=2{,}3\,\mathrm{GHz}$. Vypočítajte akú maximálnu prenosovú rýchlosť dokáže sonda vysielať a akú maximálnu prenosovú rýchlosť dokážeme zachytiť na Zemi?

*Dôležité je ešte poznamenať, že keď používame predpony kilo- (k-), mega- (M-) a giga- (G-) v spojení s digitálnymi jednotkami, myslíme celočíselné násobky tisícky, nie 1024. Pre násobky 1024 sa používajú predpony kibi- (Ki-), mebi- (Mi-) a gibi- (Gi-).*

<details class="solution">
<summary>Riešenie</summary>

Riešenie úlohy je značne priamočiare, ak sa človek nenechá nachytať pri prepočtoch z frekvencie na prenosovú rýchlosť a opačne. Celá úloha sa týka zmeny frekvencie z dôvodu rýchleho pohybu, čo nás samozrejme ihneď navádza na Dopplerov posun. Keďže sa pohybujeme nezanedbateľnou rýchlosťou voči rýchlosti svetla, je potrebné použiť relativistický vzťah

*(Poznámka: použitie klasického vzťahu nám pri $v=0{,}2\,\mathrm{c}$ ešte neurobí veľkú chybu a tak jeho použitie je penalizované mierne.)* 

$$
f =f_{0} \sqrt{\frac{1-v/c}{1+v/c}} \,. \tag{1}
$$

 Kde $f_0$ je vyžarovaná frekvencia žiarenia, $f$ je zachytená frekvencia, $v$ je rýchlosť pohybu vyžarujúceho telesa preč od prijímacieho. V klasickom prípade vyzerá rovnica nasledovne 

$$
f =f_{0} \frac{1}{1+v/c} \,. \tag{2}
$$

Ideálne je si aj zapísať ako vyzerá škálovanie alebo prevod medzi frekvenciou a prenosovou rýchlosťou. To je jednoducho dané nasledovným vzťahom 

$$
\mu = \frac{f}{2} \left[\frac{\mathrm{bit}  \mathrm{s}}{\mathrm{Hz}}\right] \,. \tag{3}
$$

Teraz len jednoducho zodpovieme na otázky zo zadania. Prvá je akou prenosovou rýchlosťou dokáže sonda vysielať. To vypočítame jednoducho cez prevodový vzťah (3) ako 

$$
\mu = \frac{f}{2} \left[\frac{\mathrm{bit}  \mathrm{s}}{\mathrm{Hz}}\right] = \frac{2{,}3\,\mathrm{GHz}}{2} \left[\frac{\mathrm{bit}  \mathrm{s}}{\mathrm{Hz}}\right] = 1{,}15\,\mathrm{Gbit}  \mathrm{s} \,. \tag{4}
$$

Druhá otázka je, akou maximálnou prenosovou rýchlosťou môže vysielať, aby sme to dokázali stále zachytiť na Zemi. K tomu musíme najprv použiť vzťah pre relativistický Dopplerov posun v tvare (1) 

$$
f =f_{0} \, \sqrt{\frac{1-v/c}{1+v/c}} = 2{,}3\,\mathrm{GHz} \sqrt{\frac{1-0.2}{1+0.2}} \approx 1{,}88\,\mathrm{GHz} \,. \tag{5}
$$

 Čo ešte musíme skonvertovať do prenosovej rýchlosti nasledovne 

$$
\mu = \frac{1}{2} f_{0} \, \sqrt{\frac{1-v/c}{1+v/c}} \, \left[\frac{\mathrm{bit}  \mathrm{s}}{\mathrm{Hz}}\right]  \approx 0{,}939\,\mathrm{Gbit}  \mathrm{s} \,. \tag{6}
$$

Takže maximálna prenosová rýchlosť je na úrovni približne $\approx 0{,}94\,\mathrm{Gbit}  \mathrm{s}$ za použitia relativistického vzťahu. Ak použijeme nerelativistický, získame hodnotu $\approx 0{,}96\,\mathrm{Gbit}  \mathrm{s}$.

</details>
