---
title: Pevné kosti
year: 2025
round: DK
roundName: Domáce kolo
category: SŠ
type: teoria
typeName: Teória
label: T3
weight: 3003
points: '80'
authors:
- Lukáš Hudák
hasSolution: true
source: 2025:1-DK/1-SS/03-Pevne-kosti/00-zadanie.tex
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

Pozorovateľ s pevnými kosťami stojaci na nerotujúcej neutrónovej hviezde s hmotnosťou $2{,}1\,\mathit{M}_\Sun$, vzdialenej $1400\,\mathrm{pc}$ od Zeme, pozoruje Slnko. Spektrálnou fotometriou zistil, že maximum toku žiarenia Slnka je na $\lambda = 372\,\mathrm{nm}$. Predpokladajte, že po odčítaní efektu rozpínania vesmíru sú Slnko a neutrónová hviezda vzhľadom na seba v pokoji.

<ol type="a">

<li>

<span class="body">[25 b]</span> Popíšte a vypočítajte vplyv rozpínania vesmíru (kozmologického červeného posunu) na vlnovú dĺžku slnečného svetla, ktoré zaznamenával pozorovateľ na neutrónovej hviezde.

</li>

<li>

<span class="body">[55 b]</span> Určte, či môžeme vplyv rozpínania vesmíru zanedbať voči gravitačnému posunu vlnovej dĺžky a vypočítajte polomer neutrónovej hviezdy.

</li>

</ol>

Fotón si predstavte ako malú guličku s ekvivalentnou hmotnosťou $m_F$, ktorá sa pohybuje v gravitačnom poli hmotného objektu (hviezdy). Keďže platí zákon zachovania energie, tak sa pri vzďaľovaní fotónu od hviezdy musí predlžovať jeho vlnová dĺžka. Tento efekt označujeme gravitačný červený (modrý) posun.

Ako pomôcku uvádzame vzťahy pre kinetickú ($E_K$) a potenciálnu ($E_P$) energiu fotónu vo vzdialenosti $r$ od stredu telesa s hmotnosťou $M$. 

$$
E_K (r) = \frac{hc}{\lambda(r)} \a
    E_P (r) = -G\frac{Mm_F}{r} \a
    m_F = \frac{h}{c\lambda(r)} \,, \tag{1}
$$

 kde $h$ je Planckova konštanta a $c$ je rýchlosť svetla vo vákuu. Pre záujemcov o ďalšie informácie o gravitačnom červenom a modrom posune odporúčame online dostupný zdroj: <https://vixra.org/pdf/1704.0123v1.pdf>

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

Keďže sa neutrónová hviezda a Slnko vplyvom rozpínania vesmíru vzďaľujú, budeme pozorovať červený posun $z$, ktorý je definovaný ako 

$$
z = \frac{\lambda^{\prime}-\lambda_e}{\lambda_e} \,, \tag{2}
$$

 kde $\lambda^{\prime}$ je výsledná vlnová dĺžka a $\lambda_e$ emitovaná vlnová dĺžka, ktorú môžeme vyjadriť pomocou Wienovho zákona ako 

$$
\lambda_e = \frac{b}{T_\Sun^{(C)}} \,, \tag{3}
$$

 kde $b$ je Wienova konštanta a $T_\Sun^{(C)}$ je farebná teplota Slnka. Pre malé rýchlosti vzďaľovania platí pre červený posun vzťah 

$$
z = \frac{v}{c} \,, \tag{4}
$$

 kde $c$ je rýchlosť svetla vo vákuu a $v$ je rýchlosť vzďaľovania daná Hubblovým-Lemaîtrovým zákonom 

$$
v = H_0 d\,, \tag{5}
$$

 kde $H_0$ je Hubblova-Lemaîtreva konštanta a $d$ je vzdialenosť neutrónovej hviezdy od Slnka.

Spojením vzťahov (2), (3), (4) a vyjadrením $\lambda^\prime$ dostávame 

$$
\lambda^{\prime} = \lambda_e\frac{H_0 d}{c}+\lambda_e \,, \tag{6}
$$

 pričom 

$$
\frac{H_0 d}{c} \approx 3,15\cdot10^{-7} \ll 1 \,. \tag{7}
$$

Z toho vyplýva, že $\lambda^\prime \approx \lambda_e$. Teda vieme povedať, že vplyv rozpínania vesmíru na zmenu vlnovej dĺžky je zanedbateľný.

</li>

<li>

Predstavme si prázdny vesmír, do ktorého umiestnime Slnko a vyšleme z jeho povrchu fotón. Celková energia fotónu $E$ bude súčtom jeho kinetickej energie $E_K$ a potenciálnej energie $E_P$, ktoré sú závislé na vzdialenosti $r$ od Slnka. Zákon zachovania energie hovorí 

$$
E_K(r) + E_P(r) = E = \text{konštanta} \,. \tag{8}
$$

 Teraz umiestnime ďaleko od Slnka neutrónovú hviezdu zo zadania a sledujme putovanie fotónu medzi týmito dvomi hviezdami. Fotón začne svoju cestu na povrchu Slnka. To je vzdialenosti $r = R_\Sun$ od jeho ťažiska, ktoré je centrom gravitačného pôsobenia. Neutrónová hviezda je veľmi ďaleko, takže jej gravitačný efekt môžeme zatiaľ zanedbať.

Následne fotón odletí do medzihviezdneho priestoru, ďaleko od Slnka, teda jeho potenciálna energia bude nulová, $E_P(\infty)=0$. Po čase sa priblíži k neutrónovej hviezde a začne ”cítiť” jej gravitačné pôsobenie, až dopadne na jej povrch, kedy bude vo vzdialenosti polomeru neutrónovej hviezdy $R_N$ od jej ťažiska.

Keďže je vplyv rozpínania vesmíru zanedbateľný, tak sa celková energia fotónu $E$ zachová počas jeho ”letu”. Pomocou (8) dostávame 

$$
\text{konštanta} = E = E_K(R_\Sun) + E_P(R_\Sun) = E_K(\infty) + E_P(\infty) = E_K(R_N) + E_P(R_N) \,. \tag{9}
$$

 Dosadením vzťahov (1) zo zadania dostávame pre povrch Slnka a neutrónovej hviezdy rovnosť 

$$
\frac{hc}{\lambda_\Sun} - \frac{GM_\Sun h}{cR_\Sun \lambda_\Sun} = \frac{hc}{\lambda_N} - \frac{GM_Nh}{cR_N\lambda_N} \,, \tag{10}
$$

 kde $\lambda_N$ značí pozorovanú vlnovú dĺžku na povrchu neutrónovej hviezdy, $M_N$ je hmotnosť neutrónovej hviezdy, $R_N$ je polomer neutrónovej hviezdy a analogicky index $\Sun$ značí Slnko. Vlnovú dĺžku fotónu možno znova vyjadriť pomocou Wienovho zákona (3) a po vyjadrení $R_N$ máme 

$$
R_N = \frac{GM_N}{c^2-\lambda_N\frac{T_\Sun}{b}\left(c^2-\frac{GM_\Sun}{R_\Sun}\right)} \approx \frac{GM_N}{c^2 \left( 1-\lambda_N\frac{T_\Sun^{(C)}}{b} \right)} \approx 12,8 \, \text{km} \,, \tag{11}
$$

 kde sme využili, že $c^2 \gg GM_\Sun/R_\Sun$ na aproximovanie zátvorky v menovateli.

</li>

</ol>

</details>

## Komentár autora

Netradičný príklad predstavujúci zaujímavú tému relativistickej astrofyziky.
