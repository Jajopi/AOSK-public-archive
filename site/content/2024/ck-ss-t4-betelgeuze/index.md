---
title: Betelgeuze
year: 2024
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: T4
weight: 2304
points: '80'
authors:
- Ondrej Juhás
hasSolution: true
source: 2024:zCK/SS/aTeoria/zz-Betelgeuze.tex
rocniky:
- '2024'
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

Betelgeuze ($\alpha$ Ori) je červený nadobor a druhá najjasnejšia hviezda súhvezdia Orión. Pôvodne veľmi horúca hviezda hlavnej postupnosti sa aktuálne nachádza v poslednom štádiu svojho života, a predpokladá sa, že počas najbližších 100 000 rokov vybuchne ako supernova. Betelgeuze je pulzujúca polopravidelná premenná hviezda, a jej zdanlivá magnitúda typicky kolíše medzi hodnotami $m_\textrm{max} = 0{,}28\,\mathrm{mag}$ a $m_\textrm{min} = 1{,}11\,\mathrm{mag}$. Bolometrická korekcia pre hviezdu Betelgeuze je $\mathrm{BC} = -1{,}30\,\mathrm{mag}$.

Pri výpočtoch budete potrebovať nasledujúce údaje o hviezde Betelgeuze 

$$
\begin{align*}
    \text{Vzdialenosť od Zeme:} & \quad d_\textrm{Bet} = 494\,\mathrm{ly}\,,\\
    \text{Polomer:} & \quad R_\textrm{Bet} = 764 R_{\Sun}\,. 
\end{align*}
$$

<ol type="a">

<li>

Vypočítajte, aký je žiarivý tok na povrchu Zeme v momente, keď je hviezda najjasnejšia a keď je najmenej jasná.

</li>

<li>

Vypočítajte absolútnu magnitúdu Betelgeuze vo viditeľnom spektre v momente, keď je v minime.

</li>

</ol>

Na prelome rokov 2019 a 2020 došlo k udalosti nazvanej ”Great dimming”, kedy sa zdanlivá magnitúda Betelgueze drasticky znížila až na $m_\textrm{dim} = 1{,}59\,\mathrm{mag}$. Populárna bola hypotéza, že povrchová teplota hviezdy prudko klesla, a jej zánik môže prísť oveľa skôr ako sa predpokladalo.

<ol type="a" start="3">

<li>

Zistite, o koľko kelvinov by sa musela zmeniť povrchová teplota, aby magnitúda poklesla z $m_\textrm{min}$ na $m_\textrm{dim}$. Uvažujte zjednodušený model, kde sa pri meniacej teplote nemení bolometrická korekcia pre hviezdu.

</li>

</ol>

Toto ”stmavnutie” bolo však zrejme spôsobené vyvrhnutím materiálu samotnou hviezdou Betelgeuze (tzv. Surface Mass Ejection), ktorý pohlcoval časť žiarenia hviezdy, čo bolo skutočnou príčinou výrazného poklesu zdanlivej magnitúdy.

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Využijeme Pogsonovu rovnicu a porovnanie so Slnkom. Nemôžeme však zabudnúť na pripočítanie bolometrickej korekcie a taktiež dosadzujeme bolometrickú magnitúdu Slnka. Pre tok na Zemi, keď je Betelgeuze v maxime máme 

$$
m_\textrm{max} + BC - m_{\Sun\textrm{bol}} = 
        -2,5 \log \left( \frac{f_\textrm{max}}{\frac{L_{\Sun}}{4 \pi a_{\Ze}^2}} \right) \,. \tag{1}
$$

 Po úpravách a vyjadrení toku $f_\textrm{max}$ dostávame 

$$
f_\textrm{max} = \frac{L_{\Sun}}{4 \pi a_{\Ze}^2} 10^{\frac{m_\textrm{max} + BC - m_{\Sun\textrm{bol}}} {-2,5} } \,. \tag{2}
$$

 Výpočet toku pri minime bude úplne analogický a výsledný vzťah je až na magnitúdu Betelgeuze identický. Po dosadení konštánt a zadaných hodnôt dostávame $f_\textrm{max} = 6{,}45 \cdot 10^{-8}\,\mathrm{W}\,{\mathrm{m}}^{-2}$, resp. $f_\textrm{min} = 3{,}00 \cdot 10^{-8}\,\mathrm{W}\,{\mathrm{m}}^{-2}$.

</li>

<li>

Využijeme tzv. modul vzdialenosti, ktorý upravíme do tvaru 

$$
M_\textrm{V} = m_\textrm{V} + 5 - 5 \log d_\mathrm{Bet} \,, \tag{3}
$$

 kde za $m_\textrm{V}$ dosadzujeme hodnotu zdanlivej magnitúdy v minime, teda $m_\textrm{min}$, a za $d_\textrm{Bet}$ vzdialenosť od Zeme v parsekoch. Po dosadení dostávam e výslednú hodnotu $M_\textrm{V} = -4{,}79\,\mathrm{mag}$.

</li>

<li>

Keďže potrebujeme zistiť teplotu, ktorá súvisí so žiarivým tokom a magnitúdou, opäť začneme Pogsonovou rovnicou 

$$
(m_\textrm{dim} + BC) - (m_\textrm{min} + BC) = m_\textrm{dim} - m_\textrm{min} =  -2,5 \log \left( \frac{f_\textrm{dim}}{f_\textrm{min}} \right) \,. \tag{4}
$$

 V tomto prípade uvažujeme samozrejme bolometrické magnitúdy, ale keďže používame rovnakú bolometrickú korekciu, tá sa v konečnom dôsledku odčíta, preto sú v rovnici len magnitúdy vo viditeľnom spektre. Keďže porovnávame toky na zemský povrch $f$ z rovnakej hviezdy, tak ich môžeme jednoducho nahradiť tokmi na povrchu hviezdy označené $F$. Potom platí použitím Stefan-Boltzmannovho zákona 

$$
m_\textrm{dim} - m_\textrm{min} = -2,5 \log \left( \frac{F_\textrm{dim}}{F_\textrm{min}} \right)
        = -2,5 \log \left( \frac{\sigma (T_\textrm{min} - \Delta T)^4}{\sigma T_\textrm{min}^4} \right) 
        = -10 \log \left( 1 - \frac{\Delta T}{T_\textrm{min}} \right) \,. \tag{5}
$$

 Vyjadríme si hľadaný rozdiel teplôt 

$$
\Delta T = T_\textrm{min} \left(1 - 10^{ \frac{m_\textrm{dim} - m_\textrm{min}}{-10} } \right) \,. \tag{6}
$$

Potrebujeme ešte zistiť teplotu $T_\textrm{min}$, teda teplotu Betelgeuzu pri magnitúde $m_\textrm{min}$. Tú zistíme na základe faktu, že poznáme toky z podzadania (a). Pre tok $f_\textrm{min}$ máme 

$$
f_\textrm{min} = \frac{L_\textrm{Bet}}{4 \pi d_\textrm{Bet}^2} 
        = \frac{\sigma T_\textrm{min}^4 4 \pi R_\textrm{Bet}^2}{4 \pi d_\textrm{Bet}^2} \,. \tag{7}
$$

 Teraz si už môžeme vyjadriť teplotu $T$ pri minime cyklu hviezdy 

$$
T_\textrm{min} = \sqrt[4]{ \frac{f_\textrm{min} d_\textrm{Bet}^2 }{\sigma R_\textrm{Bet}^2} } \,. \tag{8}
$$

 Po dosadení do rovnice (6) a dosadení hodnôt dostávame výsledok $\Delta T \approx 260\,\mathrm{K}$ (teplota pri minime je približne rovná $T_\textrm{min} \approx 2500\,\mathrm{K}$).

</li>

</ol>

</details>
