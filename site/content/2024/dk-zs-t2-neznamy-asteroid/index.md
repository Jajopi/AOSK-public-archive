---
title: Neznámy asteroid
year: 2024
round: DK
roundName: Domáce kolo
category: ZŠ
type: teoria
typeName: Teória
label: T2
weight: 2
points: '50'
authors:
- Samuel Buranský
hasSolution: true
source: 2024:DK/ZS/Neznamy-asteroid.tex
years:
- '2024'
rounds:
- Domáce kolo
categories:
- ZŠ
types:
- Teória
topics:
- Nezaradené
---

## Zadanie

Asteroid je najbližšie k Zemi $r_{\textrm{min}} = 1\,\mathrm{au}$ a najďalej $r_{\textrm{max}} = 5\,\mathrm{au}$. Určte parametre dráhy tohto asteroidu, konkrétne veľkú polos $a$, excentricitu $e$ a obežnú periódu $T$. Taktiež určte ako často môžeme pozorovať tento asteroid v západnej kvadratúre. Dráhu Zeme považujte za kruhovú s polomerom $r = 1\,\mathrm{au}$.

<details class="solution">
<summary>Riešenie</summary>

<figure>

<div class="fig-images"><img class="invert" src="neznamy_asteroid.svg" alt="obrázok" loading="lazy" style="width:100%"></div>

<figcaption>

**Obrázok 1:** Schéma dráhy Zeme a asteroidu.
</figcaption>

</figure>

Ak si nakreslíme dráhy Zeme a asteroidu (obrázok 1) vidíme, že najbližšie k Zemi je asteroid v opozícii, kedy je zároveň v perihéliu, a najďalej v konjunkcii, kedy je zároveň v aféliu. Priamo z obrázku platí $2a = r_\mathrm{min}+r_\mathrm{max} = 6\,\mathrm{au}$, kde $a$ je veľká polos dráhy asteroidu. Z toho dostávame $a = 3\,\mathrm{au}$.

Zároveň vzdialenosť od Slnka je v perihéliu $q = 2\,\mathrm{au}$ a v aféliu $Q = 4\,\mathrm{au}$. Excentricitu dráhy spočítame ako 

$$
e = \frac{a e}{a} = \frac{a - q}{a} = \frac{1}{3}\,, \tag{1}
$$

 kde $a e = a - q$ je lineárna excentricita, ktorá je rovná vzdialenosti stredu elipsy a jej ohniska.

Obežnú periódu $T$ určíme podľa 3. Keplerovho zákona pre slnečnú sústavu v tvare 

$$
a^3 = T^2\,, \tag{2}
$$

 kde $a$ udávame v astronomických jednotkách a $T$ v rokoch. Po úprave a dosadení dostávame 

$$
T = \sqrt{a^3} = \sqrt{27} \approx 5{,}20\,\mathrm{roka} \,. \tag{3}
$$

Opakovanie západnej kvadartúry je obežná doba asteroidu pri pohľade zo Zeme, teda jeho synodická obežná doba $S$, pre ktorú v rokoch platí 

$$
\frac{1}{S} = \frac{1}{T_\Ea} - \frac{1}{T} = 1\,{\mathrm{rok}}^{-1} - \frac{1}{\sqrt{27}}\;{\mathrm{roka}}^{-1} \approx 0{,}81\,{\mathrm{roka}}^{-1}\,, \tag{4}
$$

 odkiaľ po prevrátení zlomkov dostaneme $S \approx 1{,}24\,\mathrm{roka}$.

</details>
