---
title: Hviezdokopa
year: 2024
round: RK
roundName: Regionálne kolo
category: ZŠ
type: teoria
typeName: Teória
label: T1
weight: 1001
points: '80'
authors:
- Jana Švrčková
hasSolution: true
source: 2024:RK/ZS/aTeoria/Hviezdokopa.tex
rocniky:
- '2024'
kola:
- Regionálne kolo
kategorie:
- ZŠ
typy:
- Teória
tagy:
- Nezaradené
---

## Zadanie

Otvorená hviezdokopa sa skladá z $10\,000$ hviezd, každá z hviezd má magnitúdu 18. Vypočítajte celkovú magnitúdu hviezdokopy. Je možné ju pozorovať voľným okom?

<details class="solution">
<summary>Riešenie</summary>

Na riešenie nám stačí využiť fakt, že 100-násobný pomer jasností zodpovedá rozdielu 5 magnitúd. 100 hviezd 18. magnitúdy je 100-krát jasnejších ako jediná hviezda 18. magnitúdy. Týchto 100 hviezd bude mať dohromady 13. magnitúdu, lebo $18-5=13$. Celá hviezdokopa má až 10 000 hviezd, takže je ešte 100-krát jasnejšia ako 100 hviezd. Magnitúda hviezdokopy je preto $13-5=8$.

Úloha sa dá riešiť aj s využitím Pogsonovej rovnice 

$$
m_1-m_2=-2,5\log \left(\frac{I_1}{I_2}\right)\,, \tag{1}
$$

 kde $m_2=18$ je magnitúda jednej hviezdy, $m_2$ je magnitúda celej hviezdokopy a $\frac{I_1}{I_2}=10\,000$ je pomer jasností hviezdokopy a jedinej hviezdy. Po dosadení čísel nám opäť vyjde $m_1=8$.

</details>
