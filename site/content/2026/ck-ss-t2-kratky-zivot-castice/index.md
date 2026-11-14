---
title: Krátky život častice
year: 2026
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: T2
weight: 5002
points: '20'
authors:
- Samuel Buranský
hasSolution: true
source: 2026:.SS/¹CK/Kratky-zivot-castice.tex
years:
- '2026'
rounds:
- Celoštátne kolo
categories:
- SŠ
types:
- Teória
topics:
- Nezaradené
---

## Zadanie

Interakciou s kozmickým žiarením vznikajú v horných vrstvách atmosféry okrem iných častíc aj mióny s veľmi krátkou dobou života (v zlomkoch sekundy). Pri uvažovaní klasickej mechaniky by tieto častice nikdy nemali šancu dostať sa k povrchu Zeme. Vypočítajte, ako rýchlo by musel mión letieť, aby z výšky $h  = 100\,\mathrm{km}$ trafil Zem skôr než zanikne, pričom jeho pokojová doba života je $\tau_0 \approx 2{,}197\,\mu \mathrm{s}$. Neuvažujte zrážky s inými časticami a výsledok vyjadrite v percentách rýchlosti svetla.

<details class="solution">
<summary>Riešenie</summary>

Ak sa častica pohybuje dostatočne rýchlo, je nutné započítať relativistické efekty, ktoré spôsobujú odlišné plynutie času v rozdielnych vzťažných sústavách. Životnosť častice podlieha pri vysokých rýchlostiach dilatácii času, pre ktorý platí vzťah 

$$
\Delta t = \Delta t_0 \gamma \,, \qquad\textit{[2\,b]} \tag{1}
$$

 kde $\gamma$ je tzv. Lorentzov faktor definovaný vzťahom 

$$
\gamma = \frac{1}{\sqrt{1 - \left(\frac{v}{c}\right)^2}} \,. \qquad\textit{[3\,b]} \tag{2}
$$

 Podiel rýchlosti voči rýchlosti svetla sa často označuje $\beta$, čo je vlastne bezrozmerná rýchlosť 

$$
\beta = \frac{v}{c} \,, \tag{3}
$$

 pričom tento podiel je to, čo chceme vypočítať. Pomocou bezrozmernej rýchlosti môžeme Lorentzov faktor prepísať ako 

$$
\gamma = \frac{1}{\sqrt{1 - \beta^2}} \,. \qquad\textit{[2\,b]} \tag{4}
$$

Na výpočet rýchlosti použijeme klasický vzťah 

$$
s = v t \,, \tag{5}
$$

 kde $s = h$ je dráha, ktorú musí mión prejsť, $v$ je rýchlosť, ktorú podľa rovnice (3) prepíšeme ako $v = c \beta$, a $t = \tau$ je životnosť častice. Podľa rovníc (4) a (1) platí 

$$
\tau = \tau_0 \frac{1}{\sqrt{1 - \beta^2}} \,. \qquad\textit{[3\,b]} \tag{6}
$$

 Keď dosadíme všetky výrazy do rovnice (5), dostaneme rovnicu 

$$
h = \frac{c \beta \tau_0}{\sqrt{1 - \beta^2}} \,. \qquad\textit{[5\,b]} \tag{7}
$$

 Osamostatníme odmocninu na ľavej strane a celú rovnicu umocníme na druhú 

$$
\begin{align*}
    1 - \beta^2 = \beta^2 \left(\frac{c \tau_0}{h}\right)^2 \,, \tag{8}\\
    1 = \beta^2 \left(\frac{c \tau_0}{h}\right)^2 + \beta^2 \,, \tag{9}\end{align*}
$$

 na pravej strane vyjmeme $\beta^2$ pred zátvorku a rovnicu podelíme zátvorkou 

$$
\beta^2 = \frac{1}{\left(\frac{c \tau_0}{h}\right)^2 + 1} \,, \qquad\textit{[2\,b]} \tag{10}
$$

 rovnicu odmocníme a dostaneme výraz pre bezrozmernú rýchlosť $\beta$ 

$$
\beta = \sqrt{\frac{1}{1 + \left(\frac{c \tau_0}{h}\right)^2}} \doteq 0,99998 = \boxed{99,998 \,\%}\,. \qquad\textit{[3\,b]} \tag{11}
$$

</details>
