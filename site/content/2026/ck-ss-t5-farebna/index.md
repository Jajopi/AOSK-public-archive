---
title: Farebná
year: 2026
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: T5
weight: 2305
points: '60'
authors:
- Radovan Lascsák
hasSolution: true
source: 2026:.SS/¹CK/Farebna.tex
rocniky:
- '2026'
kola:
- Celoštátne kolo
kategorie:
- SŠ
typy:
- Teória
tagy:
- Nezaradené
---

## Zadanie

Spektrum slnečného žiarenia je možné hrubo aproximovať ako žiarenie absolútne čierneho telesa pomocou Planckovho zákona pre povrchový spektrálny tok $F_\lambda$, čo je veličina predstavujúca tok na povrchu telesa na jednotku vlnovej dĺžky $\lambda$ 

$$
F_\lambda = \frac{2\pi hc^2}{\lambda^5} \frac{1}{\exp\!\big( \frac{hc}{\lambda k_B T} \big) - 1} \,, \tag{1}
$$

 kde $h$ je Planckova konštanta, $c$ rýchlosť svetla, $\lambda$ vlnová dĺžka, $k_B$ Boltzmannova konštanta, $T$ efektívna teplota a $\exp(x)$ alternatívny zápis pre funkciu $e^x$.

Pri pozorovaniach je zvykom používať štandardný fotometrický systém založený na filtroch U, B, V, R, I ktorých parametre sú zhrnuté v tabuľke 1. Spektrálnu priepustnosť filtrov pre jednoduchosť uvažujte ako konštantných $100\,\%$ v oblasti filtra a $0\,\%$ mimo neho. Pod referenčným tokom myslíme tok vo filtri, pri ktorom je v ňom meraná nulová magnitúda.

<ol type="a">

<li>

<span class="body">[30 b]</span> Vypočítajte absolútnu magnitúdu Slnka vo filtroch B a V. Uvažujte konštantný spektrálny tok $F_\lambda$ v oblasti filtra.

</li>

<li>

<span class="body">[15 b]</span> V ďalekohľade pozorujeme hviezdu fyzikálne totožnú so Slnkom, ktorej zdanlivá magnitúda je $21{,}90\,\mathrm{mag}$ vo filtri B a $20{,}27\,\mathrm{mag}$ vo filtri V. Vypočítajte jej farebný index $(\text{B}-\text{V})$ a farebný exces $E_{(B - V)}$.

</li>

<li>

<span class="body">[15 b]</span> Vypočítajte vzdialenosť hviezdy so zarátaním medzihviezdnej absorpcie. Predpokladajte, že magnitúda Slnka vo V filtri je rovná vizuálnej magnitúde Slnka. Hodnotu R-čísla (extinkčného koeficientu priamej úmery medzi absorpciou vo V filtri a farebným excesom $(\text{B}-\text{V})$) uvažujte ako $R_V = 3{,}1$.

</li>

</ol>

<div class="table-caption">

**Tabuľka 1:** Prehľad štandardných fotometrických filtrov.
</div>

| Označenie | Stred filtra | Šírka filtra | Referenčný tok |
|:---------:|:------------:|:------------:|:--------------:|
|     U     |  $365\,\mathrm{nm}$   |  $66\,\mathrm{nm}$   |   $2{,}71\,\mathrm{nW}\,{\mathrm{m}}^{-2}$    |
|     B     |  $445\,\mathrm{nm}$   |  $94\,\mathrm{nm}$   |   $6{,}13\,\mathrm{nW}\,{\mathrm{m}}^{-2}$    |
|     V     |  $551\,\mathrm{nm}$   |  $88\,\mathrm{nm}$   |   $3{,}18\,\mathrm{nW}\,{\mathrm{m}}^{-2}$    |
|     R     |  $658\,\mathrm{nm}$   |  $138\,\mathrm{nm}$   |   $2{,}98\,\mathrm{nW}\,{\mathrm{m}}^{-2}$    |
|     I     |  $806\,\mathrm{nm}$   |  $149\,\mathrm{nm}$   |   $1{,}77\,\mathrm{nW}\,{\mathrm{m}}^{-2}$    |

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Ako prvé vypočítame spektrálne povrchové toky Slnka (jednotka je $\mathrm{W}\,{\mathrm{m}}^{-2}\,{\mathrm{nm}}^{-1}$) vo filtri B a V pomocou zadanej rovnice (1) pre Planckovo spektrum po dosadení stredu filtrov za vlnovú dĺžku $\lambda$ a teploty Slnka $T_\Sun$ za teplotu $T$. 

$$
\begin{align*}
    F_{\Sun,\lambda}^{\mathrm{B}} = F_\lambda \big(\lambda=445\,\mathrm{nm}, T = T_\Sun\big) &=
    79{,}574 \cdot 10^{12}\,\mathrm{W}\,{\mathrm{m}}^{-2}\,{\mathrm{m}}^{-1}  \\
    &= 79{,}574\,\mathrm{kW}\,{\mathrm{m}}^{-2}\,{\mathrm{nm}}^{-1}    \,, \qquad\textit{[5\,b]} \tag{2}\\
    F_{\Sun,\lambda}^{\mathrm{V}} = F_\lambda \big(\lambda=551\,\mathrm{nm}, T = T_\Sun\big) &=
    80{,}878 \cdot 10^{12}\,\mathrm{W}\,{\mathrm{m}}^{-2}\,{\mathrm{m}}^{-1}  \\
    &= 80{,}878\,\mathrm{kW}\,{\mathrm{m}}^{-2}\,{\mathrm{nm}}^{-1}
    \,. \qquad\textit{[5\,b]} \tag{3}\end{align*}
$$

 Spektrálne povrchové toky prepočítame na celkové povrchové toky (jednotka je $\mathrm{W}\,{\mathrm{m}}^{-2}$) vo filtroch B a V prenásobením šírkou filtrov. 

$$
\begin{align*}
    F_\Sun^{\mathrm{B}} = F_{\Sun,\lambda}^{\mathrm{B}} \cdot 94\,\mathrm{nm} &=
    7479{,}9\,\mathrm{kW}\,{\mathrm{m}}^{-2} \,, \qquad\textit{[1\,b]} \tag{4}\\
    F_\Sun^{\mathrm{V}} = F_{\Sun,\lambda}^{\mathrm{V}} \cdot 88\,\mathrm{nm} &=
    7117{,}3\,\mathrm{kW}\,{\mathrm{m}}^{-2} \,. \qquad\textit{[1\,b]} \tag{5}\end{align*}
$$

 Ďalej prepočítame povrchové toky na Slnku na toky vo vzdialenosti 10 parsekov od Slnka. 

$$
\begin{align*}
    f_\Sun^{\mathrm{B}} = F_\Sun^{\mathrm{B}} \left(\frac{R_\Sun}{10\,\mathrm{pc}}\right)^2 &= 0{,}038015\,\mathrm{nW}\,{\mathrm{m}}^{-2} \,, \tag{6}\\
    f_\Sun^{\mathrm{V}} = F_\Sun^{\mathrm{V}} \left(\frac{R_\Sun}{10\,\mathrm{pc}}\right)^2 &= 0{,}036172\,\mathrm{nW}\,{\mathrm{m}}^{-2} \,. \tag{7}\end{align*}
$$

 Nakoniec využijeme Pogsonovu rovnicu na prepočet toku $f_\Sun$ na absolútnu magnitúdu $M_\Sun$ pomocou referenčného toku $f_{ref}$ pre nulovú magnitúdu. 

$$
\begin{align*}
    M_\Sun^{\mathrm{B}} - 0\,\mathrm{mag} = -2,5 \log\left( \frac{f_\Sun^{\mathrm{B}}}{f_{ref}^{\mathrm{B}}} \right)
    &\ztv M_\Sun^{\mathrm{B}} \doteq \boxed{5{,}52\,\mathrm{mag}} \,, \tag{8}\\
    M_\Sun^{\mathrm{V}} - 0\,\mathrm{mag} = -2,5 \log\left( \frac{f_\Sun^{\mathrm{V}}}{f_{ref}^{\mathrm{V}}} \right)
    &\ztv M_\Sun^{\mathrm{V}} \doteq \boxed{4{,}86\,\mathrm{mag}} \,. \tag{9}\end{align*}
$$

</li>

<li>

Výpočet farebného indexu $(\text{B}-\text{V})$ je triviálny. Odčítame od seba magnitúdu vo filtri B a magnitúdu vo filtri V. Dostávame 

$$
(\text{B} - \text{V}) = 21{,}90\,\mathrm{mag} - 20{,}27\,\mathrm{mag} = \boxed{1{,}63\,\mathrm{mag}} \,. \qquad\textit{[6\,b]} \tag{10}
$$

Pre výpočet farebného excesu potrebujeme takzvanú *intrinsic* hodnotu farebného indexu, ktorú budeme značiť $(\text{B} - \text{V})_0$ a predstavuje počiatočnú hodnotu farebného indexu, tesne po vyslaní žiarenia z pozorovanej hviezdy. Keďže je hviezda fyzikálne identická so Slnkom, tak intrinsic hodnota farebného indexu hviezdy je rovná hodnote farebného indexu Slnka, pretože Slnko je blízko Zeme, a teda absorpcia je zanedbateľná. Preto 

$$
(\text{B} - \text{V})_0 = (\text{B} - \text{V})_\Sun = M_\Sun^{\mathrm{B}} - M_\Sun^{\mathrm{V}} = 0{,}66\,\mathrm{mag} \,. \qquad\textit{[4\,b]} \tag{11}
$$

Farebný exces je následne rozdiel pozorovaného a intrinsic farebného indexu, teda 

$$
E_{(B - V)} = (\text{B} - \text{V}) - (\text{B} - \text{V})_0 = \boxed{0{,}97\,\mathrm{mag}} \,. \qquad\textit{[5\,b]} \tag{12}
$$

</li>

<li>

Na výpočet vzdialenosti $d$ využijeme vzorec pre modul vzdialenosti vo filtri V so zarátaním absorpcie; 

$$
m_V - M_V = -5 +5\log d + A_V \,, \qquad\textit{[6\,b]} \tag{13}
$$

 kde $m_V$ je zdanlivá (pozorovaná) magnitúda hviezdy vo filtri V, $M_V$ je absolútna magnitúda hviezdy vo filtri V, $d$ je vzdialenosť hviezdy v parsekoch a $A_V$ je celková absorpcia vo filtri V. Zdanlivú magnitúdu $m_V = 21{,}59\,\mathrm{mag}$ máme zadanú v zadaní, absolútna magnitúda $M_V$ je rovnaká ako spočítaná absolútna vizuálna magnitúda Slnka $M_\Sun^{\textrm{V}} = 4{,}86\,\mathrm{mag}$ a absorpciu $A_V$ určíme pomocou R-čísla ($R_V = 3,1$) a farebného excesu ako 

$$
A_V = R_V \cdot E_{(B - V)} \,. \qquad\textit{[6\,b]} \tag{14}
$$

Vyjadrením vzdialenosti z rovnice (13) a dosadením máme 

$$
d = 10^{0,2(m_V - M_\Sun^{\textrm{V}} + 5 - A_V)} \doteq
    \boxed{3{,}0\,\mathrm{kpc}} \,. \qquad\textit{[3\,b]} \tag{15}
$$

</li>

</ol>

</details>

## Komentár autora

V tomto príklade chýbali hodnoty referenčných tokov pre nulovú magnitúdu v jednotlivých filtroch. Pre korektnosť úlohy som preto tieto toky do zadania pridal za cenu miernej odlišnosti od originálnej úlohy riešenej na celoslovenskom kole. Ďakujem Peťovi Švrlovi za túto správnu pripomienku.
