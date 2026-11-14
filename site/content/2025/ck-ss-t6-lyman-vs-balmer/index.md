---
title: Lyman vs Balmer
year: 2025
round: CK
roundName: Celoštátne kolo
category: SŠ
type: teoria
typeName: Teória
label: T6
weight: 2306
points: '70'
authors:
- Samuel Amrich
hasSolution: true
source: 2025:3-CK/1-SS/06-Lyman-vs-Balmer/00-zadanie.tex
rocniky:
- '2025'
kola:
- Celoštátne kolo
kategorie:
- SŠ
typy:
- Teória
tagy:
- Nezaradené
---

## Zadanie

Jeden nadaný astrofyzik si počas štúdií veľmi obľúbil Johanna Jakoba Balmera, ale zato sa mu znepáčil Theodore Lyman IV. Preto sa rozhodol, že vytvorí hypotetickú časticu Košicetrón, ktorá má úplne rovnaké vlastnosti ako elektrón, ale má inú hmotnosť. Pomocou nej vytvoril nový atóm vodíka, v ktorého obale nie je elektrón, ale práve Košicetrón. Akú hmotnosť $m_K$ musí mať Košicetrón, v hmotnostiach elektrónu $m_e$, aby nová čiara Lyman-$\alpha$ mala vlnovú dĺžku ako pôvodná čiara Balmer-$\alpha$? Na akú vlnovú dĺžku sa posunie nová čiara Balmer-$\alpha$? Je táto čiara stále okom viditeľná?

Pre občerstvenie pamäte, Lymanova čiara $\alpha$ je vzniká prechodom elektrónu v atóme vodíka z druhej na prvú hladinu ($2\rightarrow1$) a Balmerova čiara $\alpha$ je vzniká prechodom elektrónu v atóme vodíka z tretej na druhú energetickú hladinu ($3\rightarrow2$). Energiám prechodov zodpovedajú vlnové dĺžky 

$$
\lambda_{L\alpha} = 121{,}567\,\mathrm{nm} \a \lambda_{B\alpha} =656{,}279\,\mathrm{nm} \,, \tag{1}
$$

 pre Lyman-$\alpha$, respektíve Balmer-$\alpha$ čiaru. Pre výpočet budete potrebovať Rydbergov vzorec. Ak ho nepoznáte, viete si ho odvodiť z predpokladu, že elektrón, respektíve Košicetrón, obieha okolo nehybného protónu po stabilnej kruhovej dráhe a moment hybnosti je kvantovaný 

$$
L=n\hbar \,, \tag{2}
$$

 kde $\hbar=h/2\pi$ je redukovaná Planckova konštanta a $n$ je hlavné kvantové číslo, číslo hladiny.

<details class="solution">
<summary>Riešenie</summary>

Ako prvé si musíme uvedomiť niekoľko základných pojmov, s ktorými pracujeme. Obe čiary odkazujú na prechody elektrónu medzi energetickými hladinami v atóme vodíka, ako je spomenuté v zadaní. Preto musíme vedieť akú energiu uvoľní elektrón pri prechode medzi dvoma hladinami v atóme vodíka. K tomu si buď pamätáme Rydbergov vzorec 

$$
\frac{1}{\lambda} = R_H\cdot \left(  \frac{1}{n_2^2}-\frac{1}{n_1^2} \right) \,, \tag{3}
$$

kde $n_1$ je pôvodná hladina, $n_2$ je koncová hladina a $R_H$ je Rydbergova konštanta. Keď si tento vzorec ale nepamätáme, musíme si ho odvodiť. Cesta k tomu je trošku náročnejšia, ale v zásade ľahko pochopiteľná.

Celková energia $E$ elektrónu obiehajúceho na energetickej hladine okolo jadra atómu vodíka (protónu) je 

$$
E=E_K+E_P \, . \tag{4}
$$

Kde $E_K$ je kinetická energia a $E_P$ je potenciálna energia. Kinetická energia je jednoducho 

$$
E_K=\frac{1}{2} m v^2 \, . \tag{5}
$$

A potenciálna energia pochádza iba čisto z elektromagnetickej sily, teda 

$$
E_P=\frac{q_1 q_2}{4\pi\epsilon r} = -\frac{e^2}{4\pi\epsilon r}\, . \tag{6}
$$

Kde $\epsilon$ je permitivita vákua z konštantovníka. Zároveň musíme pridať jednu zásadnú vec, kvantovanie momentu hybnosti v tvare 

$$
L=rm v=n\hbar \, . \tag{7}
$$

Aby sme túto trojicu vzťahov vedeli úspešne spojiť, pridám ešte jednu znalosť, je to tak trochu skratka, ale v astronómii veľmi dobre známa; je to viriálová teoréma. Možno bežnejšie sa človek stretne s odvodením cez vzťahy pre kruhové dráhy (ktoré je hodnotené taktiež plným počtom bodov), ale odvodenie cez viriálovú teorému mi osobne príde ako ťažšie na pokazenie, resp. je menšia šanca v ňom urobiť chybu. 

$$
E_P+2E_K=0 \, . \tag{8}
$$

Takže po dosadení $E_K$ a $E_P$ 

$$
-\frac{e^2}{4\pi\epsilon r} +m v^2 =0 \, . \tag{9}
$$

Po vynásobení $r$ 

$$
-\frac{e^2}{4\pi\epsilon} +r m v^2 =0  \, . \tag{10}
$$

Kde vidíme, že druhý člen v súčte je podobný definícií $L$. 

$$
-\frac{e^2}{4\pi\epsilon} +\frac{L^2}{m r} = 0 \, . \tag{11}
$$

Zároveň vieme o kvantovaní, tak ho tam dosadíme 

$$
-\frac{e^2}{4\pi\epsilon} +\frac{n^2 \hbar^2}{m r} =0  \, . \tag{12}
$$

Z čoho už nepoznáme iba $r$, ktoré osamostatníme 

$$
r=\frac{n^2 \hbar^2 4\pi\epsilon}{m e^2}  \, . \tag{13}
$$

Čo ale ešte nie je výsledok, ktorý potrebujeme. Nás zaujíma energia. Preto si spomenieme, že celková energia je rovná $E=E_K+E_P$ a, že $E_K=-1/2 E_P$ z viriálovej teorémy. Teda celková energia je rovná $E=E_P-1/2E_P=1/2E_P$ 

$$
E=\frac{1}{2}E_P=\frac{1}{2}\frac{e^2}{4\pi\epsilon r}=\frac{1}{2}\frac{e^2}{4\pi\epsilon}\cdot\frac{m e^2}{n^2 \hbar^2 4\pi\epsilon}=-\frac{1}{32}\frac{e^4 m}{\pi^2 \epsilon^2 n^2 \hbar^2 }= -\frac{e^4 m}{8\epsilon^2 n^2 h^2 }  =-R\frac{1}{n^2}   \,. \tag{14}
$$

Kde v poslednom kroku sme $\hbar$ nahradila obyčajným, ktoré sú prepojené podľa vzorca $\hbar=h/2\pi$. Takto sme získali vzťah pre energiu elektrónu na nejakej energetickej hladine $n$. Nás ale zaujíma rozdiel medzi dvojicou hladín. Vyžiarená energia sa dá zapísať nasledovne 

$$
E_\gamma = h\nu = \frac{ch}{\lambda} =\Delta E=E_{n_2}-E_{n_1}=-R\frac{1}{n_2^2}+R\frac{1}{n_1^2}=R\left(\frac{1}{n_1^2}-\frac{1}{n_2^2}\right)  \, . \tag{15}
$$

$$
\frac{1}{\lambda}=\frac{R}{ch}\left(\frac{1}{n_1^2}-\frac{1}{n_2^2}\right)=R_H\left( \frac{1}{n_1^2}-\frac{1}{n_2^2} \right)     \, . \tag{16}
$$

Takto sme získali hľadaný Rydbergov vzorec. Pričom $R$ je len pomocná konštanta a až po jej vydelení veličinou $ch$ získavame konštantu $R_H$, ktorá je známa aj ako Rydbergova konštanta. Pre prehľadnosť, vzťah pre Rydbergovu konštantu vodíka je 

$$
R_H=\frac{e^4 m}{8\epsilon^2 h^3 c} \,. \tag{17}
$$

Teraz môžeme pristúpiť k samotnému riešeniu.

Pôvodné vlnové dĺžky majú označenie 

$$
\lambda_{L\alpha} \a \lambda_{B\alpha} \,. \tag{18}
$$

 Nech Lymanova $\alpha$ čiara tvorená Košicetrónom má označenie $\lambda_{L\alpha}^{\prime}$. Zo zadania nám je jasné, že 

$$
\lambda_{L\alpha}^{\prime}=\lambda_{B\alpha} \,. \tag{19}
$$

 Po plnom rozpísaní cez rovnicu 16, kde musíme počítať s tým, že hmotnosť Košicetrónu mení $R_H$ na $R_H^{\prime}$ a zároveň, že Lymanova čiara je spôsobená prechodom ($2\rightarrow1$) a Balmerova je spôsobená prechodom ($3\rightarrow2$) získame vzťah 

$$
\frac{1}{\lambda_{L\alpha}^{\prime}}=R_H^{\prime}\left( \frac{1}{1^2}-\frac{1}{2^2} \right) = \frac{1}{\lambda_{B\alpha}}=R_H\left( \frac{1}{2^2}-\frac{1}{3^2} \right) \,. \tag{20}
$$

 

$$
\frac{1}{\lambda_{L\alpha}^{\prime}}=R_H^{\prime}\left( \frac{1}{1}-\frac{1}{4} \right) = \frac{1}{\lambda_{B\alpha}}=R_H\left( \frac{1}{4}-\frac{1}{9} \right) \,. \tag{21}
$$

 

$$
\frac{1}{\lambda_{L\alpha}^{\prime}}=R_H^{\prime}\left( \frac{3}{4} \right) = \frac{1}{\lambda_{B\alpha}}=R_H\left( \frac{5}{36} \right) \,. \tag{22}
$$

Keď sa ale bližšie pozrieme na rovnicu 14, kde je zadefinovaná $R_H$, vidíme, že ju vieme rozpísať ako $R_H=C\cdot m$, kde $C$ je konštanta a $m$ je hmotnosť orbitujúcej nabitej častice. Nech podľa zadania $m_e$ je hmotnosť elektrónu a $m_K$ hmotnosť Košicetrónu. Potom rovnica 22 sa dá rozpísať ako 

$$
C\cdot m_K\frac{3}{4} =C\cdot m_e\frac{5}{36} \,. \tag{23}
$$

 Nás zaujíma $m_K$, ktoré osamostatníme ako 

$$
m_K = \frac{5}{27}m_e \approx 1{,}687 \cdot 10^{-31}\,\mathrm{kg} \,. \tag{24}
$$

V druhej časti príkladu máme zistiť, na akú vlnovú dĺžku sa teraz posunie Balmerova $\alpha$ čiara v atóme vodíka s Košicetrónom. Začnime napísaním Rydbergovho vzorca pre Balmerovu $\alpha$ s elektrónom a Košicetrónom 

$$
\frac{1}{\lambda_{B\alpha}} = \frac{5}{36}R_H = \frac{5}{36}C\cdot m_e\a \frac{1}{\lambda_{B\alpha}^{\prime}} = \frac{5}{36}C\cdot m_K = \frac{5}{36}C\cdot \frac{5}{27}m_e  \,. \tag{25}
$$

Teraz predelíme prvý výraz druhým 

$$
\frac{\cfrac{1}{\lambda_{B\alpha}}}{\cfrac{1}{\lambda_{B\alpha}^{\prime}}}= \frac{\lambda_{B\alpha}^{\prime}}{\lambda_{B\alpha}} = \frac{\cfrac{5}{36}C\cdot m_e}{ \cfrac{5}{36}C\cdot \cfrac{5}{27}m_e} = \frac{27}{5} \,. \tag{26}
$$

Čo po vydestilovaní podstatnej informácie predstavuje vzťah 

$$
\lambda_{B\alpha}^{\prime} = \frac{27}{5}\lambda_{B\alpha} \approx 3544\,\mathrm{nm} \,, \tag{27}
$$

hodnota ďaleko mimo viditeľnej oblasti.

</details>

## Komentár autora

Spektrografia je zaujímavá oblasť a možnosť preskúmať zmenu vlnových dĺžok v závislosti od hmotnosti nabitej častice v obale atómu komplexne overí, či účastník rozumie atómovej fyzike.
