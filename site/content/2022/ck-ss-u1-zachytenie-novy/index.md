---
title: Zachytenie novy
year: 2022
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú1
weight: 5001
hasSolution: true
source: ZAO:I_Zadania/08_Rozsiahle/08_SS_FI.tex
years:
- '2022'
rounds:
- Celoštátne kolo
categories:
- SŠ
types:
- Teória
topics:
- Rozsiahle príklady
collection: ZAO
---

## Zadanie

V súčasnosti je už takmer každý jeden objav, ktorý učiníme v astronómií zaznamenaný nie jedným ale dvoma, troma či viacerými prístrojmi. A tak sa aj stalo v tomto hypotetickom prípade (nova je reálna, ale niektoré parametre sú domyslené).

Predstavte si, že tento rok počas leta, konkrétne 8. augusta 21:55 UT ste boli vo vedení multiodborovej komisie ktorá sleduje novy a jedna taká sa práve odohrala. Konkrétne rekurentná nova RS Ophiuchi v súhvezdí Hadonosa. Okamžite ste začali zbierať všetky dáta ktoré dokážete. Konkrétne ste sa dostali ku dátam z fotometrov, sprektrografov a neutrínových detektorov. A tak je na vás aby ste o tejto nove zistili čo najviac čo len dokážete z dát ktoré obdržíte z pozorovaní.\
Dáta z fotometrov vám podali informáciu o svetelnosti novy. Po uplynutí určitého času ste na veľkých detektoroch zaznamenali zopár neutrín a určili ich plošnú hustotu ako aj ich rýchlosť. Následne ste po nejakom čase namerali svetelné čiary na spektrografoch.

Odpozorovali ste novu RS Ophiuchi a namerali ste nasledujúce parametre.

|                                                               |           |
|:-------------------------------------------------------------:|:---------:|
|                    Bolometrická magnitúda                     | $m=0\,\mathrm{mag}$ |
|           Časový rozdiel medzi fotónmi a neutrínami           | $\Delta t = 2{,}5\,\min$ |
|                       Rýchlosť neutrín                        | $v_\nu = 0{,}999999999\ c$ |
|                    Plošná hustota neutrín                     | $\sigma_\nu = 4{,}5 \cdot 10^{15}\,{\mathrm{m}}^{-2}$ |
| Pomer intenzít pre 3 filtre ($U$, $B$, $V$) | $\frac{U}{V}=1,790$ |
|                                                               | $\frac{V}{B}=1,8231$ |
|             Zmerané vlnové dĺžky čiary H$\alpha$             | $\lambda_{\rightarrow}=6654{,}67942\,\mathring{A}$ |
|                                                               | $\lambda_{\leftarrow}=6470{,}92102\,\mathring{A}$ |

Každá podúloha sa vzťahuje na jednu veličinu, ktorú viete vypočítať zo zadania a iných podúloh.

Konštanty a zákony:

|                                       |           |
|:-------------------------------------:|:---------:|
|  Energia protón-protónového procesu   | $E_\mathrm{pp}=26{,}73\,\mathrm{MeV}$ |
|     Vlnová dĺžka H$\alpha$ čiary     | $\lambda_{\mathrm{H}\alpha} = 6562{,}8\,\mathring{A}$ |
|         Vlnové dĺžky filtrov          | $\lambda_\mathrm{U} = 364\,\mathrm{nm}$ |
|                                       | $\lambda_\mathrm{B} = 442\,\mathrm{nm}$ |
|                                       | $\lambda_\mathrm{V} = 540\,\mathrm{nm}$ |
| Wienova aproximácia Planckovho zákona | $I(f,T)=\frac{2hf^3}{c^2}e^{-\frac{hf}{k_\mathrm{B}T}}$ |

<ol type="a">

<li>

Zistite aká je vzdialenosť $r$ Zem-nova. Ideálne v rozumných jednotkách ako je ly alebo pc.

</li>

</ol>

<ol type="a" start="2">

<li>

Aká je absolútna bolometrická magnitúda novy $M$.

</li>

<li>

Počet neutrín $N_\nu$, ktoré vznikli pri nove.

</li>

</ol>

Predpokladajte, že pri nove funguje iba protón-protónový cyklus, a že pri Zemi, ani pri nove nie sú žiadne ďalšie zdroje neutrín. Rovnica protón-protónového cyklu je 

$$
4p^+ \; \rightarrow \; ^4He \;+ \; 2\nu_e \; + \; E_\mathrm{pp} \, .
$$

 Nova prebehla tak, že v jednom momente došlo ku vzniku všetkých neutrín, ktoré sme následne zachytili pri Zemi. Ale el.mag. žiarenie s energiou $E^*$ sa následne uvoľňovalo postupne za čas $\tau$. Zistite:

<ol type="a" start="4">

<li>

Energiu výbuchu novy $E^*$.

</li>

<li>

Dobu výbuchu novy $\tau$.

</li>

</ol>

Predpokladajte, že všetka uvoľnená energia zistená z neutrín sa vyžaruje za čas $\tau$ tak, aby bola absolútna magnitúda $M$.

<ol type="a" start="6">

<li>

Povrchovú teplotu novy $T$. Typické teploty sú $T_\textrm{tab}=10^{11}\,\mathrm{K}$. Vami zistená hodnota bude značne odlišná. Rozdiel diskutujte.

</li>

<li>

Hubblovu konštantu $H_0$. Prípadné rozdiely diskutujte.

</li>

</ol>

<ol type="a" start="8">

<li>

Rýchlosť odhodených obálok $v_\mathrm{O}$.

</li>

</ol>

Zmerali ste 2 vlnové dĺžky z obálky ktorá odlieta od novy.

<ol type="a" start="9">

<li>

BONUS úloha. Vymyslite si ešte jednu zaujímavú veličinu, ktorú viete určiť z dáta ktoré máte k dispozícií, a ktoré ste už vypočítali. Túto veličinu vypočítajte.

</li>

</ol>

Snažte sa vypočítať všetky podúlohy, niektoré na sebe nezávisia, takže sa nemusia riešiť v zadanom poradí (i keď zadané poradie je odporúčané). Body sú udeľované najmä za postup.\
Úlohy by sa mali dať vypočítať bez extrémnych aproximácií. Skúste sa vyhnúť zaokrúhľovacím chybám. Výsledok ale uveďte na rozumný počet platných cifier.

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Stačí nám napísať si základný vzťah pre rýchlosť, čas a vzdialenosť pre svetlo a pre neutrína

</li>

</ol>

$$
r=ct \, , \tag{1}
$$

 

$$
r=v_{\nu}(t+\Delta t)=v_{\nu}t+v_{\nu}\Delta t \, , \tag{2}
$$

 

$$
r=v_{\nu}\frac{r}{c}+v_{\nu}\Delta t \, , \tag{3}
$$

 

$$
r\left(1-\frac{v_{\nu}}{c}\right)=v_{\nu}\Delta t \, , \tag{4}
$$

 

$$
r=\frac{cv_{\nu}}{c-v_{\nu}}\Delta t \, . \tag{5}
$$

 Vypočítame rozdiel rýchlostí svetla a neutrín 

$$
c-v_{\nu}=(1-0{,}999999999)c=1 \cdot 10^{-9}c \, . \tag{6}
$$

 Dosadíme do menovateľa zlomku a vykrátime $c$. Vzdialenosť novy je 

$$
r=\frac{cv_{\nu}}{1 \cdot 10^{-9}c}\Delta t =\frac{v_{\nu}}{1 \cdot 10^{-9}}\Delta t\, . \tag{7}
$$

 

$$
r=\frac{2{,}9979 \cdot 10^{8}}{10^{-9}}\cdot2,5\cdot60=4{,}5 \cdot 10^{19}\,\mathrm{m}=1457\,\mathrm{pc} \, . \tag{8}
$$

 Za $v_{\nu}$ sme dosadili hodnotu rýchlosti svetla, pretože je takmer rovnaká a dosadenie presnej hodnoty $v_{\nu}$ by nám výsledok v rámci platných číslic vôbec nezmenilo.

<ol type="a" start="2">

<li>

Absolútna bolometrická magnitúda novy je

</li>

</ol>

$$
M=m+5-5\log r=0+5-5\log(1457)=-10{,}82\,\mathrm{mag} \, . \tag{9}
$$

<ol type="a" start="3">

<li>

Poznáme plošnú hustota neutrín pri Zemi a vzdialenosť novy. Predstavíme si, že všetky neutrína sú na sfére s polomerom rovným vzdialenosť k nove a celkový počet neutrín spočítame jednoducho ako

</li>

</ol>

$$
N_{\nu}=4\pi r^2\sigma_{\nu}=4\pi \cdot(4{,}5 \cdot 10^{19})^2\cdot4{,}5 \cdot 10^{15}=1{,}15 \cdot 10^{56} \, . \tag{10}
$$

<ol type="a" start="4">

<li>

Pri každom p-p cykle sa vyprodukujú 2 neutrína. Na jedno neutríno pripadá energia

</li>

</ol>

$$
E_{\nu}=\frac{E_\textrm{pp}}{2} \, . \tag{11}
$$

 Celkovú energiu výbuchu novy získame prenásobením počtom neutrín 

$$
E^*=N_{\nu}E_{\nu}=1{,}15 \cdot 10^{56}\cdot\frac{26,142}{2}\cdot1{,}602 \cdot 10^{-13}=2{,}4 \cdot 10^{44}\,\mathrm{J} \, . \tag{12}
$$

<ol type="a" start="5">

<li>

Z Pogsonovej rovnice pre absolútne bolometrické magnitúdy vieme vypočítať žiarivý výkon novy

</li>

</ol>

$$
M_{\Sun}-M=2,5\log \left(\frac{L}{L_{\Sun}}\right) \, , \tag{13}
$$

 

$$
L=2,512^{M_{\Sun}-M}L_{\Sun} \, . \tag{14}
$$

 Vieme, že sa dobu $\tau$ nova vyžiarila energiu $E^*$, z toho dostaneme 

$$
\tau=\frac{E^*}{L}=\frac{E^*}{2,512^{M_{\Sun}-M}L_{\Sun}}=\frac{2{,}4 \cdot 10^{44}}{2,512^{4,72+10,82}\cdot3{,}826 \cdot 10^{26}}=3{,}81 \cdot 10^{11}\,\mathrm{s}=12\,000\,\mathrm{rokov} \, . \tag{15}
$$

<ol type="a" start="6">

<li>

Využijeme Wienovu aproximáciu zo zadania. Je vhodnejšie ju použiť pre filtre $U$ a $B$ s kratšími vlnovými dĺžkami. Podelíme Wienov zákon pre tieto dva filtre a dostaneme

</li>

</ol>

$$
\frac{U}{B}=\frac{f_\textrm{U}^3}{f_\textrm{B}^3}\frac{\exp \left(\frac{-hf_\textrm{U}}{k_\textrm{B}T}\right)}{\exp \left(\frac{-hf_\textrm{B}}{k_\textrm{B}T}\right)} \, . \tag{16}
$$

 Namiesto frekvencií chceme použiť vlnové dĺžky 

$$
f=\frac{c}{\lambda} \, , \tag{17}
$$

 

$$
\frac{U}{B}=\frac{U}{V}\frac{V}{B}=\frac{\lambda_B^3}{\lambda_\textrm{U}^3}\frac{\exp \left(\frac{-hc}{k_\textrm{B}T\lambda_\textrm{U}}\right)}{\exp \left(\frac{-hc}{k_\textrm{B}T\lambda_\textrm{B}}\right)}=\frac{\lambda_\textrm{B}^3}{\lambda_\textrm{U}^3}\exp \left[\frac{hc}{k_\textrm{B}T}\left(\frac{1}{\lambda_\textrm{B}}-\frac{1}{\lambda_\textrm{U}}\right)\right] \, . \tag{18}
$$

 Rovnicu zlogaritmujeme 

$$
\ln \left(\frac{U}{B}\frac{\lambda_\textrm{U}^3}{\lambda_\textrm{B}^3}\right)=\frac{hc}{k_\textrm{B}T}\left(\frac{1}{\lambda_\textrm{B}}-\frac{1}{\lambda_\textrm{U}}\right) \, . \tag{19}
$$

 Vyjadríme teplotu 

$$
T=\frac{hc}{k_\textrm{B}}\left(\frac{1}{\lambda_\textrm{B}}-\frac{1}{\lambda_\textrm{U}}\right)\frac{1}{\ln \left(\frac{U}{v}\frac{V}{B}\frac{\lambda_\textrm{U}^3}{\lambda_\textrm{B}^3}\right)} \, , \tag{20}
$$

 

$$
T=\frac{6{,}626 \cdot 10^{-34}\cdot2{,}9979 \cdot 10^{8}}{1{,}381 \cdot 10^{-23}}\left(\frac{1}{442}-\frac{1}{364}\right)\frac{10^9}{\ln \left(1,79\cdot1,8231\cdot\frac{364^3}{442^3}\right)}=11\,600\,\mathrm{K} \, . \tag{21}
$$

 Rozdiel oproti typickým teplotám je spôsobený tým, že nova nežiari ako absolútne čierne teleso, preto na výpočet jej teploty nie je vhodné použiť Planckov zákon ani jeho aproximácie.

<ol type="a" start="7">

<li>

Najskôr vypočítame strednú pozorovanú vlnovú dĺžku čiary H$\alpha$, z tej potom vypočítame rýchlosť vzďaľovania sa novy

</li>

</ol>

$$
\lambda=\frac{6654,67942+6470,92102}{2}=6562{,}80022\,\mathrm{rokov} \, , \tag{22}
$$

 

$$
v=\frac{\lambda-\lambda_0}{\lambda_0}c \, . \tag{23}
$$

 Hubblovu konštantu určíme ako podiel rýchlosti a vzdialenosti novy 

$$
H_0=\frac{\lambda-\lambda_0}{\lambda_0}\frac{c}{r}=\frac{0,00022}{6562,8}\cdot\frac{2,9979e5}{1457 \cdot 10^{-6}}=6{,}9\,\mathrm{km}\,{\mathrm{s}}^{-1}\,{\mathrm{Mpc}}^{-1} \, . \tag{24}
$$

 To je pochopiteľne úplne mimo známej hodnoty Hubblovej konštanty, pretože meriame na malých vzdialenostiach kde sa prejavujú relatívne vzájomné pohyby objektov a nie rozpínanie vesmíru.

<ol type="a" start="8">

<li>

Z krajných hodnôt nameranej vlnovej dĺžky čiary H$\alpha$ vieme vypočítať rýchlosť časti obálky, ktorá sa od Zeme najrýchlejšie vzďaluje

</li>

</ol>

$$
v_{\leftarrow}=\frac{\lambda_{\leftarrow}-\lambda_0}{\lambda_0}c=\frac{6654,67942-6562,8}{6562,8}\cdot2{,}9979 \cdot 10^{5}=4200\,\mathrm{km}\,{\mathrm{s}}^{-1} \, . \tag{25}
$$

 Aj časti obálky, ktorá sa ku Zemi najrýchlejšie približuje 

$$
v_{\leftarrow}=\frac{\lambda_{\leftarrow}-\lambda_0}{\lambda_0}c=\frac{6470,92102-6562,8}{6562,8}\cdot2{,}9979 \cdot 10^{5}=-4200\,\mathrm{km}\,{\mathrm{s}}^{-1} \, . \tag{26}
$$

 Ako vidíme, obidve rýchlosti sú rovnaké, obálka sa pravdepodobne rozpína symetricky.

</details>
