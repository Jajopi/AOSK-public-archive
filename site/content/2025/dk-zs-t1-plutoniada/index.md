---
title: Plutoniáda
year: 2025
round: DK
roundName: Domáce kolo
category: ZŠ
type: teoria
typeName: Teória
label: T1
weight: 1
points: '45'
authors:
- Samuel Amrich
hasSolution: true
source: 2025:1-DK/0-ZS/01-Plutoniada/00-zadanie.tex
rocniky:
- '2025'
kola:
- Domáce kolo
kategorie:
- ZŠ
typy:
- Teória
tagy:
- Nezaradené
---

## Zadanie

V neďalekej budúcnosti sa rozhodli osadníci na Plute usporiadať svoju vlastnú olympiádu. Hoci športov, v ktorých sa súťaží je mnoho, všetci sa najviac tešia na hod oštepom. Všetci totiž dúfajú, že padne neporaziteľný rekord. Akou najmenšou rýchlosťou musíme hodiť oštep, aby nikdy nedopadol naspäť na Pluto a natrvalo ostal okolo neho obiehať po kruhovej dráhe? Pluto si predstavujte ako guľu s polomerom $R_{\Pl}$ a hmotnosťou $M_{\Pl}$. Hádžeme priamo z povrchu Pluta a rovnobežne s jeho povrchom.

<details class="solution">
<summary>Riešenie</summary>

Ak chceme, aby oštep nikdy nedopadol naspäť na povrch, musíme ho hodiť takou rýchlosťou, aby obiehal okolo Pluta po kruhovej dráhe. V takom prípade sa príťažlivá sila Pluta, spôsobená gravitáciou, vyrovná s odstredivou silou, vyvolanou pohybom po kružnici. Pre gravitačnú silu platí vzťah

$$
F_G= \frac{GM_{\Pl}m}{R_{\Pl}^2} \, , \tag{1}
$$

a pre odstredivú silu platí vzťah 

$$
F_O=\frac{mv_{I}^2}{R_{\Pl}} \, . \tag{2}
$$

Kde $M_{\Pl}$, $G$ a $R_{\Pl}$ si vieme nájsť na internete, $m$ je hmotnosť oštepu a $v_I$ je naša hľadaná rýchlosť. Na plný počet bodov úplne postačuje mať výsledný všeobecný vzorec bez dosadených hodnôt. Keďže požadujeme, aby sa sily vyrovnali, požadujeme $F_G=F_O$, čo po rozpísaní vyzerá nasledovne 

$$
\frac{GM_{\Pl}m}{R_\Pl^2}=\frac{mv_{I}^2}{R_{\Pl}} \, . \tag{3}
$$

Urobíme jednoduchú aritmetickú úpravu a to, že na oboch stranách škrtneme $m$, čo je pre nás výhodné, keďže sme ho nepoznali a zároveň škrtneme jedno $R_{\Pl}$. Po úpravách teda bude vzorec vyzerať nasledovne. 

$$
\frac{GM_{\Pl}}{R_{\Pl}}=v_I^2 \, . \tag{4}
$$

Teraz máme našu hľadanú rýchlosť osamotenú na jednej strane, takže nám stačí výraz iba odmocniť. 

$$
v_I=\sqrt{\frac{GM_{\Pl}}{R_{\Pl}}} \approx 857\,\mathrm{m}\,{\mathrm{s}}^{-1}  \, . \tag{5}
$$

Čo je náš hľadaný výsledok. Dôvod prečo sme písali všade $v_I$ je, že náš výsledok je označovaný aj ako prvá kozmická rýchlosť.

</details>

## Komentár autora

Príklad sa účastníka snaží oboznámiť s koncepciou prvej kozmickej rýchlosti z nebeskej mechaniky. Napojenie na športovú olympiádu je pre spestrenie a zaujatie.
