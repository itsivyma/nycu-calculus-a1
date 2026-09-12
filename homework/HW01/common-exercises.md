# 微積分小組勾選題逐題教學

[考前複習](review.md) · [Homework 1 作業逐題教學](homework-solutions.md)

> 收錄本次範圍 §1.4 與 §1.5 的所有勾選題，包含英文原題、中文翻譯與不跳步詳解。題號來源：[陽明交大微積分小組 9E 共同習題](https://calculus.math.nycu.edu.tw/calculusmath/ch/app/artwebsite/view?module=artwebsite&id=39529&serno=3e458c4c-38ac-4e7a-b6c2-4499670c07ba)。

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

---

[回到考前複習](review.md) · [回到 Homework 1 作業](homework-solutions.md)
