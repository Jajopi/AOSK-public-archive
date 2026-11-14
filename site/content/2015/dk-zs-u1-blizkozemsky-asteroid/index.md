---
title: Blízkozemský asteroid
year: 2015
round: DK
roundName: Domáce kolo
category: ZŠ
type: teoria
typeName: Teória
label: Ú1
weight: 1
hasSolution: true
source: ZAO:I_Zadania/01_NebMech/01_ZS_DK.tex
rocniky:
- '2015'
kola:
- Domáce kolo
kategorie:
- ZŠ
typy:
- Teória
tagy:
- Nebeská mechanika
collection: ZAO
---

## Zadanie

Blízkozemský asteroid má synodickú obežnú dobu $S = 1200$ dní a excentricitu dráhy $e = 0,4$. Ako najbližšie sa teoreticky môže priblížiť k Zemi? Počítate s tým, že dráha asteroidu leží v rovine dráhy Zeme a dráhu Zeme považujeme za kruhovú s polomerom $r = 1\,\mathrm{au}$.

<details class="solution">
<summary>Riešenie</summary>

Ak je asteroid vnútorný, jeho siderická obežná doba je 

$$
P=\frac{SP_\Ea}{S+P_\Ea}=\frac{1200\cdot365,25}{1200+365,25}=280{,}02\,\mathrm{dní}=0{,}767\,\mathrm{rokov} \, . \tag{1}
$$

 Veľká polos je v tomto prípade 

$$
a=\sqrt[3]{P^2}=\sqrt[3]{0,767^2}=0{,}838\,\mathrm{au} \, . \tag{2}
$$

 To je menej ako vzdialenosť Zeme od Slnka. Skúsime preto vypočítať vzdialenosť afélia asteroidu od Slnka a zistiť nakoľko sa priblíži k Zemi, prípadne, či môže križovať dráhu Zeme. Dostaneme 

$$
r_\textrm{a}=a(1+e) = 1,4\cdot0,838=1{,}17\,\mathrm{au} \, . \tag{3}
$$

 Asteroid križuje dráhu Zeme a tak sa môže potenciálne k Zemi dostať ľubovoľne blízko.

Ak je asteroid vonkajší, siderická obežná doba je 

$$
P=\frac{SP_\Ea}{S-P_\Ea}=\frac{1200\cdot365,25}{1200-365,25}=525{,}07\,\mathrm{dní}=1{,}438\,\mathrm{rokov} \, . \tag{4}
$$

 Veľká polos a vzdialenosť perihélia sú 

$$
a=\sqrt[3]{P^2}=\sqrt[3]{1,438^2}=1{,}274\,\mathrm{au} \, . \tag{5}
$$

 Na rozdiel od vnútorného asteroidu je tentokrát veľká polos vonkajšieho asteroidu väčšia ako $1\,\mathrm{au}$. V tomto prípade teda dopočítame vzdialenosť periélia asteroidu od Slnka a tým overíme, či križuje dráhu Zeme. Dostaneme 

$$
r_\textrm{p}=a(1+e) = 0,6\cdot1,274=0{,}764\,\mathrm{au} \, . \tag{6}
$$

 Je to menej ako vzdialenosť Zeme od Slnka, takže aj vonkajší asteroid križuje dráhu Zeme a môže sa k nej dostať ľubovoľne blízko.

</details>
