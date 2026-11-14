---
title: Úloha 4
year: 2013
round: DK
roundName: Domáce kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú4
weight: 3004
hasSolution: true
source: ZAO:I_Zadania/04_FotoSpek/04_SS_DK.tex
years:
- '2013'
rounds:
- Domáce kolo
categories:
- SŠ
types:
- Teória
topics:
- Fotometria a spektroskopia
collection: ZAO
---

## Zadanie

O koľko Kelvinov sa zmení teplota atmosféry hviezdy spektrálnej triedy A0 s $T = 10\,000\,\mathrm{K}$, ak sa jej absolútna bolometrická magnitúda zmenší o $0{,}5\,\mathrm{mag}$ (t.j. hviezda sa zjasní), pričom jej polomer sa nezmení?

<details class="solution">
<summary>Riešenie</summary>

Pogsonova rovnica pre absolútne bolometrické magnitúdy a žiarivé výkony je 

$$
M_1-M_2 = 2,5\log{\frac{L_2}{L_1}} \, . \tag{1}
$$

 Polomer hviezdy sa nemení, takže pomer žiarivých výkonov sa rovná pomeru štvrtých mocnín teplôt hviezdy. Po dosadení teplôt do Pogsonovej rovnice dostaneme postupnými úpravami výraz pre zmenu teploty hviezdy. 

$$
M_1-M_2 = 2,5\log{\frac{T_2^4}{T_1^4}}=2,5\log{\frac{(T_1+\Delta T)^4}{T_1^4}}=10\log{\frac{T_1+\Delta T}{T_1}} \, , \tag{2}
$$

 

$$
\frac{T_1+\Delta T}{T_1} = 1+\frac{\Delta T}{T_1} = 10^{\frac{M_1-M_2}{10}} \, , \tag{3}
$$

 

$$
\frac{\Delta T}{T_1}=10^{0,05}-1=0,122 \, , \tag{4}
$$

 

$$
\Delta T = 0,122 T_1 = 0,122\cdot10 000 = 1220\,\mathrm{K} \, . \tag{5}
$$

</details>
