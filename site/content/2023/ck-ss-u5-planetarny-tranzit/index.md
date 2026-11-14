---
title: Planetárny tranzit
year: 2023
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: Ú5
weight: 2305
hasSolution: true
source: ZAO:I_Zadania/02_GmtrCas/02_SS_FI.tex
rocniky:
- '2023'
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

Jedným zo zriedkavých javov v Slnečnej sústave sú prechody planét popred slnečný disk. Zo všetkých kombinácií planét, z ktorých jav pozorujeme, a planét, ktoré popred Slnko prechádzajú, je prechod Uránu popred slnečný disk pozorovaný z Neptúnu ten najzriedkavejší. Uvažujte, že dráhy Uránu a Neptúna sú kruhové a ich ostatné parametre sú dané údajmi v tabuľke. Ďalej uvažujme, že tento tranzit pozorujeme zo Zeme.

|        | veľká poloos | sklon dráhy | dĺžka výstupného uzla | polomer planéty |
|:-------|:------------:|:-----------:|:---------------------:|:---------------:|
| Urán   |  $19{,}19\,\mathrm{au}$   |  $0{,}773^{\circ}$  |       $74{,}0^{\circ}$       |    $25\,360\,\mathrm{km}$    |
| Neptún |  $30{,}07\,\mathrm{au}$   |  $1{,}770^{\circ}$  |       $131{,}8^{\circ}$       |    $24\,620\,\mathrm{km}$    |

**Úlohy:**

<ol type="a">

<li>

V akom súhvezdí sa budú planéty počas prechodu nachádzať?

</li>

<li>

O koľko magnitúd Neptún potemnie?

</li>

<li>

Ako najdlhšie môže trvať úplná fáza tranzitu? Ako najdlhšie môže trvať tranzit medzi 1. a 4. kontaktom?

</li>

</ol>

<details class="solution">
<summary>Riešenie</summary>

<ol type="a">

<li>

V tejto úlohe musíme nájsť smer, v ktorom sa dráhy Uránu a Neptúnu pretínajú. Presné riešenie by si vyžadovalo sférickú trigonometriu, vďaka malým sklonom však môžeme postupovať aj nasledovne. Pre ekliptikálnu šírku planét $\beta$ máme približne

</li>

</ol>

$$
\beta = i\sin (\lambda -\Omega) \, . \tag{1}
$$

 kde $i$ je sklon dráhy, $\lambda$ je ekliptikálna dĺžka a $\Omega$ je dĺžka výstupného uzla. Priesečník dráh sa nachádza v mieste, kde sa rovnajú ekliptikálne šírky oboch planét. 

$$
i_{\Ur}\sin (\lambda -\Omega_{\Ur})=i_{\Ne}\sin (\lambda -\Omega_{\Ne}) \, . \tag{2}
$$

 Využijeme vzorec pre sínus rozdielu uhlov 

$$
\sin (x-y)=\sin x\cos y-\cos x\sin y \, , \tag{3}
$$

 

$$
i_{\Ur}(\sin \lambda\cos \Omega_{\Ur}-\cos \lambda\sin \Omega_{\Ur})=i_{\Ne}(\sin \lambda\cos \Omega_{\Ne}-\cos \lambda\sin \Omega_{\Ne}) \, , \tag{4}
$$

 

$$
\sin \lambda (i_{\Ur} \cos \Omega_{\Ur} - i_{\Ne} \cos \Omega_{\Ne})=\cos \lambda(i_{\Ur}\sin \Omega_{\Ur}-i_{\Ne} \sin \Omega_{\Ne}) \, , \tag{5}
$$

 

$$
\tan \lambda=\frac{i_{\Ur}\sin \Omega_{\Ur}-i_{\Ne} \sin \Omega_{\Ne}}{i_{\Ur} \cos \Omega_{\Ur} - i_{\Ne} \cos \Omega_{\Ne}} \, , \tag{6}
$$

 

$$
\tan \lambda=\frac{0{,}773^{\circ}\cdot\sin (74^{\circ}) - 1{,}77^{\circ}\cdot \sin (131{,}8^{\circ})}{0,773\cdot \cos (74^{\circ}) - 1{,}77^{\circ}\cdot \cos (131{,}8^{\circ})}=-0,414 \, . \tag{7}
$$

 Existujú dve možné riešenia, $\lambda_1=157{,}5^{\circ}$ a $\lambda_2=337{,}5^{\circ}$. Tieto ekliptikálne dĺžky sú heliocentrické - merané z pohľadu Slnka. Obidve planéty sú ďaleko od Zeme, preto ich poloha z pohľadu Zeme bude veľmi podobná. Na základe ekliptikálnych dĺžok sa dá odhadnúť, že planéty sa budú nachádzať v súhvezdí Vodnár alebo Lev.

<ol type="a" start="2">

<li>

Najskôr určíme uhlové priemery Slnka a Uránu pri pohľade z Neptúna. Pre Slnko máme

</li>

</ol>

$$
\theta_{\Sun}=\frac{2R_{\Sun}}{a_{\Ne}}=\frac{2\cdot6{,}955 \cdot 10^{8}}{30,07\cdot1{,}496 \cdot 10^{11}}=3{,}09 \cdot 10^{-4}\,\mathrm{rad}=63{,}8'' \, . \tag{8}
$$

 Uhlový priemer Uránu je 

$$
\theta_{\Ur}=\frac{2R_{\Ur}}{a_{\Ne}-a_{\Ur}}=\frac{2\cdot2{,}536 \cdot 10^{7}}{(30,07-19,19)\cdot1{,}496 \cdot 10^{11}}=3{,}12 \cdot 10^{-5}\,\mathrm{rad}=6{,}4'' \, . \tag{9}
$$

 Pre pokles jasnosti Neptúnu si stačí uvedomiť, že jeho jasnosť poklesne rovnako, ako množstvo svetla, ktoré k nemu prichádza od Slnka. Pre pokles tak máme 

$$
\Delta m = 2,5\log \left(\frac{\theta_{\Sun}^2-\theta_{\Ur}^2}{\theta_{\Sun}^2}\right)=2,5\log \left(\frac{63,8^2-6,4^2}{63,8^2}\right)=-0,011 \, . \tag{10}
$$

<ol type="a" start="3">

<li>

Dobu trvania určíme ako podiel uhlovej vzdialenosti, o ktorú sa pri pohľade z Neptúna musia Slnko a Urán vzájomne pohnúť pri centrálnom zákryte a uhlovej rýchlosti, ktorou sa voči sebe Urán a Slnko pri pohľade z Neptúna pohybujú

</li>

</ol>

$$
t_{14}=\frac{\theta_{\Sun}+\theta_{\Ur}}{\omega_{\Sun}+\omega_{\Ur}} \, , \tag{11}
$$

 

$$
t_{23}=\frac{\theta_{\Sun}-\theta_{\Ur}}{\omega_{\Sun}+\omega_{\Ur}} \, . \tag{12}
$$

 Uhlová rýchlosť Slnka voči Neptúnu je rovnaká ako uhlová rýchlosť Neptúnu voči Slnku 

$$
\omega_{\Sun}=\frac{v_{\Ne}}{a_{\Ne}}=\sqrt{\frac{GM_{\Sun}}{a_{\Ne}^3}}=\sqrt{\frac{6{,}67 \cdot 10^{-11}\cdot1{,}9891 \cdot 10^{30}}{(30,07\cdot1{,}496 \cdot 10^{11})^3}}=1{,}2 \cdot 10^{-9}\,\mathrm{rad}\,{\mathrm{s}}^{-1} \, . \tag{13}
$$

 Uhlovú rýchlosť Uránu voči Neptúnu získame ako podiel vzájomnej rýchlosti Uránu a Neptúnu a ich vzdialenosti 

$$
\omega_{\Ur}=\frac{v_{\Ur}-v_{\Ne}}{a_{\Ne}-a_{\Ur}} \tag{14}
$$

 Obežné rýchlosti Uránu a Neptúnu sú 

$$
v_{\Ur}=\sqrt{\frac{GM_{\Sun}}{a_{\Ur}}}=\sqrt{\frac{6{,}67 \cdot 10^{-11}\cdot1{,}9891 \cdot 10^{30}}{19,19\cdot1{,}496 \cdot 10^{11}}}=6798\,\mathrm{m}\,{\mathrm{s}}^{-1} \, , \tag{15}
$$

 

$$
v_{\Ne}=\sqrt{\frac{GM_{\Sun}}{a_{\Ne}}}=\sqrt{\frac{6{,}67 \cdot 10^{-11}\cdot1{,}9891 \cdot 10^{30}}{30,07\cdot1{,}496 \cdot 10^{11}}}=5431\,\mathrm{m}\,{\mathrm{s}}^{-1} \, . \tag{16}
$$

 Uhlová rýchlosť Uránu je teda 

$$
\omega_{\Ur}=\frac{6798-5431}{(30,07-19,19)\cdot1{,}496 \cdot 10^{11}}=8{,}4 \cdot 10^{-10}\,\mathrm{rad}\,{\mathrm{s}}^{-1} \, . \tag{17}
$$

 Dĺžka trvania maximálneho tranzitu je 

$$
t_{23}=\frac{63,8-6,4}{206\,265\cdot(1{,}2 \cdot 10^{-9}+8{,}4 \cdot 10^{-10})}=1{,}36 \cdot 10^{5}\,\mathrm{s}=37{,}9\,\mathrm{h} \, . \tag{18}
$$

 Maximálny čas medzi 1. a 4. kontaktom je 

$$
t_{14}=\frac{63,8+6,4}{206\,265\cdot(1{,}2 \cdot 10^{-9}+8{,}4 \cdot 10^{-10})}=1{,}67 \cdot 10^{5}\,\mathrm{s}=46{,}3\,\mathrm{h} \, . \tag{19}
$$

</details>
