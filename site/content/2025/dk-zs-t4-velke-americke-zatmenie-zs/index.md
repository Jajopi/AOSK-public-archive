---
title: Veľké americké zatmenie (ZŠ)
year: 2025
round: DK
roundName: Domáce kolo
category: ZŠ
type: teoria
typeName: Teória
label: T4
weight: 4
points: '60'
authors:
- Jana Švrčková
hasSolution: true
source: 2025:1-DK/0-ZS/04-Zatmenie-Slnka/00-zadanie.tex
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

8\. apríla 2024 bolo možné na americkom kontinente pozorovať úplné zatmenie Slnka. Do USA vtedy za zatmením cestovala aj skupina astronómov z Astronomického klubu Bratislava, ktorej súčasťou bolo aj niekoľko bývalých riešiteľov AO. Počas cesty sa zamýšľali nad tým, ako najďalej od Zeme môže byť Mesiac, aby sa aspoň na jednom mieste na Zemi dalo pozorovať úplné zatmenie Slnka. Vašou úlohou je vypočítať túto maximálnu vzdialenosť stredu Mesiaca od stredu Zeme za predpokladu, že Zem obieha okolo Slnka po kruhovej dráhe. Uvažujte, že spomínané nebeské telesá majú guľový tvar. Nezabudnite na to, že pozorovateľ stojí na povrchu Zeme.

<details class="solution">
<summary>Riešenie</summary>

Najskôr je potrebné si uvedomiť, na ktorom mieste na Zemi by sa dalo úplné zatmenie pozorovať, ak by Mesiac bol v maximálnej vzdialenosti prípustnej pre úplné zatmenie. Mesiac je ďaleko, preto pozorovateľ musí byť k nemu čo najbližšie, aby sa mu Mesiac javil čo najväčší v porovnaní so Slnkom. Hraničná situácia nastane práve vtedy, keď sa pozorovateľ nachádza na zemskom rovníku na spojnici stredu Zeme so Slnkom a Mesiac má z jeho pohľadu presne rovnakú uhlovú veľkosť ako Slnko. Keďže sa jedná o úplné zatmenie, stred Slnka, stred Mesiaca a pozorovateľ sa musia nachádzať na jednej priamke.

<figure>

<div class="fig-images"><img class="invert" src="DK-ZS-zatmenie-riesenie-v4.svg" alt="obrázok" loading="lazy" style="width:60%"></div>

<figcaption>

**Obrázok 1:** Geometria úplného zatmenia Slnka pri maximálnej vzdialenosti stredu Mesiaca od stredu Zeme.
</figcaption>

</figure>

Pri riešení tejto úlohy je dôležité si nakresliť dobrý obrázok. Na obr. 1 je veľká polos $a_\Ea$ vzdialenosť od stredu Slnka po stred Zeme, zatiaľ čo $d_\Mo$ je vzdialenosť stredu Mesiaca od pozorovateľa na zemskom rovníku. Vieme, že uhlová veľkosť Slnka a Mesiaca je rovnaká, vďaka tomu môžeme využiť podobnosť trojuholníkov. Platí 

$$
\frac{R_\Sun}{a_\Ea-R_\Ea}=\frac{R_\Mo}{d_\Mo}\, . \tag{1}
$$

 Polomer Zeme je veľmi malý v porovnaní so vzdialenosťou Zeme od Slnka, preto by nevadilo, ak by sme ho v našom výpočte zanedbali. Zo vzorca (1) vyššie vyjadríme $d_\Mo$ 

$$
d_\Mo = \frac{R_\Mo}{R_\Sun}(a_\Ea-R_\Ea) \approx 3{,}735 \cdot 10^{8}\,\mathrm{m}\, . \tag{2}
$$

 Aby sme dostali vzdialenosť stredu Mesiaca od stredu Zeme $x_\Mo$, musíme k $d_\Mo$ ešte pripočítať polomer Zeme 

$$
x_\Mo = d_\Mo + R_\Ea \approx 3{,}799 \cdot 10^{8}\,\mathrm{m}\, . \tag{3}
$$

</details>
