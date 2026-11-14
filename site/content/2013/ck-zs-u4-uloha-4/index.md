---
title: Úloha 4
year: 2013
round: CK
roundName: Celoštátne kolo
category: ZŠ
type: teoria
typeName: Teória
label: Ú4
weight: 2004
hasSolution: true
source: ZAO:I_Zadania/02_GmtrCas/02_ZS_FI.tex
rocniky:
- '2013'
kola:
- Celoštátne kolo
kategorie:
- ZŠ
typy:
- Teória
tagy:
- Geometria a čas
collection: ZAO
---

## Zadanie

V diele K. Ptolemaia je o.i. odkaz na jedno pozorovanie úplného zatmenia Mesiaca, asi najstaršie presne zaznamenané pozorovanie:

V 27. roku Nabonassara, v noci z 29. na 30. dňa mesiaca Thot začalo hodinu po východe Mesiaca v Babylone zatmenie Mesiaca a bolo úplné... Prevod do Juliánskeho kalendára dáva pre stred zatmenia v Babylone, $\lambda = 44^{\circ}\,25'$ E, 19. marec 721 p.n.l., 21:00 hod. miestneho času. Posledné u nás pozorovateľné úplné zatmenie Mesiaca nastalo: 15. 6. 2011 so stredom o 20:14 UT. Zistite strednú synodickú periódu Mesiaca za toto obdobie!

Pozor! Pri výpočte zohľadnite, že každý štvrtý rok bol priestupný, okrem rokov 1700, 1800 a 1900. Tiež si uvedomte, že po štvrtku 4. októbri 1582 nasledoval piatok 15. október (tzv. Gregoriánska reforma), 10 dní medzi týmito dátami neexistuje. Rovnako neexistuje rok 0, pred rokom 1 n.l. bol rok 1 pred n.l.

<details class="solution">
<summary>Riešenie</summary>

Na vyriešenie úlohy stačí určiť, koľko dní uplynulo medzi uvedenými okamihmi. Čas stredu zatmenia v Babylone korigujeme na UT o $2\,\mathrm{h}$ $58\,\min$, t. j. 19. 3. 721 pred n. l., 18:02 UT.\
Priestupný bol rok 4 n. l., priestupný bol aj rok 1 pred n. l., priestupné boli aj roky 5 pred n. l., 9 pred n. l. 21 pred n.l. a aj 721 pred n. l. Zo spolu 720 rokov od roku 721 pred n. l. do roku 1 pred n. l. bolo priestupných 180 a obyčajných 540 rokov.\
Od 19. marca 721 pred n. l. do 19. marca roku 1 pred n. l. spolu uplynulo 

$$
180\cdot366+540\cdot365=262\,980\,\mathrm{dní} \, . \tag{1}
$$

 Od 19. marca roku 1 pred n. l. do 19. marca roku 1 n. l. uplynul rok s 365 dňami.\
Od 19. marca roku 1 n. l. do 19. marca roku 2011 by boli priestupnými, ak by sa nezmenil Juliánsky kalendár na Gregoriánsky, roky 4, 8, 12 n. l. , ... až 2008, t. j. bolo by spolu 502 priestupných rokov. Na obyčajné roky by zostalo z intervalu 2010 rokov práve 1508 rokov. Ich sčítaním dostaneme pre dĺžku tohto obdobia 

$$
502\cdot366+1508\cdot365=734\,152\,\mathrm{dní} \, . \tag{2}
$$

 Od 19. marca 2011 do 15. júna 2011 uplynulo spolu 12 dní marca, 30 dní apríla, 31 dní mája a 15 dní júna (pretože stred zatmenia nastal neskôr v čase UT, ako v Babylonskom zatmení), spolu 88 dní.\
Ak by zostal v platnosti Juliánsky kalendár, boli by tieto dva úkazy oddelené uplynutím súčtu týchto vyššie uvedených dní v zvolených intervaloch čísel, t.j. spolu: $997\,585\,\mathrm{dní}$.\
Reforma kalendára však 13 dní ubrala. Po štvrtku 4. 10. 1582 nasledoval piatok 15. 10. 1582, a roky 1700, 1800 a 1900 neboli po Gregoriánskej reforme priestupné. Odčítaním spolu 13 dní sa hľadaný interval zmenší na 

$$
997\,585-13=997\,572\,\mathrm{dní} \, . \tag{3}
$$

 Dopočítaním rozdielu v UT časoch maximálnej fázy zatmenia môžeme ešte pridať 

$$
20\,\mathrm{h}\ 14\,\min-18\,\mathrm{h}\ 2\,\min=2\,\mathrm{h}\ 12\,\min=0{,}092\,\mathrm{dní} \, . \tag{4}
$$

 Celkový čas medzi zatmeniami (v podstate rozdiel JD oboch udalostí) teraz delíme približnou hodnotou synodického Mesiaca, napr 29,5306. Dostaneme počet lunácií 

$$
\frac{997\,572{,}092}{29,5306}=33\,780{,}95941 \, . \tag{5}
$$

 Počet lunácií by sa tiež mohol získať z ďalších údajoch o zatmeniach, najmä ich čísla Sarosu. Zaokrúhlením počtu lunácií na najbližšie celé číslo ($33\,781$) dostávame pre strednú periódu synodického Mesiaca hodnotu 

$$
\frac{997\,572{,}092}{33\,781}=29{,}53056724\,\mathrm{dní} \, , \tag{6}
$$

 t.j. $29\,\mathrm{dní}$ $12\,\mathrm{h}$ $44\,\min$ $1\,\mathrm{s}$ stredného slnečného času.

</details>
