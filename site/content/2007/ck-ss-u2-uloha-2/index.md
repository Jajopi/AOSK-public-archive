---
title: Úloha 2
year: 2007
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú2
weight: 5002
hasSolution: true
source: ZAO:I_Zadania/01_NebMech/01_SS_FI.tex
years:
- '2007'
rounds:
- Celoštátne kolo
categories:
- SŠ
types:
- Teória
topics:
- Nebeská mechanika
collection: ZAO
---

## Zadanie

Určite, kedy trvá úplné zatmenie Mesiaca dlhšie – keď je Mesiac v apogeu, alebo v perigeu. Počítajte, že Zem je od Slnka vzdialená $1\,\mathrm{au}$. Zem, Mesiac i Slnko považujte za guľové. Zatmenie považujte za centrálne, t.j. Mesiac prechádza stredom tieňa Zeme. (Pre výpočet obvodovej rýchlosti Mesiaca v apogeu/perigeu využite zákon zachovania momentu hybnosti.)

<details class="solution">
<summary>Riešenie</summary>

Potrebujeme vypočítať šírku tieňa Zeme vo vzdialenosti perigea a apogea Mesiaca a rýchlosť Mesiaca v týchto miestach. Využitím podobnosti trojuholníkov na obrázku dostaneme pre pomery ich strán 

$$
\frac{R_\Sun}{a_\Ea+r_\textrm{t}}=\frac{d_1}{r_\textrm{t}-r_\textrm{p}}=\frac{d_2}{r_\textrm{t}-r_\textrm{a}}=\frac{R_\Ea}{r_\textrm{t}} \, . \tag{1}
$$

<figure>

<div class="fig-images"><img class="invert" src="AO2020_SS_DK_3.svg" alt="obrázok" loading="lazy" style="width:100%"></div>

</figure>

Najskôr zistíme, aká je dĺžka tieňa Zeme 

$$
R_\Sun r_\textrm{t}=R_\Ea a_\Ea +R_\Ea r_\textrm{t} \, , \tag{2}
$$

 

$$
(R_\Sun - R_\Ea) r_\textrm{t}=R_\Ea a_\Ea \, , \tag{3}
$$

 

$$
r_\textrm{t}=\frac{R_\Ea}{R_\Sun-R_\Ea}a_\Ea \, . \tag{4}
$$

Polovica šírky tieňa v perigeu a apogeu je 

$$
d_1=\frac{r_\textrm{t}-r_\textrm{p}}{a_\Ea+r_\textrm{t}}R_\Sun \, , \tag{5}
$$

 

$$
d_2=\frac{r_\textrm{t}-r_\textrm{a}}{a_\Ea+r_\textrm{t}}R_\Sun \, . \tag{6}
$$

 Vzorce na výpočet vzdialenosti perigea a apogea sú 

$$
r_\textrm{p}=a_\Mo (1-e_\Mo) \, , \tag{7}
$$

 

$$
r_\textrm{a}=a_\Mo (1+e_\Mo) \, . \tag{8}
$$

Číselné hodnoty sú 

$$
r_\textrm{t}=\frac{6378}{6{,}955 \cdot 10^{5}-6378}\cdot1{,}496 \cdot 10^{8}=1{,}385 \cdot 10^{6}\,\mathrm{km} \, , \tag{9}
$$

 

$$
r_\textrm{p}=3{,}844 \cdot 10^{5}\cdot(1-0,0549)=3{,}633 \cdot 10^{5}\,\mathrm{km} \, , \tag{10}
$$

 

$$
r_\textrm{a}=3{,}844 \cdot 10^{5}\cdot(1+0,0549)=4{,}055 \cdot 10^{5}\,\mathrm{km} \, , \tag{11}
$$

 

$$
d_1=\frac{1{,}385 \cdot 10^{6}-3{,}633 \cdot 10^{5}}{1{,}496 \cdot 10^{8}+1{,}385 \cdot 10^{6}}\cdot6{,}955 \cdot 10^{5}=4706\,\mathrm{km}\,{\mathrm{s}}^{-1} \, , \tag{12}
$$

 

$$
d_2=\frac{1{,}385 \cdot 10^{6}-4{,}055 \cdot 10^{5}}{1{,}496 \cdot 10^{8}+1{,}385 \cdot 10^{6}}\cdot6{,}955 \cdot 10^{5}=4512\,\mathrm{km}\,{\mathrm{s}}^{-1} \, . \tag{13}
$$

 Na výpočet rýchlosti Mesiaca využijeme zákon zachovania hybnosti 

$$
L_\Mo=\textrm{konštanta}=M_\Mo r_\textrm{p} v_\textrm{p} = M_\Mo r_\textrm{a} v_\textrm{a} \, . \tag{14}
$$

 Ďalej použijeme fakt, že keď sa teleso nachádza vo vzdialenosti veľkej polosi od centra, tak sa pohybuje kruhovou (1. kozmickou rýchlosťou) $v_\textrm{k}$ 

$$
v_\textrm{k}=\frac{2\pi a_\Mo}{P_\Mo} \, , \tag{15}
$$

 

$$
L_\Mo=M_\Mo a_\Mo \frac{2\pi a_\Mo}{P_\Mo} \, . \tag{16}
$$

 Rýchlosť Mesiaca voči Zemi v perigeu a v apogeu je 

$$
v_\textrm{p}=\frac{2\pi a_\Mo^2}{P_\Mo r_\textrm{p}}=\frac{2\pi a_\Mo}{P_\Mo (1-e_\Mo)}=\frac{2\pi\cdot3{,}844 \cdot 10^{5}}{27,3217\cdot86400\cdot(1-0,0549)}=1{,}08\,\mathrm{km}\,{\mathrm{s}}^{-1} \, , \tag{17}
$$

 

$$
v_\textrm{a}=\frac{2\pi a_\Mo}{P_\Mo (1+e_\Mo)}=\frac{2\pi\cdot3{,}844 \cdot 10^{5}}{27,3217\cdot86400\cdot(1+0,0549)}=0{,}97\,\mathrm{km}\,{\mathrm{s}}^{-1} \, . \tag{18}
$$

 Predtým, než vypočítame dĺžku trvania zatmenia si musíme uvedomiť, že rýchlosti Mesiaca, ktoré sme vypočítali sú voči Zemi a nie voči tieňu Zeme. Kvôli obehu Zeme okolo Slnka sa jej tieň pohybuje rovnakou uhlovou rýchlosťou $\omega$ akou obieha Zem. Mesiac obieha okolo Zeme prográdne, to znamená, že tieň Zeme sa otáča okolo Zeme v rovnakom zmysle ako Mesiac. Preto Mesiacu trvá prechod zemským tieňom o niečo dlhšie než keby Zem stála na mieste. Rýchlosť Mesiaca voči tieňu Zeme vypočítame tak, že od rýchlosti Mesiaca voči Zemi odčítame rýchlosť tieňa Zeme v danom mieste. Rýchlosti tieňa sú 

$$
\omega=\frac{2\pi}{365,25\cdot86400} \, , \tag{19}
$$

 

$$
v_\textrm{tp}=\omega r_\textrm{p} =\frac{2\pi\cdot3{,}633 \cdot 10^{5}}{365,25\cdot86400}=0{,}07\,\mathrm{km}\,{\mathrm{s}}^{-1} \, , \tag{20}
$$

 

$$
v_\textrm{ta}=\omega r_\textrm{a} =\frac{2\pi\cdot4{,}055 \cdot 10^{5}}{365,25\cdot86400}=0{,}08\,\mathrm{km}\,{\mathrm{s}}^{-1} \, . \tag{21}
$$

 Mesiac sa teda voči tieňu pohybuje rýchlosťami 

$$
v_1=v_\textrm{p}-v_\textrm{tp}=1,08-0,07=1{,}01\,\mathrm{km}\,{\mathrm{s}}^{-1} \, , \tag{22}
$$

 

$$
v_2=v_\textrm{a}-v_\textrm{ta}=0,97-0,08=0{,}89\,\mathrm{km}\,{\mathrm{s}}^{-1} \, . \tag{23}
$$

 Zostáva nám už iba vypočítať čas trvania zatmení. Úplné zatmenie nastane až vo chvíli, kedy je Mesiac celý v tieni Zeme. Počas úplného zatmenia preto Mesiac prejde dráhu rovnú šírke tieňa v danej vzdialenosti mínus 2-krát polomer Mesiaca. Dĺžka trvania zatmení je 

$$
t_1=\frac{2d_1-2R_\Mo}{v_1}=\frac{2\cdot4706-2\cdot1737,4}{1,01}=5878\,\mathrm{s}=1\,\mathrm{h}\; 38\,\min \, , \tag{24}
$$

 

$$
t_2=\frac{2d_2-2R_\Mo}{v_2}=\frac{2\cdot4512-2\cdot1737,4}{0,89}=6235\,\mathrm{s}=1\,\mathrm{h}\;44\,\min \, . \tag{25}
$$

 Vidíme, že dlhšie trvá úplné zatmenie Mesiaca v apogeu.

</details>
