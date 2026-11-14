---
title: Veľké americké zatmenie II (ZŠ)
year: 2025
round: RK
roundName: Regionálne kolo
category: ZŠ
type: teoria
typeName: Teória
label: T3
weight: 1003
points: '110'
authors:
- Jana Švrčková
hasSolution: true
source: 2025:2-RK/0-ZS/03-Zatmenie-Slnka-ZS-2/00-zadanie.tex
rocniky:
- '2025'
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

Na americkom kontinente sa 8. apríla 2024 odohralo úplné zatmenie Slnka. Hoci tento úkaz nastáva pomerne často, je stále veľmi vzácny, pretože je ho možné pozorovať iba z úzkeho pruhu na zemskom povrchu – tzv. pásu totality. Tento pás sa pri každom zatmení nachádza niekde inde, preto sa na jednom mieste na Zemi zatmenie vyskytuje extrémne zriedkavo. Navyše, máme šťastie, že tento úchvatný úkaz vôbec môžeme pozorovať. Pomerne známym faktom je, že Mesiac sa postupne vzďaľuje od Zeme. Jeho veľká polos sa zväčšuje tempom $3{,}78\,\mathrm{cm}/\mathrm{rok}$. Za určitú dobu sa Mesiac vzdiali natoľko, že už nebude možné pozorovať úplné zatmenie Slnka – Mesiac bude pri pohľade zo Zeme príliš malý na to, aby zakryl celé Slnko.

Vašou úlohou je zistiť, kedy k tomu dôjde. Vypočítajte, za koľko rokov bude naposledy možné aspoň z jedného miesta na Zemi pozorovať úplné zatmenie Slnka. Uvažujete eliptické dráhy Zeme aj Mesiaca okolo Slnka a nemennosť excentricity týchto dráh v čase, ako aj nemennosť veľkosti Slnka. Excentricita mesačnej dráhy je $e_\Mo = 0,0549$.

<details class="solution">
<summary>Riešenie</summary>

Podobne ako v úlohe o zatmení v domácom kole, je potrebné si dobre premyslieť geometriu úlohy. Hraničná situácia opäť nastane v momente, kedy pozorovateľ, ktorý sa nachádza na rovníku na priamke Slnko – Mesiac – pozorovateľ – stred Zeme, vidí Mesiac zdanlivo rovnako veľký ako Slnko.

Uhlový priemer Mesiaca, pod akým ho vidí pozorovateľ pri zatmení, závisí na dvoch okolnostiach: na veľkej polosi dráhy Mesiaca, ktorá sa postupne zväčšuje, a na aktuálnej polohe Mesiaca na jeho dráhe (teda či je v perigeu, apogeu alebo niekde medzi). Zato uhlový priemer Slnka závisí iba na polohe Zeme na jej dráhe.

Keďže sa veľká polos Mesiaca zväčšuje, jeho uhlový priemer sa zmenšuje. Zároveň vrámci jednej obežnej doby sa nám Mesiac javí najväčší vtedy, keď je v perigeu. Slnko sa nám javí najmenšie, keď je Zem v aféliu. Po uplynutí určitej doby sa dostaneme do situácie, kedy uhlový priemer Mesiaca v perigeu bude rovnaký ako uhlový priemer Slnka, keď je Zem v aféliu. Práve v tej chvíli bude (aspoň teoreticky) možné pozorovať posledné úplné zatmenie Slnka. Ak sa veľká polos Mesiaca ešte o niečo zväčší, Mesiac už nikdy nebude mať dostatočnú uhlovú veľkosť na to, aby zakryl celé Slnko, a preto nastane iba prstencové zatmenie.

Potrebujeme teda vypočítať vzdialenosť stredu Mesiaca od stredu Zeme, resp. veľkú polos Mesiaca, v tomto momente. Na základe známej rýchlosti zväčšovania jeho veľkej polosi vieme následne vypočítať, kedy bude možné pozorovať posledné úplné zatmenie Slnka.

Nakreslíme si podobný obrázok ako pri riešení úlohy z domáceho kola. V tomto prípade je ale Zem v aféliu, takže sa vzdialenosť Slnka od Zeme rovná $a_\Ea (1+e_\Ea)$. Vzdialenosť Mesiaca v perigeu od stredu Zeme je $a_\Mo(1-e_\Mo)$.

<figure>

<div class="fig-images"><img class="invert" src="AO-2025-RK-ZS-Zatmenie-1.svg" alt="obrázok" loading="lazy" style="width:60%"></div>

<figcaption>

**Obrázok 1:** Geometria posledného úplného zatmenia Slnka, ktoré by sa teoreticky dalo pozorovať z povrchu Zeme.
</figcaption>

</figure>

Keďže pre pozorovateľa na rovníku Zeme majú Slnko aj Mesiac rovnaký uhlový rozmer, môžeme využiť podobnosť trojuholníkov. Vzdialenosť Mesiaca od pozorovateľa je $d_\Mo = a_\Mo(1-e_\Mo) - R_\Ea$. Rovnakým spôsobom získame aj vzdialenosť Slnka od pozorovateľa. Kvôli podobnosti trojuholníkov platí rovnosť v tvare 

$$
\frac{R_\Sun}{a_\Ea (1+e_\Ea)-R_\Ea}=\frac{R_\Mo}{d_\Mo}\, . \tag{1}
$$

Vyjadríme si $d_\Mo$, 

$$
d_\Mo = \frac{R_\Mo}{R_\Sun}\big(a_\Ea (1+e_\Ea)-R_\Ea\big) \approx 3{,}798 \cdot 10^{8}\,\mathrm{m} \, . \tag{2}
$$

Teraz vypočítame veľkú polos Mesiaca v čase zatmenia 

$$
a_\Mo = \frac{d_\Mo+R_\Ea}{(1-e_\Mo)} \approx 4{,}086 \cdot 10^{8}\,\mathrm{m} \, . \tag{3}
$$

Hodnotu veľkej polosi mesiaca v súčasnosti si nájdeme v zozname konštánt, $a_{\Mo,0} = 3{,}844 \cdot 10^{8}\,\mathrm{m}$. Čas, ktorý uplynie od súčasnosti po posledné pozorovateľné úplné zatmenie Slnka, vypočítame ako 

$$
t=\frac{a_\Mo-a_{\Mo,0}}{v}\, , \tag{4}
$$

kde $v$ je rýchlosť zväčšovania sa veľkej polosi mesačnej dráhy. Treba si dať pozor na to, že v zadaní je táto hodnota uvedená v cm za rok. Číselne vyjde $t=6{,}4 \cdot 10^{8}\,\mathrm{rokov}$.

</details>
