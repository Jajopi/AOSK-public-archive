---
title: Nadsvetelný výtrysk
year: 2015
round: DK
roundName: Domáce kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú3
weight: 303
hasSolution: true
source: ZAO:I_Zadania/07_Kozmo/07_SS_DK.tex
rocniky:
- '2015'
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

V okolí mnohých extragalaktických objektov pozorujeme unikajúce štruktúry – prúdy, výtrysky, bubliny, atď. Pozorovania ukazujú, že mnohé z týchto výtryskov sa pohybujú zdanlivo nadsvetelnými rýchlosťami. Skutočné rýchlosti musia byť v súlade s teóriou relativity menšie ako rýchlosť svetla vo vákuu. Zdanlivé nadsvetelné rýchlosti sú dôsledkom geometrického efektu relativisticky sa pohybujúceho výtrysku, za predpokladu, že výtrysk sa deje smerom k nám (resp. smerom od nás) a rýchlosť svetla je konečná. Ak pozorovaná rýchlosť výtrysku $v_\mathrm{z}$ (meraná kolmo na zorný lúč) je nadsvetelná a uhol smeru výtrysku a zorného lúča je $\alpha$, ukážte, že vlastná (skutočná) rýchlosť je menšia ako rýchlosť svetla vo vákuu $c$. Konkrétny výpočet urobte pre výtrysk so zdanlivou rýchlosťou $v_\mathrm{z} = 10c$, $\alpha = 10^{\circ}$.

<details class="solution">
<summary>Riešenie</summary>

<figure>

<div class="fig-images"><img class="invert" src="AO2015_SS_DK_3.svg" alt="obrázok" loading="lazy" style="width:15%"></div>

</figure>

Všetky naše úvahy vychádzajú z obrázku. Signál z bodu 1 je vyslaný v čase 0, k pozorovateľovi na Zemi dorazí v čase $t_1=\frac{d_1}{c}$. Výtrysk dorazí do bodu 2 v čase $t=\frac{r}{v}$, v tej chvíli vyrazí z bodu 2 svetelný signál, ktorý dorazí k pozorovateľovi o $\frac{d_2}{c}$ neskôr, teda v čase $t_2=\frac{r}{v}+\frac{d_2}{c}$.\
Pozorovateľovi sa zdá, že za čas $t_2-t_1$ prešiel výtrysk vzdialenosť $D$ rýchlosťou $v_\textrm{z}=10c$ 

$$
\frac{D}{v_\textrm{z}}=t_2-t_1=\frac{r}{v}+\frac{d_2}{c}-\frac{d_1}{c} \, . \tag{1}
$$

 Ako bolo uvedené v zadaní, takéto výtrysky sa pozorujú v extragalaktických objektoch. To znamená, že vzdialenosti $d_1$, $d_2$ od pozorovateľa k bodom 1 a 2 sú oveľa väčšie ako vzdialenosť $r$ (aj $D$), ktorú výtrysk prejde počas doby pozorovania. Vďaka tomu môžeme použiť nasledujúce 2 zjednodušené vzťahy pre pomery a rozdiely vzdialeností 

$$
\frac{x}{d_2}\approx \frac{D}{d_1} \, , \tag{2}
$$

 

$$
d_1-d_2\approx r\cos \alpha \, . \tag{3}
$$

 Úsečka $x$ vychádza z bodu 2 a je kolmá na $d_1$, jej dĺžka je 

$$
x=r \sin \alpha \, . \tag{4}
$$

 Všetky tieto predpoklady dosadíme do rovnice 1 

$$
\frac{D}{v_\textrm{z}}=\frac{r}{v}-\frac{r}{c}\cos\alpha \, , \tag{5}
$$

 

$$
D\approx \frac{d_1}{d_2}x=\frac{d_1}{d_2}r\sin\alpha\approx r\sin \alpha \, . \tag{6}
$$

 V poslednej rovnosti sme využili, že pomer vzdialeností $d_1$ a $d_2$ je približne rovný 1, pretože sú obidve oveľa väčšie ako $r$ (ich rozdiel je ale stále nenulový) 

$$
\frac{r\sin \alpha}{v_\textrm{z}}\approx \frac{r}{v}-\frac{r\cos \alpha}{c} \, , \tag{7}
$$

 

$$
\frac{\sin \alpha}{v_\textrm{z}}\approx \frac{1}{v}-\frac{\cos \alpha}{c} \, , \tag{8}
$$

 

$$
\frac{1}{v}=\frac{\sin \alpha}{v_\textrm{z}}+\frac{\cos \alpha}{c} \, , \tag{9}
$$

 

$$
v=\frac{1}{\frac{\sin \alpha}{v_\textrm{z}}+\frac{\cos \alpha}{c}}=\frac{1}{\frac{\sin 10^{\circ}}{10c}+\frac{\cos 10^{\circ}}{c}}=\frac{1}{\frac{\sin 10^{\circ}}{10c}+\frac{10\cdot \cos 10^{\circ}}{10c}} \, , \tag{10}
$$

 

$$
v=\frac{10c}{\sin 10^{\circ}+\cos 10^{\circ}}=0,9978c \, . \tag{11}
$$

 Skutočná rýchlosť výtrysku je naozaj nižšia ako rýchlosť svetla.

</details>
