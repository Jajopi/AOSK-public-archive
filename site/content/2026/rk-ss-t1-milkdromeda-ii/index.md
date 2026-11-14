---
title: Milkdroméda II
year: 2026
round: RK
roundName: Regionálne kolo
category: SŠ
type: teoria
typeName: Teória
label: T1
weight: 4001
points: '80'
authors:
- R. Lascsák
- T. Hanáková
hasSolution: true
source: 2026:.SS/.RK/MilkdromedaII.tex
years:
- '2026'
rounds:
- Regionálne kolo
categories:
- SŠ
types:
- Teória
topics:
- Nezaradené
---

## Zadanie

V tejto úlohe nadviažeme na domáce kolo a budeme sa ďalej zaoberať jedným z najvzdialenejších objektov viditeľných voľným okom. Galaxia v Androméde ($\messier{31}$) sa v súčasnosti nachádza vo vzdialenosti $d_0 = 2{,}537\,\mathrm{Mly}$ od Zeme a má celkovú zdanlivú magnitúdu $m_0 = 3{,}44\,\mathrm{mag}$. Na oblohe sa však javí ako menej jasná, keďže ide o plošný zdroj svetla. Jej jadro má plošnú magnitúdu $\mu_0 = 17\,\mathrm{mag}/{\mathrm{arcsec}}^{2}$.

<ol type="a">

<li>

<span class="body">[40 b]</span> Galaxia $\messier{31}$ sa postupne približuje k Mliečnej ceste a o približne 3 miliardy rokov sa bude nachádzať vo vzdialenosti $d = 200\,\mathrm{kpc}$. Akú budeme pozorovať jej zdanlivú magnitúdu $m$ a plošnú magnitúdu jadra $\mu$ v tejto dobe?

</li>

</ol>

V domácom kole ste zistili, že pozorovaná vlnová dĺžka spektrálnej čiary H$\alpha$ galaxie $\messier{31}$ je v súčasnosti $\lambda_0 = 655{,}62\,\mathrm{nm}$, pričom laboratórna vlnová dĺžka tejto čiary je $\lambda_{lab} = 656{,}28\,\mathrm{nm}$. Posun spektra je výsledkom kombinácie vlastnej rýchlosti $\messier{31}$ a rozpínania vesmíru.

<ol type="a" start="2">

<li>

<span class="body">[40 b]</span> Na akej vlnovej dĺžke $\lambda$ budeme pozorovať spektrálnu čiaru H$\alpha$ galaxie $\messier{31}$ v budúcnosti v čase, keď bude vo vzdialenosti $d = 200\,\mathrm{kpc}$? V tejto dobe bude na základe štandardného kozmologického modelu hodnota Hubblovej konštanty rovná $90\,\%$ dnešnej hodnoty. Zanedbajte gravitačnú interakciu galaxie $\messier{31}$ a Mliečnej cesty.

</li>

</ol>

<details class="solution">
<summary>Riešenie</summary>

V celej úlohe sa budeme držať klasického kozmologického značenia, v ktorom budeme dolným indexom 0 označovať veličiny vztiahnuté na súčasnosť a bez indexu budeme označovať veličiny vztiahnuté na budúcnosť.

<ol type="a">

<li>

Tok $f$, ktorý zachytíme z celej galaxie $\messier{31}$, je nepriamo úmerný druhej mocnine vzdialenosti<span class="subbody">[7 b]</span>, teda $f \;\propto\; d^{-2}$. Magnitúdu $m$ prepočítame z toku $f$ pomocou Pogsonovej rovnice 

$$
m - m_0 = -2,5 \log \left( \frac{f}{f_0} \right) . \qquad\textit{[7\,b]} \tag{1}
$$

 Dosadením nepriamej úmery toku a vzdialenosti máme 

$$
m - m_0 = -2,5 \log \left( \frac{d_0^2}{d^2} \right) = -5 \log \left( \frac{d_0}{d} \right), \qquad\textit{[1\,b]} \tag{2}
$$

 čiže po prepočte $d_0$ na $\mathrm{kpc}$ ($1\,\mathrm{Mly} = 306{,}6\,\mathrm{kpc}$) a dosadení známych veličín dostávame 

$$
m = m_0 -5 \log \left( \frac{d_0}{d} \right) =
    3{,}44\,\mathrm{mag} - 5 \log \left( \frac{777{,}8\,\mathrm{kpc}}{200\,\mathrm{kpc}} \right) 
    \doteq \boxed{0{,}49\,\mathrm{mag}} \,. \qquad\textit{[5\,b]} \tag{3}
$$

Pod plošnou magnitúdou $\mu$ v jednotke $\mathrm{mag}/{\mathrm{arcsec}}^{2}$ rozumieme magnitúdu, ktorá do našich očí prichádza z oblasti oblohy s uhlovými rozmermi $1\times1$ uhlovej sekundy <span class="subbody">[5 b]</span> (angl. *arc second*). Takýto štvorček oblohy pokryje iba malú časť galaxie $\messier{31}$, a preto je plošná magnitúda $\mu$ výrazne väčšia ako celková magnitúda $m$. Označme $S_0$ reálnu plochu $\messier{31}$, ktorá v súčasnosti zodpovedá uhlovej ploche $1\,{\mathrm{arcsec}}^{2}$. V budúcnosti, keď bude $\messier{31}$ bližšie k nám, tak bude rovnakej uhlovej ploche zodpovedať menšia reálna plocha $S$,<span class="subbody">[5 b]</span> nakoľko sa $\messier{31}$ na oblohe zdanlivo natiahne. Konkrétne platí 

$$
\frac{S}{S_0} = \frac{d^2}{d_0^2} \,, \qquad\textit{[3\,b]} \tag{4}
$$

 teda $S \;\propto\; d^2$. Tok $f_1$ pripadajúci na $1\,{\mathrm{arcsec}}^{2}$ je priamo úmerný ploche $S$, a zároveň nepriamo úmerný druhej mocnine vzdialenosti $d$ podobne ako celkový tok $f$. Čiže 

$$
f_1 \;\propto\; \frac{S}{d^2} \;\propto\; \frac{d^2}{d^2} = 1 \ztv
    f_1 = \konst \,. \qquad\textit{[6\,b]} \tag{5}
$$

 Dospeli sme k záveru, že plošný tok, a tým pádom aj plošná magnitúda, sú konštantné. Preto 

$$
\boxed{\mu = \mu_0 = 17\,\mathrm{mag}/\mathrm{arcsec}^2}\,. \qquad\textit{[1\,b]} \tag{6}
$$

 Tento záver sa môže zdať zvláštny. Prečo potom nevidíme všetky galaxie, keď ich plošná jasnosť je konštantná? Problémom je, že vzdialené galaxie majú príliš malý celkový tok a do našich očí dopadne od nich príliš málo fotónov. Dá sa na to pozrieť aj z druhej strany. Keď sa zamyslíte nad tým, aká jasná je na oblohe Mliečna cesta, tak to nie je až tak rozdielne voči galaxii $\messier{31}$. Avšak Mliečna cesta je výrazne bližšie k nám ako $\messier{31}$.

</li>

<li>

Pozorovaný posun vlnovej dĺžky spektrálnej čiary H$\alpha$ je spôsobený kombináciou Hubblovej rýchlosti rozpínania vesmíru $v_H$ smerom od nás a vlastnej rýchlosti $v$ galaxie $\messier{31}$<span class="subbody">[10 b]</span> smerom k nám. V súčasnosti (index 0) platí 

$$
\frac{v_{H,0} - v_0}{c} = z_0 = \frac{\lambda_0 - \lambda_{lab}}{\lambda_{lab}} = \frac{\lambda_0}{\lambda_{lab}} - 1
    \qquad\textit{[5\,b]} \tag{7}
$$

 a v budúcnosti (bez indexu) bude platiť 

$$
\frac{v_H - v}{c} = z = \frac{\lambda - \lambda_{lab}}{\lambda_{lab}} = \frac{\lambda}{\lambda_{lab}} - 1 \,.
    \qquad\textit{[5\,b]} \tag{8}
$$

 Túto sústavu rovníc chceme vyriešiť pre vlnovú dĺžku $\lambda$. Začneme doplnením ďalších dvoch rovníc pre Hubblove rýchlosti, ktoré vychádzajú z definície Hubblovej konštanty $H$. 

$$
\begin{align*}
    v_{H,0} &= H_0 \, d_0 \,,  \qquad\textit{[4\,b]} \tag{9}\\
    v_H &= H d \,.  \qquad\textit{[4\,b]} \tag{10}\end{align*}
$$

 Dostali sme sústavu štyroch rovníc s piatimi neznámymi ($v_0, v, v_{H,0}, v_H, \lambda$), čo nie je riešiteľný systém. Na skompletizovanie potrebujeme využiť informáciu zo zadania o tom, že máme zanedbať gravitačnú interakciu medzi $\messier{31}$ a Mliečnou cestou. To znamená, že sa vlastná rýchlosť $\messier{31}$ nemení, teda sa galaxia hýbe rovnomerným pohybom (podľa prvého Newtonovho zákona). Jej rýchlosť sa bude meniť iba zdanlivo, kvôli tomu, že čím bližšie k nám bude, tým menšia bude jej Hubblova rýchlosť, a zároveň bude klesať Hubblova konštanta na základe kozmologického vývoja. Preto 

$$
v_0 = v \,,  \qquad\textit{[10\,b]} \tag{11}
$$

 čím sme skompletizovali sústavu piatich rovníc s piatimi neznámymi. Jej riešenie začneme vyjadrením $v_0$ a $v$ z (7) a (8), kam dosadíme z (9) a (10). 

$$
\begin{align*}
    v_0 &= v_{H,0} - c \, \left( \frac{\lambda_0}{\lambda_{lab}} - 1 \right)
    = H_0 \, d_0 - c \, \left( \frac{\lambda_0}{\lambda_{lab}} - 1 \right) \,, \tag{12}\\
    v &= v_H - c \, \left( \frac{\lambda}{\lambda_{lab}} - 1 \right)
    = H d - c \, \left( \frac{\lambda}{\lambda_{lab}} - 1 \right) \,. \tag{13}\end{align*}
$$

Finálnym dosadením do (11), využitím $H = 0,9 H_0$ <span class="subbody">[2 b]</span> zo zadania a úpravou dostávame 

$$
\begin{align*}
    H_0 \, d_0 - c \, \left( \frac{\lambda_0}{\lambda_{lab}} - 1 \right) &=
    0,9 H_0 \, d - c \, \left( \frac{\lambda}{\lambda_{lab}} - 1 \right) \,, \tag{14}\\
    \frac{H_0}{c} \big(d_0 - 0,9 \, d \big) &= 
    \frac{\lambda_0}{\lambda_{lab}} - 1 - \frac{\lambda}{\lambda_{lab}} + 1 \,, \tag{15}\\
    \lambda &= \lambda_0 - \lambda_{lab} \frac{H_0}{c} \big(d_0 - 0,9 \, d \big) \,, \tag{16}\\
    \boxed{\lambda = 655{,}53\,\mathrm{nm}} \,. \qquad\textit{[10\,b]} \tag{17}\end{align*}
$$

</li>

</ol>

</details>

## Komentár autora

Druhý zo série príkladov zameraných na možnú zrážku našej galaxie s galaxiou v Androméde ($\messier{31}$). Najnovšie modely zarátavajúce gravitáciu malých galaxií (Magelanove mraky alebo $\messier{31}$) výrazne znížili pravdepodobnosť zrážky Mliečnej cesty a $\messier{31}$.
