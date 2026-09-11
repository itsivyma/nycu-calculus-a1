# Homework 1 完整教學

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

---

## 3. 核心觀念二：根式、實數指數與指數函數

### 3.1 指數律

對正底數 $a,b>0$：

\[
a^r a^s=a^{r+s},\qquad
\frac{a^r}{a^s}=a^{r-s},\qquad
(a^r)^s=a^{rs},\qquad
(ab)^r=a^r b^r.
\]

負指數表示倒數：$a^{-r}=1/a^r$。分數指數表示根式：$a^{m/n}=(\sqrt[n]{a})^m$。

### 3.2 單調性是解不等式的關鍵

- $a>1$ 時，$a^x$ 嚴格遞增，所以 $a^u\le a^v\iff u\le v$。
- $0<a<1$ 時，$a^x$ 嚴格遞減，所以 $a^u\le a^v\iff u\ge v$。

常見失分點：底數小於 1 時忘記反向。

### 3.3 指數方程

看到 $4^x$ 與 $2^x$ 同時出現，令 $u=2^x>0$，則 $4^x=u^2$。先解代數方程，再把 $u$ 換回去。

---

## 4. 核心觀念三：函數不只是一條公式

一個函數由「定義域、對應規則、陪域」共同決定。因此兩條相同的化簡公式，只要定義域不同，就不是同一個函數。

### 4.1 函數運算的定義域

\[
D_{f+g}=D_f\cap D_g,\qquad
D_{fg}=D_f\cap D_g,
\]

\[
D_{f/g}=\{x\in D_f\cap D_g:g(x)\ne0\}.
\]

合成函數的規則是

\[
D_{f\circ g}=\{x\in D_g:g(x)\in D_f\}.
\]

不要只找最外層函數的限制；必須先讓內層有定義，再讓內層輸出落入外層定義域。

---

## 5. 核心觀念四：反函數

函數要有反函數，必須一對一；圖形上等價於通過水平線測試。找反函數：

1. 寫 $y=f(x)$。
2. 交換 $x,y$。
3. 解出 $y$。
4. 寫出反函數的定義域與值域。
5. 用 $f(f^{-1}(x))=x$ 與 $f^{-1}(f(x))=x$ 驗證。

反函數的圖形是原圖對直線 $y=x$ 的鏡射。原函數的定義域與值域會互換。

---

## 6. 核心觀念五：對數

\[
\log_b x=y\iff b^y=x,\qquad b>0,\ b\ne1,\ x>0.
\]

對數真數一定要正：

\[
\log_b(MN)=\log_bM+\log_bN,
\]

\[
\log_b(M/N)=\log_bM-\log_bN,
\]

\[
\log_b(M^r)=r\log_bM.
\]

若因式可能為負，不能直接寫 $\ln(x-1)$；應寫 $\ln|x-1|$。例如

\[
\ln((x-1)^2)=2\ln|x-1|.
\]

換底公式：

\[
\log_bx=\frac{\ln x}{\ln b}.
\]

解對數方程的固定流程：先列定義域、再合併或指數化、最後把候選解代回定義域。

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

---

# 8. Homework 1 逐題帶寫

## #1 上確界

### (a) $A=\{x\in\mathbb R:x^2<3\}$

$x^2<3$ 等價於 $-\sqrt3<x<\sqrt3$，所以

\[
\sup A=\sqrt3.
\]

但 $\sqrt3$ 不在集合內，因為它的平方等於 3，不小於 3。

### (b) $B=\{q\in\mathbb Q:q<5/2\}$

\[
\sup B=\frac52.
\]

$5/2$ 是有理數，但條件是嚴格小於，因此不在集合中。有理數的稠密性保證任何比 $5/2$ 小的數都不是上界。

### (c) $C=[-1,2]\cup\{4\}$

\[
\sup C=4,
\]

而且 $4\in C$，所以它也是最大值。

**檢查點：** 題目問的是 supremum 和是否取到，不要只寫一個數。

## #2 指數化簡

\[
\left(\frac{81}{16}\right)^{-3/4}
=\left(\frac{3^4}{2^4}\right)^{-3/4}
=\left(\frac32\right)^{-3}
=\frac8{27}.
\]

\[
32^{2/5}=(2^5)^{2/5}=2^2=4.
\]

\[
(\sqrt[3]{25})^{3/2}
=(25^{1/3})^{3/2}=25^{1/2}=5.
\]

## #3 指數律

### (a)

\[
\frac{(a^{\sqrt5-1})^{\sqrt5+1}}{a^2}
=a^{(\sqrt5-1)(\sqrt5+1)-2}
=a^{4-2}=a^2.
\]

### (b)

\[
\frac{(x^{3/2}y^{-1/2})^2}{xy^{-2}}
=\frac{x^3y^{-1}}{xy^{-2}}
=x^2y.
\]

## #4 不使用分數指數證明根式乘法

令 $\alpha=\sqrt[n]{a}$、$\beta=\sqrt[n]{b}$。依根式定義，

\[
\alpha>0,\quad \beta>0,\quad \alpha^n=a,\quad \beta^n=b.
\]

因此

\[
(\alpha\beta)^n=\alpha^n\beta^n=ab.
\]

$\alpha\beta>0$，而正的 $n$ 次方根唯一，所以

\[
\sqrt[n]{ab}=\alpha\beta=\sqrt[n]a\,\sqrt[n]b.
\]

關鍵不是套指數律，而是使用「正 $n$ 次方根的唯一性」。

## #5 指數不等式

\[
\left(\frac12\right)^{x^2-x}\ge\frac14
=\left(\frac12\right)^2.
\]

因底數 $1/2$ 小於 1，函數遞減，所以

\[
x^2-x\le2
\iff x^2-x-2\le0
\iff(x-2)(x+1)\le0.
\]

答案：

\[
\boxed{[-1,2]}.
\]

## #6 指數方程

\[
4^x-5\cdot2^x+4=0.
\]

令 $u=2^x>0$，則

\[
u^2-5u+4=(u-1)(u-4)=0.
\]

$u=1$ 或 $u=4$，故

\[
\boxed{x=0,\ 2}.
\]

## #7 函數運算與定義域

令 $f(x)=\sqrt{x+2}$、$g(x)=\sqrt{3-x}$。有

\[
D_f=[-2,\infty),\qquad D_g=(-\infty,3].
\]

因此

\[
(f+g)(x)=\sqrt{x+2}+\sqrt{3-x},\quad D=[-2,3],
\]

\[
(fg)(x)=\sqrt{(x+2)(3-x)},\quad D=[-2,3],
\]

\[
(-2f)(x)=-2\sqrt{x+2},\quad D=[-2,\infty),
\]

\[
\left(\frac fg\right)(x)=\frac{\sqrt{x+2}}{\sqrt{3-x}},
\quad D=[-2,3).
\]

最後一題的 $x=3$ 必須排除，因為分母為零。

## #8 合成函數

$f(x)=\sqrt x$、$g(x)=1/(x-2)$。

\[
(f\circ g)(x)=\sqrt{\frac1{x-2}}.
\]

要有 $1/(x-2)\ge0$ 且 $x\ne2$，得到

\[
D_{f\circ g}=(2,\infty).
\]

\[
(g\circ f)(x)=\frac1{\sqrt x-2}.
\]

要有 $x\ge0$ 且 $\sqrt x\ne2$，得到

\[
D_{g\circ f}=[0,\infty)\setminus\{4\}.
\]

兩者公式和定義域都不同，所以 $f\circ g\ne g\circ f$。

## #9 函數相等

\[
F(x)=\frac{x^2-9}{x-3}=x+3\qquad(x\ne3).
\]

雖然化簡後與 $G(x)=x+3$ 形式相同，但 $F$ 在 $x=3$ 沒有定義，而 $G$ 有。因此兩者不是同一函數。

若把 $G$ 的定義域限制為 $\mathbb R\setminus\{3\}$，兩者才相等。

## #10 限制定義域後找反函數

\[
f(x)=(x+2)^2-3,\qquad x\le-2.
\]

從 $y=(x+2)^2-3$ 得

\[
x+2=\pm\sqrt{y+3}.
\]

因原定義域要求 $x+2\le0$，必須選負號：

\[
f^{-1}(x)=-2-\sqrt{x+3}.
\]

\[
D_{f^{-1}}=[-3,\infty),\qquad
R_{f^{-1}}=(-\infty,-2].
\]

驗證 $f^{-1}(f(x))$ 時，

\[
\sqrt{(x+2)^2}=|x+2|=-(x+2)
\]

是因為 $x\le-2$。這一步最容易漏。

## #11 自身就是反函數

\[
f(x)=\frac{x+1}{x-1},\qquad x\ne1.
\]

直接合成：

\[
f(f(x))
=\frac{\frac{x+1}{x-1}+1}{\frac{x+1}{x-1}-1}
=x.
\]

另外 $f(x)\ne1$，所以值域也是 $\mathbb R\setminus\{1\}$。因此

\[
\boxed{f^{-1}=f}.
\]

它不是恆等函數，例如 $f(0)=-1\ne0$。

## #12 指數函數的反函數與圖形

\[
h(x)=2^{x+1}-2.
\]

由 $y=2^{x+1}-2$：

\[
y+2=2^{x+1}
\implies x=\log_2(y+2)-1.
\]

所以

\[
h^{-1}(x)=\log_2(x+2)-1.
\]

圖形資訊：

| | $h$ | $h^{-1}$ |
| --- | --- | --- |
| 定義域 | $\mathbb R$ | $(-2,\infty)$ |
| 值域 | $(-2,\infty)$ | $\mathbb R$ |
| 漸近線 | $y=-2$ | $x=-2$ |
| 對應點 | $(-1,-1),(0,0),(1,2)$ | $(-1,-1),(0,0),(2,1)$ |

兩圖對 $y=x$ 對稱。

## #13 對數與指數精確值

\[
\log_9 27=\frac32,\qquad
\log_{1/4}8=-\frac32.
\]

\[
\ln(e^3\sqrt e)=\ln(e^{7/2})=\frac72.
\]

\[
e^{\ln7-2\ln\sqrt7}
=e^{\ln7-\ln7}=1.
\]

## #14 展開對數且保留完整定義域

\[
L(x)=\ln\left(\frac{(x-1)^2}{x+2}\right).
\]

真數為正。分子在 $x\ne1$ 時為正，所以需要 $x+2>0$ 且 $x\ne1$：

\[
D_L=(-2,1)\cup(1,\infty).
\]

正確展開：

\[
\boxed{L(x)=2\ln|x-1|-\ln(x+2)}.
\]

若寫成 $2\ln(x-1)$，會錯誤刪掉 $-2<x<1$。

## #15 對數方程

### (a)

先列定義域 $x>1$。合併對數並指數化後得到

\[
x^2+x-6=0
\iff(x-2)(x+3)=0.
\]

只有 $x=2$ 符合定義域，因此 $\boxed{x=2}$。

### (b)

先列定義域 $x>0$。化簡後

\[
x^2=3x+4
\iff(x-4)(x+1)=0.
\]

只有 $x=4$ 合法，因此 $\boxed{x=4}$。

## #16 對數不等式

\[
\log_{1/2}(x-1)\ge-2.
\]

先有 $x>1$。因底數 $1/2<1$，對數函數遞減：

\[
0<x-1\le\left(\frac12\right)^{-2}=4.
\]

所以

\[
\boxed{x\in(1,5]}.
\]

## #17 換底公式

由

\[
\log_ba\cdot\log_ab
=\frac{\ln a}{\ln b}\frac{\ln b}{\ln a}=1
\]

得到

\[
\boxed{\log_ab=\frac1{\log_ba}}.
\]

又

\[
\frac{\log_au}{\log_av}
=\frac{\ln u/\ln a}{\ln v/\ln a}
=\frac{\ln u}{\ln v}
=\boxed{\log_vu}.
\]

## #18 反三角函數精確值

依主值範圍：

\[
\arcsin\left(-\frac{\sqrt3}{2}\right)=-\frac\pi3,
\]

\[
\arccos\left(-\frac12\right)=\frac{2\pi}{3},
\]

\[
\arctan(1)=\frac\pi4,
\]

\[
\operatorname{arcsec}(-2)=\frac{2\pi}{3}.
\]

## #19 折回主值範圍

\[
\arcsin(\sin(7\pi/6))=-\frac\pi6,
\]

\[
\arccos(\cos(7\pi/4))=\frac\pi4,
\]

\[
\arctan(\tan(5\pi/6))=-\frac\pi6,
\]

\[
\operatorname{arcsec}(\sec(5\pi/4))=\frac{3\pi}{4}.
\]

做題時先看外層反函數的值域，再找同值且落在該區間的角。

## #20 化成代數式並寫定義域

### (a) $\sin(\arctan x)$

令 $\theta=\arctan x$，則 $\tan\theta=x/1$。取直角三角形的鄰邊 1、對邊 $x$，斜邊為 $\sqrt{1+x^2}$。因 $\theta\in(-\pi/2,\pi/2)$，餘弦為正：

\[
\boxed{\sin(\arctan x)=\frac{x}{\sqrt{1+x^2}}},
\qquad D=\mathbb R.
\]

### (b) $\tan(\arccos x)$

令 $\theta=\arccos x$，則 $\cos\theta=x$ 且 $\theta\in[0,\pi]$，所以 $\sin\theta=\sqrt{1-x^2}$：

\[
\tan(\arccos x)=\frac{\sqrt{1-x^2}}x.
\]

除了 $-1\le x\le1$，還要排除分母 $x=0$：

\[
\boxed{D=[-1,0)\cup(0,1]}.
\]

---

# 9. 微積分小組共同勾選題

以下依課本 9E Metric Version 原題核對，保留解題核心，不抄錄大段題文。

## §1.4 #2 指數律

\[
\text{(a) }\frac{\sqrt[3]4}{\sqrt[3]{108}}=\sqrt[3]{\frac1{27}}=\frac13,
\qquad
\text{(b) }27^{2/3}=9.
\]

\[
\text{(c) }2x^2(3x^5)^2=18x^{12},
\qquad
\text{(d) }(2x^{-2})^{-3}x^{-3}=\frac{x^3}{8}.
\]

\[
\text{(e) }\frac{3a^{3/2}a^{1/2}}{a^{-1}}=3a^3,
\]

\[
\text{(f) }\frac{\sqrt{a\sqrt b}}{\sqrt[3]{ab}}
=a^{1/6}b^{-1/12}
=\frac{\sqrt[6]a}{\sqrt[12]b}.
\]

**自問：** 每次相乘、相除、乘方時，指數分別做了什麼？

## §1.4 #9 指數圖形變換

$g(x)=3^x+1$ 是 $3^x$ 上移 1：

- 定義域 $\mathbb R$，值域 $(1,\infty)$。
- 水平漸近線 $y=1$。
- $y$ 截距 $(0,2)$，嚴格遞增。

$h(x)=2(1/2)^x-3$：

- 先縱向放大 2 倍，再下移 3。
- 定義域 $\mathbb R$，值域 $(-3,\infty)$。
- 水平漸近線 $y=-3$。
- $y$ 截距 $(0,-1)$，嚴格遞減。

## §1.4 #13 指數圖形

\[
y=1-\frac12e^{-x}.
\]

可由 $e^x$ 依序做左右反射、乘 $-1/2$、上移 1：

- 定義域 $\mathbb R$。
- 值域 $(-\infty,1)$。
- 水平漸近線 $y=1$。
- $y$ 截距 $(0,1/2)$。
- 函數嚴格遞增。

## §1.4 #17 定義域

### (a)

分母含 $1-e^{\,1-x^2}$。令分母為零：

\[
e^{1-x^2}=1
\iff1-x^2=0
\iff x=\pm1.
\]

所以定義域為 $\boxed{\mathbb R\setminus\{-1,1\}}$。

### (b)

分母為 $e^{\cos x}$，指數函數永遠大於零，因此不會造成限制；定義域為 $\boxed{\mathbb R}$。

## §1.5 #18 從反函數定義讀值

反函數只是把輸入輸出交換。題目給的函數滿足 $f(1)=3$，所以

\[
\boxed{f^{-1}(3)=1}.
\]

而合成恆等式直接給出

\[
\boxed{f(f^{-1}(2))=2}.
\]

## §1.5 #26 分式線性函數的反函數

\[
h(x)=\frac{6-3x}{5x+7}.
\]

令 $y=(6-3x)/(5x+7)$，交叉相乘後解 $x$：

\[
x=\frac{6-7y}{5y+3}.
\]

所以

\[
\boxed{h^{-1}(x)=\frac{6-7x}{5x+3}}.
\]

原函數定義域排除 $-7/5$、值域排除 $-3/5$；反函數剛好互換。

## §1.5 #30 反函數

\[
y=\frac{1-e^{-x}}{1+e^{-x}}.
\]

整理：

\[
y(1+e^{-x})=1-e^{-x}
\implies e^{-x}=\frac{1-y}{1+y}.
\]

取對數可得

\[
\boxed{f^{-1}(x)=\ln\left(\frac{1+x}{1-x}\right)}.
\]

其定義域為 $(-1,1)$，值域為 $\mathbb R$。

## §1.5 #44 展開對數

### (a)

\[
\ln\sqrt{\frac{3x}{x-3}}
=\frac12\ln3+\frac12\ln|x|-\frac12\ln|x-3|.
\]

原式完整定義域為

\[
\boxed{(-\infty,0)\cup(3,\infty)}.
\]

### (b)

\[
\log_2\left((x^3+1)\sqrt[3]{(x-3)^2}\right)
=\log_2(x^3+1)+\frac23\log_2|x-3|.
\]

要有 $x^3+1>0$ 且 $x\ne3$，所以

\[
\boxed{D=(-1,3)\cup(3,\infty)}.
\]

## §1.5 #58 解方程

### (a)

\[
\log_2(x^2-x-1)=2
\iff x^2-x-1=4.
\]

\[
\boxed{x=\frac{1\pm\sqrt{21}}2}.
\]

兩根代回時真數都是 4，均合法。

### (b)

\[
1+e^{4x+1}=20
\iff e^{4x+1}=19
\]

\[
\boxed{x=\frac{\ln19-1}{4}}.
\]

## §1.5 #63 定義域與反函數

\[
f(x)=\ln(e^x-3).
\]

因 $e^x-3>0$，

\[
\boxed{D_f=(\ln3,\infty)}.
\]

由 $y=\ln(e^x-3)$：

\[
e^y=e^x-3
\implies x=\ln(e^y+3).
\]

所以

\[
\boxed{f^{-1}(x)=\ln(e^x+3)},\qquad D_{f^{-1}}=\mathbb R.
\]

## §1.5 #74 反三角函數

\[
\boxed{\arcsin(\sin(5\pi/4))=-\pi/4}.
\]

令 $\theta=\arcsin(5/13)$。則 $\sin\theta=5/13$，且主值範圍保證 $\cos\theta=12/13$：

\[
\cos(2\theta)=1-2\sin^2\theta
=1-\frac{50}{169}
=\boxed{\frac{119}{169}}.
\]

## §1.5 #77 化簡

令 $\theta=\arctan x$。用直角三角形或 $1+\tan^2\theta=\sec^2\theta$：

\[
\boxed{\sin(\arctan x)=\frac{x}{\sqrt{1+x^2}}},
\qquad x\in\mathbb R.
\]

## §1.5 #81 定義域與值域

\[
g(x)=\arcsin(3x+1).
\]

要有

\[
-1\le3x+1\le1
\iff-\frac23\le x\le0.
\]

因此

\[
\boxed{D_g=[-2/3,0]},\qquad
\boxed{R_g=[-\pi/2,\pi/2]}.
\]

因 $3x+1$ 在該定義域內剛好跑完整個 $[-1,1]$，所以值域是完整的 arcsin 主值範圍。

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
