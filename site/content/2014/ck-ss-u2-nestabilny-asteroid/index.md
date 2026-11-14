---
title: Nestabilný asteroid
year: 2014
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú2
weight: 5002
hasSolution: true
source: ZAO:I_Zadania/04_FotoSpek/04_SS_FI.tex
years:
- '2014'
rounds:
- Celoštátne kolo
categories:
- SŠ
types:
- Teória
topics:
- Fotometria a spektroskopia
collection: ZAO
---

## Zadanie

Do nestabilného asteroidu približne guľového tvaru s priemerom $1\,\mathrm{km}$ narazil veľkou rýchlosťou meteoroid, podstatne menší ako asteroid. Po náraze sa asteroid rozpadol na trosky, ktoré sa vzápätí spojili do štyroch menších častí, približne rovnakého tvaru a veľkosti, ktoré sa pomaly od seba vzďaľujú. Vypočítajte, o koľko sa zmení jasnosť asteroidu tesne po svojom rozpade.

<details class="solution">
<summary>Riešenie</summary>

Pri výpočte použijeme niekoľko predpokladov: pôvodný asteroid aj štyri nové útvary majú guľový tvar, rovnakú hustotu a rovnakú odrazivosť a po zrážke sa všetok materiál z pôvodného asteroidu zoskupil do štyroch nových a nič neuniklo preč. V tom prípade zo zachovania hmotnosti dostaneme vzťah medzi pôvodným polomerom $R_1$ a novými polomermi $R_2$ 

$$
\frac{4}{3}\pi R_1^3\rho=4\frac{4}{3}\pi R_2^3\rho \, , \tag{1}
$$

 

$$
R_1=\sqrt[3]{4}R_2 \, . \tag{2}
$$

 Intenzita svetla závisí iba na odrazovej ploche asteroidov, pre pomer intenzít preto platí 

$$
\frac{I_1}{I_2}=\frac{\pi R_1^2}{4\pi R_2^2}=\left(\frac{R_1}{2R_2}\right)^2=\left(\frac{\sqrt[3]{4}}{2}\right)^2 \, . \tag{3}
$$

 Z Pogsonovej rovnice získame rozdiel magnitúd 

$$
m_2-m_1=2,5\log \frac{I_1}{I_2}=5\log \left(\frac{\sqrt[3]{4}}{2}\right)=-0,5 \, . \tag{4}
$$

 Asteoid po rozpade zjasní o $0{,}5\,\mathrm{mag}$.

</details>
