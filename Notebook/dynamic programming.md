
### 动态规划 Dynamic Programming

<h4>(1) [生活例子]</h4>

<p>

先来看看生活中经常遇到的事吧——假设您是个土豪，身上带了足够的1、5、10、20、50、100元面值的钞票。现在您的目标是凑出某个金额w，需要用到尽量少的钞票。

依据生活经验，我们显然可以采取这样的策略：能用100的就尽量用100的，否则尽量用50的……依次类推。在这种策略下，666=6×100+1×50+1×10+1×5+1×1，共使用了10张钞票。
这种策略是 贪心策略 [(尽可能让剩下的值最小, 贪心是一种只考虑眼前情况的策略)]

但是，如果我们换一组钞票的面值，贪心策略就也许不成立了。
如果一个奇葩国家的钞票面额分别是1、5、11，那么我们在凑出15的时候，贪心策略会出错: 15=1×11+4×1（贪心策略使用了5张钞票）15=3×5 正确的策略，只用3张钞票
为什么会这样呢？贪心策略错在了哪里？
</p>

- brute force: 暴力是枚举 有些是是否冗余信息
- Dynamic Programming: 将一个问题拆成几个子问题，分别求解这些子问题，即可推断出大问题的解
- greedy algorithm: 在对问题求解时，总是做出在当前看来是最好的选择

<h4>(2) 斐波那契数列(Fibonacci)</h4>
1， 1， 2， 3， 5， 8， 13 ，21 ...

Fn = Fibonacci(n-1) + Fibonacci(n-2)
例如: F(3) = F(2) + F(1)
(其中Fibonacci(0)=Fibonacci(1)=1)
<img data-rawheight="310" src="https://pic1.zhimg.com/80/v2-82dbeb092f6723332e4fbe2ad773b16c_hd.jpg" data-size="normal" data-rawwidth="734" class="origin_image zh-lightbox-thumb lazy" width="400" data-original="https://pic1.zhimg.com/v2-82dbeb092f6723332e4fbe2ad773b16c_r.jpg" data-actualsrc="https://pic1.zhimg.com/50/v2-82dbeb092f6723332e4fbe2ad773b16c_hd.jpg">

大量的重复问题会让计算效率贬低

<pre>
也就是说，动态规划一定是具备了以下三个特点：

把原来的问题分解成了几个相似的子问题。（强调“相似子问题”）
所有的子问题都只需要解决一次。（强调“只解决一次”）
储存子问题的解。（强调“储存”）
</pre>

这个问题很好解决，我们只需要利用动态规划的第三个特点——”储存子问题的解“就可以了.

<img data-rawheight="296" src="https://pic3.zhimg.com/80/v2-e6134d1195f7413d56b060462be26c75_hd.jpg" data-size="normal" data-rawwidth="562" class="origin_image zh-lightbox-thumb lazy" width="400" >

从下往上加上去就好了, 红色的部分代表, 已经是存储的部分了。

<div>
dynamic programming is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions.
</div>