---
title: Úloha 2
year: 2017
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú2
weight: 5002
hasSolution: true
source: ZAO:I_Zadania/02_GmtrCas/02_SS_FI.tex
years:
- '2017'
rounds:
- Celoštátne kolo
categories:
- SŠ
types:
- Teória
topics:
- Geometria a čas
collection: ZAO
---

## Zadanie

21\. augusta 2017 nastane úplné zatmenie Slnka, ktoré budú mnohí astronómovia z celého sveta pozorovať v USA. Preto je veľmi aktuálne riešiť aj úlohu o zatmení Slnka. Zdanlivý priemer, teda uhlový priemer Mesiaca je o málo menší ako Slnka, preto je počet prstencových zatmení Slnka o trochu väčší ako úplných zatmení. Pre pozorovateľa na Zemi najdlhšie úplné zatmenie Slnka trvá $7{,}5\,\min$ a najdlhšie prstencové zatmenie trvá $12{,}5\,\min$. V tomto prípade trvanie prstencového zatmenia je časový interval od druhého po tretí kontakt. Predpokladáme, že môžeme vypočítať počet oboch typov zatmení pre veľmi dlhú dobu. Určte pomer prstencových a úplných zatmení. Predpokladáme, že dráha Zeme je kruhová, mesačná dráha je eliptická. Všetky hybridné zatmenia treba započítať medzi prstencové.

<details class="solution">
<summary>Riešenie</summary>

Najdlhšie úplné zatmenie nastane vo chvíli, kedy je Mesiac v perigeu, pretože zdanlivý uhlový priemer Mesiaca $\theta_\textrm{p}$ je vtedy najväčší. Naopak, uhlový priemer Mesiaca v apogeu $\theta_\textrm{a}$ je najmenší, preto vtedy nastane najdlhšie prstencové zatmenie. Zo zachovania momentu hybnosti dostaneme 

$$
r_\textrm{p}^2\omega_\textrm{p}=r_\textrm{a}^2\omega_\textrm{a} \tag{1}
$$

 kde $r_\textrm{p}=a(1-e)$ je vzdialenosť Mesiaca od Zeme v perigeu a $r_\textrm{a}=a(1+e)$ je vzdialenosť Mesiaca od Zeme v apogeu, $\omega_\textrm{p}$ a $\omega_\textrm{a}$ je uhlová rýchlosť Mesiaca v perigeu resp. apogeu. Ak zanedbáme pohyb Zeme okolo Slnka počas zatmenia (inak by bolo riešenie príkladu oveľa komplikovanejšie), tak je dĺžka trvania zatmenia v perigeu 

$$
t_\textrm{p}=\frac{\theta_\textrm{p}-\theta_{\Sun}}{\omega_\textrm{p}} \, , \tag{2}
$$

 kde $\theta_{\Sun}$ je uhlový priemer Slnka. Dĺžka trvania zatmenia v apogeu je 

$$
t_\textrm{a}=\frac{\theta_{\Sun}-\theta_\textrm{a}}{\omega_\textrm{a}} \, . \tag{3}
$$

 Pre uhlové rýchlosti a priemery platia nasledujúce vzťahy 

$$
\frac{\omega_\textrm{p}}{\omega_\textrm{a}}=\left(\frac{1+e}{1-e}\right)^2 \, , \tag{4}
$$

 

$$
\theta_\textrm{p}=\frac{2R_{\Mo}}{r_\textrm{p}} \, , \tag{5}
$$

 

$$
\theta_\textrm{a}=\frac{2R_{\Mo}}{r_\textrm{a}} \, . \tag{6}
$$

 Výrazy pre časy zatmení podelíme 

$$
\frac{t_\textrm{a}}{t_\textrm{p}}=\frac{\omega_\textrm{p}}{\omega_\textrm{a}}\frac{\theta_{\Sun}-\theta_\textrm{a}}{\theta_\textrm{p}-\theta_{\Sun}}=\frac{(1+e)^2}{(1-e)^2}\frac{\theta_{\Sun}-\theta_\textrm{a}}{\theta_\textrm{p}-\theta_{\Sun}} \, . \tag{7}
$$

 Kvôli prehľadnejším výpočtom zavedieme označenie 

$$
k:=\frac{t_\textrm{a}}{t_\textrm{p}}\frac{(1-e)^2}{(1+e)^2} \, , \tag{8}
$$

 

$$
k=\frac{\theta_{\Sun}-\theta_\textrm{a}}{\theta_\textrm{p}-\theta_{\Sun}} \, , \tag{9}
$$

 

$$
k\theta_\textrm{p}-k\theta_{\Sun}=\theta_{\Sun}-\theta_\textrm{a} \, , \tag{10}
$$

 

$$
k\theta_\textrm{p}+\theta_\textrm{a}=\theta_{\Sun}+k\theta_{\Sun}=(1+k)\theta_{\Sun} \, . \tag{11}
$$

 Pre uhlové priemery platí nasledujúci vzťah 

$$
\theta_\textrm{a}=\frac{r_\textrm{p}}{r_\textrm{a}}\theta_\textrm{p}=\frac{1-e}{1+e}\theta_\textrm{p} \, , \tag{12}
$$

 

$$
\theta_{\Sun}=\left(k+\frac{1-e}{1+e}\right)\frac{\theta_\textrm{p}}{1+k} \, . \tag{13}
$$

 Vypočítame číselnú hodnotu $k$ 

$$
\frac{12,5}{7,5}\frac{(1-0,0549)^2}{(1+0,0549)^2}=1,3378 \, , \tag{14}
$$

 

$$
\theta_{\Sun}=\left(1,3378+\frac{1-0,0549}{1+0,0549}\right)\cdot\frac{\theta_\textrm{p}}{1+1,3378}=0,9555\theta_\textrm{p} \, . \tag{15}
$$

 Hľadáme miesto na mesačnej dráhe, kde platí $\theta_{\Mo}=\theta_{\Sun}$, práve tam sa totiž nachádza hranica medzi prstencovými a úplnými zatmeniami. Využijeme pri tom rovnicu elipsy v polárnych súradniciach 

$$
r=\frac{a(1-e^2)}{1+e\cos (v)} \, , \tag{16}
$$

 kde $v$ je pravá anomália. Na obrázku nižšie ja načrtnutý význam pravej aj excentrickej anomálie.

<figure>

<div class="fig-images"><img class="invert" src="AO2017_SS_FI_2.svg" alt="obrázok" loading="lazy" style="width:60%"></div>

</figure>

V mieste rovnosti slnečného a mesačného uhlového priemeru platí 

$$
r\theta_{\Sun}=r_\textrm{p}\theta_\textrm{p} \, , \tag{17}
$$

 

$$
0,9555r\theta_\textrm{p}=r_\textrm{p}\theta_\textrm{p} \, . \tag{18}
$$

 Dosadíme za $r$ do rovnice elipsy 

$$
\frac{r_\textrm{p}}{0,9555}=\frac{a(1-e^2)}{1+e\cos (v)} \, , \tag{19}
$$

 

$$
\frac{a(1-e)}{0,9555}=\frac{a(1-e)(1+e)}{1+e\cos (v)} \, , \tag{20}
$$

 

$$
1+e\cos (v) = 0,9555(1+e) \, , \tag{21}
$$

 

$$
\cos (v)=\frac{0,9555\cdot(1+0,0549)-1}{0,0549} \, . \tag{22}
$$

 Uhlový priemer Mesiaca a Slnka sa rovnajú v momente, kedy je pravá anomália Mesiaca $v=81{,}7^{\circ}$. V okolí $81{,}7^{\circ}$ na obidve strany od perigea dochádza k úplným zatmeniam, na zvyšku dráhy Mesiaca dochádza k prstencovým zatmeniam. Pomer počtu týchto dvoch typov zatmení, ktoré nastanú za dlhý časový úsek sa zhruba rovná pomeru časov, ktoré Mesiac strávi na príslušných úsekoch jeho dráhy (zatmenia môžu nastať v náhodných miestach dráhy Mesiaca). Na zistenie pomeru potrebujeme vypočítať koľko času uplynie, kým Mesiac prejde z perigea do miesta s $v=81{,}7^{\circ}$. Využijeme vzťah medzi pravou a excentricku anomáliou 

$$
\tan \left(\frac{v}{2}\right)=\sqrt{\frac{1+e}{1-e}}\tan \left(\frac{E}{2}\right) \, . \tag{23}
$$

 Excentrická anomália v mieste s $v=81{,}7^{\circ}$ je 

$$
E=2\cdot\arctan \left[\sqrt{\frac{1-0,0549}{1+0,0549}}\tan \left(\frac{81,7}{2}\right)\right]=78{,}6^{\circ} \, . \tag{24}
$$

 Strednú anomáliu vypočítame z Keplerovej rovnice, pričom si treba dať pozor na to, že je potrebné dosadiť hodnoty v radiánoch 

$$
M=E-e\sin E=\frac{78,6}{180}\cdot \pi-0,0549\cdot\sin (78{,}6^{\circ})=1{,}32\,\mathrm{rad}=75{,}5^{\circ} \, , \tag{25}
$$

 

$$
t=\frac{M}{360^{\circ}}P_{\Mo}=\frac{75{,}5^{\circ}}{360}\cdot27,32=5{,}73\,\mathrm{dní} \, . \tag{26}
$$

 Pomer počtu prstencových a úplných zatmení je 

$$
\frac{N_\textrm{p}}{N_\textrm{u}}=\frac{P_{\Mo}-2t}{2t}=\frac{27,32-2\cdot5,73}{2\cdot5,73}=1,3 \, . \tag{27}
$$

</details>
