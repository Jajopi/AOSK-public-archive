---
title: Úloha 6
year: 2015
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú6
weight: 2306
hasSolution: true
source: ZAO:I_Zadania/01_NebMech/01_SS_FI.tex
rocniky:
- '2015'
kola:
- Celoštátne kolo
kategorie:
- SŠ
typy:
- Teória
tagy:
- Nebeská mechanika
collection: ZAO
---

## Zadanie

Vypočítajte o koľko sa zväčší polomer zemskej dráhy ako výsledok straty hmotnosti Slnka v dôsledku termonukleárnych reakcií prebiehajúcich v jeho jadre za 100 rokov. Predpokladáme, že dráha Zeme okolo Slnka je počas tohto obdobia kruhová.

<details class="solution">
<summary>Riešenie</summary>

Na riešenie využijeme zákon zachovania momentu hybnosti (mechanická energia Zeme sa v tomto prípade nezachováva, pretože sa mení hmotnosť Slnka). Na začiatku je hmotnosť Slnka $M_\Sun$, vzdialenosť Zeme od Slnka $r_1$ a moment hybnosti Zeme 

$$
L_1=M_\Ea r_1 v_1 = M_\Ea r_1 \sqrt{\frac{GM_\Sun}{r_1}}=M_\Ea \sqrt{GM_\Sun r_1} \, . \tag{1}
$$

 Na konci sme využili vzorec pre kruhovú rýchlosť. Po 100 rokoch sa hmotnosť Slnka zníži na $M_\Sun - \Delta m$, zníži sa gravitačná sila Slnka pôsobiaca na Zem a Zem bude obiehať vo väčšej vzdialenosti $r_2=r_1+\Delta r$. Moment hybnosti Zeme bude 

$$
L_2=M_\Ea r_2 v_2 = M_\Ea (r_1+\Delta r) \sqrt{\frac{G(M_\Sun-\Delta m)}{r_1+\Delta r}}=M_\Ea \sqrt{G(M_\Sun-\Delta m)(r_1+\Delta r)} \, . \tag{2}
$$

 Z rovnosti momentov hybnosti $L_1=L_2$ dostaneme 

$$
\sqrt{M_\Sun r_1}=\sqrt{(M_\Sun-\Delta m)(r_1+\Delta r)} \, . \tag{3}
$$

 Energia jadrových reakcií je Slnkom vyžiarená do okolia a pre zmenu hmotnosti Slnka platí 

$$
\Delta m =\frac{L_\Sun t}{c^2}=\frac{3{,}826 \cdot 10^{26}\cdot100\cdot365,25\cdot86400}{(2{,}9979 \cdot 10^{8})^2}=1{,}34 \cdot 10^{19}\,\mathrm{kg} \, . \tag{4}
$$

 Zmena hmotnosti Slnka je veľmi malá v porovnaní s hmotnosťou Slnka $\Delta m \ll M_\Sun$, preto môžeme očakávať, že aj zmena polomeru dráhy Zeme bude veľmi malá $\Delta r \ll r_1$. Rovnosť vyplývajúcu zo zákona zachovania hybnosti upravíme tak, aby na jednej strane bola hmotnosť Slnka a jej zmena a na druhej strane polomer dráhy Zeme a jeho zmena 

$$
\frac{1}{\sqrt{\frac{M_\Sun-\Delta m}{M_\Sun}}}=\sqrt{\frac{r_1+\Delta r}{r_1}} \, , \tag{5}
$$

 

$$
\frac{1}{\sqrt{1-\frac{\Delta m}{M_\Sun}}}=\sqrt{1+\frac{\Delta r}{r_1}} \, . \tag{6}
$$

 Ďalej využijeme približné vzorce, ktoré platia pre $x\ll1$, kde $x$ je v našom prípade pomer zmeny veličiny a veličiny samotnej 

$$
(1+x)^n \approx 1+nx \, , \tag{7}
$$

 

$$
(1-x)^{-n} \approx 1+nx \, , \tag{8}
$$

 

$$
1+\frac{1}{2}\frac{\Delta m}{M_\Sun}\approx1+\frac{1}{2}\frac{\Delta r}{r_1} \, , \tag{9}
$$

 

$$
\frac{\Delta m}{M_\Sun}=\frac{\Delta r}{r_1} \, . \tag{10}
$$

 Polomer Zemskej dráhy sa zväčší o 

$$
\Delta r= \frac{\Delta m}{M_\Sun}r_1=\frac{1{,}34 \cdot 10^{19}}{1{,}9891 \cdot 10^{30}}\cdot1{,}496 \cdot 10^{11}=1\,\mathrm{m} \, . \tag{11}
$$

</details>
