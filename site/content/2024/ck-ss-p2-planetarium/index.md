---
title: Planetárium
year: 2024
round: CK
roundName: Celoštátne kolo
category: SŠ
type: prakticka
typeName: Praktická úloha
label: P2
weight: 5202
points: '100'
authors:
- Samuel Buranský
- Jana Švrčková
hasSolution: true
source: 2024:zCK/SS/Prakticka/Planetarium.tex
years:
- '2024'
rounds:
- Celoštátne kolo
categories:
- SŠ
types:
- Praktická úloha
topics:
- Nezaradené
---

## Zadanie

Predstavte si, že ste sa po skončení AO so stratou pamäti zobudili na neznámom opustenom mieste. Chcete zistiť, kde sa práve nachádzate, no pri sebe nemáte nič okrem hodiniek, ktoré ukazujú LSEČ (UT+2) a mapy/atlasu oblohy, z ktorého ste sa učili na súťaž. Rozhodnete sa teda, že svoju polohu určíte podľa hviezd. Kvôli strate pamäti si nie ste úplne istí ani aký je dátum, preto sa ho na základe oblohy pokúsite aspoň odhadnúť.

Planetárium zobrazuje otáčajúcu sa oblohu počas troch po sebe nasledujúcich dní. Vašou úlohou je s presnosťou na celé stupne určiť **zemepisnú šírku**, **zemepisnú dĺžku** a aktuálny **kalendárny mesiac**.

Na začiatok máte 10 minút na prečítanie zadania. Po ich uplynutí sa spustí simulácia. Simulácia bude zobrazovať 3 po sebe nasledujúce dni (72 hodín). Následne budete mať 10 minút na zapísanie údajov, výpočty a rozmyslenie ďalšieho postupu. Následne sa rovnaká simulácia spustí znova. Na koniec budete mať posledných 10 minút na spísanie riešenia.

Nezabudnite aspoň stručne popísať aj postup, ako ste sa k výsledným hodnotám dopracovali. V prípade, že dostanete nesprávne výsledky, môžete dostať aspoň čiastkové body za správny postup či nápad na riešenie.

<details class="solution">
<summary>Riešenie</summary>

Na riešenie existuje viacero možných prístupov. Uvádzame preto iba niektoré z nich. Na úvod je vhodné si všimnúť že sa nachádzame na južnej a západnej pologuli. Západnú pologuľu určíme podľa toho, že Slnko kulminuje po 14:00 LSEČ a južnú podľa viditeľnosti južných súhvezdí a rotácie oblohy okolo južného svetového pólu.

Pri určovaní zemepisnej šírky môžeme postupovať tak, že nájdeme hviezdu, ktorá sa pri dolnej kulminácii dotýka horizontu (v našej simulácii to bol napríklad Gacrux). Na základe deklinácie tejto hviezdy je možné určiť zemepisnú šírku. Pre deklináciu a zemepisnú šírku je možné napísať vzťah 

$$
\varphi = -90 - \delta \,, \tag{1}
$$

 ktorý platí pre južnú pologuľu a južné súhvezdia ($\varphi < 0$, $\delta < 0$).

Body je možné získať podľa nasledujúcich intervalov presnosti: na stupeň presné určenie - 30b, chyba do $2^{\circ}$ - 25b, chyba do $5^{\circ}$ - 15b, chyba do $10^{\circ}$ - 5b.

Na určenie zemepisnej dĺžky je možné určiť čas poludnia alebo čas polnoci. Čas poludnia vieme určiť ako stred medzi východom a západom Slnka. Počas simulácie nastane spln Mesiaca, čas polnoci preto môžeme odhadnúť ako stred medzi východom a západom Mesiaca ale taktiež ako stred medzi východom a západom ľubovoľnej hviezdy. LSEČ je vhodné si prepočítať do UT, pre ktorý platí 

$$
\mathrm{UT}=\mathrm{LSEČ}-2\,\mathrm{h}\, , \tag{2}
$$

Následne je zemepisná dĺžka daná časovým rozdielom medzi polnocou v UT a miestnou polnocou, pričom jedna časová hodina zodpovedá $15^{\circ}$ v dĺžke. Je možné použiť aj časový rozdiel medzi miestnou polnocou a polnocou v UT, je treba si ale uvedomiť, že LSEČ zodpovedá zemepisnej dĺžke $30^{\circ}$ (a nie $15^{\circ}$ ako to je v prípade SEČ).

Body je možné získať podľa nasledujúcich intervalov presnosti: na stupeň presné určenie - 40b, chyba do $5^{\circ}$ - 25b, chyba do $10^{\circ}$ - 15b, chyba do $15^{\circ}$ - 5b.

Pre určenie mesiaca bolo možné si všimnúť, že jarný bod kulminuje približne o polnoci. Slnko sa preto musí nachádzať v blízkosti jesenného bodu. To znamená, že simulácia sa odohráva v blízkosti jesennej rovnodennosti a je teda mesiac september.

Plný počet bodov (30b) je možné získať za presné určenie mesiaca a polovicu bodov (15b) za chybu 1 mesiac.

Správna poloha bola $\varphi = -32^{\circ}\,44'\,56''$, $l = -52^{\circ}\,38'\,54''$ (západná pologuľa) a dátum prvého dňa 17. 09. Body bolo možné získať aj nezávisle na intervaloch presnosti, na základe spísaných postupov a myšlienok v riešení.

</details>
