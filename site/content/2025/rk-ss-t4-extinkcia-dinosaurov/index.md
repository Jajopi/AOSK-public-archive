---
title: Extinkcia dinosaurov
year: 2025
round: RK
roundName: Regionálne kolo
category: SŠ
type: teoria
typeName: Teória
label: T4
weight: 4004
points: '60'
authors:
- Martin Okánik
hasSolution: true
source: 2025:2-RK/1-SS/04-Extinkcia-dinosaurov-1/00-zadanie.tex
years:
- '2025'
rounds:
- Regionálne kolo
categories:
- SŠ
types:
- Teória
topics:
- Nezaradené
---

## Zadanie

<figure>

<div class="fig-images"><img class="invert" src="dinosaurus.png" alt="obrázok" loading="lazy" style="width:50%"></div>

<figcaption>

**Obrázok 1:** Rekonštrukcia dinosaura z rodu *theropoda*.
</figcaption>

</figure>

V tejto úlohe ide o život dinosaurovi (obr. 1), pretože na konci druhohôr sa so Zemou zrazil mohutný asteroid. V dôsledku tejto dramatickej kolízie vyhynuli takmer všetky suchozemské živočíchy väčšie ako corgi. Aj tento rok nastáva výročie tejto pohnutej vesmírnej udalosti, tak si ju dôstojne pripomeňme aspoň v tomto príklade.

Uvažujte, že sférický asteroid s priemerom $D = 10\,\mathrm{km}$ z približne rovnakého materiálu ako Zem bol pred priblížením k Zemi na parabolickej dráhe okolo Slnka a so Zemou sa zrazil v smere kolmom na jej vektor rýchlosti okolo Slnka. Uvažujte, že v dôsledku nárazu sa všetka jeho kinetická energia premenila na teplo.

<ol type="a">

<li>

<span class="body">[20 b]</span> Vypočítajte približnú hodnotu uvoľneného tepla.

</li>

</ol>

Nesmierne veľké množstvo uvoľneného tepla spôsobilo celosvetové lesné požiare. Podľa vedcov sa do atmosféry uvoľnilo asi $3 \cdot 10^{13}\,\mathrm{kg}$ uhlíka v podobe sadzí. Uvažujte, že sa častice v atmosfére rozprestreli homogénne nad povrchom až do výšky $20\,\mathrm{km}$. Ďalej predpokladajte, že častice sadzí sú guľové a majú fyzický polomer $3000\,\mathrm{nm}$, a že ich efektívny polomer pre interakciu so žiarením je rovnaký ako fyzický polomer. Hustota sadze je $2\,\mathrm{g}\,{\mathrm{cm}}^{-3}$.

<ol type="a" start="2">

<li>

<span class="body">[30 b]</span> Aká časť slnečného žiarenia prejde vrstvou sadzí bez narušenia až na povrch Zeme? Vyjadrite percentuálne a aj pomocou novej zdanlivej magnitúdy Slnka. Ak je spodný limit na fotosyntézu približne $1\,\%$ obvykle dopadajúceho žiarenia, prežije vegetácia a s ňou celý ekosystém (obr. 1) túto udalosť?

</li>

<li>

<span class="body">[10 b]</span> Ak by boli všetky častice sadzí väčšie/menšie, ako by sa zmenil výsledok, ak všetky ostatné parametre zostanú rovnaké? Nie sú potrebné podrobné výpočty, stačí intuitívna, logická argumentácia. Túto úlohu viete vyriešiť úvahou, aj ak ste nespravili (b).

</li>

</ol>

***Pomôcka:***

(najmä k časti (b))\
Pre útlm toku žiarenia $F$ v dôsledku jeho rozptylu v opticky hustom prostredí pozdĺž osi $x$ platí klesajúci exponenciálny vzťah 

$$
F(x) = F_0 e^{-n S_{eff} \, x} \,, \tag{1}
$$

 kde $S_{eff}$ je efektívny prierez častice pre interakciu so žiarením \[${\mathrm{m}}^{2}$\], $n$ je objemová koncentrácia častíc \[${\mathrm{m}}^{-3}$\], $F_0$ je tok žiarenia \[$\mathrm{W}\,{\mathrm{m}}^{-2}$\] pred vstupom do opticky hustého prostredia. Táto rovnica sa nazýva aj Lambertov-Beerov zákon.

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Keďže zrážka je uvedená ako kolmá na rýchlosť Zeme, rýchlosť Zeme do výpočtu nijako nevstupuje a kinetickú energiu $K$ premenú na teplo vypočítame iba z rýchlosti asteroidu $v$.

Rýchlosť asteroidu je daná skladaním gravitačných polí Zeme ($M = M_\Ze$, $r = R_\Ze$) a Slnka ($M = M_\Sun$, $r = a_{\Ze} =$ $1\,\mathrm{au}$). V zadaní sa píše, že kým sa asteroid nedostal blízko k Zemi, bol na parabolickej dráhe okolo Slnka. To znamená že v ”nekonečne” vzhľadom na Zem aj Slnko bol v pokoji, a kinetickú energiu $K$ získal presunutím sa hlbšie do gravitačného poľa Zeme a Slnka. Platí teda 

$$
K = \frac{1}{2} m v^2 = \frac{G M_\Sun m}{a_{\Ze}} + \frac{G M_\Ze m}{R_{\Ze}} \,, \tag{2}
$$

kde $m$ je hmotnosť asteroidu, $M_\Sun$ hmotnosť Slnka, $M_\Ea$ hmotnosť Zeme a $G$ gravitačná konštanta. Pre výpočet hmotnosti asteroidu $m$ využijeme informáciu, že je z podobného materiálu ako Zem, čiže 

$$
m = M_{\Ze} \left(\frac{D}{2R_{\Ze}}\right)^3 , \tag{3}
$$

 odkiaľ kinetická energia 

$$
\begin{align*}
        K &= G \left(\frac{M_\Sun}{a_{\Ze}} + \frac{M_\Ze}{R_{\Ze}}\right)M_{\Ze} \left(\frac{D}{2R_{\Ze}}\right)^3\,. \tag{4}\end{align*}
$$

Táto energia sa následne premení na teplo. Numericky vychádza teplo 

$$
\Delta Q = K \approx 2{,}73 \cdot 10^{24}\,\mathrm{J} \,. \tag{5}
$$

</li>

<li>

Využijeme Lambertov-Beerov zákon uvedený v pomôcke, 

$$
F(x) = F_0 e^{-n S_{eff} x}. \tag{6}
$$

 Kľúčová je interpretácia osi $x$, ktorá udáva smer šírenia žiarenia v prostredí. V zadaní sa píše, že sadza rovnomerne pokryje spodných $20\,\mathrm{km}$ atmosféry. Preto hladina $20\,\mathrm{km}$ v atmosfére zodpovedá $x = 0$ a zemský povrch zodpovedá $x = H =$ $20\,\mathrm{km}$. Pomer prepusteného žiarenia $T$ vyplýva jednoducho ako 

$$
T = \frac{F(x=H)}{F_0(x=0)} =  e^{-n S_{eff} H} \,. \tag{7}
$$

$S_{eff}$ je kolmý prierez sférických častíc sadze s polomerom $r_s = 3000\,\mathrm{nm}$, čiže kruhová plocha s obsahom $S_{eff} = \pi r_s^2 \approx 2{,}83 \cdot 10^{-11}\,{\mathrm{m}}^{2}$.

Koncentráciu častíc sadze $n$ vypočítame zo znalosti celkovej hmoty sadze $M$ uvoľnenej do atmosféry, hmotnosti jednej častice sadze $m_1$, a objemu vrstvy v atmosfére zaplnenej časticami. Prvé dve veličiny nám udávajú celkový počet častíc sadze $N$, 

$$
N = \frac{M}{m_1} = \frac{3M}{4 \pi r_s^3 \rho_s} \,. \tag{8}
$$

Objem atmosférickej vrstvy $V$ vypočítame ako objem medzigulia medzi povrchom a atmosférickou hladinou $20\,\mathrm{km}$.

$$
V = \frac{4}{3} \pi ((R_\Ze+H)^3 - R_\Ze^3) \approx 4\pi R_\Ze^2 H \,. \tag{9}
$$

Tu sme využili zjednodušenie ”spodný povrch krát výška” (platné pri $H\ll R_\Ze$) na výpočet objemu, prvá formulácia bola presná, obe sú pre potreby príkladu správne. Vzťah medzi dvoma formuláciami je jasný z rozvinutia výrazu $(R_\Ze+H)^3$.

Spojac znalosť $N$ a $V$, koncentrácia $n$ častíc sadze je 

$$
n = \frac{N}{V} = \frac{3M}{16\pi^2 R_\Ze^2 H  \rho_s r_s^3} \approx  1{,}30 \cdot 10^{7}\,{\mathrm{m}}^{-3} \,. \tag{10}
$$

Bezrozmerná veličina $\tau \equiv n S_{eff} H$ v exponenciále je známa ako optická hĺbka. Dosadením 

$$
\begin{align*}
    \tau &= n S_{eff} H \tag{11}\\
    &= \frac{3M}{16\pi^2 R_\Ze^2 H  \rho_s r_s^3} \cdot \pi r_s^2 \cdot H \tag{12}\\
    &= \frac{3M}{16\pi R_\Ze^2  \rho_s r_s} \tag{13}\\
    &\approx 7,34 \,. \tag{14}\end{align*}
$$

Z toho vyplýva pomer priamo prepusteného žiarenia 

$$
T = e^{-\tau} \approx 6{,}52 \cdot 10^{-4} \,, \tag{15}
$$

 čo je výrazne menej ako $1\,\%$ potrebných na prežitie vegetácie. Tu však treba poznamenať, že čo sme vypočítali je iba útlm priameho (nerozptýleného) svetla, to nutne neznamená že osvetlenie na povrchu je takéto nízke. Časť z rozptýleného žiarenia sa na Zem tak či tak dostane, len časť je v atmosfére napokon pohltená alebo odrazená naspäť do vesmíru. Bez hlbších znalostí elektromagnetickej interakcie medzi časticami a svetlom nemožno viac usúdiť.

Nová magnitúda Slnka je 

$$
m_\Sun' = m_\Sun - 2,5\log_{10}\left(e^{-\tau}\right) = m_\Sun + (2,5\log_{10} e)\cdot \tau \approx m_\Sun + 1,086 \cdot \tau \,, \tag{16}
$$

 po dosadení bežnej zdanlivej magnitúdy Slnka $m_\Sun \approx -26,74$ dostávame $m_\Sun' \approx -18,77$. Toto je niekde medzi bežným Slnkom a Mesiacom v splne. Ako zaujímavosť sme zdôraznili fakt, že magnitúda zdroja po extinkcii je lineárne závislá na optickej hĺbke, čo by nemalo byť prekvapením, keďže obe závisia exponenciálne na intenzite žiarenia.

**Poznámky k optickej hĺbke**\
Hodnota $\tau$ vychádza väčia ako 1, čo znamená, že sa jedná o opticky husté prostredie. Inými slovami, súčet všetkých tieniacich plôch v stĺpci vzduchu s podstavou $1\,{\mathrm{m}}^{2}$ je viac ako $1\,{\mathrm{m}}^{2}$, a to že vôbec nejaké žiarenie prenikne až na Zem je tým, že častice sú náhodne rozmiestnené, viacero zorných lúčov prechádza cez viac než jednu časticu, a teda niekde zostáva ”diera”. Tento fenomén je zachytený práve klesajúcou exponenciálnou funkciou. V limite $\tau\rightarrow\infty$ sa celkový tieniaci povrch častíc blíži k nekonečnu, a zakrytý pomer oblohy sa blíži k 1.

Tiež si všimnite že v rovnici pre $\tau$ hĺbka vrstvy $H$ nevystupuje, keďže projekcia na povrch Zeme všetkých tieniacich častíc nezávisí na výške, iba na ich množstve a veľkosti.

</li>

<li>

Optická hĺbka $\tau$ závisí nepriamo úmerne na polomere častíc $r_s$, takže menšie častice zakryjú väčšiu časť oblohy ako väčšie častice. Toto nie je až také prekvapivé, keďže pomer povrch/objem sférických častíc je 

$$
\frac{4\pi r^2}{\frac{4}{3}\pi r^3} \sim \frac{1}{r} \,. \tag{17}
$$

Ak jednu guľu rozdelíme na 8 gúľ s polovičným polomerom, povrch každej z nich bude štvrtinový, a celkový povrch bude dvojnásobný. Ekvivalentne, v rovnici $\tau = nSx$ bude $n$ osemnásobné, $S$ štvrtinové, takže optická hĺbka bude dvojnásobná. Pre opticky tenké prostredie $\tau \ll 1$ sa $e^{-\tau}$ dá aproximovať lineárnym vzťahom (vzájomný prekryv tieniacich častíc je zanedbateľný), dvojnásobná plocha by teda znamenala aj dvojnásobné tienenie. Pre opticky husté prostredie $\tau\gtrsim 1$ je dvojnásobný nárast tieniacej plochy zmiernený zvýšeným vzájomným prekryvom tieniacich plôch, a nový podiel zatieneného žiarenia bude v rozmedzí jedna až dvojnásobku pôvodného.

</li>

</ol>

</details>
