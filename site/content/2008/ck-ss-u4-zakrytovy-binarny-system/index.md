---
title: Zákrytový binárny systém
year: 2008
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú4
weight: 2304
hasSolution: true
source: ZAO:I_Zadania/08_Rozsiahle/08_SS_FI.tex
rocniky:
- '2008'
kola:
- Celoštátne kolo
kategorie:
- SŠ
typy:
- Teória
tagy:
- Rozsiahle príklady
collection: ZAO
---

## Zadanie

Ak sa pozorovateľ nachádza presne v rovine dráhy dvojhviezdy, môže pozorovať vzájomné zákryty jej zložiek. Predpokladajme, že zložky takejto dvojhviezdy obiehajú okolo spoločného ťažiska po kruhových dráhach s uhlovou rýchlosťou $\omega$, povrchové teploty týchto hviezd sú $T_1$ a $T_2$ ($T_1 > T_2$) a odpovedajúce polomery $R_1$ a $R_2$ ($R_1 > R_2$). Presné merania ukázali, že svetlo prichádzajúce z týchto hviezd v okamihoch odpovedajúcich minimám odpovedá 90% a 63% maximálneho toku spoločného svetla ($F = 4{,}8 \cdot 10^{-9}\,\mathrm{W}\,{\mathrm{m}}^{-2}$) oboch hviezd.

V spektre tejto dvojhviezdy pozorujeme spektrálnu čiaru sodíka D1 s laboratórnou vlnovou dĺžkou $\lambda = 5895{,}9\,\mathring{A}$. V nasledujúcej tabuľke sú vlnové dĺžky tejto čiary $\lambda_1$, $\lambda_2$ pre jednotlivé zložky pozorované pozorovateľom na Zemi v priebehu niekoľkých dní. Počiatok vodorovnej osi na obrázku v predchádzajúcom príklade a v tejto tabuľke je zhodný.

| Dni | $\lambda_1 - 5800$ (Å) | $\lambda_2 - 5800$ (Å) |
|:---:|:-------------:|:-------------:|
| 0,3 |     97,5      |     93,1      |
| 0,6 |     97,7      |     92,8      |
| 0,9 |     97,2      |     93,7      |
| 1,2 |     96,2      |     96,2      |
| 1,5 |     95,1      |     97,3      |
| 1,8 |     94,3      |     98,7      |
| 2,1 |     94,1      |     99,0      |
| 2,4 |     94,6      |     98,1      |
| 2,7 |     95,6      |     96,4      |
| 3,0 |     96,7      |     94,5      |
| 3,3 |     97,3      |     93,1      |
| 3,6 |     97,7      |     92,8      |
| 3,9 |     97,2      |     93,7      |
| 4,2 |     96,2      |     96,2      |
| 4,5 |     95,0      |     97,4      |
| 4,8 |     94,3      |     98,7      |

**Vypočítajte:**

<ol type="a">

<li>

Hmotnosť každej zložky.

</li>

<li>

Pomery povrchových teplôt $T_1/T_2$ a polomerov $R_1/R_2$ zložiek dvojhviezdy.

</li>

<li>

Aká je maximálna možná uhlová vzdialenosť zložiek pre pozorovateľa na Zemi? Využite nasledujúci empirický vzťah medzi žiarivým výkonom a hmotnosťou hviezdy

</li>

</ol>

$$
\frac{L}{L_{\Sun}}=\left(\frac{M}{M_{\Sun}}\right)^{3,8} \, . \tag{1}
$$

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Z tabuľky vidno, že sa hodnoty nameraných vlnových dĺžok začínajú opakovať po uplynutí 3 dní, perióda je preto $P=3\,\mathrm{dní}$. Maximálna vlnová dĺžka prvej zložky je $\lambda_\textrm{1,max}=5897{,}7\,\mathring{A}$, maximálna vlnová dĺžka druhej zložky je $\lambda_\textrm{2,max}=5899{,}0\,\mathring{A}$. Semi-amplitúdy radiálnych rýchlostí hviezd sú

</li>

</ol>

$$
v_\textrm{1,max}=\frac{\lambda_\textrm{1,max}-\lambda_0}{\lambda_0}c=\frac{97,7-95,9}{5895,9}\cdot2{,}9979 \cdot 10^{8}=91{,}5\,\mathrm{km}\,{\mathrm{s}}^{-1} \, , \tag{2}
$$

 

$$
v_\textrm{2,max}=\frac{\lambda_{2,max}-\lambda_0}{\lambda_0}c=\frac{99,0-95,9}{5895,9}\cdot2{,}9979 \cdot 10^{8}=157{,}6\,\mathrm{km}\,{\mathrm{s}}^{-1} \, . \tag{3}
$$

 Pomer hmotností hviezd sa rovná prevrátenému pomeru semi-amplitúd radiálnych rýchlostí 

$$
\frac{M_1}{M_2}=\frac{v_\textrm{2,max}}{v_\textrm{1,max}}=\frac{157,6}{91,5}=1,72 \, . \tag{4}
$$

 Vypočítame polomery dráh jednotlivých hviezd a potom ich súčet 

$$
a_1=\frac{v_1P}{2\pi} \, , \tag{5}
$$

 

$$
a_2=\frac{v_2P}{2\pi} \, , \tag{6}
$$

 

$$
a=a_1+a_2=\frac{P}{2\pi}(v_1+v_2)=\frac{3\cdot86400}{2\pi}\cdot(91,5+157,6)\cdot10^3=1{,}03 \cdot 10^{10}\,\mathrm{m} \, . \tag{7}
$$

 Z 3. Kepleroveho zákona dostaneme súčet hmotností 

$$
M_1+M_2=\frac{4\pi^2a^3}{GP^2}=\frac{4\pi^2\cdot(1{,}03 \cdot 10^{10})^3}{6{,}67 \cdot 10^{-11}\cdot(3\cdot86400)^2}=9{,}63 \cdot 10^{30}\,\mathrm{kg}=4{,}84\,\mathit{M}_\Sun \, . \tag{8}
$$

 Hmotnosti jednotlivých hviezd sú 

$$
M_2=\frac{4,82}{2,72}=1{,}78\,\mathit{M}_\Sun \, , \tag{9}
$$

 

$$
M_1=1,78\cdot1,72=3{,}06\,\mathit{M}_\Sun \, . \tag{10}
$$

<ol type="a" start="2">

<li>

Relatívne intenzity v primárnom a sekundárnom minime si označíme $f_\textrm{p}=0,63$ a $f_\textrm{s}=0,9$. Pretože podľa zadania úlohy môžeme predpokladať, že dochádza ku stredovému zákrytu a hviezda 2 je menšia ako hviezda 1, počas sekundárneho minima je hviezda 2 úplne zakrytá. Preto platí

</li>

</ol>

$$
f_\textrm{s}=\frac{L_1}{L_1+L_2} \, . \tag{11}
$$

 V primárnom minime je zakrytá iba časť hviezdy 1, preto platí 

$$
f_\textrm{p}=\frac{L_1-4\pi R_2^2\sigma T_1^4+L_2}{L_1+L_2}=\frac{L_1-\frac{R_2^2}{R_1^2}L_1+L_2}{L_1+L_2}=1-\left(\frac{R_2}{R_1}\right)^2\frac{L_1}{L_1+L_2} \, , \tag{12}
$$

 

$$
f_\textrm{p}=1-\left(\frac{R_2}{R_1}\right)^2f_\textrm{s} \, . \tag{13}
$$

 Pre pomer polomerov hviezd dostaneme 

$$
\left(\frac{R_2}{R_1}\right)^2=\frac{1-f_\textrm{p}}{f_\textrm{s}} \, , \tag{14}
$$

 

$$
\frac{R_1}{R_2}=\sqrt{\frac{f_s}{1-f_p}}=\sqrt{\frac{0,9}{1-0,63}}=1,56 \, . \tag{15}
$$

 Zo vzorca pre $f_s$ si vyjadríme pomer svietivostí a dosadíme doň zistený pomer polomerov, vďaka tomu získame pomer teplôt 

$$
\frac{L_2}{L_1}=\frac{R_2^2}{R_1^2}\frac{T_2^4}{T_1^4}=\frac{1}{f_\textrm{s}}-1=\frac{1-f_\textrm{s}}{f_\textrm{s}} \, , \tag{16}
$$

 

$$
\frac{T_1}{T_2}=\sqrt[4]{\frac{f_\textrm{s}}{1-f_\textrm{s}}}\sqrt{\frac{R_2}{R_1}}=\sqrt[4]{\frac{0,9}{1-0,9}}\cdot\sqrt{\frac{1}{1,56}}=1,39 \, . \tag{17}
$$

<ol type="a" start="3">

<li>

Zo vzťahu medzi hmotnosťou a luminozitou vypočítame luminozity oboch hviezd

</li>

</ol>

$$
L_1=\left(\frac{M_1}{M_\Sun}\right)^{3,8}L_\Sun=3,06^{3,8}\cdot3{,}826 \cdot 10^{26}=2{,}68 \cdot 10^{28}\,\mathrm{W} \, , \tag{18}
$$

 

$$
L_2=\left(\frac{M_2}{M_\Sun}\right)^{3,8}L_\Sun=1,78^{3,8}\cdot3{,}826 \cdot 10^{26}=3{,}42 \cdot 10^{27}\,\mathrm{W} \, . \tag{19}
$$

 Na Zemi nameriame mimo zákrytov tok dvojhviezdy 

$$
F=\frac{L_1+L_2}{4\pi d^2} \, . \tag{20}
$$

 Vzdialenosť dvojhviezdy je označená $d$. Dráhy sú kruhové, vzdialenosť zložiek sa nemení, preto sa nemení ani ich uhlová vzdialenosť, ktorá je 

$$
\alpha=\frac{a}{d}=\sqrt{\frac{4\pi F}{L_1+L_2}}a=\sqrt{\frac{4\pi\cdot4{,}8 \cdot 10^{-9}}{2{,}68 \cdot 10^{28}+3{,}42 \cdot 10^{27}}}\cdot1{,}03 \cdot 10^{10}=1{,}45 \cdot 10^{-8}\,\mathrm{rad}=0{,}003'' \, . \tag{21}
$$

</details>
