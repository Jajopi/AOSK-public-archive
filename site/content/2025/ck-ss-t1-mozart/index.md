---
title: Mozart
year: 2025
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: T1
weight: 5001
points: '60'
authors:
- Terézia Hanáková
hasSolution: true
source: 2025:3-CK/1-SS/01-Mozart/00-zadanie.tex
years:
- '2025'
rounds:
- Celoštátne kolo
categories:
- SŠ
types:
- Teória
topics:
- Nezaradené
---

## Zadanie

Wolfgang Amadeus Mozart, jeden z najväčších hudobných skladateľov, sa narodil 27. 1. 1756. V tomto mesiaci nastalo hneď niekoľko astronomických úkazov, medzi ktorými bola 21. 1. aj konjunkcia Saturna.

<ol type="a">

<li>

<span class="body">[30 b]</span> Jeho priateľ mu na štrnáste narodeniny povedal, že posledné leto pozoroval presne tento istý úkaz – konjunkciu Saturna. Nepamätal si však, ktorý dátum to bolo. Pomôžte im to zistiť.

</li>

<li>

<span class="body">[20 b]</span> Mozarta to zaujalo, a preto sa rozhodol, že najbližšie bude túto konjunkciu pozorovať aj on. Kedy to bude? Výsledok uveďte s najväčšou presnosťou, ako je rozumné.

</li>

<li>

<span class="body">[10 b]</span> Prečo v realite nastanú časové odchýlky od vášho výsledku?

</li>

</ol>

Uvažujte, že konjunkcia z 21. januára 1756 nastala, ako uvádzajú historické zdroje, o 18:49 miestneho času a obežná doba Saturna je $10\,757{,}73648\,\mathrm{dní}$. Dráhy planét považujte za kruhové. Obežnú dobu Zeme uvažujte $365{,}2563604\,\mathrm{dní}$.

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Spôsob, akým zistiť, kedy nastane ďalší aspekt planét, ktorým je aj konjunkcia Saturna, možno pomocou výpočtu synodickej doby z obežných dôb Zeme a Saturna 

$$
\begin{align*}
    \frac{1}{S} &= \frac{1}{P_\Ea} - \frac{1}{P_\Sa} \,, \tag{1}\\
    \frac{1}{S} &= \frac{P_\Sa - P_\Ea}{P_\Ea P_\Sa} \,, \tag{2}\\
    S &= \frac{P_\Ea P_\Sa}{P_\Sa - P_\Ea} \,, \tag{3}\end{align*}
$$

 čo po dosadení $P_\Sa$ a $P_\Ea$ v dňoch dáva $S = 378{,}0937397\,\mathrm{dní}$.

***Poznámka:*** Synodická obežná doba $S$ je čas, ktorý uplynie medzi dvomi rovnakými relatívnymi polohami dvoch objektov z miesta pozorovania, zo Zeme. Je to teda vlastnosť, ktorá sa vždy musí vzťahovať na dve telesá. V našom prípade je to doba, kedy po konjunkcii Saturna so Slnkom nastane opäť konjunkcia Saturna so Slnkom (bežne sa konjunkcia so Slnkom nazýva jednoducho konjunkcia). Dôležité pritom je za $P_\Ze$ a $P_\Sa$ dosadzovať presné hodnoty zo zadania a pri následných výpočtoch si v kalkulačke držať čo najväčšiu presnosť čísel.

Teraz sa už môžme zamýšľať nad hlavným výpočtom. Zo zadania vieme, že konjunkcia Saturna nastala 21. 1. 1756, a že Mozart svoje 14. narodeniny oslávil 27. 1. 1770.

Prvou dôležitou vecou je vypočítať, koľkokrát nastala konjunkcia od tej v januári 1756 až po Mozartove 14. narodeniny.

Ako prvé si musíme určiť, koľko času ubehlo medzi týmito dvoma dátumami. Mohli by sme byť presný a brať to, ako sa v zadaní píše, od 18:49, no náš výsledok by to nezmenilo, lebo nás nakoniec bude zaujímať iba celočíselná (nie presná) hodnota, koľkokrát nastala konjunkcia. Preto nám stačí povedať, že čas, ktorý dovtedy ubehol, je 14 rokov a 6 dní. Pri prepočte tohto čísla na dni musíme rátať s priestupnými a nepriestupnými rokmi. Mali by sme vedieť, že každý štvrtý rok je priestupný, inými slovami každý, ktorý je deliteľný štyrmi. Čiže napríklad hneď rok 1756, v ktorom sa narodil Mozart, bol priestupný, potom znova rok 1760, 1764 a 1768. Tieto štyri roky teda mali v sebe 366 dní. Ostatných 10 rokov malo zvyčajných 365 dní. Dokopy teda $14\,\mathrm{rokov} = 10 \cdot 365 + 4 \cdot 366 = 5114\,\mathrm{dní}$. Pripočítame zvyšných 6 dní a dostávame 5120 dní.

Koľko opozícií nastalo vypočítame podielom tohto času a synodickej doby, ktorú sme vypočítali vyššie 

$$
\text{počet konjunkcií} = \frac{5114\,\mathrm{dní}}{378{,}0937397\,\mathrm{dní}} \,, \tag{4}
$$

 čo nám vyjde okolo 13,5, čiže vieme povedať, že konjunkcia nastala 13-krát, keďže k 14-tej ešte nedošlo.

Kedy teda pozoroval Mozartov priateľ konjunkciu? Zistíme to, ak 13-krát vynásobíme hodnotu synodickej doby od času, kedy nastala 21. 1. 1756, čiže od 18:49. Tu už bude dôležité počítať presne.

Najskôr si ale vypočítajme, koľko vôbec je 13-násobok synodickej doby 

$$
13 \cdot 378{,}0937397\,\mathrm{dní} = 4915{,}218616\,\mathrm{dní}\,. \tag{5}
$$

A teraz len riešime nasledujúcu úlohu: 21. 1. 1756 18:49 + $4915{,}218616\,\mathrm{dní}$. Najjednoduchšie bude si toto číslo v dňoch prepísať, čo najpresnejšie, t.j. do rokov, dní, hodín, minút a sekúnd. Riešme postupne.

Pri rýchlom výpočte vidíme, že by to malo byť okolo 13 rokov, no pre presný výpočet musíme opäť dbať na priestupné a nepriestupné roky. Rok 1756 bol priestupný, čiže mal 366 dní. Ak sa zamyslíme, tak 21. 1. 1756 + $366\,\mathrm{dní}$ dá 21. 1. 1757. Potom po pripočítaní $365\,\mathrm{dní}$ (lebo rok 1757 už priestupný nebol) dostaneme 21. 1. 1758 a tak ďalej. 13 rokov nám dáva: $4 \cdot 366 + 9 \cdot 365 = 4749\,\mathrm{dní}$. Ak toto odpočítame od výsledku, dostávame $166{,}218616\,\mathrm{dní}$. Čiže konjunkcia nastane o toľko dní po 21. 1. 1769.

Teraz riešime nasledovné: 21. 1. 1769 + $166{,}218616\,\mathrm{dní}$. Vieme, že január toho roku (ako aj každého roku) mal 31 dní, február 28 dní, marec 31, apríl 30, máj 31, jún 30, júl 31, august 31, september 30, október 31, november 30 a december 31 dní.[^1] Postupujeme podobne ako pri rokoch. Ak k 21. 1. 1769 pripočítame 31 dní, budeme v 21. 2. 1769. Ak k tomuto teraz pripočítame 28 dní, budeme v 21. 3. 1769 a tak ďalej. V mesiacoch dospejeme ku 21. 6. 1769 (čo je 151 dní po 21. 1. 1769), a tým pádom nám zostáva $166{,}2186157\,\mathrm{dní} - 151\,\mathrm{dní} =  15{,}21861566\,\mathrm{dní}$.

Teraz sme na 21. 6. 1769 o 18:49 hodine. A musíme k tomuto ešte pripočítať $15{,}218616\,\mathrm{dní}$. Jún má 30 dní, čiže do 1. 7. 1769 18:49 ubehne 10 dní. Čiže nám ostáva ešte $5{,}218616\,\mathrm{dňa}$. O päť celých dní teda bude 6. 7. 1769 18:49 a zostáva nám $0{,}218616\,\mathrm{dňa}$, ktoré musíme previesť tentoraz na hodiny, čiže 

$$
0{,}218616 \cdot 24\,\mathrm{h} = 5{,}246784\,\mathrm{h} \,. \tag{6}
$$

 To nám dáva 6.7.1769 18:49 + $5{,}246784\,\mathrm{h}$.

O päť celých hodín bude 6. 7. 1769 23:49 a zostane nám $0{,}246784\,\mathrm{h}$, čo prepočítame na minúty 

$$
0{,}246784 \cdot 60\,\mathrm{min} = 14{,}807\,\mathrm{min} \doteq 14\,\mathrm{min}\;48\,\mathrm{s} \doteq 15\,\mathrm{min} \tag{7}
$$

 Čiže ak k 23:49 pripočítame túto hodnotu, dostaneme už nasledovný deň, 7. 7. 1769, asi štyri minúty po polnoci. Počítať presnejšie, t.j. až na sekundy by išlo, ale nemá to zmysel, keďže čas v zadaní je určený s presnosťou na minúty. Vieme ale teda, že Mozartov priateľ pozoroval konjunkciu 7.7.1769 o 00:04.

</li>

<li>

Teraz nám už len stačí určiť, kedy nastane ďalšia konjunkcia a to bude tá, ktorú bude môcť pozorovať už aj sám Wolfgang. Bude to opäť o jednu synodickú dobu neskôr a na určenie dátumu a času $t$ budeme postupovať obdobne 

$$
\begin{align*}
    t &= 7.\ 7.\ 1769 \enspace \text{00:03:48} + 378{,}09373967\,\mathrm{dní} \tag{8}\\
    &= 7.\ 7.\ 1770 \enspace \text{00:03:48} + 13{,}09373967\,\mathrm{dní} \tag{9}\\
    &= 20.\ 7.\ 1770 \enspace \text{00:03:48} + 0{,}09373967\,\mathrm{dní} \tag{10}\\
    &= 20.\ 7.\ 1770 \enspace \text{00:03:48} + 2{,}24975208\,\mathrm{h} \tag{11}\\
    &= 20.\ 7.\ 1770 \enspace \text{02:03:48} + 0{,}24975208\,\mathrm{h} \tag{12}\\
    &= 20.\ 7.\ 1770 \enspace \text{02:03:48} + 14{,}9851248\,\mathrm{min} \tag{13}\\
    &= 20.\ 7.\ 1770 \enspace \text{02:17:48} + 0{,}9851248\,\mathrm{min} \tag{14}\\
    &= 20.\ 7.\ 1770 \enspace \text{02:17:48} + 59{,}107488\,\mathrm{s} \tag{15}\\
    &\doteq 20.\ 7.\ 1770 \enspace \text{02:19}\,. \tag{16}\end{align*}
$$

 Teda ďalšia konjunkcia nastane 20. 7. 1770 ráno o 02:19.

Treba však podotknúť, že hoci sa v tejto úlohe hovorí o pozorovaní konjunkcie Saturna, v skutočnosti konjunkciu Saturna zo Zeme pozorovať nemôžeme, pretože počas takejto konjunkcie sa Slnko nachádza pod obzorom.

Na záver by sa ešte malo spomenúť, že pri takýchto príkladoch je veľmi dôležitá presnosť výsledkov. Najlepšie je nezaokrúhľovať medzivýsledky a počítať s presnými hodnotami a až na samý záver výsledok zaokrúhliť. V tomto prípade je rozumným zaokrúhlením rád minút, pretože v zadaní je čas konjunkcie zadaný na minúty a obežné doby sú zadané s dostatočnou presnosťou.

</li>

<li>

Faktory, ktoré znižujú presnosť našich výsledkov, sú:

- elipticita (výstrednosť) dráh planét – je najsignifikantnejším vplyvom, pretože spôsobuje, že synodická doba nie je konštantná,

- gravitácia ostatných planét – má slabší vplyv, ale stále ovplyvňuje dráhy, a teda aj synodickú dobu,

- relativistické vplyvy – malý vplyv pre nízke excentricity dráh, spôsobujú stáčanie perihélia, teda zmeny synodickej doby,

- spomaľovanie rotácie planét – slabý vplyv na malých časových škálach, avšak zákon zachovania momentu hybnosti spôsobuje predlžovanie obežnej doby na úkor spomalenia rotácie (obdobne ako sa Mesiac vzďaľuje od Zeme),

- strata hmotnosti Slnka – veľmi slabý vplyv, ale obdobne spôsobuje predlžovanie periód,

- tlak žiarenia a slnečného vetra – minoritný vplyv pre veľmi hmotné objekty ako planéty.

Realisticky jediný dôležitý vplyv pre náš výsledok je elipticita dráh. Konjunkcie v skutočnosti nastanú 14. 7. 1769 a 29. 7. 1770, čiže naše výsledky ani zďaleka nedosahujú presnosť v ráde minút, ale líšia sa o približne týždeň.

</li>

</ol>

[^1]: Na toto je dobrý trik s hánkami prstov. Ak spojíme obe ruky, tak prvá vystupuje hánka (január má 31 dní), potom medzi hánkami je ”dolinka”, čiže február má menej dní - 28 (pre priestupný rok 29 dní), marec je znova na hánke (má 31 dní) a takto sa to opakuje až do chvíle, kedy sa nám nespoja ruky - tam sú dve hánky za sebou (vychádza to na júl a august, ktoré majú 31 dní).

</details>

## Komentár autora

Aj laikov a neastronómov fascinuje vesmír.
