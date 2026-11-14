---
title: Hviezdna evolúcia
year: 2025
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: T4
weight: 2304
points: '70'
authors:
- Jana Švrčková
hasSolution: true
source: 2025:3-CK/1-SS/04-Hviezdna-evolucia/00-zadanie.tex
rocniky:
- '2025'
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

Hviezdna evolúcia sa dá rozdeliť do troch významných etáp, pričom v každej z nich dominuje určitý fyzikálny proces. Všetky tieto procesy prebiehajú na určitej charakteristickej časovej škále, ktorá nám dáva dobrý odhad toho, ako dlho trvá dané štádium života hviezdy.

Nukleárna časová škála je čas, za ktorý hviezda vyžiari všetku energiu, ktorú môže získať z jadrových reakcií. Z teoretických modelov vieme, že hviezda stihne jadrovými reakciami (premenou vodíka na hélium) spotrebovať iba $10\ \%$ vodíka predtým, ako začnú prevládať iné, rýchlejšie evolučné mechanizmy. Na energiu sa v jadrových reakciách premení len $0,7\ \%$ pokojovej hmotnosti jadier vodíka, ktoré sa zúčastnia reakcií.

<ol type="a">

<li>

<span class="body">[15 b]</span> Napíšte všeobecné vyjadrenie pre nukleárnu časovú škálu $t_n$ a vypočítajte jej číselnú hodnotu pre Slnko. Pre jednoduchosť predpokladajte, že hviezdy sa skladajú iba z vodíka.

</li>

</ol>

Termálna (Kelvinova-Helmholtzova) časová škála je čas, za ktorý by hviezda vyžiarila všetku svoju tepelnú energiu za predpokladu, že by neprebiehali žiadne jadrové reakcie. Táto škála je zároveň dobrým odhadom času, za ktorý sa žiarenie dostane z jadra hviezdy na jej povrch.

Z termodynamiky vieme, že tepelná (vnútorná) energia plynu sa rovná celkovej kinetickej energii $E_k$ častíc plynu. Predpokladajte, že hviezdy majú rovnomerne rozloženú hustotu a sú to gravitačne viazané sústavy častíc, pre ktoré platí viriálová rovnováha. Gravitačná väzbová energia takejto hviezdy je

$$
E_p = -\frac{3GM^2}{5R}\, . \tag{1}
$$

<ol type="a" start="2">

<li>

<span class="body">[20 b]</span> Napíšte všeobecné vyjadrenie pre termálnu časovú škálu $t_t$ a vypočítajte jej číselnú hodnotu pre Slnko.

</li>

</ol>

Dynamická škála je čas, za ktorý by hviezda skolabovala, ak by proti gravitácii nepôsobil gradient tlaku. Počíta sa ako čas voľného pádu častice z povrchu do stredu hviezdy.

Voľný pád z povrchu do stredu hviezdy si môžete predstaviť ako pohyb po veľmi sploštenej elipse s apocentrom na povrchu a pericentrom v strede hviezdy. Môžete predpokladať, že všetka hmotnosť je sústredená v strede hviezdy.

<ol type="a" start="3">

<li>

<span class="body">[20 b]</span> Napíšte všeobecné vyjadrenie pre dynamickú časovú škálu $t_d$ a vypočítajte jej číselnú hodnotu pre Slnko.

</li>

<li>

<span class="body">[15 b]</span> Upravte všeobecné výrazy pre všetky tri časové škály do nasledujúceho tvaru

</li>

</ol>

$$
t_x = \left(\frac{R}{R_\Sun}\right)^a\left(\frac{M}{M_\Sun}\right)^b\left(\frac{L}{L_\Sun}\right)^ct_{x\Sun} \, , \tag{2}
$$

kde $t_x$ je časová škála hviezdy, $\mathrm{x} = \{\mathrm{n, t, d}\}$, $t_{x\Sun}$ je časová škála Slnka, $R$, $M$ a $L$ sú polomer, hmotnosť a svietivosť hviezdy. Konštanty $a$, $b$ a $c$ sú pre každú časovú škálu odlišné.

<details class="solution">
<summary>Riešenie</summary>

Nukleárna škála – využijeme známy Einsteinov vzorec $E=mc^2$, aby sme vypočítali energiu, ktorú hviezda vyžiari. Jadrových reakcií sa zúčastní len $\epsilon = 10\ \%$ hmotnosti jadier vodíka vo hviezde. Z toho sa $99,3\ \%$ premení na jadrá hélia a len $\eta = 0,7\ \%$ sa premení na energiu. Celkovo sa teda na energiu v reakciách premení iba nasledujúca hmotnosť 

$$
m = \epsilon\eta M \, . \tag{3}
$$

Hviezda so svietivosťou $L$ vyžiari túto energiu za čas 

$$
t_n = \frac{\epsilon\eta Mc^2}{L} \, . \tag{4}
$$

Číselná hodnota nukleárnej škály pre Slnko je dobrým odhadom veku, ktorého by sa malo dožiť 

$$
t_{n\Sun} = \frac{\epsilon\eta M_\Sun c^2}{L_\Sun} \approx 3{,}27 \cdot 10^{17}\,\mathrm{s} \approx 10{,}4 \cdot 10^{9}\,\mathrm{rokov}\, . \tag{5}
$$

 Vydelíme vzťahy pre $t_n$ a $t_{n\Sun}$ 

$$
\frac{t_n}{t_{n\Sun}} = \frac{\epsilon\eta Mc^2}{L} \frac{L_\Sun}{\epsilon\eta M_\Sun c^2}\, , \tag{6}
$$

 

$$
\frac{t_n}{t_{n\Sun}} = \frac{M}{L} \frac{L_\Sun}{M_\Sun}\, . \tag{7}
$$

 Vzorec upravený do podoby vyžadovanej v zadaní je 

$$
t_n = \left(\frac{M}{M_\Sun}\right)\left(\frac{L}{L_\Sun}\right)^{-1}t_{n\Sun} \, . \tag{8}
$$

Termálna škála – hviezda je vo viriálovej rovnováhe, čo znamená, že kinetická energia jej častíc a gravitačná väzbová energia spĺňajú nasledujúcu rovnicu

$$
2E_K + E_p = 0\, , \tag{9}
$$

$$
E_K = -\frac{1}{2} E_p\, . \tag{10}
$$

Využijeme vzorec pre väzbovú energiu zo zadania a zistíme celkovú kinetickú, resp. tepelnú energiu hviezdy 

$$
E_K = \frac{3GM^2}{10R} \,. \tag{11}
$$

Termálna škála je potom čas, za ktorý hviezda vyžiari všetku túto energiu 

$$
t_t = \frac{E_K}{L}=\frac{3GM^2}{10RL} \,. \tag{12}
$$

 Číselná hodnota tejto škály pre Slnko je 

$$
t_{t\Sun} = \frac{3GM_\Sun^2}{10R_\Sun L_\Sun} \approx 2{,}98 \cdot 10^{14}\,\mathrm{s} \approx 9{,}43 \cdot 10^{6}\,\mathrm{rokov}\,. \tag{13}
$$

 Upravený vzorec požadovaný v zadaní dostaneme, ak vydelíme vzorec pre $t_t$ a $t_{t\Sun}$ 

$$
\frac{t_t}{t_{t\Sun}} = \frac{3GM^2}{10RL} \frac{10R_\Sun L_\Sun}{3GM_\Sun^2}\, , \tag{14}
$$

 

$$
\frac{t_t}{t_{t\Sun}} = \frac{M^2}{RL} \frac{R_\Sun L_\Sun}{M_\Sun^2}\, , \tag{15}
$$

 

$$
t_t = \left(\frac{M}{M_\Sun}\right)^2\left(\frac{R}{R_\Sun}\right)^{-1}\left(\frac{L}{L_\Sun}\right)^{-1}t_{t\Sun} \, . \tag{16}
$$

Dynamická škála – na základe nápovedy zo zadania je jasné, že na výpočet tejto škály stačí využiť 3. Keplerov zákon. V tomto prípade nám ide iba o pohyb z povrchu do stredu hviezdy, takže nás zaujíma iba polovica obežnej doby. Dĺžka elipsy sa rovná polomeru hviezdy, veľká polos je preto polovicou polomeru hviezdy $a=\frac{R}{2}$ .

$$
\frac{P^2}{a^3}=\frac{4\pi^2}{GM}\, , \tag{17}
$$

 

$$
t_d = \frac{P}{2} = \frac{1}{2}\sqrt{\frac{4\pi^2a^3}{GM}} = \sqrt{\frac{\pi^2a^3}{GM}} = \sqrt{\frac{\pi^2R^3}{8GM}} \,. \tag{18}
$$

Hodnota pre Slnko je 

$$
t_{d\Sun} = \sqrt{\frac{\pi^2R_\Sun^3}{8GM_\Sun}} \approx 1770\,\mathrm{s} \approx 29{,}5\,\mathrm{min}\,. \tag{19}
$$

Všeobecný vzťah opäť podelíme vzťahom pre Slnko a upravíme 

$$
\frac{t_d}{t_{d\Sun}}=\sqrt{\frac{\pi^2R^3}{8GM}} \sqrt{\frac{8GM_\Sun}{\pi^2R_\Sun^3}}\, , \tag{20}
$$

 

$$
\frac{t_d}{t_{d\Sun}}=\sqrt{\frac{R^3}{M}} \sqrt{\frac{M_\Sun}{R_\Sun^3}}\, , \tag{21}
$$

 

$$
t_d = \left(\frac{M}{M_\Sun}\right)^{-\frac{1}{2}}\left(\frac{R}{R_\Sun}\right)^{\frac{3}{2}}t_{d\Sun} \, . \tag{22}
$$

</details>
