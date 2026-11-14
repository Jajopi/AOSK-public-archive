---
title: Neapochromat
year: 2024
round: RK
roundName: Regionálne kolo
category: ZŠ
type: teoria
typeName: Teória
label: T2
weight: 1002
points: '90'
authors:
- Samuel Amrich
hasSolution: true
source: 2024:RK/ZS/aTeoria/Neapochromat.tex
rocniky:
- '2024'
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

Predstavte si klasický šošovkový ďalekohľad Keplerovho typu, zložený z dvoch spojných šošoviek. Objektív je vyrobený z nekvalitného skla a tak má veľkú farebnú chybu. Čo znamená, že má rozdielne indexy lomu $n$ pre rôzne vlnové dĺžky a teda rôzne farby svetla.

|          |           |
|:---------|:----------|
| Červená: | $n_{\mathrm{red}}=1{,}6 \,.$ |
| Modrá:   | $n_{\mathrm{blue}} = 1{,}7 \,.$ |

Pre červené svetlo bola zistená ohnisková vzdialenosť objektívu $f_\mathrm{red}=1{,}2\,\mathrm{m}$. O koľko $\mathrm{cm}$ je potrebné posunúť okulár, aby bol obraz zaostrený pre modré svetlo?

Predpokladajte index lomu vzduchu $n_\mathrm{air}=1$ a že objektív je tenká šošovka, pre ktorej ohniskovú vzdialenosť platí nasledujúci vzťah ($R_1$ a $R_2$ sú polomery krivosti šošovky) 

$$
\frac{1}{f} = \left(\frac{n}{n_\mathrm{air}} - 1\right)\cdot \left[ \frac{1}{R_1} + \frac{1}{R_2} \right]. \tag{1}
$$

<details class="solution">
<summary>Riešenie</summary>

Vzťah pre tenkú šošovku je

$$
\frac{1}{f} = \left(\frac{n}{n_\mathrm{air}} - 1\right)\cdot \left[ \frac{1}{R_1} + \frac{1}{R_2} \right] \,. \tag{2}
$$

Kde $f$ je ohnisková vzdialenosť, $n_\mathrm{air}$ je index lomu okolia (vzduchu), $n$ je index lomu šošovky a $R_1$, $R_2$ sú polomery krivosti prvej a druhej strany šošovky.

V našom prípade máme stále tú istú geometriu šošovky, takže polomery krivosti sa nemenia a celú hranatú zátvorku môžeme zameniť za konštantu neznámu $k$.

$$
\frac{1}{f} = \left(\frac{n}{n_\mathrm{air}} - 1\right)\cdot k \,. \tag{3}
$$

Čo po prepísaní pre dvojicu vlnových dĺžok zo zadania, a po dosadení $n_\mathrm{air} = 1$, dostaneme 

$$
\begin{align*}
    \frac{1}{f_{\mathrm{red}}} &= (n_{\mathrm{red}} - 1)\cdot k\,, \tag{4}\\
    \frac{1}{f_{\mathrm{blue}}} &= (n_{\mathrm{blue}} - 1)\cdot k\,. \tag{5}\end{align*}
$$

 Vidíme, že poznáme všetko okrem $k$ a $f_{\mathrm{blue}}$, ktoré chceme zistiť. Keďže máme 2 rovnice, vieme sa $k$ zbaviť. Využijeme pritom poznatok, že 

$$
x=y \and a=b \ztv \frac{x}{a}=\frac{y}{b} \,. \tag{6}
$$

 Potom ak to aplikujeme na rovnice (4) a (5), dostaneme výraz ktorý vyzerá najprv zložito ale následne sa jednoducho vyrieši. 

$$
\frac{\frac{1}{f_{\mathrm{red}}}}{\frac{1}{f_{\mathrm{blue}}}} = \frac{(n_{\mathrm{red}} - 1)\cdot k}{(n_{\mathrm{blue}} - 1)\cdot k} \,. \tag{7}
$$

Kde vyriešime zložený zlomok naľavo ako $\frac{f_{\mathrm{blue}}}{f_{\mathrm{red}}}$ a $k$ napravo vykrátime, potom 

$$
\frac{f_{\mathrm{blue}}}{f_{\mathrm{red}}} = \frac{(n_{\mathrm{red}} - 1)}{(n_{\mathrm{blue}} - 1)} \,. \tag{8}
$$

 Z čoho jednoducho zistíme riešenie 

$$
f_{\mathrm{blue}} = f_{\mathrm{red}} \cdot \frac{(n_{\mathrm{red}} - 1)}{(n_{\mathrm{blue}} - 1)} \approx 1{,}03\,\mathrm{m} \,. \tag{9}
$$

A teda je potrebné posunúť okulár o $\triangle = f_{\mathrm{red}} - f_{\mathrm{blue}} \approx 0{,}17\,\mathrm{m}$ bližšie ku šošovke.

</details>
