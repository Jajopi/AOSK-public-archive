---
title: Úloha 2
year: 2013
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú2
weight: 2302
hasSolution: true
source: ZAO:I_Zadania/04_FotoSpek/04_SS_FI.tex
rocniky:
- '2013'
kola:
- Celoštátne kolo
kategorie:
- SŠ
typy:
- Teória
tagy:
- Fotometria a spektroskopia
collection: ZAO
---

## Zadanie

Predpokladajme, že slnečné panely družice typu IRIDIUM odrážajú všetko slnečné svetlo (t.j. ich odrazivosť je 100%) a každý má rozmer $2 \times 1\,\mathrm{m}$. Družica je od pozorovateľa vzdialená $800\,\mathrm{km}$. Aký jasný záblesk (v magnitúdach) dokáže odraz svetla Slnka od jedného panelu kolmo natočeného k pozorovateľovi vyprodukovať? Atmosféru Zeme zanedbajte.

<details class="solution">
<summary>Riešenie</summary>

Pretože družica má 100 % odrazivosť, všetko svetlo, ktoré na ňu dopadne zo Slnka odrazí k pozorovateľovi. V tom prípade pomer jasností družice aj Slnka závisí iba na pomere priestorových uhlov, pod ktorými družicu aj Slnko vidíme. Uhlové rozmery panelu sú 

$$
\alpha=\frac{2}{800 \cdot 10^{3}}\cdot206\,265=0{,}52'' \, , \tag{1}
$$

 

$$
\beta=\frac{1}{800 \cdot 10^{3}}\cdot206\,265=0{,}26'' \, . \tag{2}
$$

 Priestorový uhol, pod ktorým pozorovateľ na Zemi vidí jeden panel Irídia je $\Omega_\textrm{I}=\alpha\beta$. Uhlový polomer Slnka je 

$$
\vartheta_{\Sun}=\frac{6{,}955 \cdot 10^{8}}{1{,}496 \cdot 10^{11}}\cdot206\,265=959'' \, . \tag{3}
$$

 Priestorový uhol, pod ktorým je vidieť slnečný disk je $\Omega_{\Sun}=\pi \vartheta^2$ Magnitúdu záblesku Irídia vypočítame z Pogsonovej rovnice 

$$
m_\textrm{I}=m_{\Sun}+2,5\log \left(\frac{I_{\Sun}}{I_\textrm{I}}\right)=m_{\Sun}+2,5\log \left(\frac{\Omega_{\Sun}}{\Omega_\textrm{I}}\right) \, , \tag{4}
$$

 

$$
m_\textrm{I}=-26,72+2,5\log \left(\frac{2{,}89 \cdot 10^{6}}{0,135}\right)=-8,4 \, . \tag{5}
$$

</details>
