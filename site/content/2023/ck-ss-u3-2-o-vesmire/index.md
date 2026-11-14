---
title: .2 - O vesmíre
year: 2023
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú3
weight: 2303
hasSolution: true
source: ZAO:I_Zadania/07_Kozmo/07_SS_FI.tex
rocniky:
- '2023'
kola:
- Celoštátne kolo
kategorie:
- SŠ
typy:
- Teória
tagy:
- Kozmológia
collection: ZAO
---

## Zadanie

Za predpokladu, že faktor škály $a$ je úmerný $t^{2/3}$, kde $t$ je vek vesmíru, vypočítajte v $\mathrm{kg}\,{\mathrm{m}}^{-3}$ hustotu normálnej hmoty, tmavej hmoty a tmavej energie v čase, kedy bol vek vesmíru 8 miliárd rokov. Parameter hustoty normálnej hmoty v súčasnosti je $\Omega_\mathrm{N,0} = 0{,}049$, tmavej hmoty $\Omega_\mathrm{DM,0} = 0{,}259$ a tmavej energie $\Omega_\mathrm{DE,0} = 0{,}691$. Parameter hustoty sa vypočíta ako $\Omega = \frac{\rho}{\rho_\mathrm{C}}$, kde je kritická hustota vesmíru $\rho_\mathrm{C} = 9 \cdot 10^{-27}\,\mathrm{kg}\,{\mathrm{m}}^{-3}$ . Hustota tmavej energie nezávisí na škálovom faktore $a$. Vesmír je v súčasnosti starý približne 14 miliárd rokov.

<details class="solution">
<summary>Riešenie</summary>

Hustota tmavej energie sa nemení, takže jej hodnota je stále $\rho_\textrm{DE,0}=0,691\cdot9 \cdot 10^{-27}=6{,}22 \cdot 10^{-27}\,\mathrm{kg}\,{\mathrm{m}}^{-3}$.\
Závislosť medzi hustotou normálnej (aj tmavej) hmoty a škálovým faktorom si zjednodušene môžeme odôvodniť s pomocou predstavy vesmíru, v ktorom sa nemení celková hmotnosť normálnej (tmavej) hmoty. Potom platí 

$$
\rho a^3 \ \propto \ m\, . \tag{1}
$$

 Z toho dostaneme 

$$
\rho \ \propto \ a^{-3}\, . \tag{2}
$$

 Všetky veličiny, ktoré sa týkajú súčasnosti si označíme indexom 0. Zo zadania poznáme úmernosť medzi faktorom škály a časom. Obidve úmernosti si prepíšeme ako pomery veličín v súčasnosti $t_0$ a v čase $t$ 

$$
\frac{a_0}{a}=\left(\frac{t_0}{t}\right)^{2/3}=\left(\frac{\rho_0}{\rho}\right)^{-1/3} \, , \tag{3}
$$

 

$$
\left(\frac{t_0}{t}\right)^{2}=\frac{\rho}{\rho_0} \, , \tag{4}
$$

 

$$
\rho =\left(\frac{t_0}{t}\right)^2\rho_0=\left(\frac{t_0}{t}\right)^2\Omega_0\rho_\textrm{c} \, . \tag{5}
$$

 Po číselnom dosadení dostaneme hustotu normálnej hmoty a tmavej hmoty 

$$
\rho_{NM}=\left(\frac{14}{8}\right)^2\cdot0,049\cdot9 \cdot 10^{-27}=1{,}35 \cdot 10^{-27}\,\mathrm{kg}\,{\mathrm{m}}^{-3} \, , \tag{6}
$$

 

$$
\rho_{DM}=\left(\frac{14}{8}\right)^2\cdot0,259\cdot9 \cdot 10^{-27}=7{,}14 \cdot 10^{-27}\,\mathrm{kg}\,{\mathrm{m}}^{-3} \, . \tag{7}
$$

</details>
