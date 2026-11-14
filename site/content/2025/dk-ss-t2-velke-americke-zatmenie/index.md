---
title: Veľké americké zatmenie
year: 2025
round: DK
roundName: Domáce kolo
category: SŠ
type: teoria
typeName: Teória
label: T2
weight: 3002
points: '70'
authors:
- R. Lascsák
- J. Švrčková
hasSolution: true
source: 2025:1-DK/1-SS/02-Velke-americke-zatmenie/00-zadanie.tex
years:
- '2025'
rounds:
- Domáce kolo
categories:
- SŠ
types:
- Teória
topics:
- Nezaradené
---

## Zadanie

Výpravu cestovateľov za zatmením Slnka zastihne nepriaznivé počasie, a tak sa rozhodnú mrakom utiecť. Na základe radarovej predpovede počasia zistia, že jasná obloha bude počas zatmenia v meste Hot Springs Village. Zaparkovať vedia pri mexickej reštaurácii El Padrino, ktorá sa nachádza presne jednu hodinu jazdy autom od ich štartovnej polohy.

Podarí sa im tam docestovať pred začiatkom úplného zatmenia, ak v momente ich štartu sa v Hot Springs Village práve začalo čiastočné zatmenie Slnka (kotúč Mesiaca sa zdanlivo na oblohe prvýkrát dotkol kotúča Slnka)? Predpokladajte, že dráhy Zeme a Mesiaca sú kružnice a polomer Mesiaca je $1800\,\mathrm{km}$.

<details class="solution">
<summary>Riešenie</summary>

Na vyriešenie tejto úlohy musíme najskôr odpovedať na 2 otázky. Akú uhlovú vzdialenosť $\alpha$ musí Mesiac prejsť medzi začiatkom čiastočného a začiatkom úplného zatmenia? Akou uhlovou rýchlosťou $\omega_{\Mo\Sun}$ sa Mesiac pohybuje po oblohe vzhľadom na Slnko? Následne čas $t$, ktorý má výprava na docestovanie pred El Padrino, bude 

$$
t = \frac{\alpha}{\omega_{\Mo\Sun}}  \,. \tag{1}
$$

Počas fázy čiastočného zatmenia Mesiac postupne zakrýva Slnko, ako vidíme na obrázku 1. Ružovou farbou je znázornený bod na okraji Mesiaca, ktorý počas doby čiastočného zatmenia putuje popred kotúč Slnka. Znázornili sme takto pohyb Mesiaca po oblohe relatívne k Slnku. Celková prejdená uhlová vzdialenosť počas doby zakrývania Slnka bude $\alpha =$ uhlový priemer Slnka. Ten spočítame priamou úmerou 

$$
\frac{\text{uhlový priemer Slnka}}{\text{uhlový obvod kruhu}} = \frac{\alpha}{360^{\circ}} \approx \frac{2 R_\Sun}{2\pi a_\Ea} \ztv
    \alpha = \frac{2 R_\Sun}{a_\Ea} \cdot \frac{360^{\circ}}{2\pi} \approx 0^{\circ}\,31'\,58{,}455'' \,. \tag{2}
$$

Táto jednoduchá priama úmera platí, pretože $R_\Sun \ll a_\Ea$ (Slnko je veľmi ďaleko od Zeme v porovnaní s jeho vlastným rozmerom). Presný výpočet vo všeobecnosti vyžaduje trigonometriu. Konkrétne $\sin(\alpha/2) = R_\Sun/a_\Ea$, z čoho $\alpha \approx 31'\,58{,}462''$. Rozdiel oproti (2) je teda zanedbateľný. To je z dôvodu, že pre malé uhly $\alpha$ platí $\sin x \approx x$ (a takisto $\tan x \approx x$).

<figure>

<div class="fig-images"><img src="DK-SS-Zatmenie-1-riesenie.svg" alt="obrázok" loading="lazy" style="width:100%"></div>

<figcaption>

**Obrázok 1:** Pohyb Mesiaca vzhľadom na Slnko počas fázy čiastočného zatmenia. Ružový bod na okraji Mesiaca (a teda aj jeho stred) prejde uhlovú vzdialenosť rovnú uhlovému priemeru slnečného kotúča.
</figcaption>

</figure>

Zostáva určiť relatívnu uhlovú rýchlosť Mesiaca. Dôležité je, že táto uhlová rýchlosť je voči Slnku, nie voči hviezdam. Preto na jej výpočet budeme potrebovať synodickú obežnú dobu Mesiaca $P_{\Mo,sy}$. Takisto nebudeme uvažovať rozdielny vplyv rotácie Zeme na zdanlivý pohyb Mesiaca a Slnka. Ten je spôsobený tým, že Mesiac je bližšie ako Slnko. Avšak, tento vplyv pohyb Mesiaca na oblohe spomaľuje, čo znamená, že sa predlžuje čas na zakrytie Slnka $t$ ktorý má výprava na cestu.

My preskúmame najhorší scenár (najrýchlejšie zatienenie), ktoré odpovedá situácii ráno alebo večer. Vtedy rotácia Zeme nijak neovplyvňuje zdanlivú rýchlosť Mesiaca na oblohe, keďže rotácia Zeme nemá zložku v tangenciálnom smere voči polohe Mesiaca. Potom 

$$
\omega_{\Mo\Sun} = \frac{\text{obvod kruhu}}{\text{perióda obehu}} = \frac{360^{\circ}}{P_{\Mo,sy}} \approx 12{,}1910\,^\circ/\mathrm{deň} \,. \tag{3}
$$

Na záver stačí dosadiť $\alpha$ a $\omega_{\Mo\Sun}$ do (1), z čoho vypočítame dobu čiastočného zatmenia 

$$
t = \frac{\alpha}{\omega_{\Mo\Sun}} = \frac{\cfrac{2 R_\Sun}{a_\Ea} \cdot \cfrac{360^{\circ}}{2\pi}}{\cfrac{360^{\circ}}{P_{\Mo,sy}}} = \frac{R_\Sun}{\pi a_\Ea} P_{\Mo,sy} \approx 63\,\mathrm{minút} \,. \tag{4}
$$

Keďže cesta autom trvá $60\,\mathrm{minút}$, tak úplné zatmenie tesne stihnú.

**Poznámka**

\
V realite by pre kruhové dráhy Zeme a Mesiaca nastávali iba prstencové zatmenia Slnka. To je dôvod, prečo sme do zadania umiestnili predpoklad o polomere Mesiaca tak, aby vytvoril dostatočne veľký tieň. Chceli sme sa vyhnúť potrebe výpočtu uhlovej rýchlosti Mesiaca na eliptickej dráhe. Prípadných záujemcov odkazujeme na rovnicu Vis viva.

</details>

## Komentár autora

Janka a Michal boli v Amerike pozorovať zatmenie Slnka. V skutočnosti im utekanie pred mrakmi zabralo oveľa dlhšie a precestovali pri tom viac ako $700\,\mathrm{km}$. Na miesto pozorovania ale dorazili pár minút pred začiatkom čiastočného zatmenia.
