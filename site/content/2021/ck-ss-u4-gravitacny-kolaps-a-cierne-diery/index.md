---
title: Gravitačný kolaps a čierne diery
year: 2021
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú4
weight: 5004
hasSolution: true
source: ZAO:I_Zadania/01_NebMech/01_SS_FI.tex
years:
- '2021'
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

V úlohách (a) – (c) uvažujte hviezdu podobnú Slnku.

<ol type="a">

<li>

Akou rýchlosťou musí letieť vesmírna loď na stabilnej kruhovej dráhe okolo hviezdy vo vzdialenosti $a = 5 \cdot 10^{7}\,\mathrm{km}$ od jej stredu? Aký veľký impulz (zmena hybnosti) a v ktorom smere treba udeliť lodi s hmotnosťou $m = 100\,\mathrm{t}$, aby sme docielili jej radiálny pád na povrch hviezdy?

</li>

<li>

Odvoďte trvanie takéhoto pádu. Najskôr odvoďte výsledok bez bezrozmerného faktora pomocou rozmerovej analýzy. Potom začnite uvažovať fyziku a odvodťe celý výsledok. Pre účely tohto výpočtu považujte hviezdu za hmotný bod v strede. Z pohybovej rovnice a Newtonových zákonov by si takýto výpočet vyžadoval zložitú matematiku. Skúste teda radšej porozmýšľať nad rôznymi limitnými prípadmi kužeľosečiek.

</li>

<li>

Na základe vyššie uvedeného rádovo odhadnite tzv. dynamickú časovú škálu (čas gravitačného kolapsu) Slnku podobnej hviezdy. Predstavujme si, že toto je zhruba čas, za aký skolabuje hviezda na čiernu dieru. Skúste vymenovať čo najviac aproximácii / nie celkom správnych predpokladov pri takomto odhade založenom na výsledku z (b).

</li>

<li>

Loď s astronautom je na orbite okolo čiernej diery so Schwarzschildovým polomerom $R_S = 1\,\mathrm{m}$. Polomer dráhy je $10^9$ metrov. Aká je obežná doba a taktiež gravitačný červený posun (meraný pozorovateľom v nekonečne)? Načrtnite závislosť červeného posunu na polomere dráhy a okomentujte jeho limitné prípady. Dáva to zmysel?

</li>

</ol>

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Kruhová rýchlosť je

</li>

</ol>

$$
v=\sqrt{\frac{GM}{a}}=\sqrt{\frac{6{,}67 \cdot 10^{-11}\cdot1{,}9891 \cdot 10^{30}}{50 \cdot 10^{9}}}=51{,}5\,\mathrm{km}\,{\mathrm{s}}^{-1} \, . \tag{1}
$$

 Na to, aby loď začala radiálne padať na hviezdu, musí impulz sily pôsobiť proti smeru jej obežného pohybu a znížiť jej rýchlosť na nulu 

$$
\Delta p = mv=100 \cdot 10^{3}\cdot51{,}5 \cdot 10^{3}=5{,}15 \cdot 10^{9}\,\mathrm{kg}\,\mathrm{m}\,{\mathrm{s}}^{-1} \, . \tag{2}
$$

<ol type="a" start="2">

<li>

Ku radiálnemu pádu dochádza kvôli pôsobeniu gravitačnej sily, trvanie pádu môže preto závisieť iba na gravitačnej konštante $G$, hmotnosti hviezdy $M$ a počiatočnej vzdialenosti lodi od hviezdy $a$. Tieto veličiny musia byť vo vzorci na výpočet času skombinované tak, aby kombinácia ich fyzikálnych jednotiek mala rozmer času (teda sekundy). Jednotky spomínaných veličín sú

</li>

</ol>

$$
[t]=1\,\mathrm{s} \, , \tag{3}
$$

 

$$
[G]=1\,{\mathrm{m}}^{3}\,{\mathrm{kg}}^{-1}\,{\mathrm{s}}^{-2} \, , \tag{4}
$$

 

$$
[M]=1\,\mathrm{kg} \, , \tag{5}
$$

 

$$
[a]=1\,\mathrm{m} \, . \tag{6}
$$

 Vzorec pre čas voľného pádu hľadáme v tvare 

$$
t=KG^{\alpha}M^{\beta}a^{\gamma} \, . \tag{7}
$$

 Pre mocniny platí nasledujúca sústava rovníc 

$$
\rm s: \ 1=-2\alpha \, , \tag{8}
$$

 

$$
\rm kg: \ 0=-\alpha+\beta \, , \tag{9}
$$

 

$$
\rm m: \ 0=3\alpha+\gamma \, . \tag{10}
$$

 Riešením sú hodnoty $\alpha=-\frac{1}{2}$, $\beta=-\frac{1}{2}$, $\gamma=\frac{3}{2}$, takže vzorec pre čas má tvar 

$$
t=K\sqrt{\frac{a^3}{GM}} \, . \tag{11}
$$

 Vzorec pre čas sa dá získať aj pomocou nasledujúcej úvahy: predstavme si priamku po ktorej teleso padá do gravitačného centra. Priamka zodpovedá extrémne sploštenej Keplerovskej elipse s veľkou polosou rovnou polovici pôvodnej vzdialenosti od centra: $a/2=25 \cdot 10^{6}\,\mathrm{km}$. Pád bude zodpovedať času prechodu z afélia do perihélia (limitne zhodného s gravitačným centrom), teda polovici štandardnej Keplerovskej periódy, $t=P/2$. 

$$
P^2=\frac{4\pi^2(a/2)^3}{GM}=\frac{4\pi^2a^3}{8GM}\ , \tag{12}
$$

 

$$
P^2=(2t)^2=4t^2 \ , \tag{13}
$$

 

$$
t=\sqrt{\frac{\pi^2a^3}{8GM}} \, . \tag{14}
$$

<ol type="a" start="3">

<li>

Dosadíme hodnoty pre Slnko

</li>

</ol>

$$
t=\sqrt{\frac{\pi^2\cdot(6{,}955 \cdot 10^{8})^3}{8\cdot6{,}67 \cdot 10^{-11}\cdot1{,}9891 \cdot 10^{30}}}=1770\,\mathrm{s}=29{,}5\,\min \, . \tag{15}
$$

 Aproximácie/nezrovnalosti:

- odvodili sme to pre pád hmotného bodu na hmotný bod, nie pre kolaps približne sféricky symetrického rozloženia hmoty v hviezde,

- v odvodení vystupuje iba gravitácia, v kolabujúcej hviezde bude proti gravitačnej sile pôsobiť tlak a spomaľovať pád (plyn, žiarenie, degenerovaný plyn),

- odvodili sme to cez Keplerove zákony/Newtonovskú mechaniku, no pri kolapse na čiernu dieru sa hviezda nutne dostane do silne relativistického režimu.

<ol type="a" start="4">

<li>

Vzorec pre gravitačný červený posun sa dá odvodiť na základe zjednodušenej (aj keď fyzikálne nesprávnej) predstavy. Využije sa pri tom zachovanie energie fotónu v mieste vyžiarenia a v nekonečne

</li>

</ol>

$$
\frac{hc}{\lambda_0}-\frac{GMm}{r}=\frac{hc}{\lambda_{\infty}} \, . \tag{16}
$$

 Namiesto hmotnosti fotónu dosadíme 

$$
m=\frac{E}{c^2}=\frac{h}{\lambda c} \, , \tag{17}
$$

 

$$
\frac{hc}{\lambda_0}-\frac{GMhc}{r\lambda_0 c^2}=\frac{hc}{\lambda_{\infty}} \, , \tag{18}
$$

 

$$
\lambda_{\infty}\left(1-\frac{GM}{rc^2}\right)=\lambda_0 \, . \tag{19}
$$

 Červený posun v nekonečne je 

$$
z=\frac{\lambda_{\infty}}{\lambda_0}-1=\frac{1}{1-\frac{GM}{rc^2}}-1=\frac{\frac{GM}{rc^2}}{1-\frac{GM}{rc^2}} \, . \tag{20}
$$

 V prípade, že je fotón vyžiarený ďaleko od čiernej diery (čo je v našom prípade splnené), je možné v menovateli zanedbať člen $\frac{GM}{rc^2}$ a dostaneme 

$$
z=\frac{GM}{rc^2} \, . \tag{21}
$$

 Hmotnosť čiernej diery s daným Schwarzschildovým polomerom je 

$$
M=\frac{R_\textrm{s}c^2}{2G}=\frac{1\cdot(2{,}9979 \cdot 10^{8})^2}{2\cdot6{,}67 \cdot 10^{-11}}=6{,}74 \cdot 10^{26}\,\mathrm{kg} \, . \tag{22}
$$

 Červený posun v nekonečne je v tomto prípade 

$$
z=\frac{6{,}67 \cdot 10^{-11}\cdot6{,}74 \cdot 10^{26}}{10^9\cdot(2{,}9979)^2}=5 \cdot 10^{-10} \, . \tag{23}
$$

 Dostali sme závislosť $z\sim\frac{1}{r}$, tá ale platí pre $\frac{GM}{rc^2}\ll 1$, čo je predpoklad, ktorý sme využili pri jej odvodení. Bližšie ku čiernej diere je závislosť $z(r)$ komplikovanejšia. Ak by bol fotón vyžiarený na horizonte, jeho červený posun v nekonečne by bol $z=\infty$. Graf závislosti $z$ na $r$ teda nebude obyčajná hyperbola, ale bude to klesajúca funkcia, ktorá v $r=R_\textrm{s}$ diverguje a pre veľké $r$ sa bude správať ako klasická hyperbola.

</details>
