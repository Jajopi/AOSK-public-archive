---
title: Slnečné neutrína
year: 2018
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú1
weight: 2301
hasSolution: true
source: ZAO:I_Zadania/08_Rozsiahle/08_SS_FI.tex
rocniky:
- '2018'
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

Neutrínová astronómia je jedným z mladých oborov astronómie, umožňuje vedcom nahliadnuť hlboko do slnečného vnútra. Tu elektrónové neutrína $\rm{\nu_e}$ - slabo interagujúce ľahké častice - vznikajú v rámci p-p cyklu: 

$$
4\rm{p}\rightarrow ^4\rm{He} + 2\rm{e}^+ +2\rm{\nu_e} + 4{,}28 \cdot 10^{-12}\,\mathrm{J} \, .
$$

 Na Zemi boli postavené veľké detektory na ich skúmanie. Modelujme náš detektor ako valec s rozmermi $R=20\,\mathrm{m}$ a $h=40\,\mathrm{m}$. Je celkom naplnený vodou a po obvode má tisícky fotonásobičov, ktoré číhajú na slabé záblesky pochádzajúce z reakcie neutrín s látkou. Účinný prierez pre túto interakciu (t.j. plocha pod akou vidí prichádzajúce neutríno cieľové častice - uvažujte molekuly vody) je pritom len asi $\sigma=10^{-47}\,{\mathrm{m}}^{2}$.

<ol type="a">

<li>

Ak je slnečná konštanta $S=1366\,\mathrm{W}\,{\mathrm{m}}^{-2}$, skúste odhadnúť, koľko neutrín by mohol detektor zachytiť počas jedného roka.

</li>

</ol>

V skutočnosti je toto číslo o niekoľko rádov nižšie než vyplýva z a), keďže len malá časť neutrín dosiahne energiu potrebnú na túto špecifickú reakciu s látkou v detektore. Aj po vykonaní všetkých potrebných teoretických opráv však vedci zistili, že stále detegujú iba $y=40\,\%$ v porovnaní s teóriami postavenými na štandardnom modeli Slnka. Vyzeralo to už, že sa slneční astronómovia mýlili v svojich modeloch štruktúry vnútra našej hviezdy. Podľa hypotézy neutrínových oscilácií však existujú tri druhy neutrín, ktoré sa môžu na seba vzájomne dosť čudným spôsobom premieňať: elektrónové ($\rm{\nu_e}$) a miónové, tauónové (spoločne značené $\rm{\nu_x}$). Premena časti $\rm{\nu_e}$ na iné druhy $\rm{\nu_x}$ by mohla vysvetliť nezrovnalosti v pozorovaných počtoch netrín.

<ol type="a" start="2">

<li>

Za predpokladu, že detektor má účinnosť pre $\rm{\nu_x}$ iba $1/7$ z tej pre $\rm{\nu_e}$, vypočítajte, aký relatívny pomer $q$ častíc $\rm{\nu_e}$ sa cestou zo Slnka na Zem muselo premeniť z $\rm{\nu_e}$ na $\rm{\nu_x}$, $0<q<1$.

</li>

</ol>

Dodatočné informácie: Uvažujte, že všetka energia zo Slnka pochádza z p-p cyklu a tiež, že všetky neutrína pochádzajú zo Slnka. Hmotnosť molekuly vody je $m_\mathrm{H_2O}=3{,}00 \cdot 10^{-26}\,\mathrm{kg}$, hustota vody je štandardných $1000\,\mathrm{kg}\,{\mathrm{m}}^{-3}$.

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Pri každom p-p cykle vzniknú 2 neutrína. Počet neutrín, ktoré v Slnku vzniknú za $1\,\mathrm{s}$ je

</li>

</ol>

$$
\frac{\Delta N_{\nu}}{\Delta t}=\frac{2L_{\Sun}}{E_\textrm{pp}} \, . \tag{1}
$$

 Tok neutrín na Zem, teda počet neutrín, ktoré dopadnú na meter štvorcový za sekundu, je 

$$
S_{\nu}=\frac{2S}{E_\textrm{pp}} \, . \tag{2}
$$

 Počet molekúl vody v detektore je 

$$
N_{\textrm{H}_2\textrm{O}}=\frac{\pi R^2 h\rho_{\textrm{H}_2\textrm{O}}}{m_{\textrm{H}_2\textrm{O}}} \, . \tag{3}
$$

 Každá z týchto molekúl môže zachytiť neutríno, pričom účinný prierez reakcie je $\sigma$. Detektor má tak celkovú efektívnu plochu 

$$
A=N_{\textrm{H}_2\textrm{O}}\sigma \, . \tag{4}
$$

 Počet neutrín, ktoré detektor zachytí za rok je 

$$
\begin{gathered}
N_{\nu}=S_{\nu}At=\frac{2S}{E_\textrm{pp}}\frac{\pi R^2 h\rho_{\textrm{H}_2\textrm{O}}}{m_{\textrm{H}_2\textrm{O}}}\sigma t=\frac{2\cdot1366}{4{,}28 \cdot 10^{-12}}\frac{\pi \cdot20^2 \cdot 40 \cdot 1000}{3 \cdot 10^{-26}}\cdot10^{-47} \cdot 365,25 \cdot 86400 =\\=3{,}36 \cdot 10^{8} \, . \end{gathered}\tag{5}
$$

<ol type="a" start="2">

<li>

Účinnosť detektora pre elektrónové neutrína si označíme $\eta_\textrm{e}$, účinnosť pre ostatné neutrína je $\eta_\textrm{x}=\frac{1}{7}\eta_\textrm{e}$. Pôvodný počet elektrónových neutrín vyprodukovaných v Slnku si označíme $N_\textrm{e}$. Počet elektrónových neutrín, ktoré dopadnú na detektor je $(1-q)N_\textrm{e}$, počet ostatných neutrín je $N_\textrm{x}=qN_\textrm{e}$. Ak by sa elektrónové neutrína nemenili na miónové a tauónové, detektor by zachytil $\eta_\textrm{e}N_\textrm{e}$ neutrín. V experimentoch ale detektory zachytávajú iba $40\%$ z nich, teda $0,4\eta_\textrm{e}N_\textrm{e}$. Zo všetkých týchto úvah vyplýva, že pre počet zachytených neutrín detektorom platí

</li>

</ol>

$$
0,4\eta_\textrm{e}N_\textrm{e}=\eta_\textrm{e}(1-q)N_\textrm{e}+\frac{1}{7}\eta_\textrm{e} N_\textrm{x}=\eta_\textrm{e}(1-q)N_\textrm{e}+\frac{1}{7}\eta_\textrm{e} q N_\textrm{e} \, . \tag{6}
$$

 Účinnosť a počet neutrín sa nám skrátia a rovnica sa zjednoduší na 

$$
0,4=1-q+\frac{1}{7}q \, , \tag{7}
$$

 

$$
\frac{6}{7}q=0,6 \, . \tag{8}
$$

 Dostávame $q=0,7$.

</details>
