---
title: Úloha 3
year: 2010
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú3
weight: 2303
hasSolution: true
source: ZAO:I_Zadania/02_GmtrCas/02_SS_FI.tex
rocniky:
- '2010'
kola:
- Celoštátne kolo
kategorie:
- SŠ
typy:
- Teória
tagy:
- Geometria a čas
collection: ZAO
---

## Zadanie

Pozorovateľ zisťoval rozdiely v jasnostiach planét pri ich rôznych aspektoch. Pre prvú – vonkajšiu planétu – zistil rozdiel v jej zdanlivej jasnosti medzi polohou v opozícii a v konjunkcii so Slnkom v hodnote 0,85 magnitúdy. Pre druhú – vnútornú planétu – zmeral rozdiel medzi jej jasnosťou v najväčšej východnej elongácii a jasnosťou v hornej konjunkcii v hodnote 0,92 magnitúdy.\
O ktoré planéty slnečnej sústavy ide? Predpokladajte kruhové dráhy s polomerom veľkej polosi príslušnej planéty.

<details class="solution">
<summary>Riešenie</summary>

V Pogsonovej rovnici pre vonkajšiu planétu použijeme index 1 pre opozíciu a 2 pre konjunkciu. Vzdialenosti planéty od Zeme sú $r_1=a-a_{\Ea}$ a $r_2=a+a_{\Ea}$ 

$$
m_2-m_1=5\log{\frac{r_2}{r_1}} \, , \tag{1}
$$

 

$$
\frac{a+a_{\Ea}}{a-a_{\Ea}}=10^{\frac{0,85}{5}}=1,48 \, , \tag{2}
$$

 

$$
a+a_{\Ea}=1,48 a-1,48a_{\Ea} \, , \tag{3}
$$

 

$$
2,48a_{\Ea}=0,48a \, , \tag{4}
$$

 

$$
a=\frac{2,48}{0,48}a_{\Ea}=5{,}17\,\mathrm{au} \, . \tag{5}
$$

 Prvou planétou je Jupiter. V Pogsonovej rovnici pre vnútornú planétu použijeme index 1 pre maximálnu elongáciu (vzdialenosť planéty je $r_1=\sqrt{a_{\Ea}^2-a^2}$) a 2 pre hornú konjunkciu (vzdialenosť planéty je $r_2=a_{\Ea}+a$) 

$$
m_2-m_1=5\log{\frac{r_2}{r_1}} \, , \tag{6}
$$

 

$$
\frac{a_{\Ea}+a}{\sqrt{a_{\Ea}^2-a^2}}=10^{\frac{0,92}{5}} \, , \tag{7}
$$

 

$$
\frac{(a_{\Ea}+a)^2}{(a_{\Ea}+a)(a_{\Ea}-a)}=10^{\frac{2\cdot0,92}{5}}=2,33 \, , \tag{8}
$$

 

$$
a_{\Ea}+a=2,33a_{\Ea}-2,33a \, , \tag{9}
$$

 

$$
3,33a=1,33a_{\Ea} \, , \tag{10}
$$

 

$$
a=\frac{1,33}{3,33}a_{\Ea}=0{,}40\,\mathrm{au} \, . \tag{11}
$$

 Druhou planétou je Merkúr.

</details>
