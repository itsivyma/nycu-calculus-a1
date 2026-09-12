# Homework 1 零基礎雙語完整教學

> 下次考試範圍先以 Homework 1 為準。這份講義把作業需要的前置觀念、課本 §1.3–§1.5、老師 Lecture 1–2，以及微積分小組共同勾選題串在一起。

## 0. 範圍與使用方式

- 作業：Homework 1，共 20 題，繳交日 2026-09-14。
- 老師講義：Lecture 1（實數、上確界、指數）與 Lecture 2（函數、反函數、對數、反三角函數）。
- 課本：Stewart, Clegg, Watson, Calculus: Early Transcendentals, 9th ed., Metric Version。
- 課本頁碼：§1.3 pp. 36–44、§1.4 pp. 45–53、§1.5 pp. 54–66。
- 共同勾選題：§1.4 #2, 9, 13, 17；§1.5 #18, 26, 30, 44, 58, 63, 74, 77, 81。

建議每一段依序做三件事：

1. 先讀「核心觀念」，不看答案重做範例。
2. 遮住解答完成 Homework 題目，再用「檢查點」抓錯。
3. 最後做共同勾選題，確認同一觀念換一種問法仍會做。

### 給第一次學微積分的你

這份 Homework 還沒有真正開始微分，主要是在建立之後學微積分一定會用到的「函數語言」。所以現在看不懂符號很正常。先不要背整頁公式；每看到一個式子，都依序問：

1. 每個符號叫什麼？
2. 這個式子在說什麼？
3. 哪些數可以代進去？
4. 這一步用了哪一條規則？

本講義會把計算拆成小步。第一次讀時，請拿紙筆把每一行重寫一次。只用眼睛看，常會產生「好像懂了」的錯覺；能自己寫出下一行，才是真的懂。

### 最先要會讀的符號

| 符號 | 怎麼念 | 白話意思 | 例子 |
| --- | --- | --- | --- |
| $x\in A$ | $x$ 屬於 $A$ | $x$ 是集合 $A$ 裡的一員 | $2\in\{1,2,3\}$ |
| $x\notin A$ | $x$ 不屬於 $A$ | $x$ 不在集合 $A$ 裡 | $4\notin\{1,2,3\}$ |
| $\mathbb R$ | 實數集合 | 數線上的所有數 | $-2,\sqrt2,\pi\in\mathbb R$ |
| $\mathbb Q$ | 有理數集合 | 可以寫成整數比的數 | $2/3\in\mathbb Q$ |
| $\iff$ | 若且唯若 | 左右兩句完全等價，可以雙向推 | $x^2=4\iff x=\pm2$ |
| $\ne$ | 不等於 | 左右不同 | $3\ne4$ |
| $\cap$ | 交集 | 同時符合兩邊 | $[0,3]\cap[2,5]=[2,3]$ |
| $\cup$ | 聯集 | 符合任一邊 | $(-\infty,0)\cup(0,\infty)$ |
| $\sqrt[n]a$ | $a$ 的 $n$ 次方根 | 正的數，做 $n$ 次方會得到 $a$ | $\sqrt[3]8=2$ |
| $\sup A$ | $A$ 的上確界 | 所有上界中最小的一個 | $\sup(0,1)=1$ |
| $f\circ g$ | $f$ 合成 $g$ | 先做 $g$，再做 $f$ | $(f\circ g)(x)=f(g(x))$ |
| $f^{-1}$ | $f$ 的反函數 | 把輸入、輸出的角色交換 | 若 $f(2)=5$，則 $f^{-1}(5)=2$ |

### 區間符號怎麼看

- $[a,b]$：包含兩端，也就是 $a\le x\le b$。
- $(a,b)$：不包含兩端，也就是 $a<x<b$。
- $[a,b)$：包含 $a$，不包含 $b$。
- 無限大永遠配小括號，例如 $(-\infty,3]$；因為 $\infty$ 不是一個可以「包含」的數。
- $\mathbb R\setminus\{1\}$：所有實數，但挖掉 1。

例如

$$
x>-2\quad\text{而且}\quad x\ne1
$$

可寫成

$$
(-2,1)\cup(1,\infty).
$$

### 等號每一步都要有理由

以下是本講義最常使用的四種動作：

1. **代入定義**：把 $4^x$ 寫成 $(2^x)^2$。
2. **等式兩邊做同一件事**：例如兩邊同減 4。
3. **套公式**：例如 $a^ma^n=a^{m+n}$。
4. **檢查限制**：分母不能為 0、偶次根號內不能為負、對數真數必須大於 0。

看到解答從第一行跳到第二行時，請先試著指出是哪一種動作。若說不出來，就不要急著往下讀。

### 零基礎建議順序

不要直接從 Homework #1 一路硬算到 #20。比較容易理解的順序是：

1. 指數與根式：第 3 節，接著做 Homework #2–6。
2. 函數與定義域：第 4 節，接著做 #7–9。
3. 反函數：第 5 節，接著做 #10–12。
4. 對數：第 6 節，接著做 #13–17。
5. 反三角函數：第 7 節，接著做 #18–20。
6. 最後回頭學上確界並完成 #1；這題比較抽象，第一次卡住很正常。

### 原始資料

- [老師課程網站](https://catalin-carstea.github.io/courses/calculus1-2026.html)
- [Homework 1 原題](https://catalin-carstea.github.io/courses/calculus1-2026/homework-01.pdf)
- [微積分小組 9E 共同習題](https://calculus.math.nycu.edu.tw/calculusmath/ch/app/artwebsite/view?module=artwebsite&id=39529&serno=3e458c4c-38ac-4e7a-b6c2-4499670c07ba)
- [Lecture 1 本機講義](../../course-materials/lecture-notes/lecture-01-real-numbers-exponentials-student.pdf)
- [Lecture 2 本機講義](../../course-materials/lecture-notes/lecture-02-functions-inverses-logarithms-student.pdf)

本機課本已核對為指定版本：書名、作者、Ninth Edition、Metric Version 與 ISBN 978-0-357-11351-6 均吻合。課本 PDF 有第三方浮水印，因此不納入 Git；本講義只保留自行整理的觀念與解法。

## 1. 考試能力地圖

| 能力 | 課本 | Lecture Notes | Homework | 共同題 |
| --- | --- | --- | --- | --- |
| 上界、最小上界、是否取到 | 前置實數觀念 | Lecture 1 | #1 | — |
| 根式、實數指數、指數律 | §1.4 | Lecture 1 | #2–4 | §1.4 #2 |
| 指數函數、單調性、方程與不等式 | §1.4 | Lecture 1 | #5–6 | §1.4 #9, 13, 17 |
| 函數運算、合成、定義域、函數相等 | §1.3 | Lecture 2 | #7–9 | — |
| 一對一與反函數 | §1.5 | Lecture 2 | #10–12 | §1.5 #18, 26, 30 |
| 對數律、方程、不等式 | §1.5 | Lecture 2 | #13–17 | §1.5 #44, 58, 63 |
| 反三角函數主值 | §1.5 | Lecture 2 | #18–20 | §1.5 #74, 77, 81 |

---

## 2. 核心觀念一：上界與最小上界

### 2.1 定義

若對集合 $A$ 的每個 $x$ 都有 $x\le M$，則 $M$ 是 $A$ 的上界。所有上界中最小的那個叫做上確界，記為 $\sup A$。

「最大值」與「上確界」要分開：

- 最大值必須屬於集合。
- 上確界可以不屬於集合。
- 若 $\sup A\in A$，它同時就是 $\max A$。

Lecture 1 使用的實數完備性是：每個非空且有上界的實數集合都有最小上界。

### 2.2 標準證明模板

要證明 $\sup A=s$，通常做兩步：

1. 證明對所有 $x\in A$，都有 $x\le s$，所以 $s$ 是上界。
2. 證明任何 $t<s$ 都不可能是上界；也就是能在 $A$ 中找到 $x>t$。

### 2.3 先用數線建立直覺

考慮 $A=(0,1)$。集合裡有 $0.9,0.99,0.999$，可以無限靠近 1，但沒有 1。

- 1 是上界，因為集合中沒有數會超過 1。
- 2 也是上界，但它不是最小的。
- 0.99 不是上界，因為集合裡還有 0.999 比它大。
- 因此最小上界是 1，但集合沒有最大值。

再看 $B=(0,1]$。它的上確界仍是 1，但這次 $1\in B$，所以 1 同時是最大值。

**一句話分辨：** 上確界問「天花板最低能放在哪裡」；最大值問「集合裡有沒有一個最高的成員」。

### 2.4 你先試

對集合 $(-3,5)$ 與 $(-3,5]$，兩者的上確界都是多少？哪一個有最大值？

答案：兩者上確界都是 5；只有 $(-3,5]$ 有最大值 5。

---

## 3. 核心觀念二：根式、實數指數與指數函數

### 3.0 什麼是次方？

$2^4$ 表示四個 2 相乘：

$$
2^4=2\cdot2\cdot2\cdot2=16.
$$

在 $a^r$ 中，$a$ 叫「底數」，$r$ 叫「指數」。指數告訴我們如何對底數做乘法或其延伸運算。

### 3.1 指數律

對正底數 $a,b>0$：

$$
a^r a^s=a^{r+s},\qquad
\frac{a^r}{a^s}=a^{r-s},\qquad
(a^r)^s=a^{rs},\qquad
(ab)^r=a^r b^r.
$$

負指數表示倒數：$a^{-r}=1/a^r$。分數指數表示根式：$a^{m/n}=(\sqrt[n]{a})^m$。

不要把以下兩件事混在一起：

$$
a^ma^n=a^{m+n}
$$

是「同底數相乘，指數相加」；但是

$$
(a^m)^n=a^{mn}
$$

是「次方再做次方，指數相乘」。

小例子：

$$
2^3\cdot2^4=2^{3+4}=2^7,
$$

$$
(2^3)^4=2^{3\cdot4}=2^{12}.
$$

兩個答案不同，因為原本的運算不同。

### 3.2 負指數與分數指數

為了讓指數律一直成立，我們定義

$$
a^{-n}=\frac1{a^n}.
$$

例如

$$
2^{-3}=\frac1{2^3}=\frac18.
$$

而

$$
a^{1/n}=\sqrt[n]a,
$$

所以

$$
a^{m/n}=(a^{1/n})^m=(\sqrt[n]a)^m.
$$

例如

$$
8^{2/3}=(\sqrt[3]8)^2=2^2=4.
$$

閱讀 $a^{m/n}$ 時，可以先看分母 $n$：「先開 $n$ 次根」；再看分子 $m$：「結果做 $m$ 次方」。

### 3.3 單調性是解不等式的關鍵

- $a>1$ 時，$a^x$ 嚴格遞增，所以 $a^u\le a^v\iff u\le v$。
- $0<a<1$ 時，$a^x$ 嚴格遞減，所以 $a^u\le a^v\iff u\ge v$。

常見失分點：底數小於 1 時忘記反向。

為什麼要反向？用底數 $1/2$ 看就很清楚：

$$
\left(\frac12\right)^1=\frac12,\qquad
\left(\frac12\right)^2=\frac14,\qquad
\left(\frac12\right)^3=\frac18.
$$

指數從 1 變大到 3，結果反而從 $1/2$ 變小到 $1/8$。因此比較指數時，不等號方向會相反。

### 3.4 指數方程

看到 $4^x$ 與 $2^x$ 同時出現，令 $u=2^x>0$，則 $4^x=u^2$。先解代數方程，再把 $u$ 換回去。

這叫做「代換」。它把陌生的指數方程暫時變成熟悉的二次方程：

$$
4^x-5\cdot2^x+4=0
$$

先利用 $4^x=(2^x)^2$，再令 $u=2^x$：

$$
u^2-5u+4=0.
$$

解完 $u$ 之後還沒有結束；一定要再解 $2^x=u$，才能得到原本的 $x$。

---

## 4. 核心觀念三：函數不只是一條公式

一個函數由「定義域、對應規則、陪域」共同決定。因此兩條相同的化簡公式，只要定義域不同，就不是同一個函數。

### 4.0 把函數想成一台機器

函數接收一個允許的輸入，按照固定規則，產生唯一一個輸出。若

$$
f(x)=2x+1,
$$

把 $x=3$ 放進去，就得到

$$
f(3)=2\cdot3+1=7.
$$

$f(3)$ 不是 $f$ 乘以 3；它念作「$f$ 在 3 的值」。

- **定義域**：允許放進機器的輸入。
- **函數值**：機器對某個輸入產生的輸出。
- **值域**：實際可能產生的所有輸出。

### 4.1 怎麼找定義域

若題目沒有另外指定，先假設輸入是實數，再排除不合法的值。這份作業最常見三種限制：

1. 分母不能為 0。
2. 偶次根號裡面不能小於 0。
3. 對數真數必須大於 0。

例一：

$$
f(x)=\frac1{x-2}.
$$

因為 $x=2$ 會讓分母變成 0，所以

$$
D_f=\mathbb R\setminus\{2\}.
$$

例二：

$$
g(x)=\sqrt{3-x}.
$$

根號內要滿足 $3-x\ge0$，所以 $x\le3$：

$$
D_g=(-\infty,3].
$$

注意根號可以等於 0，因此端點 3 要包含。

### 4.2 函數運算的定義域

$$
D_{f+g}=D_f\cap D_g,\qquad
D_{fg}=D_f\cap D_g,
$$

$$
D_{f/g}=\{x\in D_f\cap D_g:g(x)\ne0\}.
$$

合成函數的規則是

$$
D_{f\circ g}=\{x\in D_g:g(x)\in D_f\}.
$$

不要只找最外層函數的限制；必須先讓內層有定義，再讓內層輸出落入外層定義域。

### 4.3 合成函數為什麼要由右往左

若 $f(x)=\sqrt x$、$g(x)=x-2$，那麼

$$
(f\circ g)(x)=f(g(x))=f(x-2)=\sqrt{x-2}.
$$

意思是輸入 $x$ 先經過 $g$ 變成 $x-2$，再把結果送進 $f$ 開根號。因此必須有 $x-2\ge0$，也就是 $x\ge2$。

交換次序則得到

$$
(g\circ f)(x)=g(f(x))=g(\sqrt x)=\sqrt x-2,
$$

此時只需要 $x\ge0$。所以合成次序通常不能交換。

### 4.4 函數公式化簡後，洞不會自動補回去

例如

$$
\frac{x^2-9}{x-3}
=\frac{(x-3)(x+3)}{x-3}
=x+3.
$$

約分的前提是 $x-3\ne0$。因此化簡後仍要保留 $x\ne3$；原圖在 $(3,6)$ 有一個洞。這正是 Homework #9 想檢查的觀念。

---

## 5. 核心觀念四：反函數

函數要有反函數，必須一對一；圖形上等價於通過水平線測試。找反函數：

1. 寫 $y=f(x)$。
2. 交換 $x,y$。
3. 解出 $y$。
4. 寫出反函數的定義域與值域。
5. 用 $f(f^{-1}(x))=x$ 與 $f^{-1}(f(x))=x$ 驗證。

反函數的圖形是原圖對直線 $y=x$ 的鏡射。原函數的定義域與值域會互換。

### 5.1 反函數不是倒數

這兩個符號很像，但意思完全不同：

$$
f^{-1}(x)\ne\frac1{f(x)}.
$$

- $f^{-1}$ 是反函數，用來撤銷 $f$ 做的事。
- $1/f(x)$ 是函數值的倒數。

例如 $f(x)=2x+3$。要撤銷它，就把「乘 2、加 3」倒過來做成「減 3、除以 2」：

$$
f^{-1}(x)=\frac{x-3}{2}.
$$

檢查：

$$
f^{-1}(f(x))
=\frac{(2x+3)-3}{2}
=x.
$$

### 5.2 為什麼要一對一

若 $f(x)=x^2$，則 $f(2)=4$，也有 $f(-2)=4$。現在問「輸出 4 原本來自哪個輸入」，答案可能是 2 或 $-2$，無法唯一決定，所以在整個實數域上沒有反函數。

若把定義域限制為 $x\ge0$，每個輸出只會對應一個輸入，此時反函數才是

$$
f^{-1}(x)=\sqrt x.
$$

Homework #10 限制定義域的目的，就是讓平方函數變成一對一。

### 5.3 交換的是角色，不只是字母

由 $y=f(x)$ 求反函數時交換 $x,y$，是因為原本的「輸入 $x$、輸出 $y$」在反函數中變成「輸入 $y$、輸出 $x$」。因此定義域和值域也會交換。

---

## 6. 核心觀念五：對數

$$
\log_b x=y\iff b^y=x,\qquad b>0,\ b\ne1,\ x>0.
$$

對數真數一定要正：

$$
\log_b(MN)=\log_bM+\log_bN,
$$

$$
\log_b(M/N)=\log_bM-\log_bN,
$$

$$
\log_b(M^r)=r\log_bM.
$$

若因式可能為負，不能直接寫 $\ln(x-1)$；應寫 $\ln|x-1|$。例如

$$
\ln((x-1)^2)=2\ln|x-1|.
$$

換底公式：

$$
\log_bx=\frac{\ln x}{\ln b}.
$$

解對數方程的固定流程：先列定義域、再合併或指數化、最後把候選解代回定義域。

### 6.1 對數其實是在問指數

看到

$$
\log_2 8=3,
$$

把它念成：「2 的幾次方等於 8？答案是 3。」因為

$$
2^3=8.
$$

所以對數與指數是互相撤銷的運算：

$$
\log_b(b^x)=x,\qquad b^{\log_bx}=x.
$$

但第二個式子需要 $x>0$，因為對數不能接收 0 或負數。

### 6.2 為什麼真數一定大於 0

當底數 $b>0$ 時，不論實數指數是多少，$b^x$ 永遠是正數。因此方程 $b^y=x$ 若要有實數解，右邊 $x$ 必須大於 0。這就是

$$
D_{\log_bx}=(0,\infty)
$$

的原因。

例：

$$
\ln(x-3)
$$

不是只排除 $x=3$，而是要 $x-3>0$，所以 $x>3$。

### 6.3 對數律從指數律而來

假設 $b^u=M$、$b^v=N$。那麼

$$
MN=b^ub^v=b^{u+v}.
$$

因此

$$
\log_b(MN)=u+v=\log_bM+\log_bN.
$$

這也說明為什麼「乘法」進入對數後變成「加法」。同理，除法變減法，次方則把指數移到前面。

### 6.4 解方程示範

解

$$
\ln(x-1)=\ln3.
$$

第一步先列限制 $x-1>0$，即 $x>1$。因為 $\ln$ 是一對一函數，兩邊對數相等時真數相等：

$$
x-1=3,
$$

所以 $x=4$，而且符合 $x>1$。

若代數運算得到一個不符合原始定義域的值，那個值叫做增根，必須刪掉。

---

## 7. 核心觀念六：反三角函數的主值

反三角函數不是「把角度完全還原」，而是回到指定主值範圍：

| 函數 | 定義域 | 值域（主值範圍） |
| --- | --- | --- |
| $\arcsin x$ | $[-1,1]$ | $[-\pi/2,\pi/2]$ |
| $\arccos x$ | $[-1,1]$ | $[0,\pi]$ |
| $\arctan x$ | $\mathbb R$ | $(-\pi/2,\pi/2)$ |
| $\operatorname{arcsec}x$ | $(-\infty,-1]\cup[1,\infty)$ | $[0,\pi]\setminus\{\pi/2\}$ |

所以 $\arcsin(\sin\theta)$ 不一定等於 $\theta$。做法是先找同樣的三角函數值，再挑位於主值範圍內的角。

### 7.1 先回想正弦、餘弦、正切

在直角三角形中：

$$
\sin\theta=\frac{\text{對邊}}{\text{斜邊}},\qquad
\cos\theta=\frac{\text{鄰邊}}{\text{斜邊}},\qquad
\tan\theta=\frac{\text{對邊}}{\text{鄰邊}}.
$$

反正弦 $\arcsin x$ 則是在問：「主值範圍內，哪個角的正弦是 $x$？」

例如

$$
\arcsin\left(\frac12\right)=\frac\pi6,
$$

因為 $\sin(\pi/6)=1/2$，而 $\pi/6$ 位於 $[-\pi/2,\pi/2]$。

### 7.2 為什麼需要主值範圍

正弦具有週期，同一個值對應無限多個角。例如

$$
\sin\frac\pi6=\sin\frac{5\pi}6=\frac12.
$$

反函數必須對每個輸入只給一個輸出，所以我們限制在一段一對一的區間，並約定只回傳那段裡的角。這段就是主值範圍。

### 7.3 處理 $\arcsin(\sin\theta)$ 的三步

1. 算出或判斷 $\sin\theta$ 的值。
2. 找出一個有相同正弦值的角。
3. 確認答案落在 arcsin 的主值範圍 $[-\pi/2,\pi/2]$。

例如 $7\pi/6$ 在第三象限，參考角是 $\pi/6$，正弦為負。主值範圍內具有相同正弦值的角是 $-\pi/6$，所以

$$
\arcsin(\sin(7\pi/6))=-\frac\pi6.
$$

### 7.4 用三角形化簡複合式

若 $\theta=\arctan x$，便有 $\tan\theta=x/1$。畫一個鄰邊為 1、對邊為 $x$ 的直角三角形，由畢氏定理：

$$
\text{斜邊}=\sqrt{1+x^2}.
$$

因此

$$
\sin\theta=\frac{x}{\sqrt{1+x^2}}.
$$

最後把 $\theta=\arctan x$ 換回去，就得到 Homework #20(a) 的公式。要留意主值範圍決定正負號，不能只憑圖形猜。

---

# 8. Homework 1 逐題帶寫

### Homework general instructions

> Give exact answers and show your reasoning. Do not use calculators, graphing software, or other electronic tools. All functions are real-valued, and all angles are in radians. Use the conventions for inverse trigonometric functions in Lecture 2; in particular, arcsec has range $[0,\pi]\setminus\{\pi/2\}$.

### 作業總說明中文翻譯

> 答案須為精確值，並寫出推理過程。不可使用計算機、繪圖軟體或其他電子工具。所有函數皆取實數值，所有角度皆使用弧度。反三角函數採用 Lecture 2 的約定；尤其 arcsec 的值域是 $[0,\pi]\setminus\{\pi/2\}$。

每題都用同一個閱讀方式：

- **題目在考什麼**：先辨認題型。
- **第一步為什麼這樣做**：避免只背答案。
- **逐行計算**：等號上下每一步都能說明。
- **最後檢查**：確認定義域、正負號、端點或主值範圍。

第一次做時，先用紙遮住解答，只看小標題想 30 秒。即使想不出完整答案，也要先寫下已知條件。

## #1 上確界

### English question

> Find the supremum of each set and state whether the supremum belongs to the set. Give a brief explanation.
>
> (a) $A=\{x\in\mathbb R:x^2<3\}$<br>
> (b) $B=\{q\in\mathbb Q:q<5/2\}$<br>
> (c) $C=[-1,2]\cup\{4\}$

### 中文翻譯

> 找出每個集合的上確界，並說明該上確界是否屬於集合。請簡短解釋理由。

### 一步一步解題

### (a) $A=\{x\in\mathbb R:x^2<3\}$

**題目在考什麼：** 把集合條件畫成數線，再分辨「上確界」是否真的在集合裡。

$x^2<3$ 的意思是 $x$ 與 0 的距離小於 $\sqrt3$，因此

$$
-\sqrt3<x<\sqrt3.
$$

集合就是開區間 $(-\sqrt3,\sqrt3)$。它可以無限靠近右端的 $\sqrt3$，卻不能等於右端，所以

$$
\sup A=\sqrt3.
$$

但 $\sqrt3$ 不在集合內，因為它的平方等於 3，不小於 3。

### (b) $B=\{q\in\mathbb Q:q<5/2\}$

這裡 $q\in\mathbb Q$ 表示只收有理數。條件 $q<5/2$ 讓所有成員都在 $5/2$ 左邊，所以 $5/2$ 是上界。

$$
\sup B=\frac52.
$$

$5/2$ 雖然是有理數，但題目要求嚴格小於，因此不在集合中。若嘗試把天花板降到任何 $t<5/2$，在 $t$ 與 $5/2$ 之間仍能找到有理數，因此 $t$ 擋不住整個集合。這就是有理數的稠密性。

### (c) $C=[-1,2]\cup\{4\}$

$$
\sup C=4,
$$

而且 $4\in C$，所以它也是最大值。

**檢查點：** 題目問的是 supremum 和是否取到，不要只寫一個數。

## #2 指數化簡

### English question

> Evaluate:
>
> (a) $\left(\dfrac{81}{16}\right)^{-3/4}$<br>
> (b) $32^{2/5}$<br>
> (c) $\left(\sqrt[3]{25}\right)^{3/2}$

### 中文翻譯

> 計算下列各式，答案要寫成精確值，不使用計算機。

### 一步一步解題

**題目在考什麼：** 把數字改寫成同一個底數，再使用乘方與負指數規則。

### (a)

81 是 $3^4$，16 是 $2^4$。先把括號內寫成一個四次方：

$$
\left(\frac{81}{16}\right)^{-3/4}
=\left(\frac{3^4}{2^4}\right)^{-3/4}
=\left(\frac32\right)^{-3}
=\frac8{27}.
$$

最後一步使用負指數規則：

$$
\left(\frac32\right)^{-3}
=\left(\frac23\right)^3
=\frac8{27}.
$$

### (b)

32 是 $2^5$，所以

$$
32^{2/5}=(2^5)^{2/5}=2^2=4.
$$

### (c)

先把三次根號寫成 $1/3$ 次方，再使用「次方再做次方，指數相乘」：

$$
(\sqrt[3]{25})^{3/2}
=(25^{1/3})^{3/2}=25^{1/2}=5.
$$

## #3 指數律

### English question

> Simplify the following expressions, assuming $a,x,y>0$:
>
> (a) $\dfrac{(a^{\sqrt5-1})^{\sqrt5+1}}{a^2}$<br>
> (b) $\dfrac{(x^{3/2}y^{-1/2})^2}{xy^{-2}}$

### 中文翻譯

> 假設 $a,x,y$ 都是正數，化簡下列式子。

「假設為正數」讓根式與實數指數都有良好定義，也讓我們可以直接使用題目教過的指數律。

### 一步一步解題

### (a)

外層乘方使指數相乘。$(\sqrt5-1)(\sqrt5+1)$ 是平方差：

$$
(\sqrt5-1)(\sqrt5+1)
=(\sqrt5)^2-1^2
=5-1=4.
$$

因此

$$
\frac{(a^{\sqrt5-1})^{\sqrt5+1}}{a^2}
=a^{(\sqrt5-1)(\sqrt5+1)-2}
=a^{4-2}=a^2.
$$

### (b)

先把分子整體平方，所以括號裡每個指數都乘以 2：

$$
\frac{(x^{3/2}y^{-1/2})^2}{xy^{-2}}
=\frac{x^3y^{-1}}{xy^{-2}}
=x^2y.
$$

最後一步其實是

$$
x^{3-1}y^{-1-(-2)}
=x^2y^1.
$$

## #4 不使用分數指數證明根式乘法

### English question

> Let $a,b>0$ and let $n$ be a positive integer. Use the definition of the positive $n$th root to prove
>
> $\sqrt[n]{ab}=\sqrt[n]a\sqrt[n]b$.
>
> Do not use the laws of rational exponents in your proof.

### 中文翻譯

> 設 $a,b>0$，且 $n$ 是正整數。請用「正 $n$ 次方根」的定義證明乘積的 $n$ 次方根等於兩個 $n$ 次方根的乘積。證明中不可使用分數指數律。

### 題意拆解

這題不是要求算一個數，而是要求證明一條規則。因為題目禁止把根號直接改寫成 $1/n$ 次方，我們只能使用定義：

> $\sqrt[n]a$ 是唯一一個滿足「本身為正，而且做 $n$ 次方等於 $a$」的數。

### 一步一步證明

令 $\alpha=\sqrt[n]{a}$、$\beta=\sqrt[n]{b}$。依根式定義，

$$
\alpha>0,\quad \beta>0,\quad \alpha^n=a,\quad \beta^n=b.
$$

因此

$$
(\alpha\beta)^n=\alpha^n\beta^n=ab.
$$

$\alpha\beta>0$，而正的 $n$ 次方根唯一，所以

$$
\sqrt[n]{ab}=\alpha\beta=\sqrt[n]a\,\sqrt[n]b.
$$

關鍵不是套指數律，而是使用「正 $n$ 次方根的唯一性」。

## #5 指數不等式

### English question

> Solve the inequality
>
> $\left(\frac12\right)^{x^2-x}\ge\frac14$.
>
> Give your answer as an interval.

### 中文翻譯

> 解這個指數不等式，並用區間表示答案。

### 一步一步解題

**第一步：** 先把兩邊寫成相同底數。因為 $1/4=(1/2)^2$：

$$
\left(\frac12\right)^{x^2-x}\ge\frac14
=\left(\frac12\right)^2.
$$

**第二步：** 底數 $1/2$ 小於 1，指數越大，函數值反而越小。因此拿掉相同底數時，不等號要反向：

$$
x^2-x\le2
\iff x^2-x-2\le0.
$$

**第三步：** 因式分解：

$$
x^2-x-2=(x-2)(x+1).
$$

乘積在兩個根 $-1$ 與 2 之間小於或等於 0，所以答案是

$$
\boxed{[-1,2]}.
$$

端點要包含，因為原題是不嚴格的 $\ge$，而代入 $-1$ 或 2 都會得到等號。

## #6 指數方程

### English question

> Solve $4^x-5\cdot2^x+4=0$ for $x\in\mathbb R$.

### 中文翻譯

> 在實數範圍內解方程 $4^x-5\cdot2^x+4=0$。

### 一步一步解題

$$
4^x-5\cdot2^x+4=0.
$$

先把 $4^x$ 改寫成以 $2^x$ 表示：

$$
4^x=(2^2)^x=2^{2x}=(2^x)^2.
$$

因此原式成為

$$
(2^x)^2-5(2^x)+4=0.
$$

令 $u=2^x$。因為 $2^x$ 永遠為正，所以 $u>0$。代換後：

$$
u^2-5u+4=0.
$$

尋找「乘起來是 4、加起來是 $-5$」的兩個數 $-1,-4$，所以

$$
u^2-5u+4=(u-1)(u-4).
$$

因此

$$
(u-1)(u-4)=0.
$$

所以 $u=1$ 或 $u=4$。現在換回 $u=2^x$：

$$
2^x=1=2^0\implies x=0,
$$

$$
2^x=4=2^2\implies x=2.
$$

故

$$
\boxed{x=0,\ 2}.
$$

## #7 函數運算與定義域

### English question

> Let $f(x)=\sqrt{x+2}$ and $g(x)=\sqrt{3-x}$, each on its largest real domain. Find a formula and the domain for each function:
>
> (a) $f+g$　(b) $fg$　(c) $-2f$　(d) $f/g$

### 中文翻譯

> 令 $f(x)=\sqrt{x+2}$、$g(x)=\sqrt{3-x}$，兩者都取最大的實數定義域。請寫出下列函數的公式與定義域：和、乘積、$f$ 的 $-2$ 倍，以及商。

### 題意拆解

「最大的實數定義域」表示：題目沒有先替你限制 $x$，你要找出所有能讓公式產生實數的 $x$。偶次根號內可以是 0，但不能小於 0；若做除法，分母還不能等於 0。

### 一步一步解題

令 $f(x)=\sqrt{x+2}$、$g(x)=\sqrt{3-x}$。有

$$
D_f=[-2,\infty),\qquad D_g=(-\infty,3].
$$

原因分別是

$$
x+2\ge0\iff x\ge-2,
$$

$$
3-x\ge0\iff x\le3.
$$

做加法或乘法時，兩個函數都必須有定義，因此取兩個定義域的交集：

$$
(f+g)(x)=\sqrt{x+2}+\sqrt{3-x},\quad D=[-2,3],
$$

$$
(fg)(x)=\sqrt{(x+2)(3-x)},\quad D=[-2,3],
$$

$$
(-2f)(x)=-2\sqrt{x+2},\quad D=[-2,\infty),
$$

乘上常數 $-2$ 不會增加任何限制，所以定義域仍與 $f$ 相同。

做除法時，不只要兩個根號存在，分母還不能是 0：

$$
\left(\frac fg\right)(x)=\frac{\sqrt{x+2}}{\sqrt{3-x}},
\quad D=[-2,3).
$$

在 $x=3$ 時，$g(3)=0$，所以右端從方括號改成小括號。

## #8 合成函數

### English question

> Let $f(x)=\sqrt x$ and $g(x)=1/(x-2)$, each on its largest real domain. Find $f\circ g$ and $g\circ f$, including their domains. Are these the same function?

### 中文翻譯

> 令 $f(x)=\sqrt x$、$g(x)=1/(x-2)$，各自取最大的實數定義域。求 $f\circ g$ 與 $g\circ f$，並寫出定義域。這兩個函數相同嗎？

### 題意拆解

$f\circ g$ 念作「$f$ 合成 $g$」，意思是先把 $x$ 放進 $g$，再把 $g(x)$ 放進 $f$。次序由右往左讀：

$$
(f\circ g)(x)=f(g(x)).
$$

### 一步一步解題

$f(x)=\sqrt x$、$g(x)=1/(x-2)$。

### (a) 先做 $g$，再做 $f$

$$
(f\circ g)(x)=\sqrt{\frac1{x-2}}.
$$

外層 $f$ 是開根號，所以內層輸出必須非負：

$$
\frac1{x-2}\ge0.
$$

分子 1 永遠為正，因此整個分式要非負，分母必須為正：

$$
x-2>0\iff x>2.
$$

得到

$$
D_{f\circ g}=(2,\infty).
$$

### (b) 先做 $f$，再做 $g$

$$
(g\circ f)(x)=\frac1{\sqrt x-2}.
$$

先讓 $\sqrt x$ 存在，所以 $x\ge0$；再讓分母不為 0：

$$
\sqrt x-2\ne0
\iff\sqrt x\ne2
\iff x\ne4.
$$

得到

$$
D_{g\circ f}=[0,\infty)\setminus\{4\}.
$$

兩者公式和定義域都不同，所以 $f\circ g\ne g\circ f$。

## #9 函數相等

### English question

> Let
>
> $F(x)=\dfrac{x^2-9}{x-3}$, $x\in\mathbb R\setminus\{3\}$, and<br>
> $G(x)=x+3$, $x\in\mathbb R$.
>
> Are $F$ and $G$ equal as functions? Explain. State a restriction of the domain of $G$ that makes it equal to $F$.

### 中文翻譯

> 給定上面兩個函數。$F$ 與 $G$ 作為函數是否相等？請解釋。應如何限制 $G$ 的定義域，才能使它和 $F$ 相等？

### 題意拆解

兩個函數相等，必須同時有相同的定義域，以及對每個輸入給出相同輸出的規則。不能只比較化簡後的公式。

### 一步一步解題

先因式分解分子：

$$
x^2-9=(x-3)(x+3).
$$

因此在 $x\ne3$ 的前提下，

$$
F(x)=\frac{x^2-9}{x-3}=x+3\qquad(x\ne3).
$$

雖然化簡後與 $G(x)=x+3$ 形式相同，但 $F$ 在 $x=3$ 沒有定義，而 $G$ 有。因此兩者不是同一函數。

若把 $G$ 的定義域限制為 $\mathbb R\setminus\{3\}$，兩者才相等。

## #10 限制定義域後找反函數

### English question

> Find the inverse of $f(x)=(x+2)^2-3$ with domain $(-\infty,-2]$. State the domain and range of the inverse, and verify both inverse identities on the appropriate domains.

### 中文翻譯

> 函數 $f(x)=(x+2)^2-3$ 的定義域限制為 $(-\infty,-2]$。求反函數，寫出反函數的定義域與值域，並在正確的定義域上驗證兩個反函數合成恆等式。

### 題意拆解

「兩個反函數恆等式」是

$$
f(f^{-1}(x))=x
$$

與

$$
f^{-1}(f(x))=x.
$$

前者的 $x$ 要在 $f^{-1}$ 的定義域，後者的 $x$ 要在 $f$ 的定義域。

### 一步一步解題

$$
f(x)=(x+2)^2-3,\qquad x\le-2.
$$

原函數的動作是：先加 2、平方、再減 3。求反函數時，我們用代數把這些動作倒回來。

先寫

$$
y=(x+2)^2-3.
$$

兩邊加 3：

$$
y+3=(x+2)^2.
$$

兩邊開根號時會出現正負兩支：

$$
x+2=\pm\sqrt{y+3}.
$$

因原定義域要求 $x+2\le0$，必須選負號：

$$
x=-2-\sqrt{y+3}.
$$

最後把輸入變數改回常用的 $x$：

$$
\boxed{f^{-1}(x)=-2-\sqrt{x+3}}.
$$

$$
D_{f^{-1}}=[-3,\infty),\qquad
R_{f^{-1}}=(-\infty,-2].
$$

**驗證第一個恆等式。** 當 $x\ge-3$：

$$
f(f^{-1}(x))
=f(-2-\sqrt{x+3})
$$

$$
=((-2-\sqrt{x+3})+2)^2-3
$$

$$
=(-\sqrt{x+3})^2-3
$$

$$
=x+3-3
=x.
$$

**驗證第二個恆等式。** 當 $x\le-2$：

$$
f^{-1}(f(x))
=-2-\sqrt{f(x)+3}
$$

$$
=-2-\sqrt{(x+2)^2-3+3}
$$

$$
=-2-\sqrt{(x+2)^2}
$$

$$
=-2-|x+2|.
$$

因為 $x\le-2$，所以 $x+2\le0$，從而

$$
|x+2|=-(x+2).
$$

代回去：

$$
-2-|x+2|
=-2-(-(x+2))
=x.
$$

兩個合成都得到 $x$，驗證完成。

## #11 自身就是反函數

### English question

> Let $f(x)=(x+1)/(x-1)$, with domain $\mathbb R\setminus\{1\}$.
>
> (a) Show that $f(x)\ne1$ for every $x$ in its domain, and compute $f(f(x))$.<br>
> (b) Deduce the range of $f$, show that it is one-to-one, and find $f^{-1}$. Is $f$ the identity function?

### 中文翻譯

> 令 $f(x)=(x+1)/(x-1)$，定義域為除去 1 的所有實數。
>
> (a) 證明定義域內沒有任何 $x$ 會使 $f(x)=1$，並計算 $f(f(x))$。<br>
> (b) 由此推出 $f$ 的值域，證明它是一對一函數，並求反函數。$f$ 是恆等函數嗎？

### 一步一步解題

$$
f(x)=\frac{x+1}{x-1},\qquad x\ne1.
$$

**先證明 $f(x)\ne1$。** 假設存在合法的 $x$ 使

$$
\frac{x+1}{x-1}=1.
$$

因 $x\ne1$，可以兩邊乘以 $x-1$：

$$
x+1=x-1.
$$

兩邊減去 $x$ 得到 $1=-1$，矛盾。因此 $f(x)$ 不可能等於 1。

**接著計算合成。**

直接合成：

$$
f(f(x))
=\frac{\frac{x+1}{x-1}+1}{\frac{x+1}{x-1}-1}
=x.
$$

中間若看不出如何化簡，可以把分子、分母分開：

$$
\frac{x+1}{x-1}+1
=\frac{x+1+x-1}{x-1}
=\frac{2x}{x-1},
$$

$$
\frac{x+1}{x-1}-1
=\frac{x+1-x+1}{x-1}
=\frac2{x-1}.
$$

兩者相除便得到 $x$。

因為 $f(f(x))=x$，任何 $x\ne1$ 都能成為 $f$ 的輸出：只要把 $f(x)$ 當作輸入，再做一次 $f$ 就會回到 $x$。再配合已證明輸出不可能是 1，可知值域是

$$
R_f=\mathbb R\setminus\{1\}.
$$

若 $f(a)=f(b)$，兩邊再套一次 $f$：

$$
f(f(a))=f(f(b))
\implies a=b.
$$

所以 $f$ 是一對一。又因做兩次 $f$ 會回到原數，因此

$$
\boxed{f^{-1}=f}.
$$

它不是恆等函數，例如 $f(0)=-1\ne0$。

## #12 指數函數的反函數與圖形

### English question

> Let $h(x)=2^{x+1}-2$, with domain $\mathbb R$.
>
> (a) Find $h^{-1}$, including its domain and range.<br>
> (b) Sketch $h$, $h^{-1}$, and $y=x$ on the same axes by hand. Label three points on each function, their intercepts, and their asymptotes.

### 中文翻譯

> 令 $h(x)=2^{x+1}-2$，定義域為所有實數。
>
> (a) 求 $h^{-1}$，並寫出它的定義域和值域。<br>
> (b) 在同一座標平面上手繪 $h$、$h^{-1}$ 與 $y=x$；在兩個函數上各標三個點，並標出截距與漸近線。

### 一步一步解題

$$
h(x)=2^{x+1}-2.
$$

由 $y=2^{x+1}-2$：

$$
y+2=2^{x+1}
\implies \log_2(y+2)=x+1
\implies x=\log_2(y+2)-1.
$$

所以

$$
h^{-1}(x)=\log_2(x+2)-1.
$$

**找原函數的定義域和值域。**

- 指數 $x+1$ 可以是任何實數，所以 $D_h=\mathbb R$。
- $2^{x+1}>0$，所以 $2^{x+1}-2>-2$；可以無限靠近 $-2$，但不會等於 $-2$。因此 $R_h=(-2,\infty)$。

反函數交換定義域和值域，因此

$$
D_{h^{-1}}=(-2,\infty),\qquad R_{h^{-1}}=\mathbb R.
$$

圖形資訊：

| | $h$ | $h^{-1}$ |
| --- | --- | --- |
| 定義域 | $\mathbb R$ | $(-2,\infty)$ |
| 值域 | $(-2,\infty)$ | $\mathbb R$ |
| 漸近線 | $y=-2$ | $x=-2$ |
| 對應點 | $(-1,-1),(0,0),(1,2)$ | $(-1,-1),(0,0),(2,1)$ |

兩圖對 $y=x$ 對稱。

畫圖時不要從很多小數點開始猜。先從母函數 $y=2^x$ 的三個點

$$
(-1,1/2),\quad(0,1),\quad(1,2)
$$

開始。$x+1$ 使圖形左移 1，外面的 $-2$ 再使圖形下移 2。水平漸近線也從 $y=0$ 下移到 $y=-2$。反函數圖形則把每個點的座標交換。

## #13 對數與指數精確值

### English question

> Evaluate:
>
> (a) $\log_9 27$<br>
> (b) $\log_{1/4}8$<br>
> (c) $\ln(e^3\sqrt e)$<br>
> (d) $e^{\ln7-2\ln\sqrt7}$

### 中文翻譯

> 計算下列各式的精確值。

### 一步一步解題

### (a) $\log_9 27$

把 9 與 27 都改寫成底數 3：

$$
9=3^2,\qquad27=3^3.
$$

設答案為 $y$，則

$$
9^y=27
\iff(3^2)^y=3^3
\iff2y=3
\iff y=\frac32.
$$

所以

$$
\boxed{\log_9 27=\frac32}.
$$

### (b) $\log_{1/4}8$

$1/4=2^{-2}$、$8=2^3$。設答案為 $y$：

$$
(2^{-2})^y=2^3
\iff-2y=3
\iff y=-\frac32.
$$

因此

$$
\boxed{\log_{1/4}8=-\frac32}.
$$

答案是負數很合理：小於 1 的底數必須用負次方，才能得到大於 1 的 8。

### (c) $\ln(e^3\sqrt e)$

因 $\sqrt e=e^{1/2}$：

$$
e^3\sqrt e=e^3e^{1/2}=e^{7/2}.
$$

$\ln$ 與 $e^x$ 互相撤銷：

$$
\boxed{\ln(e^3\sqrt e)=\ln(e^{7/2})=\frac72}.
$$

### (d) $e^{\ln7-2\ln\sqrt7}$

先看指數：

$$
2\ln\sqrt7
=2\ln(7^{1/2})
=2\cdot\frac12\ln7
=\ln7.
$$

所以整個指數是 0：

$$
\boxed{e^{\ln7-2\ln\sqrt7}=e^0=1}.
$$

## #14 展開對數且保留完整定義域

### English question

> Find the domain of $L(x)=\ln\left(\dfrac{(x-1)^2}{x+2}\right)$. Expand $L(x)$ using logarithm laws so that your expression is valid on its entire domain. Explain why $2\ln(x-1)-\ln(x+2)$ does not suffice.

### 中文翻譯

> 求 $L(x)$ 的定義域。使用對數律展開 $L(x)$，而且展開後的式子必須在原函數的整個定義域都成立。解釋為什麼只寫 $2\ln(x-1)-\ln(x+2)$ 不夠。

### 一步一步解題

$$
L(x)=\ln\left(\frac{(x-1)^2}{x+2}\right).
$$

**第一步：令整個真數大於 0。**

$$
\frac{(x-1)^2}{x+2}>0.
$$

分子 $(x-1)^2$ 在 $x=1$ 時等於 0，不能放進 $\ln$；在 $x\ne1$ 時則大於 0。

當分子為正時，分式要為正，分母也必須為正：

$$
x+2>0.
$$

兩邊減 2：

$$
x>-2.
$$

再排除 $x=1$：

$$
D_L=(-2,1)\cup(1,\infty).
$$

**第二步：先使用商的對數律。**

$$
L(x)=\ln((x-1)^2)-\ln(x+2).
$$

**第三步：處理平方。**

因為 $x-1$ 在部分原始定義域可能為負，所以必須寫

$$
\ln((x-1)^2)=2\ln|x-1|.
$$

因此正確展開為

$$
\boxed{L(x)=2\ln|x-1|-\ln(x+2)}.
$$

若寫成 $2\ln(x-1)$，裡面的 $\ln(x-1)$ 會額外要求 $x>1$，錯誤刪掉原本合法的 $-2<x<1$。絕對值用來保留完整定義域。

## #15 對數方程

### English question

> Solve each equation, checking the domain of the original expression:
>
> (a) $\ln(x+2)+\ln(x-1)=\ln4$<br>
> (b) $2\ln x=\ln(3x+4)$

### 中文翻譯

> 解下列方程，並依原式的定義域檢查候選答案是否合法。

### 一步一步解題

### (a)

原式是

$$
\ln(x+2)+\ln(x-1)=\ln4.
$$

兩個真數都要正：

$$
x+2>0,\qquad x-1>0.
$$

同時成立時是 $x>1$。利用 $\ln A+\ln B=\ln(AB)$：

$$
\ln((x+2)(x-1))=\ln4.
$$

$\ln$ 一對一，所以真數相等：

$$
(x+2)(x-1)=4.
$$

展開左邊：

$$
x^2+x-2=4.
$$

兩邊減 4：

$$
x^2+x-6=0.
$$

因式分解：

$$
x^2+x-6=(x-2)(x+3).
$$

所以

$$
x=2\quad\text{或}\quad x=-3.
$$

候選值是 2 與 $-3$。只有 2 符合原始定義域 $x>1$，因此 $\boxed{x=2}$。

### (b)

原式是

$$
2\ln x=\ln(3x+4).
$$

左邊要求 $x>0$；這也會自動使 $3x+4>0$。利用 $2\ln x=\ln(x^2)$：

$$
\ln(x^2)=\ln(3x+4).
$$

因 $\ln$ 一對一：

$$
x^2=3x+4.
$$

全部移到左邊：

$$
x^2-3x-4=0.
$$

因式分解：

$$
x^2-3x-4=(x-4)(x+1).
$$

所以

$$
x=4\quad\text{或}\quad x=-1.
$$

候選值是 4 與 $-1$。只有 $x=4$ 合法，因此 $\boxed{x=4}$。

## #16 對數不等式

### English question

> Solve $\log_{1/2}(x-1)\ge-2$. Explain why the direction of the inequality changes when the logarithm is removed.

### 中文翻譯

> 解不等式 $\log_{1/2}(x-1)\ge-2$，並解釋為什麼去掉對數時不等號方向會改變。

### 一步一步解題

$$
\log_{1/2}(x-1)\ge-2.
$$

**第一步：定義域。**

$$
x-1>0\iff x>1.
$$

**第二步：改寫右邊。**

$$
-2=\log_{1/2}\left(\left(\frac12\right)^{-2}\right)
=\log_{1/2}4.
$$

原不等式變成

$$
\log_{1/2}(x-1)\ge\log_{1/2}4.
$$

**第三步：使用單調性。** 因底數 $1/2<1$，對數函數遞減，拿掉兩邊對數時方向反轉：

$$
x-1\le4.
$$

與定義域的 $x-1>0$ 合併：

$$
0<x-1\le4.
$$

所以

$$
\boxed{x\in(1,5]}.
$$

## #17 換底公式

### English question

> Let $a,b>0$, with $a,b\ne1$.
>
> (a) Prove $\log_ab=\dfrac1{\log_ba}$.<br>
> (b) If also $u,v>0$ and $v\ne1$, prove $\dfrac{\log_au}{\log_av}=\log_vu$.

### 中文翻譯

> 設 $a,b$ 都是正數且都不等於 1。
>
> (a) 證明互換底數與真數後，兩個對數互為倒數。<br>
> (b) 再假設 $u,v>0$ 且 $v\ne1$，證明所給的對數比值等於 $\log_vu$。

### 一步一步證明

以下把所有對數換成自然對數。換底公式是

$$
\log_pq=\frac{\ln q}{\ln p}.
$$

### (a)

先把兩個對數都用換底公式改寫：

$$
\log_ba\cdot\log_ab
=\frac{\ln a}{\ln b}\cdot\frac{\ln b}{\ln a}.
$$

分子、分母中的 $\ln a$ 與 $\ln b$ 約掉：

$$
\frac{\ln a\cdot\ln b}{\ln b\cdot\ln a}=1.
$$

因此

$$
\log_ba\cdot\log_ab=1.
$$

兩邊除以 $\log_ba$：

$$
\boxed{\log_ab=\frac1{\log_ba}}.
$$

### (b)

先把分子、分母分別換底：

$$
\frac{\log_au}{\log_av}
=\frac{\ln u/\ln a}{\ln v/\ln a}.
$$

除以一個分數等於乘以它的倒數：

$$
=\frac{\ln u}{\ln a}\cdot\frac{\ln a}{\ln v}.
$$

約掉 $\ln a$：

$$
=\frac{\ln u}{\ln v}.
$$

依換底公式，

$$
\frac{\ln u}{\ln v}=\log_vu.
$$

所以

$$
\boxed{\frac{\log_au}{\log_av}=\log_vu}.
$$

## #18 反三角函數精確值

### English question

> Evaluate:
>
> (a) $\arcsin(-\sqrt3/2)$<br>
> (b) $\arccos(-1/2)$<br>
> (c) $\arctan1$<br>
> (d) $\operatorname{arcsec}(-2)$

### 中文翻譯

> 求下列反三角函數的精確值。答案必須位於 Lecture 2 規定的主值範圍。

### 一步一步解題

每一小題都先找出熟悉的特殊角，再用外層反函數的主值範圍決定象限。

### (a)

$\sin(\pi/3)=\sqrt3/2$。要得到負值，且 arcsin 的答案必須在 $[-\pi/2,\pi/2]$，因此選 $-\pi/3$：

$$
\arcsin\left(-\frac{\sqrt3}{2}\right)=-\frac\pi3,
$$

### (b)

$\cos(\pi/3)=1/2$。在 arccos 的主值範圍 $[0,\pi]$ 中，餘弦為負的第二象限角是 $2\pi/3$：

$$
\arccos\left(-\frac12\right)=\frac{2\pi}{3},
$$

### (c)

$\tan(\pi/4)=1$，而 $\pi/4$ 位於 arctan 的主值範圍：

$$
\arctan(1)=\frac\pi4,
$$

### (d)

$\sec\theta=-2$ 等價於 $\cos\theta=-1/2$。依老師採用的 arcsec 主值範圍，選第二象限的 $2\pi/3$：

$$
\operatorname{arcsec}(-2)=\frac{2\pi}{3}.
$$

## #19 折回主值範圍

### English question

> Evaluate each composition. State the range restriction that determines the answer.
>
> (a) $\arcsin(\sin(7\pi/6))$<br>
> (b) $\arccos(\cos(7\pi/4))$<br>
> (c) $\arctan(\tan(5\pi/6))$<br>
> (d) $\operatorname{arcsec}(\sec(5\pi/4))$

### 中文翻譯

> 計算每個複合函數，並寫出是哪一個反三角函數的值域限制決定答案。

### 一步一步解題

原角若已經在外層反函數的主值範圍內，才能直接被還原；否則要找同三角函數值的主值角。

### (a)

$7\pi/6$ 在第三象限，參考角 $\pi/6$，正弦為負。arcsin 主值範圍內的對應角是 $-\pi/6$：

$$
\arcsin(\sin(7\pi/6))=-\frac\pi6,
$$

### (b)

$7\pi/4$ 的餘弦為 $\sqrt2/2$。arccos 必須回傳 $[0,\pi]$ 中的角，所以選 $\pi/4$：

$$
\arccos(\cos(7\pi/4))=\frac\pi4,
$$

### (c)

$5\pi/6$ 與 $-\pi/6$ 的正切相同，而 $-\pi/6$ 落在 arctan 主值範圍：

$$
\arctan(\tan(5\pi/6))=-\frac\pi6,
$$

### (d)

$5\pi/4$ 的 secant 是 $-\sqrt2$。在老師採用的 arcsec 主值範圍內，具有相同 secant 的角為 $3\pi/4$：

$$
\operatorname{arcsec}(\sec(5\pi/4))=\frac{3\pi}{4}.
$$

做題時先看外層反函數的值域，再找同值且落在該區間的角。

## #20 化成代數式並寫定義域

### English question

> Express each function using only algebraic operations and square roots, and give its domain. Justify the signs of the square roots.
>
> (a) $\sin(\arctan x)$<br>
> (b) $\tan(\arccos x)$

### 中文翻譯

> 只使用代數運算與平方根改寫下列函數，並給出定義域。必須說明平方根前應取正號還是負號。

### 一步一步解題

### (a) $\sin(\arctan x)$

令

$$
\theta=\arctan x.
$$

依反正切定義，

$$
\tan\theta=x.
$$

又因

$$
\tan\theta=\frac{\text{對邊}}{\text{鄰邊}},
$$

可把對邊設成 $x$、鄰邊設成 1。利用畢氏定理：

$$
\text{斜邊}^2=x^2+1^2.
$$

斜邊長度必須為正，所以

$$
\text{斜邊}=\sqrt{1+x^2}.
$$

因此

$$
\sin\theta
=\frac{\text{對邊}}{\text{斜邊}}
=\frac{x}{\sqrt{1+x^2}}.
$$

把 $\theta=\arctan x$ 換回去：

$$
\boxed{\sin(\arctan x)=\frac{x}{\sqrt{1+x^2}}}.
$$

arctan 接受所有實數輸入，而且 $1+x^2>0$，所以定義域是

$$
\boxed{D=\mathbb R}.
$$

主值範圍 $\theta\in(-\pi/2,\pi/2)$ 保證 $\cos\theta>0$，也就是鄰邊與斜邊的比為正；這與我們把鄰邊設為正的 1 一致。

### (b) $\tan(\arccos x)$

令

$$
\theta=\arccos x.
$$

依反餘弦定義，

$$
\cos\theta=x,
\qquad
\theta\in[0,\pi].
$$

利用恆等式

$$
\sin^2\theta+\cos^2\theta=1
$$

得到

$$
\sin^2\theta=1-\cos^2\theta.
$$

代入 $\cos\theta=x$：

$$
\sin^2\theta=1-x^2.
$$

開平方根本來可能有正負號：

$$
\sin\theta=\pm\sqrt{1-x^2}.
$$

但 $\theta\in[0,\pi]$ 時，$\sin\theta\ge0$，因此一定取正號：

$$
\sin\theta=\sqrt{1-x^2}.
$$

再利用 $\tan\theta=\sin\theta/\cos\theta$：

$$
\tan(\arccos x)=\frac{\sqrt{1-x^2}}x.
$$

arccos 先要求

$$
-1\le x\le1.
$$

又因正切的分母 $\cos\theta=x$ 不能為 0，所以還要排除 $x=0$：

$$
\boxed{D=[-1,0)\cup(0,1]}.
$$

---

# 9. 微積分小組共同勾選題

以下依課本 9E Metric Version 原頁核對。每題同樣依照「英文原題、中文翻譯、一步一步解題」排列。

## §1.4 #2 指數律

### English question

> Use the Laws of Exponents to rewrite and simplify each expression.
>
> (a) $\dfrac{\sqrt[3]4}{\sqrt[3]{108}}$<br>
> (b) $27^{2/3}$<br>
> (c) $2x^2(3x^5)^2$<br>
> (d) $(2x^{-2})^{-3}x^{-3}$<br>
> (e) $\dfrac{3a^{3/2}\cdot a^{1/2}}{a^{-1}}$<br>
> (f) $\dfrac{\sqrt{a\sqrt b}}{\sqrt[3]{ab}}$

### 中文翻譯

> 使用指數律改寫並化簡每一個式子。

### 一步一步解題

### (a)

先使用同次根號的商：

$$
\frac{\sqrt[3]4}{\sqrt[3]{108}}
=\sqrt[3]{\frac4{108}}.
$$

約分 $4/108$：

$$
\frac4{108}=\frac1{27}.
$$

因此

$$
\sqrt[3]{\frac1{27}}
=\frac{\sqrt[3]1}{\sqrt[3]{27}}
=\boxed{\frac13}.
$$

### (b)

因為 $27=3^3$：

$$
27^{2/3}
=(3^3)^{2/3}.
$$

指數相乘：

$$
(3^3)^{2/3}
=3^{3\cdot(2/3)}
=3^2
=\boxed{9}.
$$

### (c)

先處理括號的平方：

$$
(3x^5)^2=3^2(x^5)^2.
$$

$$
=9x^{10}.
$$

再乘外面的 $2x^2$：

$$
2x^2\cdot9x^{10}
=18x^{2+10}
=\boxed{18x^{12}}.
$$

### (d)

先讓外層指數 $-3$ 分配到括號內：

$$
(2x^{-2})^{-3}
=2^{-3}(x^{-2})^{-3}.
$$

$$
=\frac18x^6.
$$

再乘 $x^{-3}$：

$$
\frac18x^6x^{-3}
=\frac18x^{6-3}
=\boxed{\frac{x^3}{8}}.
$$

### (e)

先合併分子中的同底數：

$$
a^{3/2}a^{1/2}
=a^{3/2+1/2}
=a^2.
$$

因此

$$
\frac{3a^2}{a^{-1}}
=3a^{2-(-1)}
=3a^3.
$$

答案是

$$
\boxed{3a^3}.
$$

### (f)

先把根號全部改成分數指數。分子為

$$
\sqrt{a\sqrt b}
=(ab^{1/2})^{1/2}.
$$

$$
=a^{1/2}b^{1/4}.
$$

分母為

$$
\sqrt[3]{ab}=a^{1/3}b^{1/3}.
$$

相除時同底數指數相減：

$$
\frac{a^{1/2}b^{1/4}}{a^{1/3}b^{1/3}}
=a^{1/2-1/3}b^{1/4-1/3}.
$$

通分：

$$
\frac12-\frac13=\frac16,
\qquad
\frac14-\frac13=-\frac1{12}.
$$

所以

$$
a^{1/6}b^{-1/12}
=\boxed{\frac{\sqrt[6]a}{\sqrt[12]b}}.
$$

**最後檢查：** 每次相乘、相除、乘方時，指數分別是相加、相減、相乘。

## §1.4 #9 指數圖形變換

### English question

> Make a rough sketch by hand of the graph of the function. Use the graphs given in Figures 3 and 15 and, if necessary, the transformations of Section 1.3.
>
> $g(x)=3^x+1$

### 中文翻譯

> 以課本的基本函數圖形與 §1.3 的圖形變換為基礎，手繪 $g(x)=3^x+1$ 的大致圖形。

### 一步一步解題

**第一步：從母函數開始。**

母函數是

$$
y=3^x.
$$

選三個容易計算的 $x$：

$$
3^{-1}=\frac13,\qquad
3^0=1,\qquad
3^1=3.
$$

所以母函數上有三個點：

$$
(-1,1/3),\qquad(0,1),\qquad(1,3).
$$

**第二步：判斷圖形變換。**

在 $3^x$ 外面加 1，表示每一個輸出值都增加 1，所以整張圖向上移 1 單位：

$$
g(x)=3^x+1.
$$

三個點跟著變成

$$
(-1,4/3),\qquad(0,2),\qquad(1,4).
$$

**第三步：找漸近線。**

$3^x$ 的水平漸近線是 $y=0$。向上移 1 後，漸近線也向上移成

$$
y=1.
$$

**第四步：整理圖形性質。**

- 定義域 $\mathbb R$，值域 $(1,\infty)$。
- 水平漸近線 $y=1$。
- $y$ 截距 $(0,2)$，嚴格遞增。
- 沒有 $x$ 截距，因為 $3^x+1$ 永遠大於 1，不可能等於 0。

## §1.4 #13 指數圖形

### English question

> Make a rough sketch by hand of the graph of the function. Use the graphs given in Figures 3 and 15 and, if necessary, the transformations of Section 1.3.
>
> $y=1-\dfrac12e^{-x}$

### 中文翻譯

> 以基本函數圖形和 §1.3 的圖形變換為基礎，手繪 $y=1-\frac12e^{-x}$ 的大致圖形。

### 一步一步解題

**第一步：** 從母函數 $y=e^x$ 開始。

**第二步：** 把 $x$ 換成 $-x$：

$$
y=e^{-x}.
$$

這會把 $y=e^x$ 對 $y$ 軸鏡射。

**第三步：** 乘以 $-1/2$：

$$
y=-\frac12e^{-x}.
$$

負號把圖形對 $x$ 軸鏡射；$1/2$ 把所有高度縮成一半。

**第四步：** 加 1：

$$
y=1-\frac12e^{-x}.
$$

整張圖再向上移 1。

**第五步：找截距。**

令 $x=0$：

$$
y=1-\frac12e^0.
$$

因 $e^0=1$：

$$
y=1-\frac12=\frac12.
$$

所以 $y$ 截距是 $(0,1/2)$。

令 $y=0$：

$$
1-\frac12e^{-x}=0.
$$

移項：

$$
\frac12e^{-x}=1.
$$

兩邊乘 2：

$$
e^{-x}=2.
$$

取自然對數：

$$
-x=\ln2.
$$

所以

$$
x=-\ln2.
$$

$x$ 截距是 $(-\ln2,0)$。

**第六步：整理圖形性質。**

- 定義域 $\mathbb R$。
- 值域 $(-\infty,1)$。
- 水平漸近線 $y=1$。
- $y$ 截距 $(0,1/2)$。
- $x$ 截距 $(-\ln2,0)$。
- 函數嚴格遞增。

## §1.4 #17 定義域

### English question

> Find the domain of each function.
>
> (a) $f(x)=\dfrac{1-e^{x^2}}{1-e^{1-x^2}}$<br>
> (b) $f(x)=\dfrac{1+x}{e^{\cos x}}$

### 中文翻譯

> 求每個函數的定義域。

### 題意拆解

指數函數 $e^u$ 對每一個實數 $u$ 都有定義，而且永遠大於 0。這兩題真正要檢查的是分母會不會等於 0。

### 一步一步解題

### (a)

分子 $1-e^{x^2}$ 對所有實數 $x$ 都有定義。分母不能為 0，因此排除使下式成立的 $x$：

$$
1-e^{1-x^2}=0.
$$

移項：

$$
e^{1-x^2}=1.
$$

因為 $e^0=1$，而指數函數是一對一，所以

$$
1-x^2=0.
$$

移項：

$$
x^2=1.
$$

因此

$$
x=1\quad\text{或}\quad x=-1.
$$

所以定義域為 $\boxed{\mathbb R\setminus\{-1,1\}}$。

### (b)

$\cos x$ 對所有實數都有定義，所以 $e^{\cos x}$ 也對所有實數有定義。又因

$$
e^{\cos x}>0,
$$

分母永遠不會是 0。分子 $1+x$ 也沒有任何限制，因此定義域為

$$
\boxed{\mathbb R}.
$$

## §1.5 #18 從反函數定義讀值

### English question

> If $f(x)=x^5+x^3+x$, find $f^{-1}(3)$ and $f(f^{-1}(2))$.

### 中文翻譯

> 若 $f(x)=x^5+x^3+x$，求 $f^{-1}(3)$ 與 $f(f^{-1}(2))$。

### 一步一步解題

### (a) 求 $f^{-1}(3)$

$f^{-1}(3)$ 的意思不是把 3 直接代入某條倒數公式，而是在問：

> 哪一個輸入值 $x$ 會使 $f(x)=3$？

先試最簡單的整數 $x=1$：

$$
f(1)=1^5+1^3+1.
$$

$$
=1+1+1.
$$

$$
=3.
$$

因此 $f(1)=3$。反函數把輸入輸出交換，所以

$$
\boxed{f^{-1}(3)=1}.
$$

### (b) 求 $f(f^{-1}(2))$

反函數的基本恆等式是

$$
f(f^{-1}(y))=y,
$$

只要 $y$ 在 $f$ 的值域內。這裡 $y=2$，因此

$$
\boxed{f(f^{-1}(2))=2}.
$$

這一小題不需要先求出 $f^{-1}(2)$；$f^{-1}$ 先把 2 帶回原輸入，再由 $f$ 送回 2，兩個動作互相抵消。

## §1.5 #26 分式線性函數的反函數

### English question

> Find a formula for the inverse of the function
>
> $h(x)=\dfrac{6-3x}{5x+7}$.

### 中文翻譯

> 求函數 $h(x)=(6-3x)/(5x+7)$ 的反函數公式。

### 一步一步解題

先把 $h(x)$ 寫成 $y$：

$$
y=\frac{6-3x}{5x+7}.
$$

兩邊乘以 $5x+7$：

$$
y(5x+7)=6-3x.
$$

展開左邊：

$$
5xy+7y=6-3x.
$$

把含 $x$ 的項移到左邊：

$$
5xy+3x=6-7y.
$$

左邊提出公因式 $x$：

$$
x(5y+3)=6-7y.
$$

兩邊除以 $5y+3$：

$$
x=\frac{6-7y}{5y+3}.
$$

交換輸入、輸出角色，也就是把 $y$ 改回 $x$：

$$
h^{-1}(x)=\frac{6-7x}{5x+3}.
$$

因此

$$
\boxed{h^{-1}(x)=\frac{6-7x}{5x+3}}.
$$

原函數的分母不能為 0：

$$
5x+7\ne0
\implies x\ne-\frac75.
$$

原函數的輸出不會等於 $-3/5$，所以

$$
D_h=\mathbb R\setminus\{-7/5\},
\qquad
R_h=\mathbb R\setminus\{-3/5\}.
$$

反函數交換定義域和值域：

$$
D_{h^{-1}}=\mathbb R\setminus\{-3/5\},
\qquad
R_{h^{-1}}=\mathbb R\setminus\{-7/5\}.
$$

## §1.5 #30 反函數

### English question

> Find a formula for the inverse of the function
>
> $y=\dfrac{1-e^{-x}}{1+e^{-x}}$.

### 中文翻譯

> 求函數 $y=(1-e^{-x})/(1+e^{-x})$ 的反函數公式。

### 一步一步解題

我們要把等式整理成「$x=$ 某個含 $y$ 的式子」。

$$
y=\frac{1-e^{-x}}{1+e^{-x}}.
$$

兩邊乘以 $1+e^{-x}$：

$$
y(1+e^{-x})=1-e^{-x}.
$$

展開左邊：

$$
y+ye^{-x}=1-e^{-x}.
$$

把含 $e^{-x}$ 的項移到左邊，把其他項移到右邊：

$$
ye^{-x}+e^{-x}=1-y.
$$

提出公因式 $e^{-x}$：

$$
e^{-x}(y+1)=1-y.
$$

兩邊除以 $y+1$：

$$
e^{-x}=\frac{1-y}{1+y}.
$$

兩邊取自然對數：

$$
\ln(e^{-x})
=\ln\left(\frac{1-y}{1+y}\right).
$$

因為 $\ln(e^u)=u$：

$$
-x=\ln\left(\frac{1-y}{1+y}\right).
$$

兩邊乘以 $-1$，並使用 $-\ln A=\ln(1/A)$：

$$
x=\ln\left(\frac{1+y}{1-y}\right).
$$

將輸入變數 $y$ 改回 $x$：

$$
\boxed{f^{-1}(x)=\ln\left(\frac{1+x}{1-x}\right)}.
$$

反函數的對數真數要正：

$$
\frac{1+x}{1-x}>0.
$$

分子與分母同號時分式為正。這發生在

$$
-1<x<1.
$$

所以反函數定義域為 $(-1,1)$，值域為 $\mathbb R$。

## §1.5 #44 展開對數

### English question

> Use the laws of logarithms to expand each expression.
>
> (a) $\ln\sqrt{\dfrac{3x}{x-3}}$<br>
> (b) $\log_2\left[(x^3+1)\sqrt[3]{(x-3)^2}\right]$

### 中文翻譯

> 使用對數律展開每一個式子。

### 一步一步解題

### (a)

先把平方根改寫成 $1/2$ 次方：

$$
\ln\sqrt{\frac{3x}{x-3}}
=\ln\left(\left(\frac{3x}{x-3}\right)^{1/2}\right).
$$

把指數 $1/2$ 移到對數前：

$$
=\frac12\ln\left(\frac{3x}{x-3}\right).
$$

使用商的對數律：

$$
=\frac12\left(\ln|3x|-\ln|x-3|\right).
$$

再使用乘積的對數律，而且 $3>0$：

$$
\ln\sqrt{\frac{3x}{x-3}}
=\frac12\ln3+\frac12\ln|x|-\frac12\ln|x-3|.
$$

現在檢查原式定義域。$\ln$ 的真數必須大於 0，而平方根也必須是正數，所以

$$
\frac{3x}{x-3}>0.
$$

臨界點是分子為 0 的 $x=0$，以及分母為 0 的 $x=3$。分式在兩邊同號時為正：

- $x<0$：分子、分母都為負，分式為正。
- $0<x<3$：分子正、分母負，分式為負。
- $x>3$：分子、分母都為正，分式為正。

因此原式完整定義域為

$$
\boxed{(-\infty,0)\cup(3,\infty)}.
$$

### (b)

先使用乘積的對數律：

$$
\log_2\left((x^3+1)\sqrt[3]{(x-3)^2}\right)
$$

$$
=\log_2(x^3+1)+\log_2\left(\sqrt[3]{(x-3)^2}\right).
$$

把三次根號改寫成 $1/3$ 次方：

$$
\sqrt[3]{(x-3)^2}
=((x-3)^2)^{1/3}.
$$

把指數移到對數前：

$$
\log_2\left(\sqrt[3]{(x-3)^2}\right)
=\frac13\log_2((x-3)^2).
$$

平方可能來自正或負的 $x-3$，所以使用絕對值：

$$
\log_2((x-3)^2)=2\log_2|x-3|.
$$

因此

$$
\log_2\left((x^3+1)\sqrt[3]{(x-3)^2}\right)
=\log_2(x^3+1)+\frac23\log_2|x-3|.
$$

最後找定義域。第一個因子要正：

$$
x^3+1>0
\iff x^3>-1
\iff x>-1.
$$

第二個因子在 $x=3$ 時等於 0，會使整個真數成為 0，所以還要 $x\ne3$。因此

$$
\boxed{D=(-1,3)\cup(3,\infty)}.
$$

## §1.5 #58 解方程

### English question

> Solve each equation for $x$. Give both an exact value and a decimal approximation, correct to three decimal places.
>
> (a) $\log_2(x^2-x-1)=2$<br>
> (b) $1+e^{4x+1}=20$

### 中文翻譯

> 解出每一題的 $x$。答案要同時包含精確值，以及四捨五入到小數點後三位的近似值。

### 一步一步解題

### (a)

先由對數定義

$$
\log_2A=2
\iff A=2^2.
$$

在這題 $A=x^2-x-1$，所以

$$
\log_2(x^2-x-1)=2
$$

等價於

$$
x^2-x-1=4.
$$

兩邊減 4：

$$
x^2-x-5=0.
$$

這個二次式不能用整數漂亮地因式分解，所以使用公式

$$
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}.
$$

這裡 $a=1$、$b=-1$、$c=-5$。代入：

$$
x=\frac{-(-1)\pm\sqrt{(-1)^2-4(1)(-5)}}{2(1)}.
$$

先算根號內：

$$
(-1)^2-4(1)(-5)=1+20=21.
$$

因此精確值是

$$
\boxed{x=\frac{1\pm\sqrt{21}}2}.
$$

近似值為

$$
x\approx2.791
\quad\text{或}\quad
x\approx-1.791.
$$

檢查時，兩根都滿足

$$
x^2-x-1=4>0,
$$

因此對數真數為正，兩根都合法。

### (b)

先把常數 1 移到右邊：

$$
1+e^{4x+1}=20
$$

$$
e^{4x+1}=19.
$$

兩邊取自然對數：

$$
\ln(e^{4x+1})=\ln19.
$$

因 $\ln(e^u)=u$：

$$
4x+1=\ln19.
$$

兩邊減 1：

$$
4x=\ln19-1.
$$

兩邊除以 4：

$$
\boxed{x=\frac{\ln19-1}{4}}.
$$

小數近似值是

$$
\boxed{x\approx0.486}.
$$

## §1.5 #63 定義域與反函數

### English question

> (a) Find the domain of $f(x)=\ln(e^x-3)$.<br>
> (b) Find $f^{-1}$ and its domain.

### 中文翻譯

> (a) 求 $f(x)=\ln(e^x-3)$ 的定義域。<br>
> (b) 求反函數 $f^{-1}$ 以及反函數的定義域。

### 一步一步解題

### (a) 原函數的定義域

$$
f(x)=\ln(e^x-3).
$$

對數真數必須大於 0：

$$
e^x-3>0.
$$

兩邊加 3：

$$
e^x>3.
$$

自然對數是遞增函數，所以兩邊取 $\ln$ 時不等號方向不變：

$$
x>\ln3.
$$

因此

$$
\boxed{D_f=(\ln3,\infty)}.
$$

### (b) 求反函數

先寫

$$
y=\ln(e^x-3).
$$

兩邊以 $e$ 為底取指數：

$$
e^y=e^x-3.
$$

兩邊加 3：

$$
e^x=e^y+3.
$$

兩邊取自然對數：

$$
x=\ln(e^y+3).
$$

把輸入變數 $y$ 改回 $x$：

$$
f^{-1}(x)=\ln(e^x+3).
$$

原函數的值域是所有實數，因此反函數的定義域是所有實數。最後答案：

$$
\boxed{f^{-1}(x)=\ln(e^x+3)},
\qquad
\boxed{D_{f^{-1}}=\mathbb R}.
$$

## §1.5 #74 反三角函數

### English question

> Find the exact value of each expression.
>
> (a) $\arcsin(\sin(5\pi/4))$<br>
> (b) $\cos(2\arcsin(5/13))$

### 中文翻譯

> 求每個式子的精確值。

### 一步一步解題

### (a)

$5\pi/4$ 在第三象限，參考角是 $\pi/4$。第三象限的正弦為負，因此

$$
\sin(5\pi/4)=-\frac{\sqrt2}{2}.
$$

arcsin 的答案必須落在

$$
[-\pi/2,\pi/2].
$$

這個範圍中，正弦為 $-\sqrt2/2$ 的角是 $-\pi/4$，所以

$$
\boxed{\arcsin(\sin(5\pi/4))=-\pi/4}.
$$

### (b)

令

$$
\theta=\arcsin(5/13).
$$

依定義：

$$
\sin\theta=\frac5{13}.
$$

使用倍角公式

$$
\cos(2\theta)=1-2\sin^2\theta.
$$

代入 $\sin\theta=5/13$：

$$
\cos(2\theta)
=1-2\left(\frac5{13}\right)^2.
$$

先平方：

$$
\left(\frac5{13}\right)^2=\frac{25}{169}.
$$

所以

$$
\cos(2\theta)
=1-\frac{50}{169}.
$$

把 1 寫成 $169/169$：

$$
\frac{169}{169}-\frac{50}{169}
=\boxed{\frac{119}{169}}.
$$

## §1.5 #77 化簡

### English question

> Simplify the expression $\sin(\tan^{-1}x)$.

### 中文翻譯

> 化簡 $\sin(\arctan x)$。

### 一步一步解題

令

$$
\theta=\arctan x.
$$

因此

$$
\tan\theta=x=\frac{x}{1}.
$$

在直角三角形中，可令對邊為 $x$、鄰邊為 1。由畢氏定理：

$$
\text{斜邊}
=\sqrt{x^2+1^2}
=\sqrt{1+x^2}.
$$

所以

$$
\sin\theta
=\frac{\text{對邊}}{\text{斜邊}}
=\frac{x}{\sqrt{1+x^2}}.
$$

換回 $\theta=\arctan x$：

$$
\boxed{\sin(\arctan x)=\frac{x}{\sqrt{1+x^2}}}.
$$

$\arctan x$ 對所有實數 $x$ 都有定義，而且分母 $\sqrt{1+x^2}$ 永遠大於 0，所以定義域是 $\mathbb R$。

## §1.5 #81 定義域與值域

### English question

> Find the domain and range of the function
>
> $g(x)=\sin^{-1}(3x+1)$.

### 中文翻譯

> 求函數 $g(x)=\arcsin(3x+1)$ 的定義域和值域。

### 一步一步解題

$$
g(x)=\arcsin(3x+1).
$$

arcsin 只接受 $[-1,1]$ 內的輸入，因此內層 $3x+1$ 必須滿足

$$
-1\le3x+1\le1.
$$

三個部分同時減 1：

$$
-2\le3x\le0.
$$

三個部分同時除以正數 3，所以不等號方向不變：

$$
-\frac23\le x\le0.
$$

因此

$$
\boxed{D_g=[-2/3,0]}.
$$

當 $x=-2/3$ 時：

$$
3(-2/3)+1=-1.
$$

當 $x=0$ 時：

$$
3(0)+1=1.
$$

而 $3x+1$ 隨 $x$ 連續地從 $-1$ 增加到 1，所以 arcsin 會跑完整個主值範圍：

$$
\boxed{R_g=[-\pi/2,\pi/2]}.
$$

---

# 10. 考前自我檢查

如果以下每一項都能不看筆記完成，就已掌握本次範圍：

- [ ] 能區分上確界與最大值，並說明 supremum 是否屬於集合。
- [ ] 能化簡分數、負數與無理數指數。
- [ ] 遇到 $0<a<1$ 的指數或對數不等式會反向。
- [ ] 每次寫函數答案都同步寫定義域。
- [ ] 知道合成函數定義域要檢查內層輸出。
- [ ] 知道公式相同但定義域不同的兩個函數不相等。
- [ ] 找反函數時能依原定義域選正負根，並交換定義域和值域。
- [ ] 展開偶次方的對數時會保留絕對值。
- [ ] 解對數方程會先列真數大於零並驗根。
- [ ] 能默寫 arcsin、arccos、arctan、arcsec 的主值範圍。
- [ ] 能用主值範圍處理 $\arcsin(\sin\theta)$ 類型。
- [ ] 能用直角三角形把反三角複合式化為代數式。

## 130 分鐘複習安排

1. 20 分鐘：讀第 2–7 節觀念，自己寫一張定義域與主值範圍表。
2. 50 分鐘：限時重做 Homework #1–20，每題先寫限制條件。
3. 40 分鐘：做 13 題共同勾選題，標出與 Homework 對應的題型。
4. 20 分鐘：只訂正錯題，為每個錯誤寫一句「下次先檢查什麼」。

最後原則：公式只是一半答案；定義域、單調方向、主值範圍與驗根，才是這份作業最常考、也最常失分的另一半。
