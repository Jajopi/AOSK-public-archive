---
title: Krátkozraký pozorovateľ
year: 2026
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: T3
weight: 5003
points: '40'
authors:
- S. Buranský
- D. Kráľ
hasSolution: true
source: 2026:.SS/¹CK/Kratkozraky-pozorovatel.tex
years:
- '2026'
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

Pri uvažovaní o optike oka sú dôležité rôzne vzdialenosti. Vzdialený bod je najvzdialenejší bod, ktorý oko vidí ostro bez akomodácie (bez námahy svalov), a pre zdravé oko leží v nekonečne. Naopak, konvenčná zraková vzdialenosť (dohodou stanovená na $25\,\mathrm{cm}$) je štandardná vzdialenosť, pri ktorej sa predpokladá pohodlné čítanie u zdravého človeka, čo si však už vyžaduje určité namáhanie oka (akomodáciu).

David je krátkozraký, čo koriguje okuliarmi. O svojom ľavom oku bez okuliarov zistil, že vzdialený bod leží vo vzdialenosti $1{,}3\,\mathrm{m}$. Pri pravom oku zistil, že text vo vzdialenosti $18{,}5\,\mathrm{cm}$ sa mu bez okuliarov javí, akoby ho mal v konvenčnej vzdialenosti.

David pozoruje hviezdu Sirius bežným binokulárom bez použitia okuliarov. Binokulár má centrálne ostrenie naraz pre oba ďalekohľady a taktiež možnosť ostrenia každého ďalekohľadu zvlášť. David zaostril centrálne oba ďalekohľady dokonale pre svoje ľavé oko. O koľko dioptrií musí teraz otočiť korekciu na pravom ďalekohľade, aby videl ostro aj pravým okom?

*Nápoveda: Dve tenké šošovky postavené za sebou sa správajú ako jedna, ktorej optická mohutnosť je súčet optických mohutností jednotlivých šošoviek.*

<details class="solution">
<summary>Riešenie</summary>

Základná rovnica, ktorú budeme v tejto úlohe potrebovať, je zobrazovacia rovnica tenkej šošovky 

$$
\frac{1}{a} + \frac{1}{a'} = \frac{1}{f} \,, \qquad\textit{[7\,b]} \tag{1}
$$

 kde $a$ je predmetová vzdialenosť (vzdialenosť zobrazovaného predmetu od šošovky), $a'$ je obrazová vzdialenosť (vzdialenosť vytvoreného obrazu, resp. tienidla, od šošovky) a $f$ je ohnisková vzdialenosť, ktorá charakterizuje šošovku.

Ďalší dôležitý pojem spomenutý v zadaní je optická mohutnosť šošovky $\varphi$, a tá sa vypočíta ako prevrátená hodnota ohniskovej vzdialenosti v metroch 

$$
\varphi = \frac{1}{f} \,. \qquad\textit{[6\,b]} \tag{2}
$$

 Pre úspešný výpočet je nutné vedieť, že oko má špeciálnu vlastnosť a tou je zmena optickej mohutnosti, teda zaostrovanie na predmety v rôznych vzdialenostiach. Ako je napísané v zadaní, zdravé oko má vzdialený bod v nekonečne a konvenčnú vzdialenosť rovnú $25\,\mathrm{cm}$. Krátkozraké oko má obe vzdialenosti zmenšené. Ak ale oko spojíme so správnou šošovkou, tak sústava oko-šošovka bude mať vzdialený bod aj konvenčnú vzdialenosť zhodnú so zdravým okom.

Začneme výpočet ľavým okom, pre ktoré si môžeme napísať dve zobrazovacie rovnice. Ako prvé si napíšeme zobrazovaciu rovnicu pre krátkozraké oko 

$$
\frac{1}{1{,}3\,\mathrm{m}} + \frac{1}{a'} = \frac{1}{f_L} \,, \qquad\textit{[4\,b]} \tag{3}
$$

 a pre krátkozraké oko s okuliarmi dostaneme 

$$
\frac{1}{\infty} + \frac{1}{a'} = \frac{1}{f_L} + \varphi_L \,, \qquad\textit{[4\,b]} \tag{4}
$$

 kde prvý zlomok je rovný nule, takže môžeme rovnicu prepísať ako 

$$
\frac{1}{a'} = \frac{1}{f_L} + \varphi_L \,. \tag{5}
$$

Ak odčítame rovnicu (3) od rovnice (5), dostaneme priamo optickú mohutnosť ľavej šošovky Davidových okuliarov 

$$
\varphi_L = -\frac{1}{1{,}3\,\mathrm{m}} \doteq -0{,}77\,\mathrm{D} \,. \qquad\textit{[3\,b]} \tag{6}
$$

Podobné rovnice si môžeme napísať pre pravé oko a jeho konvenčnú vzdialenosť. Pre krátkozraké oko platí 

$$
\frac{1}{0{,}185\,\mathrm{m}} + \frac{1}{a'} = \frac{1}{f_P} \,, \qquad\textit{[4\,b]} \tag{7}
$$

 a pre krátkozraké s okuliarmi platí 

$$
\frac{1}{0{,}25\,\mathrm{m}} + \frac{1}{a'} = \frac{1}{f_P} + \varphi_P \,. \qquad\textit{[4\,b]} \tag{8}
$$

 Ak odčítame rovnicu (7) od rovnice (8), dostaneme výraz pre Davidovu dioptriu na pravom oku 

$$
\varphi_P = \frac{1}{0{,}25\,\mathrm{m}} - \frac{1}{0{,}185\,\mathrm{m}} \doteq -1{,}4\,\mathrm{D} \,. \qquad\textit{[3\,b]} \tag{9}
$$

Preostrenie medzi nastavením ľavého a pravého oka je iba rozdiel optických mohutností Davidových okuliarov teda 

$$
\varphi_P - \varphi_L = \boxed{-0{,}64\,\mathrm{D}} \,. \qquad\textit{[5\,b]} \tag{10}
$$

Alternatívne sa dá uvažovať aj tak, že akú šošovku musí mať David pred ľavým okom aby mu objekty z nekonečna posunula do vzdialenosti $1{,}3\,\mathrm{m}$. Opäť použijeme zobrazovaciu rovnicu, kde predmetová vzdialenosť je nekonečno a obrazová je $-1{,}3\,\mathrm{m}$, pričom záporné znamienko je spôsobené tým, že sa obraz nachádza v predmetovom priestore. Po dosadení dostaneme Davidovu ľavú dioptriu <span class="subbody">[6 b]</span> 

$$
\varphi_L = \frac{1}{\infty} + \frac{1}{-1,3} = \frac{1}{-1,3} \doteq -0{,}77\,\mathrm{D} \,. \qquad\textit{[5\,b]} \tag{11}
$$

Pre pravé oko urobíme rovnaký výpočet pričom predmetová vzdialenosť je $25\,\mathrm{cm}$ a obrazová $-18{,}5\,\mathrm{cm}$. Po dosadení do zobrazovacej rovnice dostaneme Davidovu pravú dioptriu <span class="subbody">[6 b]</span> 

$$
\varphi_P = \frac{1}{0,25} + \frac{1}{-0,185} \doteq -1{,}4\,\mathrm{D} \,. \qquad\textit{[5\,b]} \tag{12}
$$

</details>
