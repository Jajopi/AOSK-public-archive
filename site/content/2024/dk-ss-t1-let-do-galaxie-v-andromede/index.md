---
title: Let do galaxie v Andromede
year: 2024
round: DK
roundName: Domáce kolo
category: SŠ
type: teoria
typeName: Teória
label: T1
weight: 3001
points: '100'
authors:
- Samuel Amrich
hasSolution: true
source: 2024:DK/SS/Let-do-Andromedy.tex
years:
- '2024'
rounds:
- Domáce kolo
categories:
- SŠ
types:
- Teória
topics:
- Nezaradené
---

## Zadanie

Predstavte si hypotetickú situáciu, že letíte z našej galaxie, Mliečnej cesty, do galaxie v Andromede (M 31). Vzdialenosť medzi nimi je $D = 2{,}54\,\mathrm{Mly} = 765\,\mathrm{kpc}$. V jednom momente sa budú galaxie javiť rovnako jasné. Vypočítajte vzdialenosť $r_{\mathrm{MW}}$ od Mliečnej cesty, v ktorej sa to udeje, ako aj hviezdnu veľkosť $m$, ktorú budú mať dané galaxie v tejto vzdialenosti. Počet hviezd v Mliečnej ceste je $n_{\mathrm{MW}} = 10^{11}$ a počet hviezd v galaxii M 31 je $n_{\mathrm{And}} = 2 \cdot 10^{11}$.

Predpokladajte, že v oboch galaxiách sa nachádzajú iba hviezdy slnečného typu. Zanedbajte medzihviezdnu extinkciu (absorpciu).

<details class="solution">
<summary>Riešenie</summary>

Začneme zapísaním si, že v momente, keď sa jasnosti galaxie v Andromede a Mliečnej cesty vyrovnajú, sme vo vzdialenosti $r_{\mathrm{MW}}$ od Mliečnej cesty a $r_{\mathrm{And}}$ od galaxie v Andromede. Keďže celková vzdialenosť medzi nimi je $D$, tak platí, že $D=r_{\mathrm{MW}}+r_{\mathrm{And}}$. Keďže sú toky $F_{\mathrm{MW}}$ a $F_{\mathrm{And}}$ vyrovnané, platí 

$$
F_{\mathrm{MW}} = F_{\mathrm{And}} \ztv
    \frac{L_{\mathrm{MW}}}{S_{\mathrm{MW}}} = \frac{L_{\mathrm{And}}}{S_{\mathrm{And}}}\,. \tag{1}
$$

 Kde $S_{\mathrm{MW}}$ a $S_{\mathrm{And}}$ sú plochy sféry s polomerom $r_{\mathrm{MW}}$ a $r_{\mathrm{And}}$ respektívne, na ktoré sa výkon $L_\mathrm{MW}$ a $L_\mathrm{And}$ hviezdy rozkladá.

Keďže plocha sféry je $S=4\pi r^2$, tak 

$$
\begin{align*}
    \frac{L_{\mathrm{MW}}}{4\pi {r_{\mathrm{MW}}^2}} &= \frac{L_{\mathrm{And}}}{4\pi {r_{\mathrm{And}}^2}}\,, \tag{2}\\
    \frac{L_{\mathrm{MW}}}{ {r_{\mathrm{MW}}^2}} &= \frac{L_{\mathrm{And}}}{ {r_{\mathrm{And}}^2}}\,, \tag{3}\\
    \frac{L_{\mathrm{MW}}}{ {r_{\mathrm{MW}}^2}} &= \frac{L_{\mathrm{And}}}{ {(D-r_{\mathrm{MW}})^2}}\,. \tag{4}\end{align*}
$$

Zároveň vieme, aký je svetelný výkon galaxií, pretože je to len vynásobenie počtu hviezd s výkonom jednej hviezdy. Taktiež vďaka znalosti, že $n_{\mathrm{And}} = 2n_{\mathrm{MW}}$ bude výkon vyzerať nasledovne 

$$
\begin{align*}
    \frac{n_{\mathrm{MW}} L_{\mathrm{Sun}}}{ {r_{\mathrm{MW}}^2}} &= \frac{n_{\mathrm{And}} L_{\mathrm{Sun}}}{ {\left(D-r_{\mathrm{MW}}\right)^2}} \,, \tag{5}\\
    \frac{n_{\mathrm{MW}} L_{\mathrm{Sun}}}{ {r_{\mathrm{MW}}^2}} &= \frac{2 n_{\mathrm{MW}} L_{\mathrm{Sun}}}{ {\left(D-r_{\mathrm{MW}}\right)^2}} \,, \tag{6}\\
    \frac{1}{ {r_{\mathrm{MW}}^2}} &= \frac{2}{ {\left(D-r_{\mathrm{MW}}\right)^2}} \,. \tag{7}\end{align*}
$$

Po roznásobení zátvorky a úprave zlomkov dostávame 

$$
\begin{align*}
    D^2 - 2Dr_{\mathrm{MW}} + r_{\mathrm{MW}}^2 &= 2r_{\mathrm{MW}}^2 \,, \tag{8}\\
    D^2 - 2Dr_{\mathrm{MW}} - r_{\mathrm{MW}}^2 &= 0 \,. \tag{9}\end{align*}
$$

 V čom jasne vieme identifikovať kvadratickú rovnicu, kde $r_{\mathrm{MW}}$ je premenná a $D$ je konštanta. Všeobecné riešenie kvadratickej rovnice je 

$$
r_{\mathrm{MW}} = \frac{-b \pm \sqrt{b^2-4ac}}{2a} \a \mathrm{kde} \quad a = -1 \a b = -2D \a c = D^2 \,. \tag{10}
$$

 Po dosadení a vykrátení dôjdeme k riešeniu 

$$
r_{\mathrm{MW}}=D\left(\sqrt{2}-1\right) \approx 0{,}414D \approx 317\,\mathrm{kpc} \,. \tag{11}
$$

 Potom 

$$
r_{\mathrm{And}}= D-r_{\mathrm{MW}} = D\left(2-\sqrt{2}\right) \approx 0{,}586D \approx 448\,\mathrm{kpc} \,. \tag{12}
$$

Teraz potrebujeme ešte spočítať akú vizuálnu magnitúdu má Mliečna cesta a galaxia v Andromede. Vieme, že $r_{\mathrm{MW}}=r_{\mathrm{And}}$. Keďže poznáme absolútnu magnitúdu Slnka, poľahky zistíme absolútnu magnitúdu $n_{\mathrm{MW}}$ Sĺnk. Je to vzťah 

$$
M_{\mathrm{MW}} = -2,5\log{\left( n_{\mathrm{MW}}\cdot 10^{-0,4M_{\Sun}} \right)} \approx -22{,}67\,\mathrm{mag} \,. \tag{13}
$$

 Čo je veličina s ktorou vieme ďalej pracovať ak si spomenieme na modul vzdialenosti 

$$
m_{\mathrm{MW}} = M_{\mathrm{MW}} +5\log{\left( r_{\mathrm{Mw}} \left[\mathrm{pc}\right] \right)} -5 \approx -0{,}16\,\mathrm{mag} \,. \tag{14}
$$

</details>
