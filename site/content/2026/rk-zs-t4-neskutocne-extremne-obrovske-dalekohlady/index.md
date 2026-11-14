---
title: Neskutočne Extrémne Obrovské ďalekohľady
year: 2026
round: RK
roundName: Regionálne kolo
category: ZŠ
type: teoria
typeName: Teória
label: T4
weight: 1004
points: '100'
authors:
- Jana Švrčková
hasSolution: true
source: 2026:-ZS/.RK/Dalekohlady.tex
years:
- '2026'
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

V čilskej púšti Atacama sa na hore Cerro Paranal nachádza observatórium známe vďaka skupine ďalekohľadov, ktoré sa dohromady nazývajú *Very Large Telescope* (VLT). VLT sa celkovo skladá z 8 ďalekohľadov, 4 z nich sa nazývajú *Unit Telescopes* (UT) a každý z nich má priemer primárneho zrkadla $8{,}2\,\mathrm{m}$. Zvyšné 4 ďalekohľady sa nazývajú *Auxiliary Telescopes* (AT) a majú priemer primárneho zrkadla $1{,}8\,\mathrm{m}$. AT sú zaujímavé najmä tým, že môžu meniť svoju polohu a využívajú sa na pozorovaciu techniku, ktorá sa nazýva interferometria.

Interferometria nám umožňuje kombinovať svetlo medzi dvomi ďalekohľadmi a získať tým oveľa lepšie rozlíšenie. Rozlíšenie interferometra totiž nezávisí od rozmerov jednotlivých ďalekohľadov, ale od vzdialenosti medzi nimi. Minimálna možná vzdialenosť medzi dvomi AT je $8\,\mathrm{m}$ a maximálna vzdialenosť je $200\,\mathrm{m}$.

O niekoľko desiatok kilometrov ďalej sa na hore Cerro Armazones buduje najväčší ďalekohľad na svete – *Extremely Large Telescope* (ELT) s priemerom primárneho zrkadla až $39\,\mathrm{m}$. Skladať sa má zo 798 šesťuholníkových segmentov a k dispozícii bude 133 náhradných segmentov, ktorými sa budú postupne nahrádzať použité segmenty. Denne je možné vymeniť 2 segmenty, vďaka čomu bude ďalekohľad neustále použiteľný a primárne zrkadlo v excelentnom stave.

<ol type="a">

<li>

<span class="body">[25 b]</span> Koľkokrát lepšie je uhlové rozlíšenie ELT (teda koľkokrát uhlovo menšie objekty dokáže ELT rozlíšiť) v porovnaní s jedným UT na Paranale? Predpokladajte, že obidva ďalekohľady pozorujú rovnaké vlnové dĺžky svetla.

</li>

<li>

<span class="body">[10 b]</span> Za akú dobu sa obmení všetkých 798 segmentov primárneho zrkadla na ELT?

</li>

<li>

<span class="body">[15 b]</span> Aké by bolo zväčšenie ELT, ak by sme namiesto rôznych prístrojov použili okulár s ohniskovou vzdialenosťou $30\,\mathrm{mm}$? Ohnisková vzdialenosť samotného ďalekohľadu je až $17{,}75\,\mathrm{m}$.

</li>

<li>

<span class="body">[25 b]</span> Koľkokrát viac svetla zozbiera ELT ako všetky 4 UT? Tvar primárneho zrkadla ELT je pomerne komplikovaný, pre účely tohto príkladu si ho ale môžete predstaviť ako kruh so spomínaným priemerom $39\,\mathrm{m}$ s dierou v strede (slúži na prechod svetla k ostatným zrkadlám), ktorá má priemer $11{,}1\,\mathrm{m}$. Primárne zrkadlá UT majú klasický, kruhový tvar.

</li>

<li>

<span class="body">[25 b]</span> Interferometer GRAVITY kombinuje svetlo dvojíc ďalekohľadov AT s vlnovou dĺžkou $2200\,\mathrm{nm}$. Vypočítajte najlepšie možné rozlíšenie, aké môže dosiahnuť GRAVITY, a porovnajte ho s rozlíšením ELT na vlnovej dĺžke $550\,\mathrm{nm}$ (viditeľné svetlo). Ktorý z týchto prístrojov má detailnejšie rozlíšenie?

</li>

</ol>

**Pomôcky:** Úlohy v tomto príklade na seba nenadväzujú a môžete ich riešiť v ľubovoľnom poradí. Pri počítaní príkladu môžete využiť vzorec na uhlové rozlíšenie ďalekohľadu 

$$
\theta = 206\,265\cdot1,22 \cdot\frac{\lambda}{D}\, , \tag{1}
$$

 kde $\lambda$ je vlnová dĺžka v metroch, na ktorej ďalekohľad pozoruje, a $D$ je priemer ďalekohľadu v metroch. Výsledný uhol $\theta$ vychádza v uhlových sekundách ($''$).

Vzorec na rozlíšenie interferometra je mierne odlišný. Platí 

$$
\theta = 206\,265\cdot\frac{\lambda}{2d}\, , \tag{2}
$$

 kde $\lambda$ je vlnová dĺžka v metroch a $d$ je vzdialenosť v metroch medzi dvomi ďalekohľadmi, ktorých svetlo kombinujeme. Výsledný uhol $\theta$ vychádza v uhlových sekundách ($''$).

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Túto úlohu je možné riešiť dvomi spôsobmi. Začneme tým rýchlejším. Stačí, ak si uvedomíme, že v prípade, keď ďalekohľady pozorujú na rovnakej vlnovej dĺžke, pomer ich rozlišovacích schopností závisí iba od pomeru ich priemerov. Ten vypočítame jednoducho 

$$
\frac{D_{ELT}}{D_{UT}}=\frac{39}{8,2} \doteq \boxed{4,8}\, .
    \qquad\textit{[25\,b]} \tag{3}
$$

Druhou, zdĺhavejšou možnosťou je vypočítať číselné hodnoty rozlíšení oboch ďalekohľadov pre určitú vlnovú dĺžku a porovnať ich. Použijeme napríklad $550\,\mathrm{nm}$, čo je typická vlnová dĺžka viditeľného svetla, a pre ELT nám vyjde rozlíšenie 

$$
\theta_{ELT} = 206\,265\cdot1,22\cdot\frac{\lambda}{D_{ELT}}\, = 
    206\,265\cdot1,22\cdot\frac{550 \cdot 10^{-9}}{39} \doteq 0{,}00355''\, . \qquad\textit{[10\,b]} \tag{4}
$$

 V prípade UT dostaneme 

$$
\theta_{UT} = 206\,265\cdot1,22\cdot\frac{\lambda}{D_{UT}} = 
    206\,265\cdot1,22\cdot\frac{550 \cdot 10^{-9}}{8,2} \doteq 0{,}0169''\, . \qquad\textit{[10\,b]} \tag{5}
$$

Porovnaním týchto dvoch rozlíšení získame opäť rovnaký výsledok ako zrýchleným postupom 

$$
\frac{\theta_{UT}}{\theta_{ELT}} = \frac{0,0169}{0,00355} \doteq 4,8\, . \qquad\textit{[5\,b]} \tag{6}
$$

Rozlíšenie ELT je teda 4,8-krát lepšie ako rozlíšenie UT.

</li>

<li>

Vieme, že za jeden deň sa dajú vymeniť 2 segmenty zrkadla, pričom celkovo ich je potrebné vymeniť 798. To sa dá stihnúť za čas 

$$
\frac{798}{2/\mathrm{deň}}=\boxed{399\,\mathrm{dní}} \, , \qquad\textit{[10\,b]} \tag{7}
$$

 čiže zhruba za rok a jeden mesiac.

</li>

<li>

Zväčšenie vypočítame jednoducho ako podiel ohniskovej vzdialenosti ďalekohľadu $f_d$ a ohniskovej vzdialenosti okuláru $f_{ok}$ 

$$
\frac{f_{d}}{f_{ok}}=
    \frac{17{,}75\,\mathrm{m}}{30\,\mathrm{mm}} = 
    \frac{17{,}75\,\mathrm{m}}{0{,}03\,\mathrm{m}} \doteq \boxed{592}\, . \qquad\textit{[15\,b]} \tag{8}
$$

</li>

<li>

Ďalekohľad zbiera svetlo celou plochou primárneho zrkadla, v tejto úlohe preto potrebujeme vypočítať pomer plochy ELT a súčtu plôch všetkých štyroch UT. Najskôr si vypočítame plochu primárneho zrkadla ELT. Je potrebné mať na pamäti, že v jeho strede je kruhová diera, ktorej plochu je potrebné odčítať. 

$$
S_{ELT} = \pi \cdot \left(\frac{D_{ELT}}{2}\right)^2 - \pi \cdot \left(\frac{D_{diera}}{2} \right)^2
    = \pi \cdot \frac{(39\,\mathrm{m})^2}{4} - \pi \cdot \frac{ (11{,}1\,\mathrm{m})^2}{4} \doteq 1098\,{\mathrm{m}}^{2} \, .\qquad\textit{[14\,b]} \tag{9}
$$

 Výpočet súčtu plôch UT je jednoduchý, keďže ide iba o 4 kruhové zrkadlá. 

$$
S_{4UT} = 4\cdot \pi \cdot \left(\frac{ D_{UT}}{2} \right)^2 = \pi D_{UT}^2 =  \pi \cdot (8{,}2\,\mathrm{m})^2 \doteq 211\,{\mathrm{m}}^{2} \, . \qquad\textit{[8\,b]} \tag{10}
$$

 ELT teda zozbiera 5,2-krát viac svetla ako všetky 4 UT dohromady, keďže pomer plôch je 

$$
\frac{S_{ELT}}{S_{4UT}} = \frac{1098\,{\mathrm{m}}^{2}}{211\,{\mathrm{m}}^{2}} \doteq \boxed{5,2} \, . \qquad\textit{[3\,b]} \tag{11}
$$

</li>

<li>

Rozlíšenie ELT na príslušnej vlnovej dĺžke sme už vypočítali v časti (a), potrebujeme už len zistiť rozlíšenie GRAVITY, ktoré získame zo špeciálneho interferometrického vzorca (2). Tu si treba uvedomiť, že najlepšie možné rozlíšenie je vlastne to najmenšie možné rozlíšenie, pretože nám umožňuje vidieť čo najviac detailov. Zo vzorca (2) vidíme, že číselná hodnota rozlíšenia je nepriamo úmerná vzdialenosti medzi ďalekohľadmi. Do vzorca preto dosadíme najväčšiu možnú vzdialenosť medzi AT, čo je $200\,\mathrm{m}$, a dostaneme 

$$
\theta_{GRAVITY} = 206\,265\cdot\frac{\lambda_{\mathrm G}}{2d_{AT,max}}
    = 206\,265\cdot\frac{2200 \cdot 10^{-9}\,\mathrm{m}}{2\cdot 200\,\mathrm{m}} \doteq 0{,}00113''\, . \qquad\textit{[20\,b]} \tag{12}
$$

 Uhol $\theta_{GRAVITY}$ je menší ako uhol $\theta_{ELT}$, teda s GRAVITY vidíme menšie detaily ako s ELT. Pomer rozlíšení je 

$$
\frac{\theta_{ELT}}{\theta_{GRAVITY}} = \frac{0{,}00355''}{0{,}00113''} \doteq \boxed{3,1}\, . \qquad\textit{[5\,b]} \tag{13}
$$

</li>

</ol>

</details>
