---
title: Datovanie Voyageru
year: 2024
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: T3
weight: 2303
points: '60'
authors:
- Samuel Amrich
hasSolution: true
source: 2024:zCK/SS/aTeoria/z-Datovanie-Voyageru.tex
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

Predstavte si situáciu, že mimozemská rasa odchytila v medzihviezdnom priestore sondu Voyager. Táto mimozemská civilizácia sa rozhodne preskúmať sondu a zistiť jej vek. To je možné aj vďaka tomu, že boli schopní odhaliť, že jej zdroj energie je RTG (rádioizotopový termoelektrický generátor). To nie je nič iné ako valec silne rádioaktívneho materiálu, ktorého atómy sa prirodzene rozpadajú a uvoľnená tepelná energia sa premieňa na elektrickú. Pričom z prekladu nápisov na RTG odhalili, že na začiatku obsahoval $100\% \; \ce{^{238}_{}Pu}$ (ale hmotnosť tam neudali). Rozpadová rada je zložitá, ale v podstate sa dá zjednodušiť na 

$$
\ce{^{238}_{}Pu} \: \rightarrow \: \ce{^{234}_{}U} \: \rightarrow \: \ce{^{230}_{}Th} \: \rightarrow \: \ce{^{206}_{}Pb} \,.
$$

 Prvý rozpad je v podstate okamžitý, teda polčas rozpadu je $T\left(\ce{^{238}_{}Pu} \: \rightarrow \: \ce{^{234}_{}U}\right) \approx 0\,\mathrm{rokov}$. Druhý rozpad je významný so svojím polčasom rozpadu $T\left(\ce{^{234}_{}U} \: \rightarrow \: \ce{^{230}_{}Th}\right) = 244\,900\,\mathrm{rokov}$. A tretí sa opäť udeje okamžite, teda $T\left(\ce{^{230}_{}Th} \: \rightarrow \: \ce{^{206}_{}Pb}\right) \approx 0\,\mathrm{rokov}$. Aktuálne v RTG Voyagera našli 

$$
m\left(\ce{^{206}_{}Pb}\right)=0{,}32\,\mathrm{kg} \a
m\left(\ce{^{234}_{}U}\right)=1{,}11\,\mathrm{kg} \, .
$$

 Vypočítajte ako dlho sa Voyager nachádzal vo vesmíre a koľko plutónia $\ce{^{238}_{}Pu}$ mal na začiatku. Pomôcť vám môže aj znalosť, že v súčasnosti sa polčas rozpadu nazýva čas polpremeny.

*Z hľadiska skúmania hmotností izotopov nezabúdajte, že sa pri rozpade uvoľňujú $\alpha$ častice (respektívne jadrá hélia ), ktoré ale unikli z kontajnera udržiavajúceho rádioizotopy. Iné častice pri rozpade zanedbajte. Predpokladajte, že hmotnosť protónu je rovná hmotnosti neutrónu a hmotnosť elektrónu je prakticky nulová. Predpokladajte, že hmotnosť izotopu je určená čisto počtom nukleónov v jadre. Vplyv kozmického žiarenia zanedbajte.*

<details class="solution">
<summary>Riešenie</summary>

Ako prvé si uvedomíme, že celá úloha sa točí okolo rádioaktívnych rozpadov. Preto potrebujeme poznať základný vzťah pre vývoj hmotnosti rádioaktívnej látky v čase 

$$
m\left(t\right) = m_0 \cdot 2^{-\frac{t}{T}} = m_0 \cdot e^{-\ln\left(2\right)\frac{t}{T}}\,. \tag{1}
$$

 Kde $m\left(t\right)$ je hmotnosť rádioaktívnej látky v čase $t$, $m_0$ je hmotnosť látky na začiatku (v čase $t=0$) a $T$ je polčas rozpadu (správne po novom čas polpremeny) danej látky.

V tejto úlohe musíme postupovať postupne a dávať pritom pozor na presnosť. Jediný rozpad, ktorý nás zaujíma je $\ce{^{234}_{}U} \: \rightarrow \: \ce{^{230}_{}Th}$. Pretože ostatné prebiehajú okamžite. Ale poznáme iba hmotnosť $m\left(\ce{^{234}_{}U}\right)$ a nie $m\left(\ce{^{230}_{}Th}\right)$ (nesmieme zabudnúť na stratenú $\alpha$ časticu). Hmotnosť $m\left(\ce{^{230}_{}Th}\right)+m\left(\ce{^{4}_{}He}\right)$ ale vieme poľahky vypočítať z hmotnosti $m\left(\ce{^{206}_{}Pb}\right)$ ako 

$$
m\left(\ce{^{230}_{}Th}\right)+m\left(\ce{^{4}_{}He}\right) = m\left(\ce{^{206}_{}Pb}\right) \cdot \frac{230+4}{206} \approx 0{,}363\,\mathrm{kg} \,. \tag{2}
$$

 Kde využívame znalosti zo zadania. Teda, že hmotnosť protónu je rovná hmotnosti neutrónu, hmotnosť elektrónu je nulová a, že hmotnosť izotopu je určená čisto počtom nukleónov v jadre. Preto hmotnosť daného izotopu Tória plus hmotnosť héliového jadra je rovná hmotnosti daného izotopu olova krát pomer ich nukleových čísel.

Teraz už môžeme vypočítať čas $t$, ktorý satelit bol vo vesmíre podľa rovnice 

$$
m\left(\ce{^{234}_{}U}\right) = \left[m\left(\ce{^{234}_{}U}\right) + m\left(\ce{^{230}_{}Th}\right)+m\left(\ce{^{4}_{}He}\right) \right]\cdot 2^{-\frac{t}{T\left(\ce{^{234}_{}U} \: \rightarrow \: \ce{^{230}_{}Th}\right)}} \,, \tag{3}
$$

 odvodený od rovnice (1). $m(t)$ je stotožnené s $m\left(\ce{^{234}_{}U}\right)$, pretože je to hmotnosť uránu, ktorý ostal po čase $t$. Na pravej strane rovnice (1) stotožníme hmotnosť $m_0$ s hmotnosťou $m\left(\ce{^{234}_{}U}\right) + m\left(\ce{^{230}_{}Th}\right)+m\left(\ce{^{4}_{}He}\right)$, pretože je to celková hmotnosť uránu ktorá musela byť na začiatku. Jednoduchými úpravami rovnice 3 získame vzťah 

$$
t = - T\left(\ce{^{234}_{}U} \: \rightarrow \: \ce{^{230}_{}Th}\right) \cdot \log_2\left(\frac{m\left(\ce{^{234}_{}U}\right)}{m\left(\ce{^{234}_{}U}\right) + m\left(\ce{^{230}_{}Th}\right)+m\left(\ce{^{4}_{}He}\right)}\right)  \approx 100\,000\,\mathrm{rokov} \,. \tag{4}
$$

 Kde len dôležité upozornenie je, že $\log_2$ je logaritmus pri základe dva. Čo zhodou náhod zodpovedá dobe za ktorú Voyager pri svojej aktuálnej rýchlosti doletí k Proxime Centauri.

Ak ešte potrebujeme vypočítať koľko bolo plutónia na začiatku. k tomu využijeme v podstate rovnaký vzťah ako (2)

$$
m\left(\mathrm{Pu}_{238}\right) = \left[m\left(\ce{^{234}_{}U}\right) + m\left(\ce{^{230}_{}Th}\right)+m\left(\ce{^{4}_{}He}\right)\right] \cdot \frac{238}{230+4} \approx 1{,}5\,\mathrm{kg} \,. \tag{5}
$$

</details>
