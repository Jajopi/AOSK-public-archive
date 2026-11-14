---
title: Úloha 4
year: 2011
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú4
weight: 2304
hasSolution: true
source: ZAO:I_Zadania/02_GmtrCas/02_SS_FI.tex
rocniky:
- '2011'
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

Z údajov o polohe Mesiaca a zistenej polohy Slnka 25. 3. 2007 o 17:59:20 UTC určite uhlovú vzdialenosť Slnka a Mesiaca pri fázovom uhle $90^{\circ}$ (Aristarchova úloha) a z nej pomer vzdialeností Slnka a Mesiaca od Zeme.\
**Pomôcka**:\
Jednoduchý spôsob, ako určiť relatívne vzdialenosti Mesiaca od Zeme a Zeme od Slnka poznali už starovekí grécki astronómovia. V okamihu, keď je osvetlená práve polovica Mesiaca (fázový uhol: pozorovateľ–Mesiac–Slnko = $90^{\circ}$; dichotómia) je potrebné určiť uhlovú vzdialenosť - elongáciu ($E$) - Mesiaca od Slnka. Doplnok tejto hodnoty do $90^{\circ}$ potom definuje relatívnu vzdialenosť oboch telies od Zeme. Pôvodné Aristarchovo riešenie bolo „tridsatina kvadrantu“, t.j. $3^{\circ}$. Pri relatívnej neznalosti presnej hodnoty čísla $\pi$ to predstavuje pomer vzdialeností Slnka ($S$) a Mesiaca ($L$) od Zeme: $18<\frac{S}{L}<20$.

<figure>

<div class="fig-images"><img class="invert" src="AO2011_SS_FI_1.svg" alt="obrázok" loading="lazy" style="width:70%"></div>

</figure>

25\. 3. 2007 nastala o 18:16 UTC prvá štvrť Mesiaca. Tá je však definovaná pomocou ekliptikálnych súradníc Slnka a Mesiaca. Vo fázovom uhle $90^{\circ}$ bude Mesiac voči Slnku pre pozorovateľa o niečo skôr, už o 17:59:20 UTC. V tomto okamihu má Mesiac geocentrické rovníkové súradnice 

$$
\alpha_{\Mo} = 6^{\mathrm{h}}\,20^{\mathrm{min}}\,40{,}536^{\mathrm{s}} \, , \ \delta_{\Mo} = 28^{\circ}\,21'\,24{,}59'' \, ,
$$

 a Slnko geocentrické rovníkové súradnice 

$$
\alpha_{\Sun} = 0^{\mathrm{h}}\,17^{\mathrm{min}}\,17{,}118^{\mathrm{s}} \, , \ \delta_{\Sun} = 1^{\circ}\,52'\,11{,}17'' \, .
$$

 Pre 25.3.2007 o 0:00 UTC je hodnota zdanlivého hviezdneho času na nultom poludníku rovná SO = 12h 08m 18,705s (AR 2007).\
Preto, že vzdialenosť Mesiaca je pomerne malá ku veľkosti Zeme, museli by sme pri pozorovaniach z ľubovoľného miesta súčasne pozorované polohy Mesiaca a Slnka zložito transformovať. Ako jednoduchšie sa nám zdá využiť špeciálne polohy so Slnkom a Mesiacom v zenite. Úlohu tak možno zredukovať na riešenie čiastkových problémov.\
**Úlohy :**

<ol type="a">

<li>

Kde na povrchu Zeme je v uvedený čas Mesiac (jeho stred) práve v miestnom zenite? Vtedy (a tam) nie je rozdiel medzi topocentrickou a geocentrickou polohou. Uveďte geografické súradnice tohto miesta $\lambda$, $\phi$.

</li>

<li>

Kde na povrchu Zeme je v uvedený čas Slnko (jeho stred) práve v miestnom zenite? Vtedy (a tam) nie je rozdiel medzi jeho topocentrickou a geocentrickou polohou. Uveďte geografické súradnice tohto miesta $\lambda$, $\phi$.

</li>

<li>

Ako sa nazývajú na Zemi body s Mesiacom a Slnkom v zenite?

</li>

<li>

Pomocou vzťahov sférickej trigonometrie spočítajte elongáciu $E$ Mesiaca od Slnka pre geocentrického pozorovateľa 

$$
\cos E = \sin \delta_{\Sun} \sin \delta_{\Mo} + \cos \delta_{\Sun} \cos \delta_{\Mo} \cos (\alpha_{\Sun} - \alpha_{\Mo})\, .
$$

 Jeho doplnok: $\delta = (90^{\circ}-E)$ je hľadaný uhol (pri Slnku) v trojuholníku Zem–Mesiac–Slnko. Kotangens tohto uhla udáva pomer vzdialenosti Slnka a Mesiaca od stredu Zeme, vypočí-tajte ho.

</li>

</ol>

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Zemepisná šírka tohto miesta je rovnaká ako deklinácia Mesiaca, $\varphi=\delta_{\Mo}=28^{\circ}\,21'\,24{,}59''$ N. Ak sa Mesiac nachádza v zenite, znamená to, že práve kulminuje. Ku kulminácii Mesiaca dochádza pri hviezdnom čase $\theta=\alpha_{\Mo}=6^{\mathrm{h}}\,20^{\mathrm{min}}\,40{,}536^{\mathrm{s}}$. Na nultom poludníku poznáme hviezdny čas pre 25.3.2007 o 0:00 UTC, potrebujeme zistiť, aký je hviezdny čas v momente, kedy nastala prvá štvrť Mesiaca, teda o 18:16. Prevodný faktor medzi hviezdnym a občianskym časom je

</li>

</ol>

$$
\frac{24\cdot3600}{23\cdot3600+56\cdot60+4,1}=1{,}002738 \, . \tag{1}
$$

 Hviezdny čas na nultom poludníku o 18:16 je $\theta=12^{\mathrm{h}}\,8^{\mathrm{min}}\,18{,}705^{\mathrm{s}}+1{,}002738\cdot18^{\mathrm{h}}\,16^{\mathrm{min}}\,0^{\mathrm{s}}-24^{\mathrm{h}}\,0^{\mathrm{min}}\,0^{\mathrm{s}}=6^{\mathrm{h}}\,27^{\mathrm{min}}\,18{,}76^{\mathrm{s}}$. Mesiac kulminuje pri o trochu skoršom hviezdnom čase, je preto potrebné sa od nultého poludníka posunúť o kúsok na západ na zemepisnú dĺžku 

$$
\lambda=\frac{6^{\mathrm{h}}\,27^{\mathrm{min}}\,18{,}76^{\mathrm{s}}-6^{\mathrm{h}}\,20^{\mathrm{min}}\,40{,}536^{\mathrm{s}}}{24^{\rm h}}\cdot360^{\circ}=1^{\circ}\,39'\,33{,}36'' \ \rm W \, . \tag{2}
$$

<ol type="a" start="2">

<li>

Postupujeme rovnakým spôsobom ako pri Mesiaci. Zemepisná šírka sa rovná deklinácii Slnka, $\varphi=\delta_{\Sun}=1^{\circ}\,52'\,11{,}17''$ N. Slnko kulminuje pri hviezdnom čase $\theta=\alpha_{\Sun}=0^{\mathrm{h}}\,17^{\mathrm{min}}\,17{,}118^{\mathrm{s}}$. Zemepisná dĺžka je

</li>

</ol>

$$
\lambda=\frac{6^{\mathrm{h}}\,27^{\mathrm{min}}\,18{,}76^{\mathrm{s}}-0^{\mathrm{h}}\,17^{\mathrm{min}}\,17{,}118^{\mathrm{s}}}{24^{\rm h}}\cdot360^{\circ}=92^{\circ}\,30'\,24{,}63'' \ \rm W \, . \tag{3}
$$

<ol type="a" start="3">

<li>

Nazývajú sa sublunárny a subsolárny bod.

</li>

</ol>

<ol type="a" start="4">

<li>

Stačí iba dosadiť do vzorca zo zadania 

$$
\begin{gathered}
\cos E =\sin 1^{\circ}\,52'\,11{,}17''\cdot\sin{28^{\circ}\,21'\,24{,}59''} \\
 + \cos{1^{\circ}\,52'\,11{,}17''}\cdot \cos{28^{\circ}\,21'\,24{,}59''}\cdot\cos{[(6^{\mathrm{h}}\,20^{\mathrm{min}}\,40{,}536^{\mathrm{s}}-0^{\mathrm{h}}\,17^{\mathrm{min}}\,17{,}118^{\mathrm{s}})\cdot 15]} \, . \end{gathered}\tag{4}
$$

 Dostávame $E=89^{\circ}\,51'\,27{,}13''$, doplnok tohto uhla je $\delta=90^{\circ}-89^{\circ}\,51'\,27{,}13''=0^{\circ}\,8'\,32{,}87''$. Pomer vzdialenosti Slnka a Mesiaca je 

$$
\frac{S}{L}=\cot{\delta}=\tan{E}=\tan{89^{\circ}\,51'\,27{,}13''}=402 \, . \tag{5}
$$

</li>

</ol>

</details>
