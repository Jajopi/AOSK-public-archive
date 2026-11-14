---
title: Úloha 4
year: 2013
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú4
weight: 5004
hasSolution: true
source: ZAO:I_Zadania/04_FotoSpek/04_SS_FI.tex
years:
- '2013'
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

Najjasnejšia hviezda nočnej oblohy, Sírius, sa skladá z hviezdy hlavnej postupnosti s teplotou $T_\textrm{A} = 10\,000\,\mathrm{K}$ a bieleho trpaslíka s teplotou $T_\textrm{B} = 30\,000\,\mathrm{K}$. Pre ich polomery platí $R_\textrm{A} = 100 R_\textrm{B}$. Na akej vlnovej dĺžke $\lambda$ vyžiaria obe zložky A i B rovnaké množstvo žiarenia? Použite Planckovu funkciu v tvare 

$$
I(\lambda,T)=\frac{2hc^2}{\lambda^5}\exp{\frac{-hc}{k_\textrm{B}T\lambda}} \, .
$$

<details class="solution">
<summary>Riešenie</summary>

Chceme nájsť vlnovú dĺžku, pre ktorú platí rovnosť 

$$
4\pi R_\textrm{A}^2 I(\lambda,T_\textrm{A})= 4\pi R_\textrm{B}^2 I(\lambda,T_\textrm{B}) \, , \tag{1}
$$

 

$$
R_\textrm{A}^2\frac{2hc^2}{\lambda^5}\exp \left(\frac{-hc}{k_\textrm{B}T_\textrm{A}\lambda}\right)=R_\textrm{B}^2\frac{2hc^2}{\lambda^5}\exp \left(\frac{-hc}{k_\textrm{B}T_\textrm{B}\lambda}\right) \, , \tag{2}
$$

 

$$
R_\textrm{A}^2\exp \left(\frac{-hc}{k_\textrm{B}T_\textrm{A}\lambda}\right)=R_\textrm{B}^2\exp \left(\frac{-hc}{k_\textrm{B}T_\textrm{B}\lambda}\right) \, , \tag{3}
$$

 

$$
\exp \left[\frac{hc}{k_\textrm{B}\lambda}\left(\frac{1}{T_\textrm{B}}-\frac{1}{T_\textrm{A}}\right)\right]=\frac{R_\textrm{B}^2}{R_\textrm{A}^2} \, , \tag{4}
$$

 

$$
\exp \left(\frac{hc}{k_\textrm{B}\lambda}\frac{T_\textrm{A}-T_\textrm{B}}{T_\textrm{A}T_\textrm{B}}\right)=\frac{R_\textrm{B}^2}{R_\textrm{A}^2} \, , \tag{5}
$$

 

$$
2\ln \frac{R_\textrm{B}}{R_\textrm{A}}=\frac{hc}{k_\textrm{B}\lambda}\frac{T_\textrm{A}-T_\textrm{B}}{T_\textrm{A}T_\textrm{B}} \, , \tag{6}
$$

 

$$
\lambda=\frac{hc}{2k_\textrm{B}}\frac{T_\textrm{A}-T_\textrm{B}}{T_\textrm{A}T_\textrm{B}}\frac{1}{\ln \left(\frac{R_\textrm{B}}{R_\textrm{A}}\right)} \, , \tag{7}
$$

 

$$
\lambda=\frac{6{,}626 \cdot 10^{-34}\cdot2{,}9979 \cdot 10^{8}}{2\cdot1{,}381 \cdot 10^{-23}}\cdot\frac{10\,000-30\,000}{10\,000\cdot30\,000}\cdot\frac{1}{\ln \left(\frac{1}{100}\right)}=1{,}04 \cdot 10^{-7}\,\mathrm{m}=104\,\mathrm{nm} \, . \tag{8}
$$

</details>
