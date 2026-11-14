---
title: Úloha 2
year: 2010
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
- '2010'
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

Dvojhviezda s obežnou dobou $10\,\mathrm{dní}$ má zložky o hmotnostiach $10\,\mathit{M}_\Sun$ a $2\,\mathit{M}_\Sun$. Menej hmotná zložka je pulzarom, ktorý má pulzačnú periódu $0{,}1\,\mathrm{s}$. Zistite, v akom intervale sa mení pozorovaná perióda pulzácií. Predpokladajte kruhovú dráhu so sklonom $90^{\circ}$, to znamená, že pozorovateľ sa nachádza v rovine dráhy dvojhviezdy.

<details class="solution">
<summary>Riešenie</summary>

Najskôr vypočítame veľkú polos systému 

$$
a=\sqrt[3]{\frac{G(M_1+M_2)P^2}{4\pi^2}}=\sqrt[3]{\frac{6{,}67 \cdot 10^{-11}\cdot12\cdot1{,}9891 \cdot 10^{30}\cdot(10\cdot86400)^2}{4\pi^2}}=3{,}11 \cdot 10^{10}\,\mathrm{m} \, . \tag{1}
$$

 Pomer hmotností jednotlivých zložiek sa rovná prevrátenému pomeru ich polomerov dráh 

$$
\frac{M_1}{M_2}=\frac{a_2}{a_1}=\frac{a_2}{a-a_2} \, . \tag{2}
$$

 Z toho zistíme polomer dráhy pulzaru 

$$
a_2=\frac{M_1}{M_2}a-\frac{M_1}{M_2}a_2 \, , \tag{3}
$$

 

$$
M_2a_2=M_1a-M_1a_2 \, , \tag{4}
$$

 

$$
a_2=\frac{M_1}{M_1+M_2}a=\frac{10}{12}\cdot3,11\cdot10^10=2{,}59 \cdot 10^{10}\,\mathrm{m} \, . \tag{5}
$$

 Rýchlosť obehu pulzaru je 

$$
v_\textrm{k}=\frac{2\pi a_2}{P}=\frac{2\pi\cdot2{,}59 \cdot 10^{10}}{10\cdot86400}=188\,\mathrm{km}\,{\mathrm{s}}^{-1} \, . \tag{6}
$$

 Ku zmene periódy pulzácií dochádza kvôli Dopplerovmu javu, ktorý platí nielen pre svetlo, ale pre všetky iné periodické signály. Medzi vlnovou dĺžkou, rýchlosťou a frekvenciou signálu platí vzťah 

$$
\lambda=\frac{c}{f} \, . \tag{7}
$$

 Zároveň perióda signálu je prevrátenou hodnotou frekvencie 

$$
f=\frac{1}{T} \, , \tag{8}
$$

 

$$
\lambda=cT \, . \tag{9}
$$

 Dopplerov vzťah pre vlnové dlžky tak môžeme prepísať na Dopplerov vzťah pre periódy signálu, v tomto prípade sa jedná o periódy pulzaru 

$$
\frac{v_\textrm{k}}{c}=z=\frac{\lambda-\lambda_0}{\lambda_0}=\frac{T-T_0}{T_0}=\frac{\Delta T}{T_0} \, . \tag{10}
$$

 Sklon dvojhviezdy je $90^{\circ}$, preto môžeme $v_\textrm{k}$ použiť vo vzorci pre Dopplerov jav. Ak by bol sklon dráhy iný, museli by sme použiť priemet rýchlosti $v_\textrm{k} \sin i$.\
Zmena periódy je maximálne 

$$
\Delta T = \frac{v_\textrm{k}}{c} T_0=\frac{188 \cdot 10^{3}}{2{,}9979 \cdot 10^{8}}\cdot0,1=6{,}3 \cdot 10^{-5}\,\mathrm{s}=63\,\mu\mathrm{s} \, . \tag{11}
$$

 Periódu pulzácií teda pozorujeme v intervale $0{,}1\,\mathrm{s} \pm 63\,\mu\mathrm{s}$.

</details>
