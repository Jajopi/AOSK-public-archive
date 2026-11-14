---
title: Výtrysk jetu
year: 2019
round: DK
roundName: Domáce kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú4
weight: 304
hasSolution: true
source: ZAO:I_Zadania/07_Kozmo/07_SS_DK.tex
rocniky:
- '2019'
kola:
- Domáce kolo
kategorie:
- SŠ
typy:
- Teória
tagy:
- Kozmológia
collection: ZAO
---

## Zadanie

Pomocou rádiointerferometrickej metódy s veľkou základňou bol monitorovaný rádiový zdroj žiarenia, vzdialený $d = 20\,\mathrm{Mpc}$. V určitom momente bol zaregistrovaný výtrysk jetu pod uhlom $\alpha = 30^{\circ}$ voči zornému lúču. Zdroj žiarenia bol pozorovaný presne po 10 rokoch a bolo zaregistrované, že jet sa už nachádza v uhlovej vzdialenosti $\psi = 0{,}0645''$ od rádiového zdroja. Vypočítajte rýchlosť, s akou bol jet vyvrhnutý do priestoru. Predpokladajme, že jet sa pohybuje konštantnou rýchlosťou. Expanziu vesmíru môžeme zanedbať.

<details class="solution">
<summary>Riešenie</summary>

<figure>

<div class="fig-images"><img class="invert" src="AO2015_SS_DK_3.svg" alt="obrázok" loading="lazy" style="width:15%"></div>

</figure>

Vychádzame z nakresleného obrázku. Na začiatku sme pozorovali jet priamo pri zdroji v polohe 1. Počas 10 rokov jet prešiel vzdialenosť $r$ a nakoniec sa nachádzal v polohe 2. Úsečka $x$ vychádza z bodu 2 a je kolmá na $d_1$, jej dĺžka je 

$$
x=r \sin \alpha \, . \tag{1}
$$

 Za 10 rokov mohol výtrysk prejsť maximálne vzdialenosť $r=10\,\mathrm{ly}=3\,\mathrm{pc}$, aj to len za predpokladu, že jeho rýchlosť bola veľmi blízka rýchlosti svetla. To znamená, že vzdialenosti $d_1$, $d_2$ od pozorovateľa k bodom 1 a 2 sú oveľa väčšie ako vzdialenosti $r$ aj $D$ a približne platí 

$$
D\approx d_1 \psi \, . \tag{2}
$$

 Použijeme nasledujúce zjednodušenie pre pomery vzdialeností 

$$
\frac{x}{d_2}\approx \frac{D}{d_1} \, . \tag{3}
$$

 Keďže vzdialenosť výtrysku od pozorovateľa sa za 10 rokov takmer nezmenila, platí $d_1\approx d_2 \approx d = 20\,\mathrm{Mpc}$, z čoho dostaneme $x\approx D = r \sin \alpha$. Rýchlosť výtrysku vypočítame jednoducho ako 

$$
v=\frac{r}{t}=\frac{D}{t\sin \alpha}=\frac{\psi d}{t \sin \alpha} \, , \tag{4}
$$

 

$$
v=\frac{0,0645}{206265}\cdot\frac{20 \cdot 10^{6}\cdot3{,}086 \cdot 10^{16}}{10\cdot365,25\cdot86400\cdot\sin 30^{\circ}}=1{,}22 \cdot 10^{9}\,\mathrm{m}\,{\mathrm{s}}^{-1}>c \, . \tag{5}
$$

 Vidíme, že nám vyšla hodnota väčšia ako je rýchlosť svetla, preto musíme príklad počítať opatrnejšie a zarátať aj rozdielnu dobu šírenia svetelného signálu z miesta výtrysku k pozorovateľovi. Pomôžu nám nasledujúce úvahy.\
Signál z bodu 1 je vyslaný v čase 0, k pozorovateľovi na Zemi dorazí v čase $t_1=\frac{d_1}{c}$. Výtrysk dorazí do bodu 2 v čase $t=\frac{r}{v}$, v tej chvíli vyrazí z bodu 2 svetelný signál, ktorý dorazí k pozorovateľovi o $\frac{d_2}{c}$ neskôr, teda v čase $t_2=\frac{r}{v}+\frac{d_2}{c}$.\
Pozorovateľovi sa zdá, že za čas $t_2-t_1=t=10\,\mathrm{rokov}$ prešiel výtrysk vzdialenosť $D\approx \psi d$. 

$$
t=t_2-t_1=\frac{r}{v}+\frac{d_2}{c}-\frac{d_1}{c} \, , \tag{6}
$$

 Pre rozdiel vzdialeností platí približný vzťah 

$$
d_1-d_2\approx r\cos \alpha \, , \tag{7}
$$

 

$$
t=\frac{r}{v}-\frac{r\cos\alpha}{c} \, . \tag{8}
$$

 Rovnicu vydelíme $r$ a potom dosadíme za $r$ na ľavej strane rovnice 

$$
\frac{t}{r}=\frac{1}{v}-\frac{\cos\alpha}{c} \, , \tag{9}
$$

 

$$
\frac{t \sin \alpha}{D}=\frac{t \sin \alpha}{\psi d} =\frac{1}{v}-\frac{\cos\alpha}{c} \, . \tag{10}
$$

 Teraz už stačí iba z rovnice vyjadriť rýchlosť $v$ 

$$
\frac{1}{v} =\frac{t \sin \alpha}{\psi d}+\frac{\cos\alpha}{c} \, , \tag{11}
$$

 

$$
v=\frac{1}{\frac{t \sin \alpha}{\psi d}+\frac{\cos\alpha}{c}}=\frac{1}{\frac{10\cdot365,25\cdot86400 \sin 30^{\circ}\cdot206265}{20 \cdot 10^{6}\cdot3{,}086 \cdot 10^{16}\cdot0,0645}+\frac{\cos30^{\circ}}{2{,}9979 \cdot 10^{8}}} \, , \tag{12}
$$

 

$$
v=2{,}7 \cdot 10^{8}\,\mathrm{m}\,{\mathrm{s}}^{-1}=0,9c \, . \tag{13}
$$

 Rýchlosť výtrysku nám tentokrát správne vyšla už nižšia ako rýchlosť svetla.

</details>
