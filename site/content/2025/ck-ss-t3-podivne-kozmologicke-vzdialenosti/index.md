---
title: Podivné kozmologické vzdialenosti
year: 2025
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: T3
weight: 5003
points: '60'
authors:
- J. Švrčková
hasSolution: true
source: 2025:3-CK/1-SS/03-Kozmologia/00-zadanie.tex
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

V kozmológii sa vyskytujú javy, ktoré sa natoľko vymykajú našej bežnej skúsenosti, že sa nám na prvý pohľad zdajú až paradoxné. Jeden z nich sa týka aj uhlovej veľkosti, pod akou pozorujeme objekty hlbokého vesmíru. Z našej bežnej skúsenosti vieme, že čím je objekt ďalej, tým sa nám javí menší, teda má menší uhlový rozmer. Tento fakt sa dá využiť na určenie vzdialenosti objektu, za predpokladu, že poznáme jeho fyzický rozmer.

V kozmológii to ale nie je tak jednoduché. Existuje určitá vzdialenosť, od ktorej sa uhlový priemer objektu s pribúdajúcou vzdialenosťou začne zväčšovať. Tento efekt sa dá zjednodušene vysvetliť ako dôsledok konečnej rýchlosti svetla. Lúče svetla pochádzajúce z galaxie z raného vesmíru k nám od nej cestovali dlhú dobu a pochádzajú z čias, kedy bola galaxia oveľa bližšie. Galaxiu kvôli tomu v podstate pozorujeme s uhlovým priemerom, aký mala v čase, keď z nej vyrazili lúče svetla. Kvôli expanzii vesmíru je ale v súčasnosti vo väčšej vzdialenosti, ktorá by mala zodpovedať menšiemu uhlovému priemeru, ako pozorujeme (zobrazené na obrázku nižšie).

<img class="invert" src="CK-Kozmologia.svg" style="width:90.0%" alt="image" />

Konkrétna vzdialenosť, v ktorej prevládne tento kozmologický efekt a uhlový priemer objektov sa začne zväčšovať, závisí na geometrii a hustote jednotlivých zložiek vesmíru. Vzdialenosť, v  ktorej k tomu dochádza, nazveme bod obratu uhlovej vzdialenosti.

Na to, aby sme dokázali vypočítať hodnotu tejto vzdialenosti, budeme potrebovať dve základné rovnice popisujúce vývoj vesmíru: Friedmannovu rovnicu a deceleračnú rovnicu 

$$
H^2 + \frac{Kc^2}{a^2} = \frac{\Lambda c^2}{3}+\frac{8\pi G }{3}\rho \, , \tag{1}
$$

 

$$
-2qH^2 + H^2 + \frac{Kc^2}{a^2} = \Lambda c^2 - \frac{8\pi G}{c^2}P \, . \tag{2}
$$

$H$ je Hubblov parameter (konštanta), $K$ je krivosť geometrie vesmíru, $a$ je faktor škály, $\rho$ je súčet hustoty hmoty a žiarenia, $\Lambda$ je kozmologická konštanta, $P$ je tlak žiarenia (tlak hmoty zanedbáme) a $q$ je deceleračný parameter (číselné vyjadrenie spomaľovania rozpínania vesmíru). Hodnota krivosti je $+1$ pre sférickú, $0$ pre plochú a $-1$ pre hyperbolickú geometriu vesmíru.

<ol type="a">

<li>

<span class="body">[10 b]</span> Vypočítajte hodnotu deceleračného parametra pre plochý vesmír bez tmavej energie, ktorý sa skladá iba z hmoty. Tieto predpoklady považujte za pravdivé aj vo všetkých zvyšných podúlohách.

</li>

</ol>

Ak poznáme lineárny (fyzický) aj uhlový priemer objektu, vieme vypočítať jeho tzv. uhlovú vzdialenosť $d_A$ – teda vzdialenosť, z akej by sme objekt s priemerom $D$ pozorovali pod uhlovým priemerom $\theta$, ak by sme neuvažovali žiadne kozmologické efekty. Uhlovú vzdialenosť vieme v kozmológii určiť aj na základe červeného posunu $z$, za predpokladov uvedených v úlohe (a) pre ňu totiž platí Mattigov vzťah: 

$$
d_A = \frac{c}{Hq^2} \cdot \frac{zq+(q-1)(\sqrt{2qz+1}-1)}{(1+z)^2}\, . \tag{3}
$$

<ol type="a" start="2">

<li>

<span class="body">[30 b]</span> Vypočítajte červený posun bodu obratu uhlovej vzdialenosti, teda miesta, na ktorom sa uhlový rozmer objektu s narastajúcou vzdialenosťou začne zväčšovať.

</li>

</ol>

Zatiaľ čo v klasickej fyzike vzdialenosti určené rôznymi metódami sú v princípe rovnaké, v kozmológii toto neplatí. Existuje niekoľko rôznych definícií vzdialenosti, pričom každá z nich má inú hodnotu. Pre malé hodnoty červeného posunu sa ale všetky rovnajú, tak ako by sme to čakali podľa našich bežných skúseností.

<ol type="a" start="3">

<li>

<span class="body">[20 b]</span> Vypočítajte uhlovú vzdialenosť $d_A$ (v parsekoch) pre červený posun bodu obratu a porovnajte ju so vzdialenosťou, ktorá vychádza z Hubblovho-Lemaîtreovho zákona. Ktorá je väčšia a koľkokrát?

</li>

</ol>

***Pomôcka:*** funkcia v tvare $f(x)=A \cdot (x^b-x^c)$ má maximum v bode $x$ spĺňajúcom rovnicu 

$$
A \cdot (bx^{b-1}-cx^{c-1})=0 \,. \tag{4}
$$

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Zadanie nám hovorí, že vesmír má byť plochý, to znamená, že jeho krivosť je $K=0$. Kozmologická konštanta popisuje v rovniciach 1 a 2 vplyv tmavej energie na evolúciu vesmíru. Keďže požadujeme vesmír bez tmavej energie, musí byť $\Lambda = 0$. Poslednou požiadavkou v zadaní je, že sa vesmír má skladať iba z hmoty, teda v ňom nie je žiadne žiarenie. Tým pádom je aj tlak žiarenia nulový, $P=0$. Deceleračná rovnica 2 sa nám vďaka tomu zjednoduší na

</li>

</ol>

$$
-2qH^2+H^2 = 0 \, . \tag{5}
$$

To môže platiť iba v prípade, že má deceleračný parameter hodnotu $q=\frac{1}{2}$.

<ol type="a" start="2">

<li>

Do rovnice 3 dosadíme hodnotu deceleračného parametra zistenú v časti (a) a budeme ju upravovať, až kým ju nedostaneme do tvaru $d_A(x)=A(x^b-x^c)$.

</li>

</ol>

$$
d_A = \frac{4c}{H}\cdot\frac{\frac{1}{2}z-\frac{1}{2}(\sqrt{z+1}-1)}{(1+z)^2} \, , \tag{6}
$$

 

$$
d_A = \frac{4c}{H}\cdot\frac{\frac{1}{2}z-\frac{1}{2}\sqrt{z+1}+\frac{1}{2}}{(1+z)^2} \, , \tag{7}
$$

 

$$
d_A = \frac{2c}{H}\cdot\frac{z+1-\sqrt{z+1}}{(1+z)^2} \, , \tag{8}
$$

 

$$
d_A = \frac{2c}{H}\left[(1+z)^{-1}-(1+z)^{-\frac{3}{2}}\right] \, . \tag{9}
$$

 Rovnica je v požadovanom tvare, pričom konštanty sú $A=\frac{2c}{H}$, $b=-1$ a $c=-\frac{3}{2}$ a premenná $x=1+z$. Teraz budeme hľadať hodnotu $1+z$ (resp. $z$), pre ktorú dosiahne pravá strana rovnice maximum. Využijeme pri tom nápovedu zo zadania.

$$
\frac{2c}{H}\left[(-1)(1+z)^{-2}+\frac{3}{2}(1+z)^{-\frac{5}{2}}\right] = 0 \, , \tag{10}
$$

 

$$
\frac{1}{(1+z)^2}=\frac{3}{2}\cdot\frac{1}{(1+z)^{\frac{5}{2}}} \, , \tag{11}
$$

 

$$
\frac{(1+z)^{\frac{5}{2}}}{(1+z)^2}=\frac{3}{2} \, , \tag{12}
$$

 

$$
(1+z)^{\frac{5}{2}-2}=\frac{3}{2} \, , \tag{13}
$$

$$
\sqrt{1+z}=\frac{3}{2} \, , \tag{14}
$$

 

$$
z = \frac{9}{4}-1 = \frac{5}{4} = 1,25\, . \tag{15}
$$

Na tomto červenom posune dosiahne uhlová vzdialenosť maximum, tým pádom uhlová veľkosť objektov tu dosahuje minimum. Našli sme teda požadovaný červený posun bodu obratu.

<ol type="a" start="3">

<li>

Najskôr dosadíme $z$ do rovnice 3 a vypočítame uhlovú vzdialenosť.

</li>

</ol>

$$
d_A = \frac{4c}{H}\cdot\frac{\frac{1}{2}\cdot\frac{5}{4}-\frac{1}{2}\left(\sqrt{\frac{5}{4}+1}-1\right)}{\left(1+\frac{5}{4}\right)^2} \, , \tag{16}
$$

 

$$
d_A = \left(\frac{2}{3}\right)^{3}\frac{c}{H} \approx 1270\,\mathrm{Mpc}\, . \tag{17}
$$

Teraz ešte vypočítame vzdialenosť bodu obratu z Hubblovho-Lemaîtrovho zákona. Červený posun je väčší ako 1, preto na výpočet radiálnej rýchlosti musíme použiť relativistický vzorec

$$
v=\frac{(1+z)^2-1}{(1+z)^2+1}\,c = \frac{\left(\frac{9}{4}\right)^2-1}{\left(\frac{9}{4}\right)^2+1} \, c = \frac{65}{97}\, c \, . \tag{18}
$$

Z Hubblovho-Lemaîtrovho zákona dostávame vzdialenosť 

$$
r=\frac{v}{H} = \frac{65}{97}\cdot\frac{c}{H} \approx 2870\,\mathrm{Mpc} \,. \tag{19}
$$

Zostáva nám už len tieto dve vzdialenosti porovnať,

$$
\frac{r}{d_A}=\frac{65}{97}\cdot\frac{27}{8} \approx 2,26 \, . \tag{20}
$$

Vzdialenosť určená z Hubblovho-Lemaîtrovho zákona je v bode obratu približne 2,26-krát väčšia ako uhlová vzdialenosť.

</details>
