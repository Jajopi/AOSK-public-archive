---
title: Slapové pôsobenie Mesiaca
year: 2008
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
- '2008'
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

Slapové pôsobenie Mesiaca na Zem zapríčinilo spomalenie zemskej rotácie a tým zníženie rotačného uhlového momentu Zeme. Toto zníženie sa nahradilo zvýšením dráhového uhlového momentu Mesiaca okolo Zeme. Dĺžka pozemského dňa v dôsledku tohto vplyvu vzrástla za posledných 3800 rokov o $0{,}1\,\mathrm{s}$. Vypočítajte, o koľko ďalej od Zeme je Mesiac dnes ako bol pred 3800 rokmi. Použite moment zotrvačnosti okolo rotačnej osi $I_\mathrm{Z} = 0{,}33\,\mathit{M}_\Earth\,{\mathit{R}_\Earth}^{2}$.

<details class="solution">
<summary>Riešenie</summary>

Celková zmena momentu hybnosti sústavy Zem-Mesiac je nulová 

$$
\Delta L_\Ea + \Delta L_\Mo =0 \tag{1}
$$

 Rotačný moment hybnosti Zeme v súčasnosti je 

$$
L_{\Ea2}=I_\Ea \omega_{\Ea2}=I_\Ea\frac{2\pi}{T} \tag{2}
$$

 $T$ je dĺžka trvania dňa na Zemi a $\omega_{\Ea2}$ je uhlová rýchlosť rotácie Zeme. Moment hybnosti Zeme pred 3800 rokmi bol 

$$
L_{\Ea1}=I_\Ea \omega_{\Ea1}=I_\Ea\frac{2\pi}{T-\Delta T} \tag{3}
$$

 Moment hybnosti Zeme sa zmenil o hodnotu 

$$
\Delta L_\Ea=L_{\Ea2}-L_{\Ea1} =2\pi I_\Ea\left(\frac{1}{T}-\frac{1}{T-\Delta T}\right)=2\pi I_\Ea \frac{-\Delta T}{T(T-\Delta T)} \tag{4}
$$

 Keďže relatívna zmena dĺžky dňa je veľmi malá, $\Delta T \ll T$, približne platí 

$$
\Delta L_\Ea \approx \frac{-2\pi I_\Ea \Delta T}{T^2}=\frac{-2\pi \cdot0,33 M_\Ea R_\Ea^2 \Delta T}{T^2} \tag{5}
$$

 Orbitálny moment hybnosti Mesiaca v súčasnosti a v minulosti je 

$$
L_{\Mo2}= M_\Mo a_\Mo v_\Mo = M_\Mo a_\Mo \sqrt{\frac{GM_\Ea}{a_\Mo}}=M_\Mo \sqrt{GM_\Ea a_\Mo} \tag{6}
$$

 

$$
L_{\Mo1}=M_\Mo \sqrt{GM_\Ea (a_\Mo-\Delta a_\Mo)} \tag{7}
$$

 Moment hybnosti Mesiaca sa zmenil o 

$$
\Delta L_\Mo=L_{\Mo2}-L_{\Mo1} =M_\Mo \sqrt{GM_\Ea}(\sqrt{a_\Mo}-\sqrt{a_\Mo-\Delta a_\Mo}) \tag{8}
$$

 

$$
\Delta L_\Mo=M_\Mo \sqrt{GM_\Ea }\left(\sqrt{a_\Mo}-\sqrt{a_\Mo}\sqrt{\frac{a_\Mo-\Delta a_\Mo}{a_\Mo}}\right) \tag{9}
$$

 Relatívna zmena vzdialenosti Mesiaca od Zeme bude tiež malá, $\Delta a_\Mo \ll a_\Mo$, využijeme preto približný vzťah, ktorý platí pre $x \ll 1$ 

$$
(1+x)^n\approx 1+nx \tag{10}
$$

 Dostaneme približnú hodnotu zmenu momentu hybnosti Mesiaca 

$$
\Delta L_\Mo \approx M_\Mo \sqrt{GM_\Ea a_\Mo}\left[1-\left(1-\frac{1}{2}\frac{\Delta a_\Mo}{a_\Mo}\right)\right]=M_\Mo \sqrt{GM_\Ea a_\Mo}\frac{1}{2}\frac{\Delta a_\Mo}{a_\Mo} \tag{11}
$$

 Porovnaním zmien momentu hybnosti dostaneme vzťah pre zmenu vzdialenosti Mesiaca od Zeme 

$$
\Delta L_\Mo = -\Delta L_\Ea \tag{12}
$$

 

$$
\frac{-2\pi \cdot0,33 M_\Ea R_\Ea^2 \Delta T}{T^2}= \frac{1}{2} M_\Mo \sqrt{\frac{GM_\Ea}{a_\Mo}}\Delta a_\Mo \tag{13}
$$

 

$$
\Delta a_\Mo = \frac{4\pi\cdot0,33 R_\Ea^2 \Delta T \sqrt{M_\Ea a_\Mo}}{\sqrt{G}M_\Mo T^2} \tag{14}
$$

 

$$
\Delta a_\Mo = \frac{4\pi\cdot0,33 \cdot (6{,}378 \cdot 10^{6})^2 \cdot 0,1 \cdot \sqrt{5{,}9736 \cdot 10^{24} \cdot 3{,}844 \cdot 10^{8}}}{\sqrt{6{,}673 \cdot 10^{-11}}\cdot7{,}4377 \cdot 10^{22} \cdot 86400^2} \tag{15}
$$

 

$$
\Delta a_\Mo = 178\,\mathrm{m} \tag{16}
$$

</details>
