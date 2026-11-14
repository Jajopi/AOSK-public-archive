---
title: Úloha 2
year: 2015
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú2
weight: 2302
hasSolution: true
source: ZAO:I_Zadania/03_Sferika/03_SS_FI.tex
rocniky:
- '2015'
kola:
- Celoštátne kolo
kategorie:
- SŠ
typy:
- Teória
tagy:
- Sférická astronómia
collection: ZAO
---

## Zadanie

Spln Mesiaca nastal 19. júna 2008 o 00:30 Západného Indonézskeho času. Vypočítajte minimálnu a maximálnu hodnotu zotrvania Mesiaca nad horizontom pre pozorovateľa na Boscha Observatóriu (východná zem. dĺžka $107^{\circ}\,35'\,0{,}0''$ E, južná zem. šírka $6^{\circ}\,49'\,0{,}0''$ S). Časové pásmo je UT + 7 hod 30 min.

<details class="solution">
<summary>Riešenie</summary>

Spln nastal v blízkosti letného slnovratu, deklinácia Slnka je preto približne $\delta_{\Sun}=23^{\circ}\,26'$. Mesiac v splne sa nachádza zhruba na opačnej strane nebeskej sféry v blízkosti deklinácie $-23^{\circ}\,26'$. Vieme ale, že dráha Mesiaca je voči ekliptike sklonená o $i=5{,}14^{\circ}$, preto maximálna možná deklinácia Mesiaca je $\delta_1=-23^{\circ}\,26'+5{,}14^{\circ}=-18^{\circ}\,17'\,36''$ a minimálna možná deklinácia je $\delta_\textrm{min}=-23^{\circ}\,26'-5{,}14^{\circ}=-28^{\circ}\,34'\,24''$.\
Využijeme vzťah pre hodinový uhol pri západe/východe 

$$
\cos t = -\tan \varphi \tan \delta \, . \tag{1}
$$

 Dvojnásobok hodinového uhla udáva čas, ktorý objekt strávi nad obzorom. 

$$
t_1=\arccos (-\tan(-6^{\circ}\,49')) \tan (-18^{\circ}\,17'\,36''))=92^{\circ}\,15'\,53'' \, , \tag{2}
$$

 

$$
t_2=\arccos (-\tan (-6^{\circ}\,49')) \tan (-28^{\circ}\,34'\,24'')=93^{\circ}\,44'\,58'' \, . \tag{3}
$$

 Zodpovedajúce časy sú $T_1=2t_1=12\,\mathrm{h}\ 18\,\min$ a $T_2=2t_2=12\,\mathrm{h}\ 30\,\min$. Na tieto dva časy je potrebné ešte urobiť niekoľko korekcií. Kvôli svojmu obehu okolo Zeme sa Mesiac za 1 deň posunie na oblohe v rektascenzii smerom na východ o $\frac{360^{\circ}}{27,3217}=13^{\circ}\,10'\,35''$, to je 52$^{\rm m}$ 43$^{\rm s}$. Za 12,5 hodiny sa rektascenzia Mesiaca zmení o 27$^{\rm m}$, časy zotrvania Mesiaca nad horizontom sú preto $T_1=12\,\mathrm{h}\ 45\,\min$ a $T_2=12\,\mathrm{h}\ 57\,\min$\
Ďalej je potrebné zarátať refrakciu, ktorá je na horizonte približne $0{,}5^{\circ}$. Tento uhol prejde Mesiac za približne 2 minúty, celkovo sa tak ku časom $T_1$ a $T_2$ pripočítajú ešte 4 minúty (2 za východ a 2 za západ).\
Tieto časy platia pre stred disku Mesiaca, ak chceme vedieť časy, kedy je Mesiac viditeľný aspoň časťou svojho disku, musíme urobiť ešte korekciu na uhlový rozmer Mesiaca. Uhlový polomer je približne $0{,}25^{\circ}$, horný okraj mesačného disku preto pri východe uvidíme o 1 minútu skôr ako jeho stred. Pri západe Mesiaca je situácia analogická, preto sú výsledné časy zotrvania Mesiaca na horizontom $T_1=12\,\mathrm{h}\ 45\,\min + 4\,\mathrm{min} + 2\,\min = 12\,\mathrm{h}\ 51\,\min$ a $T_1=12\,\mathrm{h}\ 57\,\min + 4\,\mathrm{min} + 2\,\min = 13\,\mathrm{h}\ 3\,\min$.

</details>
