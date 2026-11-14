---
title: Sírius
year: 2018
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú3
weight: 2303
hasSolution: true
source: ZAO:I_Zadania/04_FotoSpek/04_SS_FI.tex
rocniky:
- '2018'
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

Sírius je dvojhviezda. Slabšia zložka, Sírius B má zdanlivú vizuálnu magnitúdu $m_\textrm{V}=8{,}44\,\mathrm{mag}$.

<ol type="a">

<li>

Ak je vzdialenosť Síria $2{,}64\,\mathrm{pc}$, vypočítajte absolútnu vizuálnu magnitúdu Síria B. Medzihviezdnu absorpciu zanedbajte.

</li>

<li>

Spektrálne rozloženie energie ukazuje, že Sírius B má efektívnu teplotu $25\,200\,\mathrm{K}$. Bolometrická korekcia pre túto teplotu je $BC=-2{,}73\,\mathrm{mag}$. Ak pre Slnko je $BC=-0{,}1\,\mathrm{mag}$, vypočítajte absolútnu bolometrickú magnitúdu $M_\textrm{bol}$ Síria B.

</li>

<li>

Vypočítajte svietivosť a polomer Síria B.

</li>

<li>

Ak je hmotnosť Síria B $1{,}018\,\mathit{M}_\Sun$, vypočítajte aj strednú hustotu tohto bieleho trpaslíka.

</li>

</ol>

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

$$
M_\textrm{V}=m_\textrm{V}+5-5\log r = 8,44+5-5\log (2,64)=11{,}33\,\mathrm{mag} \, . \tag{1}
$$

</li>

<li>

$$
M_\textrm{bol}=M_\textrm{V}+BC=11,33-2,73=8{,}6\,\mathrm{mag} \, . \tag{2}
$$

</li>

<li>

$$
M_{\textrm{bol,}\Sun}-M_\textrm{bol}=2,5\log \left(\frac{L}{L_{\Sun}}\right) \, , \tag{3}
$$

 

$$
M_{\textrm{bol,}\Sun}=M_{\textrm{V,}\Sun}+BC_{\Sun} \, , \tag{4}
$$

 

$$
L=2,512^{M_{\textrm{V,}\Sun}+BC_{\Sun}-M_\textrm{bol}}L_{\Sun}=2,512^{4,82-0,1-8,6}\cdot3{,}826 \cdot 10^{26}=1{,}07 \cdot 10^{25}\,\mathrm{W} \, , \tag{5}
$$

 

$$
R=\sqrt{\frac{L}{4\pi \sigma T^4}}=\sqrt{\frac{1{,}07 \cdot 10^{25}}{4\pi\cdot5{,}67 \cdot 10^{-8}25\,200^4}}=6{,}1 \cdot 10^{6}\,\mathrm{m}=6100\,\mathrm{km} \, . \tag{6}
$$

</li>

<li>

$$
M=\frac{4}{3}\pi \rho R^3 \, , \tag{7}
$$

 

$$
\rho=\frac{3M}{4\pi R^3}=\frac{3\cdot1,018\cdot1{,}9891 \cdot 10^{30}}{4\pi \cdot (6{,}1 \cdot 10^{6})^3}=2{,}13 \cdot 10^{9}\,\mathrm{kg}\,{\mathrm{m}}^{-3} \, . \tag{8}
$$

</li>

</ol>

</details>
