---
title: Štvrťstoročie s exoplanétami
year: 2020
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú3
weight: 2303
hasSolution: true
source: ZAO:I_Zadania/08_Rozsiahle/08_SS_FI.tex
rocniky:
- '2020'
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

Polovicu Nobelovej ceny za rok 2019 dostali astronómovia D. Queloz a M. Mayor za objav prvej exoplanéty 51 Pegasi b okolo hviezdy hlavnej postupnosti s hmotnosťou $M_\mathrm{51Peg}=1{,}11\,\mathit{M}_\Sun$ a žiarivým výkonom $L_\mathrm{51Peg}=4{,}28 \cdot 10^{26}\,\mathrm{W}$ (rok 1995). Jedná sa o tzv. horúci Jupiter – masívne teleso na krátkej obežnej dráhe.\
Planétu objavili vysokocitlivým spektrografom `ELODIE`, ktorý monitoroval vlnovú dĺžku viacerých absorpčných čiar v svetle hviezdy. Vzájomný orbitálny pohyb hviezdy a planéty okolo hmotného stredu má za následok periodický dopplerovský posun spektrálnych čiar okolo strednej hodnoty. Táto stratégia sa nazýva metóda radiálnych rýchlostí.

<ol type="a">

<li>

Planéta bola objavená z dopplerovského signálu s periódou $4{,}23\,\mathrm{dní}$. Spočítajte strednú vzdialenosť 51 Peg b od materskej hviezdy.

</li>

<li>

Vlnové dĺžky všetkých čiar v spektre hviezdy oscilujú s malou relatívnou amplitúdou iba $1{,}85 \cdot 10^{-7}$. Signál má tvar dokonalej sínusoidy a neboli detegované žiadne iné periódy. Za predpokladu, že zorný lúč zo Zeme leží v orbitálnej rovine 51 Peg b, spočítajte hmotnosť planéty. Kvantitatívne popíšte ako by sa interpretácia výsledku zmenila, keby sme neučinili posledný predpoklad o sklone dráhy.

</li>

<li>

vypočítajte rovnovážnu teplotu planéty, ak má Bondovo albedo[^1] 0,2 a vyžaruje ako čierne teleso s homogénnou teplotou. Prečo tento model pravdepodobne nie je v prípade horúceho Jupitera použiteľný?

</li>

</ol>

Napokon opustime systém 51 Peg a zvážme širšiu populáciu hviezd. Najviac nás zaujímajú planéty v obývateľnej zóne, teda v našom zjednodušení v takom intervale vzdialenosti od hviezdy, ktorému zodpovedá povrchová teplota v intervale ($0\,^{\circ}\mathrm{C}$, $100\,^{\circ}\mathrm{C}$). Uvažujte pre (d) takýto kontext:

- planéta hmotnosti ($m$) Zeme na kruhovej dráhe okolo materskej hviezdy, v rovine zorného lúča,

- zanedbajte akýkoľvek skleníkový efekt alebo albedo povrchu,

- `ELODIE` má rozlišovaciu schopnosť $v_0 = 13\,\mathrm{m}\,{\mathrm{s}}^{-1}$ (minimálna rozlíšiteľná amplitúda radiálnej rýchlosti),

- existuje približný vzťah medzi žiarivým výkonom $L$ a hmotnosťou $M$ hviezdy v tvare

$$
\frac{L}{L_{\Sun}}=\frac{M^4}{M_{\Sun}^4} \, .
$$

<ol type="a" start="4">

<li>

Aká je najväčšia hmotnosť hviezdy $M$, pri akej vie `ELODIE` ledva detegovať vyššie špecifikovanú planétu v obývateľnej zóne? Interpretujte výsledok a jeho vplyv na pozorovateľnosť exoplanét podobných Zemi.

</li>

</ol>

[^1]: Albedo (odrazivosť planéty) – bezrozmerné číslo v intervale (0,1) vyjadrujúce pomer odrazeného žiarenia k všetkému dopadajúcemu žiareniu.

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Veľkú polos exoplanéty vypočítame z 3. Kepleroveho zákona

</li>

</ol>

$$
a=\sqrt[3]{\frac{GM_\textrm{51Peg}P^2}{4\pi^2}} \, , \tag{1}
$$

 

$$
a=\sqrt[3]{\frac{6{,}67 \cdot 10^{-11}\cdot1,11\cdot1{,}9891 \cdot 10^{30}\cdot(4,23\cdot86400)^2}{4\pi^2}}=7{,}93 \cdot 10^{9}\,\mathrm{m}=0{,}053\,\mathrm{au} \, . \tag{2}
$$

<ol type="a" start="2">

<li>

Sínusový tvar krivky znamená, že planéta sa pohybuje po kruhovej dráhe. Zo známej orbitálnej periódy a polomeru dráhy vieme vypočítať obežnú rýchlosť planéty

</li>

</ol>

$$
v_\textrm{p}=\frac{2\pi a}{P}=\frac{2\pi\cdot}{4,23\cdot86400}=1{,}36 \cdot 10^{5}\,\mathrm{m}\,{\mathrm{s}}^{-1}=136\,\mathrm{km}\,{\mathrm{s}}^{-1} \, . \tag{3}
$$

 Rýchlosť hviezdy vypočítame z Dopplerovho posunu jej spektrálnych čiar 

$$
v_\textrm{51Peg}=\frac{\Delta\lambda}{\lambda_0}c=1{,}85 \cdot 10^{-7}\cdot2{,}9979 \cdot 10^{8}=55{,}5\,\mathrm{m}\,{\mathrm{s}}^{-1} \, . \tag{4}
$$

 Využijeme, že pomer hmotností sa rovná prevrátenému pomeru rýchlostí 

$$
\frac{M_\textrm{p}}{M_\textrm{51Peg}}=\frac{v_\textrm{51Peg}}{v_\textrm{p}} \, . \tag{5}
$$

 Hmotnosť exoplanéty je 

$$
M_\textrm{p}=\frac{v_\textrm{51Peg}}{v_\textrm{p}}M_\textrm{51Peg}=\frac{55,5}{1{,}36 \cdot 10^{5}}\cdot1,11\cdot1{,}9891 \cdot 10^{30}=9{,}01 \cdot 10^{26}\,\mathrm{kg} \, . \tag{6}
$$

 Ak by sklon dráhy nebol presne $90^{\circ}$, maximum radiálnej rýchlosti by bolo iba priemetom orbitálnej rýchlosti do roviny zorného lúča $v_\textrm{r}=v\sin (i)$. Skutočná orbitálna rýchlosť hviezdy by bola väčšia. Orbitálna rýchlosť planéty je určená z veľkej polosi a periódy, preto by sa nezmenila. Hmotnosť exoplanéty by preto pri menšom sklone vyšla väčšia. Použitím $i=90^{\circ}$ sme teda získali dolný odhad hmotnosti exoplanéty.

<ol type="a" start="3">

<li>

Príkon prijatý planétou sa musí rovnať výkonu vyžiarenému planétou. Tok žiarenia na planétu je

</li>

</ol>

$$
F=\frac{L_\textrm{51Peg}}{4\pi a^2} \, . \tag{7}
$$

 Príkon energie na planétu je 

$$
P=F(1-A)R_\textrm{p}^2=\frac{L_\textrm{51Peg}}{4\pi a^2}(1-A)\pi R_\textrm{p}^2 \, . \tag{8}
$$

 Výkon vyžiarený planétou je rovný žiarivému výkonu absolútne čierneho telesa 

$$
L=4\pi R_\textrm{p}^2 \sigma T_\textrm{p}^4 \, . \tag{9}
$$

 Z rovnosti výkonu a príkonu, $L=P$, si vyjadríme teplotu planéty 

$$
\frac{L_\textrm{51Peg}}{4\pi a^2}(1-A)=4\sigma T_\textrm{p}^4 \tag{10}
$$

 

$$
T_\textrm{p}=\sqrt[4]{\frac{L_\textrm{51Peg}}{16\pi \sigma a^2}(1-A)}=\sqrt[4]{\frac{4{,}28 \cdot 10^{26}}{16\pi \cdot5{,}67 \cdot 10^{-8}\cdot(7{,}93 \cdot 10^{9})^2}(1-0,2)}=1176\,\mathrm{K} \, . \tag{11}
$$

 Tento model predpokladá, že planéta vyžaruje ako absolútne čierne teleso s rovnakou teplotou po celom povrchu. Vzhľadom na veľmi krátku veľkú polos ($\sim 0{,}05\,\mathrm{au}$) je vysoko pravdepodobné, že planéta má viazanú rotáciu, takže jej privrátená strana ku hviezde je horúca a odvrátená strana je chladná. Väčšina žiarivého výkonu planéty preto pochádza z privrátenej pologule.

<ol type="a" start="4">

<li>

Opäť použijeme vzorec pre pomery hmotností a rýchlostí

</li>

</ol>

$$
\frac{v_0}{v_\textrm{p}}=\frac{m}{M} \, . \tag{12}
$$

 Kruhová rýchlosť planéty je 

$$
v_\textrm{p}^2=\frac{GM}{a} \, . \tag{13}
$$

 Planéta sa pohybuje rýchlejšie keď sa nachádza bližšie ku hviezde, kvôli tomu má vyššiu rýchlosť aj hviezda. Pri výpočte preto uvažujeme planétu na vnútornom okraji obývateľnej zóny s teplotou $T_\textrm{p}=373\,\mathrm{K}$. Vzťah medzi teplotou planéty a luminozitou hviezdy poznáme z časti (c), pričom uvažujeme $A=0$ 

$$
\frac{L}{16\pi \sigma a^2}= T_\textrm{p}^4 \, . \tag{14}
$$

 V zadaní máme ešte napísaný vzťah medzi luminozitou a hmotnosťou hviezdy 

$$
L=\frac{M^4}{M_{\Sun}^4}L_{\Sun} \, . \tag{15}
$$

 Tieto štyri rovnice skombinujeme a vyjadríme hmotnosť hviezdy $M$ 

$$
a^2=\frac{G^2M^2}{v_\textrm{p}^4} \, , \tag{16}
$$

 

$$
v_\textrm{p}^4=\frac{M^4}{m^4}v_0^4 \, , \tag{17}
$$

 

$$
a^2=\frac{G^2M^2}{M^4v_0^4}m^4=\frac{G^2m^4}{M^2v_0^4} \, , \tag{18}
$$

 

$$
T_\textrm{p}^4=\frac{M^4L_{\Sun}}{16\pi \sigma M_{\Sun}^4}\frac{M^2v_0^4}{G^2m^4} \, , \tag{19}
$$

 

$$
M^6=\frac{16\pi \sigma G^2 M_{\Sun}^4m^4T_p^4}{L_{\Sun}v_0^4} \, , \tag{20}
$$

 

$$
M=\sqrt[6]{\frac{16\pi \sigma G^2}{L_{\Sun}}}\left(\frac{M_{\Sun}mT_\textrm{p}}{v_0}\right)^{\frac{2}{3}} \, , \tag{21}
$$

 

$$
M=\sqrt[6]{\frac{16\pi \cdot5{,}67 \cdot 10^{-8}\cdot (6{,}67 \cdot 10^{-11})^2}{3{,}826 \cdot 10^{26}}}\left(\frac{1{,}9891 \cdot 10^{30}\cdot5{,}9736 \cdot 10^{24}\cdot373}{13}\right)^{\frac{2}{3}} \, , \tag{22}
$$

 

$$
M=0{,}044\,\mathit{M}_\Sun \, . \tag{23}
$$

 Najmenej hmotné hviezdy majú hmotnosť okolo $0{,}08\,\mathit{M}_\Sun$. Na detekciu exoplanéty podobnej Zemi v uvedených podmienkach rozlišovacia schopnosť spektrografu ELODIE nestačí. Dnešné spektrografy už dosahujú ešte väčšiu presnosť v určení radiálnych rýchlostí, na úrovni desiatok cm.s$^{-1}$.

</details>
