---
title: Úloha 3
year: 2009
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
- '2009'
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

Vypočítajte, kedy vychádzala 30. 4. 2009 a zapadala 1. 5. 2009 hviezda Hocule´a pre pozorovateľa v Honolulu ($\varphi = 21^{\circ}\,20'\,39''$N, $\lambda = 157^{\circ}\,50'\,08''$W). Súradnice hviezdy sú: $\alpha=14^{\mathrm{h}}\,16^{\mathrm{min}}\,05{,}3^{\mathrm{s}}$, $\delta=19^{\circ}\,08'\,03''$.\
Miestny hviezdny čas o polnoci UTC na Greenwichskom poludníku je 30. 4. 2009 rovný 14h 32m 17,204s a 1.5.2009 rovný 14h 36m 13,765s. Refrakciu zanedbajte!\
Pre výšku hviezdy nad obzorom pritom platí 

$$
\sin h = \sin \delta \sin \varphi + \cos \delta \cos \varphi \cos t \, .
$$

<details class="solution">
<summary>Riešenie</summary>

Pri východe a západe je $h=0^{\circ}$, vzťah zo zadania sa preto zjednoduší na 

$$
\cos{t}=-\tan{\delta}\tan{\varphi}=-\tan{19^{\circ}\,8'\,3''}\tan{21^{\circ}\,20'\,39''} \, . \tag{1}
$$

 Hodinový uhol pri západe hviezdy je $t_\textrm{z}=6^{\mathrm{h}}\,31^{\mathrm{min}}\,10{,}1^{\mathrm{s}}$, pri východe je $t_\textrm{v}=-6^{\mathrm{h}}\,31^{\mathrm{min}}\,10{,}1^{\mathrm{s}}$. Hviezda zapadá pri hviezdnom čase $\theta_\textrm{z}=\alpha+t_\textrm{z}=14^{\mathrm{h}}\,16^{\mathrm{min}}\,5{,}3^{\mathrm{s}}+6^{\mathrm{h}}\,31^{\mathrm{min}}\,10{,}1^{\mathrm{s}}=20^{\mathrm{h}}\,47^{\mathrm{min}}\,15{,}4^{\mathrm{s}}$ a vychádza pri hviezdnom čase $\theta_\textrm{v}=\alpha+t_\textrm{v}=14^{\mathrm{h}}\,16^{\mathrm{min}}\,5{,}3^{\mathrm{s}}-6^{\mathrm{h}}\,31^{\mathrm{min}}\,10{,}1^{\mathrm{s}}=7^{\mathrm{h}}\,44^{\mathrm{min}}\,55{,}2^{\mathrm{s}}$.\
Časové pásmo Honolulu je UTC$-10^{\rm h}$. Rozdiel v miestnom hviezdnom čase oproti Greenwichskému poludníku je $\frac{157^{\circ}\,50'\,8''}{15}=10^{\mathrm{h}}\,31^{\mathrm{min}}\,20{,}5^{\mathrm{s}}$. 1. 5. o polnoci UTC je v Honolulu 30. 4. 14:00 a hviezdny čas je $\theta_\textrm{H}=14^{\mathrm{h}}\,36^{\mathrm{min}}\,13{,}8^{\mathrm{s}}-10^{\mathrm{h}}\,31^{\mathrm{min}}\,20{,}5^{\mathrm{s}}=4^{\mathrm{h}}\,4^{\mathrm{min}}\,53{,}3^{\mathrm{s}}$. Hviezda vyjde, keď sa hviezdny čas zvýši o $\theta_\textrm{v}-\theta_\textrm{H}=7^{\mathrm{h}}\,44^{\mathrm{min}}\,55{,}2^{\mathrm{s}}-4^{\mathrm{h}}\,4^{\mathrm{min}}\,53{,}3^{\mathrm{s}}=3^{\mathrm{h}}\,40^{\mathrm{min}}\,1{,}9^{\mathrm{s}}$. Tento rozdiel je potrebné prepočítať na rozdiel v bežnom občianskom čase. Prevodná konštanta z hviezdneho času na občiansky je 

$$
\frac{24\cdot3600}{23\cdot3600+56\cdot60+4,1}=1{,}002738 \, . \tag{2}
$$

 Hviezda vyjde $\frac{3^{\mathrm{h}}\,40^{\mathrm{min}}\,1{,}9^{\mathrm{s}}}{1{,}002738}=3^{\mathrm{h}}\,39^{\mathrm{min}}\,25{,}9^{\mathrm{s}}$ po 14:00, teda o 17:39:25,9.\
Rozdiel medzi hviezdnym časom východu a západu je $\theta_\textrm{z}-\theta_\textrm{v}=2t_\textrm{z}=2\cdot6^{\mathrm{h}}\,31^{\mathrm{min}}\,10{,}1^{\mathrm{s}}=13^{\mathrm{h}}\,2^{\mathrm{min}}\,20{,}2^{\mathrm{s}}$. Po prepočte na bežný čas nám vyjde časový rozdiel medzi východom a západom $\frac{13^{\mathrm{h}}\,2^{\mathrm{min}}\,20{,}2^{\mathrm{s}}}{1{,}002738}=13^{\mathrm{h}}\,0^{\mathrm{min}}\,12{,}0^{\mathrm{s}}$. Máme $17^{\mathrm{h}}\,39^{\mathrm{min}}\,25{,}9^{\mathrm{s}}+13^{\mathrm{h}}\,0^{\mathrm{min}}\,12{,}0^{\mathrm{s}}-24^{\rm h}=6^{\mathrm{h}}\,39^{\mathrm{min}}\,37{,}9^{\mathrm{s}}$, západ hviezdy teda nastane 1. 5. o 6:39:37,9.

</details>
