---
title: Hviezdny Mesiac
year: 2025
round: DK
roundName: Domáce kolo
category: ZŠ
type: teoria
typeName: Teória
label: T3
weight: 3
points: '45'
authors:
- Samuel Amrich
hasSolution: true
source: 2025:1-DK/0-ZS/02-Hviezdny-Mesiac/00-zadanie.tex
rocniky:
- '2025'
kola:
- Domáce kolo
kategorie:
- ZŠ
typy:
- Teória
tagy:
- Nezaradené
---

## Zadanie

Skupinka inžinierov sa rozhodla, že Mesiac už ďalej nie je zaujímavé vesmírne teleso. Preto sa dohodli na postavení zariadenia vo vesmíre, ktoré bude zachytávať všetko svetlo z Mesiaca, a bude ho následne premietať ako veľké množstvo svietiacich bodiek, umelých hviezd. To by malo pre všetkých pozorovateľov na Zemi za následok, že namiesto Mesiaca by videli iba veľké množstvo nových hviezd. Ak predpokladáme, že Mesiac má magnitúdu $m_{\Mo}=-10\,\mathrm{mag}$, a že vytvárame jasné hviezdy s magnitúdou $0\,\mathrm{mag}$, koľko takýchto hviezd vieme vytvoriť?

<details class="solution">
<summary>Riešenie</summary>

K riešeniu sa dá pristúpiť dvojako. Buď jednoduchou úvahou alebo za pomoci vzorcov.

Najprv úvahou. O magnitúdach vieme, že posun o päť magnitúd je zjasnenie stonásobne. Keďže náš Mesiac je v zadaní o desať magnitúd jasnejší ako hviezdy, ktoré chceme vytvoriť, tak to predstavuje nárast jasnosti $100\cdot100$, teda $10\,000$ násobne. Z toho je vidieť, že zo všetkého mesačného svetla dokážeme vytvoriť až $10\,000$ jasných hviezd.

Ak si chceme náš výsledok potvrdiť aj za pomoci vzorcov, musíme si napísať Pogsonovu rovnicu 

$$
m_{\Mo}-m=-2,5\log{\left(\frac{F_{\Mo}}{F}\right)}   \, , \tag{1}
$$

 ktorú predelíme číslom $-2{,}5$ do podoby 

$$
\frac{m_{\Mo}-m}{-2,5}=\log{\left(\frac{F_{\Mo}}{F}\right)}   \, . \tag{2}
$$

 Pred nami teraz stojí úloha zbaviť sa logaritmu. Spravíme to tak, že vložíme obe strany rovnice do exponentu čísla 10, pretože 10 je základ (dekadického) logaritmu $\log$, 

$$
10^{\left(\cfrac{m_{\Mo}-m}{-2,5}\right)}=10^{\left(\log{\left(\cfrac{F_{\Mo}}{F}\right)}\right)} \, . \tag{3}
$$

 Dôvod prečo sme to spravili, je ten, že funkcia $10^{(\dots\!\,)}$ je inverzná (opačná) funkcia k logaritmu. To znamená, že sa $10^{(\dots\!\,)}$ a $\log(\dots\!\,)$ na pravej strane navzájom vyrušia, teda $10^{\log(\dots\!\,)} = (\dots\!\,)$. To nám umožní ”zbaviť” sa logaritmu a vyjadriť pomer tokov 

$$
10^{\left(\cfrac{m_{\Mo}-m}{-2,5}\right)}=\frac{F_{\Mo}}{F} \ztv \frac{F_{\Mo}}{F} = 10\,000\, . \tag{4}
$$

Takže vidíme, že tok z Mesiaca je $10\,000$-krát väčší ako z jednej hviezdy s $0\,\mathrm{mag}$, teda ich potrebujeme $10\,000$.

</details>

## Komentár autora

Veľmi jednoduchá úloha z oblasti diferenciálnej fotometrie, čo je len zložito pomenované porovnávanie jasnosti objektov. Slúži na oboznámenie študenta s prácou s magnitúdami.
