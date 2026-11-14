---
title: Kam dovidí Kolonica
year: 2024
round: DK
roundName: Domáce kolo
category: ZŠ
type: teoria
typeName: Teória
label: T1
weight: 1
points: '75'
authors:
- Samuel Amrich
hasSolution: true
source: 2024:DK/ZS/Kam-dovidi-Kolonica.tex
rocniky:
- '2024'
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

Jeden z dôvodov, prečo používame ďalekohľady je, že nám umožňujú zachytiť viac svetla, a tým odpozorovať slabšie hviezdy. Aké najslabšie hviezdy možno pozorovať ďalekohľadom na Astronomickom observatóriu na Kolonickom sedle s priemerom zrkadla $D=1\,\mathrm{m}$, ak naše oko cez zrenicu s priemerom $d=1\,\mathrm{cm}$ vidí hviezdy s jasnosťou $m=6\,\mathrm{mag}$?

Výsledok uveďte v magnitúdach. Dôležité je si uvedomiť, že množstvo zachyteného svetla ďalekohľadom je závislé od zbernej plochy.

<details class="solution">
<summary>Riešenie</summary>

Najprv sa k výsledku pokúsime dostať pomocou jednoduchých úvah a takmer bez toho aby sme potrebovali zložitú matematiku. Jeden meter štvorcový predstavuje desaťtisíckrát väčšiu plochu ako jeden centimeter štvorcový. Väčšia plocha ďalekohľadu zachytí viac svetla z hviezdy, ktoré sa nám následne premieta do oka.

Posun 5 magnitúd je zadefinovaný ako stonásobne viac svetla (odborne sa tomu hovorí tok). V našom prípade máme $10\,000 = 100\cdot 100$ krát viac svetla, čo zodpovedá posunu o $5+5=10$ magnitúd. Preto Kolonica musí byť schopná zachytiť o desať magnitúd slabšie objekty ako ľudské oko. Teda z magnitúdy 6 na magnitúdu 16.

Ak ale chceme poznať pravé fyzikálne riešenie, potrebujeme začať s Pogsonovou rovnicou 

$$
m'-m=-2,5\log{\left(\frac{F'}{F}\right)}\,, \tag{1}
$$

 kde $m$ a $m'$ sú magnitúdy dvoch hviezd (alebo jednej hviezdy cez dva rôzne objektívy ako v našom príklade) a $F$, $F'$ sú prisluchajúce toky. S čiarkou označujeme veličiny spojené s pozorovaním cez ďalekohľad.

Dôležité je si uvedomiť, že limitná magnitúda je naviazaná na limitný výkon $P_L$ hviezdy (hviezdu naše oko vidí, až keď presiahne určitý limitný výkon), ktorý dokážeme zachytiť. A ten súvisí s tokom $F$ a zachytávajúcou plochou $S$ nasledujúco 

$$
P_\mathrm{L}=SF \ztv F = \frac{P_\textrm{L}}{S}\,, \tag{2}
$$

 respektíve pre $F'$ a $S'$ 

$$
P_\textrm{L}=S' F' \ztv F' = \frac{P_\textrm{L}}{S'}\,. \tag{3}
$$

Takže do všeobecnej Pogsonovej rovnice (1) vieme dosadiť vzťahy (2) a (3), čím dostávame 

$$
m'-m = -2,5\log{\left( \frac{\frac{P_\textrm{L}}{S'}}{\frac{P_\textrm{L}}{S}}\right)}
    = -2,5\log{\left(\frac{P_\textrm{L}}{S'} \cdot \frac{S}{P_\textrm{L}}\right)}
    = -2,5\log{\left( \frac{S}{S'} \right)} \,. \tag{4}
$$

Teraz potrebujeme určiť plochu $S$ a $S'$. Predpokladáme kruhový tvar oka a ďalekohľadu, potom 

$$
\begin{align*}
    S&=\pi r^2 = \pi \left( \frac{d}{2} \right)^2 = 0,25 \pi d^2 \,, \tag{5}\\
    S'&= 0,25 \pi D^2 \,. \tag{6}\end{align*}
$$

 Čo po spätnom dosadení do (4) 

$$
\begin{align*} 
    m'-m &= -2,5\log{\left( \frac{S}{S'} \right)}
    = -2,5\log{\left( \frac{0,25 \pi d^2}{0,25 \pi D^2} \right)}\,, \tag{7}\\
    &= -2,5\log{\left( \frac{d^2}{D^2} \right)}
    = -2,5\log{\left( \left( \frac{d}{D} \right)^2\right) } \,. \tag{8}\end{align*}
$$

 Čo po dosadení konkrétnych hodnôt 

$$
m' = 16\,\mathrm{mag}. \tag{9}
$$

**Poznámka:** Eventuálne vieme na zjednodušenie vzťahu vyššie využiť vlastnosť logaritmu $\log{\left(x^n\right)}=n\log{\left(x\right)}$. Potom je výsledným vzorcom 

$$
m' = m-5\log{\left(  \frac{d}{D} \right) }= 16\,\mathrm{mag} \,. \tag{10}
$$

</details>
