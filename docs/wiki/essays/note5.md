---
title: 贴吧用户：【科普贴】86版五笔中常见的一些拆分时违背了笔顺的字的拆分方法
tags:
  - 汉字编码
  - 输入法
  - 综述
date: 2020-03-31 02:02:00
src: 
  - https://tieba.baidu.com/p/6586359073?see_lz=1
---

> 作者：贴吧用户
> 
> [:link: 原文](https://tieba.baidu.com/p/6586359073?see_lz=1)

我们现在写字所用的笔顺，是由 1997 年出版的《现代汉语通用字笔顺规范》规定的。
但是，五笔 86 版出来的时候还没有这玩意，所以这导致了一些字拆分时未完全按照笔顺/字形来拆分。
本贴将列举一些常见的字，并给出拆分方法和编码（86 版和 98 版的都给出来）。建议收藏哦 😊

首先说明，非偏旁/部首类字根是无法打出来的，所以楼主会用“会意表示法”或使用组成这个字根的所有笔顺外加引号来表示这个字根。
比如“鱼”的第一个字根就表示为“无尾鱼”，98 版五笔中“逐”的第二个字根就表示为“撇、弯钩、撇、撇、撇、捺”（98 版五笔中没有“豕”这个字根）。

漏说了一点，有些字 86 版和 98 版拆分方法区别很大，在本贴中也会给出来哦～

## 戈、刀

“戈、刀”这些就不说了，初学者都应该知道的，就是注意“刀”单用的时候仍然认为末笔是撇，但用在其他字里面则认为末笔是折。

## 凹、凸

首先就是笔顺少的字中最难写的俩字了：凹、凸。

首先说说这俩字的笔顺：

- 凹：竖、横折折、竖、横折、横
- 凸：竖（左上方的）、横（左边的）、竖（左下方的）、横折折折、横。

但是 86 年那会儿谁知道这俩字咋写啊，只好自创写法了。

- “凹”拆法：第一个字根是把前两笔看成“冂”，第二个字根是把第 3、4 笔看成“冂”，最后是拆“一”，加上识别码 d，故“凹”编码为`mmgd`。
- “凸”拆法：先拆左下方的竖，再拆左边的横，接着把左上方的竖和右边“横折折折”的“横折”部分合一起看成“冂”，最后拆下面那一横。编码为`hgmg`。

98 版环境下，这俩字按照笔顺一笔一笔的拆，编码分别为`hnhg`和`hghg`。

## 非

然后是“非”字，可能很多人写的时候会先写三横，再写两竖，最后写三横。但是这是错误的笔顺，正确的笔顺是“竖横横横竖横横横”。
这个字 86 版编码是`djdd`（我也不知道为什么王永民认为它是杂合型），98 版编码是`hdhd`。

## 瓦

“瓦”字，笔顺是“横、折、折、点”（不写那么复杂的名称了，反正下面除竖钩外所有带转折的笔画楼主都会用“折”表示），
但是 86 版中认为其笔画是“横、折、点、折”，故其编码为`gnyn`，98 版中仍是正常的`gnny`。

## 止

“止”字笔顺是“竖横竖横”，但 86 版中认为是“竖竖横横”，所以其编码是`hhhg`，98 版中是正常的`hhgg`。
（楼主认为 86 版应该不是刻意不让“上”、“止”俩字重码的）

## 方、万

“方、万”，下面是先写折，再写撇。但是 86 版是反着来的。

- “方”字 86 版编码为`yygn`，98 版为`yygt`。
- 而“万”字，两个版本的拆分方法不一样。86 版是“丆、乛”，98 版是“一、’横折钩、撇’”。编码分别为`dnv`和`gqe`。

## 燕、率、兆、兜、夔

“燕”、“率”、“兆”、“兜”、“夔（kuí）”等字，书写时均遵循“先中间后两边”的原则。
但是，86 版中除“率”外，其他类似的字拆分时都是强制遵循从左到右原则。
下面是这些字的编码（按前面的顺序一一对应，撇号左边为 86 版编码，右边为 98 版。）

```
auko / akuo
yxif / yxif
iqv / qii
qrnq / rqnq
uhtt / utht
```

例外情况：“脊”字，笔顺规定了先写“点提撇点”，再写“人”。其 86 版和 98 版编码均为`iwef`。

## 平、夹、来、求、亍

“平、夹、来、求、亍”，86 版中这些字拆分时违背了基本原则。

- “平”拆分方法不是“一、丷、十”，而是“一、䒑、丨”。
- “夹”字拆分方法不是“一、丷、大”，而是“一、䒑、人”。
- “求”字拆分方法不是“一、氺、丶”，而是“十、’点提撇点’、丶”。
- “亍”字拆分方法不是“一、丁”，而是“二、亅”。
  以上四字，前面给出的拆法均为这些字在 98 版中的拆法。

“来”字，86 版中拆分方法为“一、米”，98 版中为，“一、丷、木”。

以上字的编码：

```
guhk / gufk
guwi / gudi
goi / gusi
fiyi / giyi
fhk / gsj
```

## 象

“象”字，中间那里是撇出头，并没有一竖。但是 86 版中认为那里有一竖。此字 86 版编码为`qjeu`，98 版为`qkeu`。
类似的“免、兔”等字，没有这个规定。

## 段、予、丑

“段、予、丑”，86 版中忽略了字形，拆分时强行取大。

- “段”字拆分方法：“亻、三、几、又”
- “予”：龴、了。
- “丑”：乛、土。

98 版中考虑到了字形和部首因素，拆法不同。

- “段”：丿、丨、三、又（毕竟前两笔没有组成单人旁）。
- “予”：龴、乛、亅（最后两笔拆开，不视为“了”）。
- “丑”：乛、丨、一、一（把里面不明显的“土”拆开了）。

编码：

```
wdmc / thdc
cbj / cnhj
nfd / nhgg
```

## 曳

“曳”字最后两笔要看成“匕”，但末笔还是认为是丿，不是乛（真佩服王永民这脑洞啊）。98 版中仍然是正常的分开拆。
编码：`jxe` / `jnte`。

## 幽

“幽”字，按照笔顺拆开应该是“山、幺、幺”，但是 86 版中拆法是“幺、幺、山”。

编码：`xxmk` / `mxxi`。

## 越

“越”右上部分，86 版拆法是“匚、乛、丶、丿”，98 版是“戈、乛”。

编码：`fhat` / `fhan`。
