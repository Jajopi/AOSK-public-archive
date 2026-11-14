---
title: Ďalekohľad
year: 2020
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú4
weight: 2304
hasSolution: true
source: ZAO:I_Zadania/05_OptikDek/05_SS_FI.tex
rocniky:
- '2020'
kola:
- Celoštátne kolo
kategorie:
- SŠ
typy:
- Teória
tagy:
- Optika a detektory
collection: ZAO
---

## Zadanie

Do reflektora s priemerom primárneho zrkadla $150\,\mathrm{mm}$ a svetelnosťou $f/5$ umiestnime okulár s ohniskovou vzdialenosťou $10\,\mathrm{mm}$. Aké zväčšenie má daná konfigurácia?\
Hviezda Vega (18$^{\rm{h}}$ 36$^{\rm{m}}$, $+38^{\circ}\,47'$) prešla po vypnutí hodinového stroja priemerom zorného poľa okuláru za 190 sekúnd. Určte AFOV, tj. uhlový priemer zdanlivého zorného poľa (ide o charakteristiku okuláru danú jeho konštrukciou). Okulár vymeníme za CCD čip s rozmermi\
$35{,}8 \times 23{,}9\,\mathrm{mm}$, ktorý má 12,8 Mpx. Aký veľký obraz (priemer v px) Jupitera uvidíme na obrázku, ak má Jupiter uhlový priemer $45''$?

<details class="solution">
<summary>Riešenie</summary>

Ohnisková vzdialenosť objektívu je $f=5D=5\cdot15=75\,\mathrm{cm}$. Zväčšenie ďalekohľadu je 

$$
\Gamma=\frac{f}{f_\textrm{ok}}=\frac{75}{1}=75 \, . \tag{1}
$$

 Za $190\,\mathrm{s}$ sa hodinový uhol Vegy zmení o 

$$
\Delta t=\frac{190}{86400}\cdot360^{\circ}=0{,}79^{\circ}=0^{\circ}\,47'\,30'' \, . \tag{2}
$$

 Vega sa nenachádza na rovníku, preto na oblohe prejde v skutočnosti o niečo menší uhol, ten je zároveň zorným poľom ďalekohľadu 

$$
\rm AFOV = \Delta t \cos (\delta_V)=0^{\circ}\,47'\,30''\cdot \cos (38^{\circ}\,47')=37' \, . \tag{3}
$$

 Uhol $\vartheta_{\Ju}=45''$ sa na čipe zobrazí na dĺžku 

$$
x=f\theta_{\Ju}=750\cdot\frac{45}{206265}=0{,}164\,\mathrm{mm} \, . \tag{4}
$$

 Počet pixelov, ktorý pripadá na $1\,\mathrm{mm}$ je 

$$
\frac{12{,}8 \cdot 10^{6}}{35,8}=357\,542 \, . \tag{5}
$$

 Priemer obrazu Jupitera v px je 

$$
0,164\cdot 357\,542=58\,637 \, . \tag{6}
$$

</details>
