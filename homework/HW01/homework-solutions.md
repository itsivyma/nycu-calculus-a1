# Homework 1 作業逐題教學

[考前複習](review.md) · [微積分小組勾選題](common-exercises.md)

> 收錄 Homework 1 的英文原題、中文翻譯、題意拆解與不跳步詳解。原題來源：[老師課程網站](https://catalin-carstea.github.io/courses/calculus1-2026/homework-01.pdf)。

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

---

[回到考前複習](review.md) · [繼續做微積分小組勾選題](common-exercises.md)
