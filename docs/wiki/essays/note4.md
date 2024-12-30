---
title: 戴石麟：汉字编码输入法综述(2003)
tags:
  - 汉字编码
  - 输入法
  - 综述
date: 2020-11-18 17:46:01
src: 
  - https://sbxlm.github.io/posts/hzbmsrfzs.html
  - https://github.com/sbsrf/home/blob/main/posts/hzbmsrfzs.md
---

作者：戴石麟(sbxlm@126.com) 汉字编码输入法综述 [:link: 原文](https://sbxlm.github.io/posts/hzbmsrfzs.html)

>本文是本人于2003年做的研究生论文综述，权当作一个遥远的输入法历史回顾吧。这次重新整理成HTML格式的同时，修改了个别的错别字和语法错误。当我重温此文的时候，仍然觉得收获不小，希望对读者也有所裨益。
>
>现在是2020年末，汉字输入技术已经发生了巨大变化，人工智能技术的应用使得文字识别和语音识别这些非编码输入方式日益成熟、实用，基于键盘编码的汉字输入也取得长足的进步。互联网和智能手机的普及，使中文输入产品及其用户的格局发生了深刻的变化，形成了搜狗输入法、百度输入法和讯飞输入法三大头部产品。输入法的商业模式更是焕然一新，输入法均是免费提供，变现则是通过其它方式实现。中文顶功编码理论和输入技术从2005年诞生，经过10多年的发展，到逐步为输入法爱好者接受，口碑相传，亲自动手，尝试用顶功技术对音码、形码、音形码进行改造，对字词模式和整句模式进行优化，取得了丰硕成果，最著名的有声笔系列和星空系列的顶功输入法方案，另外还有一码起顶的左飞 1811，二码起顶的西风瘦码、小兮码、灵形速影、左飞双拼、顶功雅歌，三码起顶的左飞三码、听雨三码，二四顶屏的顶功希码，星空学系列的星空两笔、星空键道及其变种，采用四二顶的 C42，采用五二顶的徐码五二顶等等。
>
>至于本文所述输入法历史之后的进展情况，本人打算另外撰文加以回顾。

<!--more-->

1978年7月9日上海《文汇报》在第一版以标题为“汉字进入了计算机”长篇文章详细报道了支秉彝先生完成“见字识码”的小键盘输入汉字的设计方案和编码码本，掀开了“编码潮”的序幕，越来越多的人卷入到汉字与电脑碰撞的旋涡，形成了陈力为先生所形容为“史无前例的规模巨大的群众性科研活动”。

1978年12月，张其睿、支秉彝等汉字编码先行者在青岛召开了我国首次“汉字编码研究会”。会后，科学技术文献出版社出版了《汉字编码方案汇编》，这是第一本关于编码方案的专著。1979年夏，陈明远主持了第一个中文信息研讨班，进行了为时两个月信息处理汉字的基础理论和编码方案研究，张普等将研究成果连续发表在《语文现代化》杂志上，这是第一批研究汉字特征信息的论文。1981年，以钱伟长为理事长的中国中文信息学会成立。中文信息学会及所属的汉字编码专业委员会、《中文信息学报》、《中文信息》等杂志成为组织交流汉字编码及理论的场所和媒介。1981年至今中文信息学会、汉字编码委员会召开国际性、全国性学术会议几十次。在上述学术会议和全国性杂志、报刊、专利公告上发表的国内外论文和公布编码方案约在数千种以上，已上机运行的也超千种。

汉字编码输入利用计算机的标准配置实现，通过编码对汉字信息进行压缩，既经济又快速，因而一直是汉字信息处理领域中参与人数最多、研究得最多、讨论得最热烈、产品竞争最激烈的领域。随着手机在中国的普及，手机短信量急剧增加，又促进了数字键盘汉字编码输入法的发展。

虽然目前的汉字编码输入法已有成千上万，然而对它的研究热潮仍然一浪高过一浪。纵观为数众多的汉字编码输入法，大多为低水平的重复设计和开发，技术上的突破很少，理论上的创新就更为罕见了，造成了巨大的人力、物力和财力的浪费。同时，虚假的广告宣传、恶性的商业竞争、猖狂的盗版使用，既使得广大的用户无所适从，又损害了汉字编码输入法开发者的利益。

本文打算分基础工作、理论研究和实用系统三个方面来对汉字编码输入技术的历史和现状进行综合评述，最后指出现有技术中存在的问题并预测今后技术的发展趋势。基础工作包括国家标准和规范的制定和推行，语料库建设，字、词和汉字特征信息使用频度统计；理论研究包括汉字各阶信息熵计算，字词编码最短极限码长的计算，汉字编码输入模型的建立，输入法评测方法的讨论；实用系统包括至今为止已投入使用的典型汉字编码输入系统的发展状况，它们在编码技术、反馈技术、接口技术等方面的特点。

## 1 基础工作

1974年8月，我国开始了第一个大型汉字信息处理工程项目“748工程”，其主要成果之一是《汉字频度表》，它首先为汉字信息处理提供了重要的基础数据。1980年前后，陈明远、盛谏等人分别公布汉语音节、声母、韵母、声调和字母频度统计。1980年，经过对《汉字频度表》和其它字表的统计分析，国家标准总局颁布了汉字信息处理领域的第一个国家标准《信息交换用汉字编码字符集·基本集》（GB2312-80）。这是一个在中国的汉字信息处理历史上划时代的、具有深远影响的标准。1981年，武汉大学、复旦大学等公布了在《新华字典》字集范围内的字根频度统计结果。1984年，国家文字改革委员会与武汉大学公布了《辞海》字集范围内汉字笔画、部件、结构的动态统计分析结果。1985年，国家文字改革委员会与山西大学公布了人命姓氏用字的抽样统计分析结果。1986年，北京航空学院、新华社利用计算机技术分别公布了基于大型语料库的新的汉字使用频度统计和流通频度统计<sup>[5]</sup>。1985年后，还有北京师范大学、上海交通大学、北京语言学院等分别使用各具特色的自动分词技术公布了大型语料库的现代汉语词语使用频度统计<sup>[8]</sup>。

武汉大学、上海交通大学、陕西大学、中国人民大学、北京语言学院、北京信息工程学院、北京师范大学、深圳大学、北京航天航空大学和新华社等单位分别建立了具有使用侧重面的大型汉语语料库。今年来我国学者提出在语料库语言学指导下建立语料库，使语料库建设走上更加科学化和规范化的道路。上海交通大学、北京图书馆、国家语委陆续推出规模越来越大、属性越来越全，数据越来越精确的大型汉字属性库。北京大学计算机语言研究所还建立了以汉语语法为中心的“现代汉语语法信息词典” <sup>[9]</sup>。内容全面、翔实、使用方便的汉语语料库、字词属性库对推动汉字编码键盘输入技术的发展无疑会起到重大作用。

九十年代后公布的与汉字键盘输入系统有关的国家标准有GB13000.1《信息技术多八位编码字符（UCS）》、GB18030 《信息技术 信息交换用汉字编码字符集 基本集的扩充》、GB18031 《信息技术 数字键盘汉字输入通用要求》、GB15834 《标点符号用法》和即将公布的有GB/T18220-2000《信息技术 通用键盘汉字输入通用要求》。语委颁布的规范有GF3001 《信息处理 GB13000.1字符汉字部件规范》、GF3002 《GB13000.1字符集汉字笔顺规范》、GF3003 《信息处理用汉语拼音方案表示规范通用键盘》。

GB2312-80包含6763个字，GB13000.1包含20902个字，GB18030包含27533个字。关于编码字符集，GB/T 18031要求数字键盘编码应包括GB2312或GB13000.1或GB18030中定义的全部汉字字符，GB/T18220-2003要求通用键盘编码应包括GB18030中定义的全部汉字符号和现代汉语标点符号。

关于键位设置，GB/T 18031对数字键盘规定输入汉字的编码元素要设定在0～9的数字键范围内，并对五种基本笔画和汉语拼音符号的键位作了规定。多笔画部件及笔画组合可以自由设定。GB/T18220-2003对通用键盘规定‘A’到‘Z’26个字母键输入汉字和词语的特征编码信息。‘0’到‘9’10个数字键，除用来输入阿拉伯数字外，还可用来输入汉字和词语的特征编码信息的辅助信息，包括汉语声调、重码字选择等。另外，还对GB/T 15834定义的23个标点符号的键位进行了规定。
关于部件规范，GF 3001对GB 13000.1的20902个汉字进行逐个拆分、归纳与统计后给出了560个基础部件，并规定：基础部件（也称末级部件）为最小的不可拆分的部件；基础部件可以组合成成字部件使用，但不得组合成非字部件；汉字拆分为部件时，应遵循“相离、相接可拆，交重不拆（可拆成笔画）”的原则。

关于笔画规范，GF 3002明确了汉字的基本笔形是五种，其排列顺序为一（横）、丨（竖）、丿（撇）、丶（点）、乛（折），分别用符号1、2、3、4、5表示。GF 3002还给出了GB 13000.1的20902字的规范笔顺。

## 2 理论研究

### 2.1字熵、最短码长和极限速度

早在50年代，钱文浩先生开始从信息论的角度研究汉字，并计算汉字的熵值。这项工作一直延续了三十年，陈文熙、王世宁、李公宜、刘源等将汉字熵值的研究从字熵推进到词熵，从零阶熵推进到高阶熵值。中文的熵值研究对包括键盘输入技术在内的中文信息处理具有重要的理论价值，并对汉字编码具有指导作用。

李公宜等按照信息论原理，计算出汉字的零阶熵 为9.66比特。他们根据不同语言的句子具有等价的语义信息这一基本前提，推出汉字的极限熵H∞在5.2比特到5.5比特之间<sup>[10]</sup>。他们同时还从中文信息熵得出了在码元数不大于36时以句子为编码对象前提下汉字编码的最短平均码长为1.25， 从而驳斥了某些编码自称能一键一字、输入速度达到每分钟300字的神话。虽然码元数大于36后，在理论上可以进一步缩短平均码长，但是由于手指移动速度会受到影响，反而会使输入速度下降，因而继续增加码元是不可取的。不能突破1.25键/字的结论是针对汉字信源总体作出的，与个别或某些词语或句子能够实现一键一字的实际情况并不矛盾。

冯志伟根据他自己建立的“汉字容量局限定理”，在汉字的字种数为12370的范围内，计算出汉字的零阶熵 为9.65比特<sup>[11]</sup>。他还利用英汉双语语料库，间接推算出汉字的极限熵H∞处于3.0212比特到5.0713比特之间，其平均值为4.0462。

王晓龙等直接用概率论的方法，在180万字的样本数据内，计算了N元字词编码的最短码长<sup>[12]</sup>。当N等于26时，字输入最短码长为2.081087，词输入最短码长为1.731010。当N等于36时，词输入最短码长为1.588347。他根据日本打字员的平均每分钟击键数（N=26时为450击，N=50时为250击，N=2000时为50击）给出了录入员的平均速度上限（N=26时为260字/分，N=50时为170字/分），再次说明了码元数的过度增加虽然可以缩短码长但却会降低输入速度的道理。他同时还指出，当N增大时，最短码长和汉字（词）熵的差距随之增加，编码效率逐步降低。

陈一凡认为“由于汉语字、词的熵值高于拼音文字和汉语的冗余度较低、组词方式灵活，使汉字小键盘输入的效率远远高于拼音文字” <sup>[5]</sup>。他在这里忽视了一个问题，那就是汉字是通过编码以后输入的，拼音文字的输入则是没有经过编码而直接进行的。根据信息论原理，编码是可以对作为信源的汉字信息进行压缩的。因此，汉字的编码输入和拼音文字的直接输入没有什么可比性。

### 2.2 输入模型

整个汉字编码输入过程涉及到人、机、文、码等多种对象，包含了一系列人和机的活动。弄清各种对象和活动之间的相互关系和影响，从而建立起汉字编码输入的概念模型和数学模型，对汉字编码输入法的研究具有重要的理论指导意义。不幸的是，输入模型并没有得到足够的重视。在现有的出版物中，对输入模型的探讨是很少的。

不过，陈一凡等的《汉字键盘输入技术与理论基础》一书对输入模型做了相当深入的研究<sup>[5]</sup>。他们分析了汉字键盘输入流程，提出了“理想的汉字特征信息键盘输入的数学模型”和“实际的汉字特征信息键盘输入的数学模型” 。他们的数学模型以集合论为工具，说明了汉字、汉字特征信息、键元、汉字内码之间的映射关系及重码的处理办法。

张侃等按照人的视听感觉、认知和动作对整个汉字键盘输入过程进行分界和说明，得到了一个汉字键盘输入的认知模型<sup>[14]</sup>。该模型的三个不同层次的加工过程和容量限制分别为评测汉字输入方法的三个主要素质提供理论依据：即长期记忆量与易学性，短期记忆量与心理负荷和易学性，认知、动作加工与易用性和输入速度。

何克杭分析了人类识别汉字的认知模型，并将认知心理学的理论方法系统地应用于汉字编码的形码方案设计，以解决快速性和易学性的矛盾<sup>[15]</sup>。

### 2.3 输入法评测

面对80年代初“编码潮”涌现出的数百种方案和上百种上机运行的汉字键盘输入系统，对它们的内在素质和使用效果的优劣评估提到议事日程。上海交通大学、北京信息工程学院、中国标准化与信息分类编码研究所、中国科学院心理研究所等单位不断探索评估理论和设计评测软件。评估对象由80年代初的编码方案发展为八十年代末的包含“编码层次”和“软件层次”的整个输入系统；评测内容由表象测定深入到与认知心理结合的内在素质测定；评测手段由定性到定量；评测方法由主观因素起作用逐渐过渡到计算机客观评测；九十年代则将评测内容和指标写进了国家标准。

从1980年起，中国开始进行过几次民间组织的评测工作。由上海交通大学牵头起草了一个评测试行草案。1983年4月，台湾中文电脑研析室主持了对汉字输入方法的调查评估，参加测试的方案有7个。1984年夏，中国中文信息研究会汉字编码委员会、上海交通大学、中国福利会少年宫组织了有5个方案参加的计算机定量测试工作，为评测的理论和实践打下了初步基础。1985年在国务院振兴办公室、国家科委和国家标准局的领导下，挂靠在国家标准局信息分类编码研究所的全国汉字输入方案评测办公室组织各方面有关专家，在对评测试行规则草案进行了全面修改和补充又先后经过三次专家评审，于1985年12月形成了汉字键盘输入方法评测规则草案<sup>[16]</sup>。

1986年3月至5月，由国务院电子振兴办公室、国家科委和国家标准化总局、中国中文信息学会联合组织的首届全国性评测历时38天，报名方案51个。经静态参数测试和资格审查，确定34个方案进入动态测试。其中，有形码20个、音码3个、音形码8个、形音码1个、形字音词码1个、整字键盘方案1个。按照测试规定和成绩评选出了11个A类方案和19个B类方案。11个A类方案是：陈代于的大众编码，张国防的五十字元多能汉字输入法，唐懋宽的中文声数编码，钱伟长的宏观字形编码，陈国斌的层次四角编码，万仁芳的前三末一拼形方案，刘书泽的部形码，李金凯的笔形编码，由中文信息学会汉字编码专业委员会组织协调、公安部十二局负责牵头的公关项目联合45-3输入法，欧阳松的CK码，李公宜的JDL无间隔输入法。以上A类方案的平均速率为43.16字/分，平均错码率为3.14%，最高平均速率为52.52字/分，最低平均速率为34.83字/分，操作员最短学习期（包括教学）时间为38小时。此次评测工作有力地推动了汉字编码输入技术的发展。

1987年在大连举办了中华杯中文电脑公开赛，探索将汉字编码输入作为计算机系统的一个子系统来进行评测，同时电子工业部向上海交通大学和北京信息工程学院下达了“汉字键盘输入评测技术”研究课题，推动了评测工作向“的客观、公证、科学”的方向发展。

进入九十年代后，汉字能否输入计算机的问题已得到解决。但随着计算机的普及，汉字编码输入者中专业打字员的比例越来越少，并且中小学生也都普遍的开始学习汉字编码输入。汉字编码的规范性问题、与语文教学的关系问题、易学性问题等日益尖锐地显现了出来。王力德就普及型汉字编码的易学性目标体系和效率目标体系进行了有益的探索<sup>[17]</sup>。文献<sup>[18]</sup>-<sup>[26]</sup>围绕认知码和五笔字型的规范性问题进行了激烈的讨论。华绍和等指出适应中小学教学用的汉字编码应具备的特点有：编码应符合国家语言文字有关标准和规范；编码实现应使用通用设备，键位设置应符合有关规定；编码以计算机输入为基础，与识字、写字、查字相结合；编码应把汉字全息输入与非全息输入有机结合起来；为基础教育服务，与语文教学紧密结合<sup>[27]</sup>。

九十年代的国家标准将编码层次和软件层次视为统一的键盘输入系统进行性能考核。《数字键盘汉字输入通用要求》和《通用键盘汉字输入通用要求》规定的系统性能指标有三个：易学性、汉字输入平均码长和重码字词键选率，给出了应当达到的最低要求。值得注意的是，这些标准用键选率取代了传统上使用的重码率。易学性指标要求“学会使用汉字编码输入系统的时间尽量短，并应符合使用汉语作为母语的使用者的思维习惯”，对数字编码则更进一步要求“做到上手能用”。平均码长指标对通用键盘汉字输入要求小于3.2键/字（汉语拼音、笔画为主的简易编码）或小于2.2键/字（部件码、音形码、形音码、双拼）；平均码长指标对数字键盘汉字输入要求小于6键/字（逐字字段输入）或小于4键/字（字词混合输入）。键选率指标对通用键盘汉字输入要求小于6%（汉语拼音、笔画为主的简易编码）或小于1.5%（部件码、音形码、形音码、双拼）；键选率指标对数字键盘汉字输入要求小于8%（逐字字段笔画、部件码输入）或小于10（字词混合笔画、部件码输入）或小于13（10键位逐字字段拼音输入）或小于14（8键位逐字字段拼音输入）或小于12（10键位字词混合拼音输入）或小于14（8键位字词混合拼音输入）。

## 3 实用系统

### 3.1 实用系统分类

最常见的分类法是按编码时使用的特征信息元（或称字元）将汉字编码输入法分为音码、形码、音形码和形音码。音码又可以细分为全拼码、双拼码、简拼码。形码又可以细分为部件码和笔画码。部件码需要将汉字拆分为部件或字根，再将它们通过音托、位托、形托等方式映射到键盘字符。音形码以音为主以形为辅。形音码以形为主以音为辅。

另外，按处理对象大小来分，汉字编码输入法可以采用单字型、字词型和语句型；按适用的输入者来分，汉字编码输入法可以分为普及型与专业型；按编码时使用的字符来分，汉字编码输入法可以分为字母码和数字码；按软件的适应性来分，汉字编码输入法可以分为通用输入法平台（又称码表输入法）和专用输入法（或称定制输入法）；按使用的键盘来分，汉字编码输入法可以分为通用键盘输入法和数字键盘输入法。

最后，还可以按照汉字编码输入的发展历程将其分代。目前，分代方法并没有形成共识。汉字编码输入法究竟分为几代？每一代的特征是什么？这些问题都有不同的看法。吴越将汉字编码输入法分为三代。其断代标志为：第一代，以单音节的字为单位输入；第二代，以词语（包括单音节和多音节）为单位输入；第三代，除了有固定词库可以用通用词输入外，还可以根据用户的需要自造词语，并具有人工智能，可以自动选择区分重码（同音）词<sup>[28]</sup>。单波也将汉字编码分为三代，但是各代的特征与吴越所描述的大不一样<sup>[29]</sup>。

本文在叙述时，按历史发展进程把汉字编码输入法分为第一代、第二代、第三代，各代的特征与单波和吴越描述的都不一样，在具体论述时会加以说明。由于除第一代外，各代的汉字编码输入法的数量都很多，因此本文只能选择具有代表型的和具有较大影响的作比较详细的介绍。数字键盘编码输入法，作为目前大家的研究热点，单列出来进行评述。最后，单独介绍一下比较常见的通用输入法平台。

### 3.2 第一代汉字编码输入法

电子工业部第六所于1983年正式公布了我国第一个中文磁盘操作系统CC-DOS，这在我国中文信息处理历史上具有划时代的意义。CC-DOS是在PC-DOS的基础上扩充、修改而成。在广泛使用的CC-DOS 2.1版中，有简拼、首尾码、快速码和区位码输入法，已经涵盖了包括音码、形码、音形码和数字码这些主要类型的输入法，对我国计算机应用的普及起到了开路先锋的作用。

当时使用得最广泛的输入法是简拼和首尾码。简拼是纯音码，使用的是介于全拼和双拼之间的一种拼音方法，对三个及三个字母以上的韵母进行了压缩。首尾码是一种纯形码，包含97个部件，分为52类；部件到键盘字母的映射没有太多的规律可循，记忆量很大；编码时只取字首和字尾各一个部件，对于未列出的变形部件需要输入者自己去猜测其应归属的键位。这两种方法都不支持联想，也不支持词组，都有很多重码。因此，在输入时选择、翻页操作很频繁，眼睛需要不断地扫描提示行以便在众多的重码中找寻所需的字，输得又累又慢，更不可能实现盲打。

快速码是通过压缩拼音加码方法实现的，可以在一定的程度上离散重码。由于快速码的加码方法没有规律可循，因此没有得到真正的应用。区位码需要完全要靠死记6763个汉字和符号的数字编码来输入，因此除了用于输入当时还没有其它办法输入的特殊符号外，基本上没有人实际使用。尽管如此，快速码仍然为后来的音、形结合编码指出了方向，区位码仍然为后来的数字码提供了一条线索，它们的理论指导意义大于实用意义。

另一个早期的汉字编码输入法是电报码。电报码最初并不是用于汉字输入的，而是用于拍发电报的，是最早的汉字数码方案。电报码由丹麦人设计，早在清光绪六年（1880年）就已经在我国使用了。电报码为4位等长码方案，使用的码字从0000到9999，可以代表一万个字符（包括汉字、字母、符号）。电报码没有重码，但编码的规律性不强，十分难记。因此，它完全是为了邮电部门那些已经熟悉电报码的人的需要而移植进计算机的，对一般的汉字输入者没有什么意义。

1986年，联想集团在推出联想汉卡的同时推出了联想式汉字环境，首先使用了联想方法来加快汉字的输入。那时还没有词组输入方法，联想技术让人耳目一新。汉字输入过程由原来的编码->翻页->选择->编码...变成了编码->选择->选择...，因此稍后的很多输入法都采用了这种技术。不过，按照现代汉字编码输入技术的标准来看，联想技术仍然存在两个致命的弱点。一个弱点是，如果后续要输入的字与前面已输入的字不能构成词组的话，则联想就会失败。另一个弱点是，联想选择时人机交互过于平凡，虽然平均码长缩短了，但是实际的输入速度反而会下降。

总之，第一代汉字编码输入法是在汉字操作系统建立的同时诞生的。在西文操作系统上实现汉字操作系统有许多工作要做，例如汉字字模的设计、汉字的显示、打印等等，汉字的输入仅仅是其中的一个部分。那时，汉字操作系统是由计算机专家完成的，汉字编码专家几乎未能参与其中，虽然当时已有一些人在专门搞汉字编码了。由于计算机的价格还很昂贵，汉字系统的用户很少。汉字编码输入法使得汉字能够输入计算机了，但几乎还没有考虑易学、易用和快速的问题。

第一代汉字编码输入法的特点是：在DOS环境下，以单字为单位进行输入，在屏幕底部提供专门的提示行显示数量众多的重码字，翻页、选择操作频繁；用数字键选择重码字，用ALT+数字键可重复选择出现在提示行中的重码字；连极为常用的标点符号的输入需要使用区位码，很不方便；联想技术的采用使输入效率有所改善，但其作用是相当有限的；各种输入法间的切换（包括切换到英文）都是通过复合功能键ALT+Fn(F1-F12)来进行的；支持全角和半角方式，但不支持中文标点方式；不支持词组输入，更不支持自定义词组。

### 3.3 第二代汉字编码输入法

1986年，四通公司与日本三井物业合作，推出了四通MS-2400中文电子打字机，宣告了中国专业电子打字时代的到来。由于当时微型计算机的价格还很昂贵，一般的个人用户根本买不起。而单位用户主要希望解决办公打字的问题，并非必须使用微机不可。四通打字机既比较便宜又能适应输入汉字和编辑打印的要求，正好迎合了市场的需要。另外，为了适应没有四通打字机的个人和单位的需要，采用四通打字机的商业打字店也应运而生。随着四通打字机的广泛使用，首先捆绑在四通打字机上的五笔字型输入法也在其发明人王永民的极力推广下流传开来，以培训专业打字员为目标的遍布全国的商业电脑培训机构更加速的五笔字型的推广，造就了几十万使用五笔字型的打字员。后来捆绑到四通打字机上的由刘卫民发明的双音输入法也在当时得到比较广泛的使用。

九十年代初，一方面由于四通公司的内部运作出现问题，另一方面也由于微机的价格迅速的下降，四通打字机逐步的被微机取代。由于在微机的汉字操作系统上汉字编码输入法是可扩展的，这就为其它非四通打字机输入法提供了发展空间。但是，与五笔字型类似的以拆分汉字为基础的部件类输入法，如表形码、郑码，虽然比五笔字型相对易学且输入速度也差不了多少，发明人的名气也比较大，然而面对已在专职打字员输入法市场上占尽先机的五笔字型，最终没能广泛被用户采用。更具有讽刺意义的是，曾在86年的首届汉字输入方案评测中被评为A类的11个汉字编码方案没有一个得到了广泛的使用。倒是面向一般使用人员的自然码脱颖而出，在克服了双音输入法在速度上的缺陷后，在日益扩大的非职业打字领域得到了广泛采纳。这样便形成了以王永民的五笔字型、刘卫民的双音输入法和周志农的自然码为代表的第二代汉字编码输入法格局。

五笔字型是最典型的纯形码部件类方案。在五笔字型中，一般将部件称为字根。五笔字型采用了130个基本字根。基本字根按起笔分为五类，对应通用键盘上的五个区。每类又细分为五组，每组对应一个键盘字母。在一个汉字中，字根间的关系被归纳为“单、散、连、交”四种。在汉字拆分时，遵循“取大优先，兼顾直观，能连不交，能散不连”的原则。

五笔字型将汉字被分为键名汉字、成字字根汉字和键外汉字三种，分别服从不同的编码规则。键名汉字有25个，其编码是重复其所在键上的字母四次。成字字根汉字有近一百个，其编码规则为“键名码+首笔码+次笔码+末笔码”，不足三笔时按“键名码+首笔码+末笔码”编码。键外汉字数量最多，其编码规则为顺序取字的第一、二、三、末字根码，不足四个字根的需补加一个交叉识别码。交叉识别码根据字的末笔（横、竖、撇、点、折）和字型（左右型、上下型、杂合型）而定。另外，字的编码还有一、二、三级简码，其形成方法是取相应全码的前一、二、三个字母。

五笔字型将词组也分为二字词、三字词和多字词三种。二字词按顺序取各字的前两个字根来编码。三字词按顺序取头两个字的第一个字根和末字的前二个字根来编码。多字词按顺序取第一、二、三、末字的第一个字根来编码。

职业打字员打字时的一个重要特征是看稿进行录入，并且要求很快的输入速度。所以他应尽量少地去观察提示行和已输入的内容，否则当他回头看稿时再次定位应输入的汉字就会非常吃力，从而极大地影响录入速度。只看稿件进行打字就是平常所说的盲打。绝对的盲打实际上是不可能的。可能的是尽量不将视线离开稿件。职业打字的另一个特征是录入的内容比较广泛，承接商业打字业务时更是如此。这就需要他记住各级简码，知道哪些字应该使用简码输入，哪些字应该用全码输入，哪些词是输入法有的，哪些词是输入法没有的。由于词组的数量巨大，收录过多的词组一方面会加大重码率，另一方面也会增加记忆量，因此职业打字员多以单字输入为主，辅以常用的词组。这也暗示着自定义词组在职业打字中起的作用是十分有限的。鉴于以上原因，要成为一个合格的职业打字员，除了具有灵敏的手指外，没有数月的专门的系统的打字培训是不可能的。

五笔字型以非常复杂的编码规则换来了在GB2312-80字符集内较低的重码率。当采用强制简码时，还可进一步将低重码率。词组编码被放进全码字的剩余编码空间中，实现了字词混合编码。只要收录的词组量不大，发生重码的可能性是比较小的。一般的五笔字型也不具备自造词的功能。五笔字型拥有的这些特点，正好适应了职业打字的需要，成为它在职业打字时代非常流行的重要原因之一。

虽然五笔字型在市场上取得了巨大的成功，但它存在的问题也是不容忽视的。首先，五笔字型是非常难学的，而且容易遗忘。它除了有非常复杂的编码规则而外，还有很多例外需要记忆。五笔字型打字员在打字时对一些常见字出现“卡壳”的现象是很普遍的事情。这时就需要临时换用拼音输入法来输入“卡壳”的字。其次，五笔字型的扩展性差。当字符集从GB2312-80到GBK和GB18030过渡时，当词组量增大时，五笔字型在码长为4的码位上会出现大量的重码，使其丧失重码率低的优势。五笔字型采用的是4码无重码自动上屏的策略，4码重码增多就迫使打字员的视线更多地离开稿件来观察提示行以确认自己的输入，从而减低录入速度。最后，五笔字型最致命的弱点是规范性差。张孝存等就此提出了言辞激烈的批评<sup>[25]</sup>。“五笔字型违反语言文字规范。它对汉字的拆分具有相当大的随意性，对国民基础文化素质具有不可忽视的负面影响。它对规范的汉字教育的冲击同其应用范围的扩大成正比。”所以，五笔字型不能适应一般汉字输入者的需要，更不能适应中小学汉字输入教学的需要。

双音输入法是一种比较巧妙的纯音码，曾经是四通打字机和西山DOS的必备汉字输入法之一<sup>[28]</sup><sup>[30]</sup>。双音输入法支持全拼、简拼和双拼三种拼音方式。对于全拼来讲，除了用v代替ü而外，音节的拼写形式和标准汉语拼音完全一致，非常简单，会拼音的人基本上不用学习就会，但效率最低。简拼是为兼容早期CCDOS而设立的。双拼用两个字母代表一个音节，是效率最高的拼音方法，但学习时的记忆量也最大。在双拼双音中，可以选择采用刘氏双拼，也可以选择采用四通双拼。

双音输入法最大的特点就是“以词定字、反向联想”，以缓解纯音码方式下单字重码过多的问题。因为二字词的数量很多，所以一般情况下总可以找到某个二字词，它的第一个字就是你想要输入的字。如果该二字词处于提示行的第一候选位置，则可以省略选择键；否则需要用数字键进行选择。如果整个二字词都是你需要的，你可以加一个空格键输入第二个字。也就是说，如果采用双拼的话，利用“以词定字”技术可以使得常用字输入时的平均击键数为2.5，而且基本上避免了传统拼音+联想方式下过多地扫视提示行和翻页、选择的毛病。联想方式仅仅作为一个选项，并不怎么推荐使用它。

在双音输入法中，对于三字词和四字词，取各字的声母作为编码来输入，必要时加空格结束。对于不认识的字，可以打入“\\”调用“手写模拟”，其规则是：首末两笔打代码，中间笔画用空格代替；如果事先计算出应输入的空格数，也可以用数字键代替应输入的空格数。虽然可以自定义词组，但它不支持在线造词。造词时需要用外部文本编辑器按照它定义的格式输入编码和对应的词组。

双音输入法是拼音汉字输入历史上的一大进步，在当时受到了许多非职业打字员的欢迎。但是，它也存在一些比较严重的不足，以至于现在几乎没有人再使用它了。首先，虽然在输入效率上它较传统的拼音有很大的提升，但是它与后来的语句级拼音输入法如智能ABC相比，还有相当的差距。另外，“以词定字”时很多字可以采用多个词来确定，而有的字难以找到词来确定，用户常常感到不知所措。虽然双音输入法中提供了很多其它的方法来解决单字的录入问题。例如，邓、郭、姚等姓氏用字的输入就有6条辅助规则。要记住这些方法并判断何时采用何种方法可不是一件容易的事情。由于只能离线造词，所以词组的自定义也很不方便。

自然码是最具代表性的音形码<sup>[31]</sup>。吴越在1993年对自然码作出了极高的评价<sup>[28]</sup>。他说自然码输入法“是目前以拼音为基础的普及型汉字输入系统中最先进、最好学、最方便、最快捷、具有最大人工智能容量的一种方案”。这种评价在当时来说，除了“最好学”这一点是言过其实了（因为它显然没有全拼或笔顺输入法简单）而外，其它的优点自然码都是具有的。自然码在拼音部分采用了在CCDOS简拼的基础上修改而来的双拼，以方便CCDOS用户向自然码过渡。自然双拼与刘氏双拼和四通双拼都是不一样的。

为了解决拼音输入中普遍存在的同音字问题，自然码采用了与双音输入法完全不同的策略。它通过在双拼后附加形码，大大减少了单字的重码。其形码部分采用“近义部部首分类”法，最多可有两码，用部首读音的声母作代码，取码时坚持“义部优先”的原则，以便减少记忆量和增加形码对重码字的离散能力。采用附加的形码来区分同音字还可以避免双音输入法中一个字可以利用多个词组来确定的不确定性。对于不认识的字，可以用单纯使用形码部分输入，但需要以“/”键开头进行引导。

自然码的简码字也很有特色，除了传统上用“声母+空格”输入的高频简码字而外，还有用“声母+;”输入的次级简码字和用“声母+’”输入的附加简码字。自然码还设置了用“声母+声母+’”输入的简码二字词，以加快高频二字词的录入。输入一般的二字词时，词组作为一个整体上屏，比双音输入法的“以词定字”每输入一个二字词就少用了一个空格键。三字词用各字的声母+“’”输入，单独享有编码空间。

自然码还设计了“中文标点状态”，使得常用标点符号的输入和半角字母、数字的输入可以不加切换的进行。自然码的外挂技术使得它可以不加改变地挂接于所有常见的中文DOS系统上。考虑到南方人普通话不准的现实，自然码还提供了南方音选项。设置南方音选项后，用户可以不区分声母z和zh、c和ch、s和sh，也可以不区分en和eng、in和ing，还可以不区分wang和huang、n和l。当然，这时的重码就增多了。联想方式在自然码中也仅仅是作为一个选项提供的，但由于人机交互过于频繁，严重影响输入速度，因而熟练的用户是不会使用的。自然码还对中文数字、日期、时间、制表符等提供了编码式的快速输入手段；对字词的叠加操作也相当方便，可以用于输入“想想”、“思考思考”、“试一试”等。

智能相关处理是自然码宣传得很多的一项技术。它实际上是一种扩展的联想技术，即把联想用到了词组与词组之间。例如，输入“知名”以后再输入“rfui”（标准拼音为“renshi”）后会把“人士”作为默认选择，而输入“不久”以后再输入“rfui”则会把“人事”作为默认选择。

在线造词是自然码自誉的另一特色。在汉字输入过程中，如果敲完某个词的拼音以后发现这个词不存在，立即敲空格键，系统便进入“自动加词状态”；这时，连续输入的字、词都作为新词的内容，在送到屏幕上的同时便被纪录到自造词库中；当再敲空格键或回车键时，系统结束自造词操作。如果想造词的编码正好与其他词的编码重复，这时就要按Shift+Tab复合键进行强制造词，此后的操作与前面相同。对于已自定义的词，还可以将其删除。删除的方法是，在输入词的编码且词还未上屏时，按Ctrl+回车复合键；此时，如果无重码则那个唯一的词被删除掉，如果有重码则还需要选择想删除的是哪个词。需要说明的是，系统自带的词是不能删除的。在进行了增、删词组的操作后，在关机或重新启动计算机之前，必须先将自造词库保存到磁盘中，否则关机后所作的修改就无效了。

总之，第二代汉字编码输入法都是在CCDOS 2.1的原始输入法的基础上发展起来的，以提高汉字的输入速度为主要目标，增加了词组的输入，单字输入时的重码也减少了，出现了中文标点状态，多数都能自定义词组。第二代汉字编码输入法非常多，除了上面介绍的而外，在大陆影响较大的还有陈爱文先生的表形码、郑易里先生的郑码、钱玉趾先生设计的未来码、肖水清先生的肖码、萧启宏先生的启宏全息码等<sup>[55]</sup> <sup>[56]</sup>，在港台影响较大的还有朱邦复先生的仓颉输入法、王赞杰先生的大易输入法、廖明德先生的行列输入法、陈华伟先生的华象中文输入法、刘重次先生的呒虾米中文输入法、戚桐欣先生的中易系统、黄金富先生的唯物输入法等，另外还有美籍华人饶达先生的饶氏笔形输入法和美国王安电脑公司开发的王安三角编码法等。

### 3.4 第三代汉字编码输入法

到了九十年代末，随着微微机价格的进一步降低、存储处理能力的进一步增强、Windows图形操作系统的流行和国际互联网的兴起，用户界面变得非常友好，微机才大面积地进入中国的普通百姓家庭，进入了中小学教育中，真正实现了微机在中国的大普及。

微机的大普及使得打字成为每个接受过基本教育的人的基本技能，就像会写汉字一样；需要别人打字就像需要别人代笔一样，实际上是文盲的标志。这样就造就了一个庞大的一般计算机用户群体他们都是非职业的打字员。这就意味着，打字员作为一个职业正在快速消失。一般用户在打字时的操作方式是“想打”，和职业打字员的“盲打”方式完全不同。“盲打”要求操作者尽量少看屏幕，输入法提供的反馈信息只有在操作不能“盲打”时才偶尔派上用场；而“想打”时操作者始终是看着屏幕的，输入法所提供反馈的方式和反馈信息量的大小都会对操作者的输入活动产生巨大影响。Windows图形操作系统也为人机界面的丰富化提供了前提条件，可以满足反馈信息多样化的需求。

现代微机强大的存储处理能力为新型的存储密集型和处理密集型输入法的诞生提供了物质基础。输入法程序不再局限于DOS时代64KB的驻留内存中。千兆级的运算速度使得复杂的智能算法得以投入运行。硬盘容量不仅从兆级扩大到千兆级，访问硬盘的速度也比DOS时代大大提高。将巨型的词库存储在硬盘上并进行快速搜索已不成问题。

计算机教育日益广泛地在中小学开展后，学生们从小就开始学习打字了。汉字编码与语言文字教育的关系问题被尖锐地提了出来。起码的要求是，汉字编码不能与语言文字知识相冲突。理想的情况是，把汉字编码输入与语言文字知识的学习结合起来，起到相互促进的作用。

在上述背景下，第三代汉字编码输入法应运而生，其指导思想是：规范、易学、易用并且尽量保持输入速度。这一时期智能化拼音输入法的研究高潮迭起<sup>[32]</sup>-<sup>[51]</sup>，也出现了以笔画或笔对为输入单位的纯形码，还出现了以声母和笔画（或笔对）为基础的音形码。

#### (1) 智能化拼音输入法

智能化拼音输入法按其实现原理可以分为四种：基于理解的、基于语用统计的、基于模板匹配的和基于上下文关联的。

基于理解的智能输入主要利用汉语语法知识来消化同音字词，化解分词歧义，是出现得最早的智能拼音输入方式。它通常表述为计算机能够识别和处理的一系列固定搭配、公式和规则，属于人工智能中的自然语言理解领域。根据自动分词得到同音字词的候选集，查找知识库获得相关规则，再经过规约推理，得出转换结果。利用句内编辑实时修改转换错误，驱动系统知识不断完善和充实。这类系统的优点是：转换的正确率比较稳定，软件的开销视知识库的规模可大可小。缺点是：连续拼音整句输入时，平均码长较长，而采用简拼时键选率很高；偏重于整句处理，当出现转换错误时，需要使用者回头去进行繁琐的矫正，干扰了正常的思维；建立知识库时，汉语知识表达困难；自动分词过程中切分歧义等影响了分词精度。这类系统中最有影响的是北京大学朱守涛研制的智能ABC，其它还有哈尔滨工业大学王晓龙等研制的InSun拼音语句输入系统、张普负责的“七五”公关项目PJS/TLS汉字输入系统、北京大学的北大CW系统、香港陈经纶的经纶系统、加拿大陈岱的天马系统和广州林才松的汉语无编码输入系统。

基于语用统计的智能输入主要利用语用统计的数据来消化同音字词和化解分词歧义，属于运筹学领域。使用概率统计运筹决策的方案很多。可以通过统计字字相关的同现概率矩阵来完成汉语语用统计库结构，这个矩阵的大小是固定不变的，只与字符集的大小有关。也可以采用基于理解和基于语用统计相结合的设计。该设计根据分词后的输入语句查找知识库，用句法、词法、语义和自定义的规则作为制约对文章进行解析推理，当存在同音词时，采用最优评价法来确定最佳选择作为转换结果。同音词的评价值，需要考虑词性、同现概率、近期使用状况等因素。具有最优评价值的选择即为转换结果。当具有最优评价值的第一选择并非目标选择时，可选用次优选择或用手工方式进行修正，候补修正或人工修正均被记录，作为下次转换时修改计算评价值因素的依据，也就是自学习功能。这类系统的优点是：对于已经进行过语用统计或者具有相同类型的领域，系统的转换正确率比较高；对于每一个用户而言，在使用过程中，语用统计库将会从最初的通用型逐渐改变为符合这个用户语用习惯的专用型；软件开销不大。缺点是：作为一个整体的同现概率矩阵，不能做到模块化、积木化；偏重于整句处理，当出现转换错误时，需要使用者回头去纠正，干扰了正常的思维；目前的自动分词准确度只能达到98％左右，使键选率的降低受到限制。这类系统中最有影响的是微软公司的微软拼音输入法，其它还有蔡榕先生的最优评价函数法拼音汉字转换系统、蒋子龙先生的Autoway、清华大学人工智能实验室夏莹等的智能输入软件。

基于模板匹配的智能输入将汉语语法知识寓于巨量的模板词中，进而利用这些模板词来消化同音字、词，以及化解歧义分词。系统通过模板词搜索引擎来完成汉语语法体系的组织。由于需要搜索巨量的语料，获取巨量的模板词，才有可能大体上包容汉语语法知识，例如，智能狂拼搜索了100亿字语料，模板词库最大时需要约540MB存储空间。根据分词后的输入语句查找模板词库和句法规则库，然后进行匹配处理。如果匹配结果唯一，则不必再用概率推理；若存在两个以上的候选结果时，则根据句法规则或概率推断进一步判定，选出一个最有希望的可能结果作为输出。这类系统的优点是：对于已经搜索过模板词的或者具有相同类型的领域，系统的转换正确率比较高；对于每一个用户而言，在使用过程中，模板词库将会从最初的通用型逐渐改变为符合这个用户语用习惯的专用型。其缺点是：由于模板词数量巨大，对电脑硬件有一定的要求；注重连续和完整的音节输入，平均码长较长，采用简化拼音输入时键选率较高；偏重于整句处理，当出现匹配错误时，需要使用者回头去纠正，干扰了正常的思维；目前的自动分词准确度只能达到98％，使键选率的降低受到限制。这类系统中最有影响的是中文之星数码科技有限公司推出的智能狂拼，其它还有黑马电子新技术公司推出的黑马智能输入软件和大自然软件开发有限责任公司推出的自然码2000（句输入版）。

基于上下文关联的智能输入利用上下文关联的语用环境来智能选择重码字、词,属于自动控制分支非线性控制范畴。它将自然语言看成是一个模糊的集合，将汉字输入系统作为一个基于非线性控制范畴的模糊控制系统来对待。预学习工具或者转换出现错误时的手工键选信号相当于一个传感器。算法程序、汉语知识库和动态语用统计库作为非线性调节器，使得系统的键选率和平均码长逐渐趋于最优。这类系统的优点是：对于已经预学习过或者具有相同类型的语料，键选率比较低；对于每一个用户而言，在使用过程中，汉语知识库将会从最初的通用型逐渐改变为符合这个用户语用习惯的专用型；采用字段输入，不使用语句级输入，使语法规则简约化，易于知识表达，不但降低了键选率，还大大缓解了输入过程中“回头看”的问题；在拼音输入时，采用人工分词，在形式上与英文接轨，既可以避免3％的歧义分词错误，大幅度降低键选率。其缺点是：字段输入还未能完全根治输入过程中“回头看”的问题，当终选字词有错时，仍然需要近距离的即时修改；对于“上下文关联”机制中的“下文关联”人机界面，用户需要一个熟悉的过程。这类系统中比较典型的有青月亮科技开发有限公司推出的青月亮汉字通智能输入软件平台GM3.1、二笔软件有限公司推出的二笔智能输入软件和字原科技有限公司推出的101智能输入软件TZ8.2/9.1/2000。

智能ABC是目前Windows操作系统上使用得最为广泛的准语句级拼音输入法，因为它是以词组和短语为单位而不是以全句为单位进行转换的。它早在DOS时代就产生了，当时使用得并不广泛。它之所以在Windows时代大肆流行，一方面是因为Windows预装了它，另一方面是因为大多数新的计算机用户都是学过汉语拼音的年轻人，他们不需要学习就可以使用智能ABC。虽然输入速度没有五笔字型那样快，但是也能基本上满足他们的需要了，同时节约了长达数月的学习时间。

智能ABC支持全拼、简拼、混拼、双拼、笔形和音形多种输入方式。全拼使用标准汉语拼音，但需用v表示韵母ü。简拼仅需输入各字的声母。混拼介于全拼和简拼之，可以不同程度地省略拼音字母。笔形输入方式将笔画归为横、竖、撇、点、折、弯、叉、方八类，分别用1、2、3、4、5、6、7、9代表，按笔画顺序为汉字编码。音形方式是在拼音（全拼、混拼、简拼）后面加笔画。智能ABC有标准和双拼两种状态。在标准状态下，可以不加切换地使用除双拼以外的输入方式，为用户提供了极大的灵活性。简拼和混拼主要是为了减少击键数。在双拼状态下，不能使用全拼、简拼和混拼。使用双拼是为了提高输入速度。笔形方式用于用户不认识的字的输入。音形方式则是为了在输入单字时减少重码。

智能ABC最大的特色是能够非常方便地自定义词组和调整重码字词的顺序。用户只需按自己的想法进行输入，输入时可以不进行手工分词，系统会从前到后逐个进行自动分词。在没有词组时，系统自动按单字显示重码字供用户选择；一旦用户选定并组成新词后，系统就可以记住它。在系统分词不正确或系统提供的词不是用户需要的词时，用户也可以加以修改，系统也能记住用户所作的修改。通过较长时间的使用后，如果用户没有发生变化，系统逐步适应该用户的使用习惯，使用户的输入过程变得自如起来。

智能ABC也有很多值得改进的地方。首先，在输入时可以随意使用全拼、简拼、混拼，输入者可以在任何时候进行音字转换，过多的方式让用户不知哪种是最好的。看似非常灵活，但却实际上是把优化输入的任务交给了用户。但大多数用户不是这方面的专家，不可能很好的完成这项任务，从而导致用户走很多弯路或形成不好的、低效的输入习惯。其次，音字转换的准确率不高，句内修改很频繁，导致输入速度不理想，即使使用双拼也没有自然码的效率高。

微软拼音是真正意义上的语句级音字转换智能输入法，是微软自然语言处理技术多年科研成果的结晶。借助于微软操作系统的优势，加上微软拼音本身的较优异的性能，它的用户群体正在逐步扩大，出现了取代智能ABC地位的趋势。

微软拼音采用拼音作为汉字的录入方式，用户不需要经过专门的学习和培训，就可以方便使用并熟练掌握这种汉字输入技术。微软拼音采用基于语句的整句转换方式，用户连续输入整句话的拼音，不必人工分词、挑选候选词语，这样既保证了用户的思维流畅，又大大提高了输入的效率。

微软拼音还为用户提供了许多特性，比如自学习和自造词功能。经过一段时间与用户交流，微软拼音能够学会用户的专业术语和用词习惯，从而提高转换准确率，使用户用得更加得心应手。为了适应方言地区用户的需要，它还提供了模糊音设置。另外，微软拼音还支持繁体字的输入。

微软拼音提供的人机界面非常具有特色。组字窗口可以嵌入正在输入的文本的插入光标处，减少用户在输入时视线的移动频率，使得输入法的易用性得到了很大提高。逐键变换提示并提示转换结果，使得用户不必自己做合适进行转换的决策。用户可以输入的输入码长度没有限制，当超过系统的长度上限或遇到句号时系统会自动进行转换，以便用户能继续不间断地输入。由于考虑的上下文较广，微软拼音能够达到很高的转换准确率。微软拼音在默认情况下拒绝用户输入简拼和混拼，引导用户养成良好的输入习惯。

微软拼音也存在一些问题。首先，在编码输入出错或转换不正确时进行句内编辑的操作很繁琐和低效。其次，逐键变换时往往会把已经转换正确的内容又修改错了，用户不得不随时监视输入内容的正确性，当已转换的内容较多是非常劳心的。另外，微软拼音没有提供方法加速单字的录入，也没提供方法来输入不认识的字，是不完备的输入法。

#### (2) 基于笔画（或笔对）和/或声母的输入法

所有智能化的拼音输入法都存在两个共同的问题。一个问题是，音字转换正确率不可能达到100%，且因输入文本不同而有很大差异，另外输入的句子越长击键出错的概率越大，因此繁琐的句内修改编辑不可避免，导致易用性和输入速度下降。还有一个问题是，对于普通话或拼音不好的人学习难度很大。

所有基于部件的输入法，如五笔字型、表形码等，虽然速度都比较快，但是都存在记忆量大、编码规则复杂、规范性差等比较严重的问题。

基于笔画（或笔对）和/或声母的输入法正是为了克服以上两类输入法的缺点并且尽量保持它们的优点而提出来的。采用笔画、声母这两个最简单的汉字特征信息来进行编码，可以极大地提高输入法的易学性<sup>[17]</sup>。但是，汉字的笔画一般归为五种。笔画种类太少，势必增加编码的长度，从而影响输入速度。于是，如何缩短码长、提高录入效率成了这类输入法成功与否的关键问题。

福建双笔码软件开发有限公司研制的双笔码是一种基于笔画的纯形码。为了克服笔画种类过少的问题，双笔码引入了一种新的笔画类型“叉”，从而将笔画种类扩大六种，取码时按顺序每取两笔构成一个笔对，共可形成36种不同的笔对，并在键盘上有序的将键位分为八个区，然后在相应的键位区内选择键位输入。另外，双笔码还规定病字旁、“口”、提手旁和“日”应作为一个整体取码。病字旁和提手旁均用其头两笔代表，“口”用竖代表，“日”用横代表。

根据汉字不同构造的组合形状，双笔码把汉字划为三类基本字型即左右型、上下型和综合型。不论哪种类型的汉字，均按四码进行编码。

左右有明显的空间分割，左右有边旁且左边先起笔的字，确定为左右型。在输入时，左右型字的左边最多用两个笔画，右边不限，即左边笔画仅为一笔，则按汉字先左后右的书写顺序，左边笔画与右边笔画一起，按顺序每两个笔画合为一对，在相应的键位区内选取。

对上部和下部明显分开，且有一方是基本汉字构成或上部是部首字头的确定为上下型。还规定如最下部是某一汉字构成，则以上的都归为上部。在输入时，按汉字书写从上到下的顺序，每两个笔画合为一对，在相应的键位区内选取。但是对上部笔画多于四笔的，有如下规定：上部笔画多于四笔，则仅用前四笔的笔画，然后与下部笔画一起，按顺序每两笔合为一对，在相应的键位区内选取。
所有的独体字，和所有不能分为上下，左右型的汉字都是综合型的。输入时，按汉字书写顺序，每两个笔画合为一对，在相应的键位区内选取。注意，辶字底的字都规定为综合型的。

在汉字中近半数字为奇数笔画，双笔码为此设立了单笔画区，该区与横区和竖区有重叠。对于奇数笔画的字有可能输入的末笔为单笔画，这时只要在单笔区输入单笔画就可以了。在汉字中还有许多字的笔画较少，这类字有可能仅一键或两键就把笔画输入完了，这时还可能需要继续进行输入。继续输入时可以使用汉语拼音，也可以重复使用基本笔画，但不能使用叉笔和特殊记忆部件进行重复。
双笔码词组的输入方法为：二字词输入每个字的头两码；三字词输入前两个字的头一码和末字打头两码，四字及四字以上词输入一、二、三、末字的头一码。

双笔码的优点是：与传统的部件类输入法相比，记忆量减少了许多；采用笔对和36键编码后平均码长也相当短；如果不按笔对而按单笔画输入，就可以非常容易地向数字键盘移植双笔码。但是双笔码的缺点也非常明显：作为基于笔画的输入法，它的取码和编码规则十分复杂，另外也不少，学习难度仍然很大；采用了上排数字键进行编码，击打不方便，且与常用数字的输入相冲突，影响了实际输入速度。

陈劲松先生发明的二笔输入法是目前使用得比较广泛的输入法之一，已有多家公司和个人推出了该输入法软件。它是一种基于声母和笔画的输入法，也可以单纯基于笔画进行输入。

二笔输入法用30个字符给汉字编码，即26个英文字母和4个非字母符号“,./;”，分别代表23个汉语拼音首字母、5种单笔画、25种双笔画和10个设定部首，共63个编码要素。26个英文字母中除了I、U、V三个，其余的23个都可以成为汉语拼音的首字母。5种单笔画为横（一）、竖（丨）、撇（丿）、点（丶）、折（┐）五种基本笔画。25种双笔画是横、竖、撇、点、折五种单笔画两两组合而成的25种笔对。10个偏旁部首是为了提高输入速度、减少重码而设置的使用频率最高的偏旁部首，包括“钅、木、氵、土、艹、日（曰）、月、人（亻）、口、扌”。 打字时遇设定部首不能拆分，直接按其代码键。

二笔输入法30个编码在通用键盘上分布于六个区：五个双笔画区和一个单笔画区。区内再根据双笔画的第二笔或根据单笔画，按横、竖、撇、点、折的顺序定位。但10个设定偏旁部首的键位需要记忆。

二笔输入法将汉字按字形结构分为独体字和合体字。输入汉字时，第一码取汉字拼音首字母，从第二码起取笔画，最多取四码，不足四码应全取，不能取双笔画时就取单笔画。独体字不必拆分；第一码取拼音首字母，第二码起按笔顺取笔画的代码，最多取四码。合体字应拆分成两半，按汉字笔顺规则，先写的部分定为前半，后写部分为后半；第一码取取拼音首字母，第二码取前半的第一、二笔，第三码取后半的第一、二笔，第四码取后半的第三、四笔。

二笔输入法词组的编码规则为：二字词取每个字的前二码，三字词取第一字的前二码和最后两个字的第一码，四字及四字以上词取前三字和最后一字的第一码。

使用二笔输入法时，遇到会写不会读的字可以用“;+字的全形”来输入。遇到会读不会写的字可以用“;+全拼码”来输入。

二笔输入法的优点是：编码规则比双笔码更加简单，使用的编码字符也仅有30个；通过使用声母和笔画两种汉字特征信息编码，区分同码字词的能力得到了增强，取得了较高的输入效率；对于不认识的字还可以按全形方式输入；如果不按笔对而按单笔画输入，也可以非常容易地向数字键盘移植。但是二笔输入法也还存在问题：由于使用了笔对、设定部首并需区分独体字和合体字进行不同的编码，因而学习难度和使用难度仍然较大。

### 3.5 数字键盘编码输入法

迄今为止，全国手机拥有量已超过3亿。估计有15亿人用手机短信息通信。手机短信息的产值将超过50亿人民币。手机拥有量超过PC机用户，手机数字键输入汉字的人群远远超过通用大键盘输入汉字的人群。

目前，美国特捷公司的T9拼音和T9笔画输入法、加拿大字源公司的字能笔画输入法和Motorola公司的iTap输入法垄断了中国大陆和港台的手机输入法市场。仅中国大陆每年手机的产量，含GSM、CDMA、小灵通，据不完全统计约在1亿部以上。如果每台输入法的LICENSE费用按2元计算，加上价格不菲的使用许可费用，也就是说，手机厂商每年需向手机输入法厂商支付上数亿元的费用。这就给国产手机输入法占领市场提供了一种必要性和紧迫性。

同时，国外的手机数字键盘输入法也很不尽人意。以笔画输入为例，iTap用9个笔画，字能用8个笔画，T9用5个笔画。相同的一个笔画不同的手机可以放在不同的位置上，输入速度也不理想。

为了打破外国手机输入法垄断中国手机市场和手机输入法不规范的尴尬局面。由中国中文信息学会、中国新闻技术工作者联合会、中国计算机学会中文信息技术专委会主办，由黄金码出版社(香港)有限公司、北京汉王科技公司协办，中国中文信息学会汉字编码专委会、中国广播网等单位承办，于2004年11月21日，在人民大会堂举行了为期三天的中国首届手机中文输入大赛暨汉字数字码输入技术应用高峰论坛。在32支参赛队伍中，有23支参加模拟手机汉字数字码输入比赛，9支参加手机中文输入比赛。

在手机中文输入比赛中，香港黄金码出版社（香港）有限公司代表队以黄金码输入平台手机码输入法和黄金码输入获得冠亚军，北京必胜电脑有限公司代表队以笔顺码输入法获得第三名；计算机模拟手机汉字数字码输入比赛则由浙江象山县科协罗康宁代表队的“大众数字码输入法”夺魁，来自南京的“纵横数字数码双拼输入法”获得亚军，必胜电脑公司的“笔顺码输入法”再次获得第三名；经过专家评委的严格评估，汉字数字码输入方案质量定性评估和输入速度综合优秀名次奖中，大众数字码输入法再次夺冠，来自广东国笔科技公司的“国笔数码智能文字输入系统”和来自广州至微数码科技公司的“两笔数码汉字输入法”分获第二名和第三名。

除了已参赛的数字编码方案外，比较引人注意的还有王永民先生的五笔数码<sup>[52]</sup>、郑岩松先生的左右数码<sup>[53]</sup>等。以下仅对当前使用得最为广泛的T9拼音、T9笔画和首届手机中文输入大赛中获得冠军的黄金码、大众数字码进行介绍。

T9拼音和T9笔画合称为T9智能中文输入法，字库容量九千多个，是由成立于1995年的美国特捷通讯(Tegic Communications)软件公司研制的。该公司总部设在美国西雅图，1999年12月被美国在线(AOL)收购后成为其全资子公司，专门致力于开发用于小型电子设备的产品和技术。T9输入法就是它的核心产品，该输入法解决了小型掌上设备的包括中文在内的文字输入问题，已经成为全球手机文字输入的标准之一。

T9拼音本质上采用的是一种全拼单字加联想的早期通用键盘输入技术。其最重要的创新是可以根据手机键盘上按键的组合情况判断是否能组合成合法的普通话音节，从而避免了传统上通过多次按键来输入一个拼音字母的弊端。但是，当按键组合适合多个合法的普通话音节，而且默认选择的普通话音节又不是用户所需要的时，用户还是得进行手动选择。另外，全拼的拼式过长、需要按1键进入选择状态和联想造成的过度人机交互都使得T9拼音的输入效率很低，而且全拼对普通话不好的人难度很大。

T9笔画采用目前多数输入法对笔画的归类方法将汉字笔画归为横、竖、撇、点、折五类，分别用1、2、3、4、5表示。录汉字时，按笔顺进行输入，逐键提示，每屏数个，高频优先，最长可输入12划，并支持联想。由于分别使用五个键表示五种笔画，因此不需要像T9拼音一样对组合情况进行智能判断，内部处理逻辑很简单。然而，因为T9笔画充分利用了丰富的笔画信息和不等长码的短码位，并可以直接键选重码字，所以它的实际输入效率比T9拼音还高，只可惜很多用户还不知道这一点。使用笔画输入存在的问题是，有个别的字的笔顺不易掌握。好在国家已有成熟的笔顺标准可以作为输入这类字时的依据。

大众数字码用10个数字对字词进行编码。除了用1、2、3、4、5分别表示横、竖、撇、点、折五种笔画外，还用6、7、8、9、0分别表示交、插、八、小、口五类部件<sup>[54]</sup>。单字按笔顺取第一、二、三、四、末五个代码、不足时按实际码长。对于可按左右、上下或内外分成首部和尾部二部分的汉字，取码规则还可以变更为“首2尾3”或“首2尾2”。词组的码长均为6位。这样，单字和词组可以各字拥有独立的编码空间。单字输入时需要用非数字键作为结束键，词组输入时不需要专门的结束键。大众数字码使用了相当多的笔画组合作为部件，但由于归类清晰，记忆起来比很多同类的输入法要容易些，加上精心的编码规则降低了重码率，使得它在比赛中脱颖而出。不过，应当看到它使用的部件相当多，编码规则也并不简单，学习难度还是相当大的。同时，除了汉字特征信息的选取和字词编码规则外，它在其它方面还没有什么引人注目的独特之处。

黄金码用9个数字对字词进行编码。除了用1、2、3、4、5分别表示横、竖、撇、点、折五种笔画外，还用6、7、8、9分别表示“口”、“十”、“八”、“亠”四类部件。编码时分字首和字尾，也区分独体字与合体字的不同。在提示行不为空时，0、*和#用做选择键。黄金码最大的特色是，在输入时若用于编码的数字与已输入的编码一起不能构成另外的字词编码时，该数字键就可以用于选择同码字词，这样就大大地增加的输入法的键选能力，缩短的动态平均码长；结合高频先见的不等长码的使用，在输入时基本上不用翻页，进一步提高了输入效率。不过，字首与字尾的区分没有标准可循，常常因人而异；动态地使用剩余编码键选择重码字词也造成选择键位置变化太大，加重了人机交互的负担。

### 3.6 通用输入法平台

发明和设计汉字编码的人很多，而真正能够编写汉字输入法软件的是很少的，因此一个功能强大的通用汉字输入法平台会对汉字编码的研究、试验和制作产生巨大的促进作用。通用输入法平台来源于对各种输入法的共性抽象，反过来又对输入法的制作有不可忽视的限制。

早在DOS时代就有人从事通用输入法平台的研究了<sup>[57]</sup>。但是，输入法平台的广泛使用还是在Windows操作系统普及以后的事。

微软公司和北京中易电子公司合作开发的码表输入法生成器（Imegen.exe）是WINDOWS操作系统上最早的也是使用得最广泛的输入法平台。汉字编码人员只需要提供一张按规定格式制作的码表，并对输入法的名称、最大码长、使用的码元集和构词规则等进行描述，就可以生成自己的输入法了。以最近的Windows 2000内置的码表输入法生成器为例，向它提供的码表需要满足的条件是：码元集合是键盘可键入键的子集；输入法能够定制的最大编码长度的限度为 12；信息元为单符或多符代码的形码或音码。这里所说的键盘可键入键共 47 键，包括26个字母键、上排10个数字键和“,./;’[]\-=`”这11个符号键，但不包括小键盘上的数字键。码表输入法生成器所生成的输入法存在着很多缺陷，已经难以满足许多现代汉字编码输入法制作的需要。首先，它硬性规定重码字词的选择只能使用10个数字键按顺序选择，翻页键只能使用“+”和“-”，同时空格键也可以选择第一重码字词；这样就限制了一些优秀的输入法希望采用更易于操作的键作为翻页键和重码字词的选择键的自由，也使得采用了10数字键作为编码键的输入法在选择重码字词时不得不用更加难以操作的复合键（Shift+数字键）。其次，它的词组管理功能非常弱，在线造词时只能增加词组而不能删除和修改词组，造词过程中出现输入错误时只能放弃已造好的部分而不能修改继续。另外，输入状态的切换不方便，对码表容量的限制，没有提供输入法的可控性发布和安装手段等都妨碍了它的进一步广泛使用。

杜志民先生开发的极点中文通用输入平台是目前影响最大的输入法生成器，与Windows内置的输入法生成器相比输入功能上有了长足的进步，但是没有考虑与应用程序的接口问题。该软件于2001年9月10日最初发布时名称叫“五笔拼音1.0”。由于可以在互联网上免费下载和使用该软件，还由于有一批热心的五笔爱好者支持和参与，更由于杜先生一直坚持不断更新和加强软件的功能并维持免费软件的局面，该软件便得以迅速地流行起来。2003年3月31日在发布3.1版时，该软件正式更名为“极点中文通用输入平台”，以反映杜先生将该软件作为输入法生成器而不单纯是五笔拼音输入法的初衷。现就2004年8月26日最新发布的4.0版作一介绍。与传统输入法生成器相比它的优点是：可以使用小键盘数字；对于纯数字输入法也采用3重码选择方式（即用空格选第1重码，左Shift选第2重码，右Shift选第3重码）；提供了灵活多变的、漂亮别致的用户界面风格供用户选择；可以使用Shift或Ctrl键进行中英文状态键的单键切换；支持自动或手动地调整重码字词的顺序；支持不等长码在编码对应的字词唯一时自动上屏；支持自动造词；可以将生成的输入法打包成安装软件；提高大量的设置选项供熟练用户对输入法进行调整和避免与操作系统或应用软件间的冲突。

在功能上与极点中文通用输入平台类似软件还有龙文输入平台和青月亮平台。它们也都是基于Windows操作系统的，但不是免费软件而是商业软件，流行得不是很广。

总之，虽然通用输入法平台取得了不小的进展，已能适应制作常规的基于字词的输入法的需要了，但是对于语句级输入法和许多有特殊要求的字词型输入法还是必须专门编程才能取得最好的效果。毕竟，搞输入法的人是极少数，而仅仅使用输入法的人才是绝大多数，因此包括编码层次和软件层次在内的汉字输入法的总体性能才是最为重要的。

通用输入法平台是在软件层面使用输入法的制作自动化。但是，一个输入法制作在编码层面也有大量的工作要做，如何利用计算机来辅助汉字编码也引起了一些研究者的兴趣，这方面的研究情况请参阅文献<sup>[58]</sup>-<sup>[63]</sup>。

## 4 面临的形势与存在的问题

虽然在汉字编码输入方面已经取得了不少进展，汉字能否输入计算机的问题已经解决，但是汉字编码输入理论一直是一个薄弱环节，迄今为止仅有的一本理论性较强的汉字键盘输入专著<sup>[5]</sup>并没有引起输入法实践者足够的重视。由于没有科学而系统的输入法理论指导，在汉字编码输入法研制时往往片面地强调某一方面、某一个指标，从而出现了很多误区，再加上商业运作上的夸大其词，就产生了诸如低重码率神话、速度神话、大词库神话、编码决定论、程序决定论、形码优越论、音码优越论之类的奇特论调<sup>[70]</sup><sup>[71]</sup>。

同时，在实用性方面，人们对汉字编码输入的现状仍然十分不满意，新的汉字编码输入法还在不断地涌现，以期克服现有输入法存在的诸多问题。不同时代问题，有着不同的背景，从而决定了问题的性质和解决问题的不同方法。汉字编码输入技术问题的性质和解决思路主要取决于人、机、文、码四个方面的因素，以下结合当前的背景进行论述。

在人方面，计算机的普及造就了巨大的用户群体，而且非职业字员用户占绝大多数，其中还包括了大量的中小学生,中国已进入了非专业打字时代<sup>[72]</sup>。非职业打字员一般都没有经过专业的打字培训，知识背景也大不相同。因此，如何使输入法易学易用和保持一定的速度是问题的关键。最好是，输入法在入门时基本上不用学习，熟悉后又有提升速度的手段，甚至达到或超过传统职业打字员的速度。但是当前的输入法往往是易学易用的输不快，如五笔字型，而输得快的难学难用，如智能ABC。非职业打字员的另一特征是根据腹稿录入，即边思考边看着屏幕打字。因此，如何利用好用户看屏输入这一点来进行反馈设计是极为重要的，它直接影响着输入法的质量。但是，目前的输入法对反馈设计没有引起足够的重视，有的过于强调盲打而丧失了易学易用性，有的又过于依赖人机交互而丧失了易用性和输入速度。另外，因为现在大多数用户都独自拥有计算机，所以输入法一般为某个用户专用，可以针对特定用户建立个性化的字词编码库，以提高用户的输入效率。但是，现在的输入法往往只有一个通用编码库，随着编码字词条目的增加就会出现大量的重码，无用词的比例也增大，进而影响输入法的性能。最后，在中小学进行打字教育时，汉字编码的规范化问题和汉字编码与语文教育的结合问题变得十分重要。在这一点上，目前很多流行的输入法都是不合格的。很多人批评五笔字型对汉字不合规范地乱拆分会导致语文教学和写字的混乱，五笔字型也因此未能进入中小学教育<sup>[25]</sup><sup>[26]</sup>。即使是教育部推荐的认知码也有许多人对其规范性提出异议<sup>[20]</sup><sup>[21]</sup>。

在机方面，计算机处理能力已相当强大，手机、PDA等手持智能设备已广泛使用，数据库技术已非常成熟。当今微型计算机强大处理能力对于个人用户来说有很多富余，使得我们可以增大程序的时间和空间复杂度来提高输入法的性能。手持智能设备的流行要求输入法在通用键盘和数字键盘上的操作方式尽量统一，以减少用户的学习和使用负担。大型的数据库，如SQL SERVER,在微机上的运行速度完全可以满足输入法检索字词的要求，所以我们可以采用数据库来存储海量字词及其属性，甚至扩展输入法的功能到学习、查询和辅助翻译等领域。目前，除了语句型输入法充分地利用的富余的计算机资源外，其他的字词型输入法在资源利用上还停留的第二代输入法的水平上；数字键盘输入法一般自成体系，与通用键盘输入法缺乏衔接；数据库技术没有在输入法里得到应有的应用。

在文方面，对于非职业打字员而言，输入文本以常用字构成的连续真实文本占绝大多数，而且对某个用户来说文本一般局限于特定的领域。因此，这类文本的冗余度比汉字文本整体的冗余度要高，可以动态地调整码长，给常用字词以短的编码，实时地、自动地创建新词组，从而充分地压缩冗余度，提高输入速度。对于离散文本和罕见字的处理，输入速度不是关键，关键是要有简单的手段实现输入。目前的输入法往往对输入文本的性质不加区别地对待，结果使得输入法的整体效率收到了影响。

在码方面，目前流行的各类编码都存在各自的问题。字词型输入模式僵化，缺乏创新。空格键作为简码字词的结束键减低了编码效率；看打方式的设计被错误地用到了想打方式上，强调盲打而忽视了反馈信息的作用；对码长的过度限制（通常为4）导致重率上升，限制重码又使可使用的词组量受限，不限制重码也会增加人机交互而影响输入速度；未能充分地利用汉字丰富的笔画信息。语句型输入模式不太适合中文，其转换正确率不高，效率不高，编码识读性差。

1) 音字转换短语或语句输入。与普及语句输入的日本不同，汉语拼音还不是文字，识读性差，输入时反馈信息需要依赖于及时的转换结果，否则不易判断输入错误，输入的编码越长越能提供更多的语境但击键出错的概率也越大，因此转换的正确率是有极限的；而日语假名是文字的一部分，容易识读。中文的汉字常用汉字使用量比日语大得多，而且没有日语一样的假名和丰富的助词帮助，转换的正确率有限。汉语拼音直接作为编码，其本身的冗余度太大，输入效率很低；而采用双拼音又会增加学习负担。中国方言区人口众多，他们的普通话不太准，使用全拼难度仍然很大。用于手持设备时，资源消耗太大，而且没有足够大的显示空间和操作按键。离散文本的输入（包括本文错误的修改）不方便。

2) 各种五笔字型输入法。学习难度太大，仅适合已会五笔的人。对中小学生还存在规范性问题。向手持设备的移植也存在同样的问题，而且其输入效率也并不高。

3) 各种二笔输入法。虽然普及程度不如五笔，但易学性提高较大，而且速度与五笔相当。向手持设备的移植也容易一些。但是，由于使用了笔对，并需要区分字型和使用一些部件，其易学性和易用性还是不令人满意的。

## 5 参考文献

1. 倪海曙. 注音识字简史. 语文现代化[J]. 1983. (6). 130
1. 胡瑞昌. 文字改革与语言文字工作答客问（上）[J]. 语文与信息. 1995. (5). 13-14
1. 汉语拼音与输入法论坛. http://sh.netsh.com/bbs/1951/
1. 周强. 计算机科学[J]. 1995. (4). 36-40
1. 陈一凡，胡宣华. 汉字键盘输入技术与理论基础[M]. 清华大学出版社，广西科学技术出版社. 1994.6.
1. 《微机办公自动化丛书》编委会. 中国微机办公自动化软件大全[M]. 北京经济学院出版社. 1993.7.
1. Lawrence Rabiner, Biing-Hwang Juang, Fundamentals of Speech Recognition[M]. 清华大学出版社, Prentice Hall. 1999.9.
1. 北京语言学院语言教学研究所. 现代汉语频率词典[M]. 北京语言学院出版社. 1986.6.
1. 俞士汶, 朱学锋, 郭锐. 现代汉语语法电子词典的概要与设计[J]. Proceedings Of ICCIP92. 1992.
1. 李公宜, 李海飚. 论汉字编码的最短极限码长[J]. 中文信息. 1992.(1).
1. 冯志伟. 再谈汉字的熵值[J]. 语文与信息. 1996.(2).
1. 王晓龙, 王轩. N元汉字字词编码输入的最短码长和速度上限[J]. 中文信息学报. 1993. 7(4).
1. Robert Kruse, C.L. Tondo, Bruce Leung. Data Structures & Program Design in C[M]. 2nd Edition. Prentice Hall, Inc. 1997.
1. 张侃, 陈一凡. 汉字键盘输入的认知模型[J]. 中文信息学报. 1991.5(4).
1. 何克杭. 汉字认知模型与形码方案设计[J]. 中文信息学报. 1994.9(3).
1. 周冰洋, 刘植婷, 姚世全. 常用汉字编码字典[M]. 宇航出版社. 1990.9.
1. 王力德. 汉字编码的普及目标体系与编码实例[J]. 中文信息学报. 1993.8(4).
1. 刘爱莲. 什么样的输入法才能为大众接受[J]. 语文与信息. 1995.(6).
1. 卫至上. 电脑如何普及：教委走错了方向！[J]. 语文与信息. 1995.(3).
1. 周宪. “认知码”规范性探讨[J]. 语文与信息. 1995.(5).
1. 宁基. 从“认知码”谈推荐什么样的汉字编码[J]. 语文与信息. 1995.(6).
1. 王相东. “万码奔腾”可以休矣[J]. 语文与信息. 1995.(4).
1. 潘骑, 潘德孚. 编码的“速度误区”[J]. 语文与信息. 1996.(2).
1. 潘德孚. 汉字编码与识字教育[J]. 中文信息. 1997.(1).
1. 张孝存, 王梅. 从“邱氏鼠药案”想到“五笔字型”编码[J]. 语文与信息. 1995.(4).
1. 张在云. 谈谈’98规范王码的得失[J]. 安徽广播电视大学学报, 2001, (2).
1. 华绍和, 肖金卯, 蒋顺炳. 适应中小学教学用的汉字编码的特点[A]. 中国中文信息学会汉字编码专业委员会第八届年会、中国计算机学会中文信息技术专业委员会第六届年会暨汉字输入技术与应用研讨会文集[C]. 2002.
1. 吴越. 电脑打字普及教材[M]. 北京群言出版社. 1993.5.
1. 单波. 论汉字编码的分代与第三代汉字编码[J]. 中文信息. 1989.(2).
1. 金山电脑有限公司. WPS桌面印刷系统用户大全[M]. 1991.6. 17-23.
1. 周山芙. 自然码实用教程[M]. 清华大学出版社. 1994.12.
1. 章森, 宗成庆, 孙建军. 新一代中文输入系统面临的问题[J]. 中文信息. 1997.(1).
1. 赵以宝, 孙圣和. 一种基于单字统计二元文法的自组词音字转换算法[J]. 电子学报. 1998. 26(10).
1. 刘来旸, 瞿有利, 樊孝忠. 汉语智能输入系统的设计[J]. 北京理工大学学报. 2001. 21(3).
1. 陈正, 李开复. 拼写纠正在拼音输入法中的应用[J]. 计算机学报. 2001. 24(7).
1. 仲兴国. 多词组一次性拼音·汉字变换[J]. 中文信息学报. 1990.4(2).
1. 王晓龙, 王开铸, 白小华. 自然语言理解中的音字流自动分词[J]. 中文信息学报. 1990.5(3).
1. 万建成. 拼音 – 汉字转换输入中的结构识别方法[J]. 中文信息学报. 1991.6(1).
1. 万建成. 可分隔动词及其在拼音 – 汉字输入中同音词识别的应用[J]. 中文信息学报. 1991.6(4).
1. 万建成. 语音代码 – 汉字智能转换研究[J]. 中文信息学报. 1993.8(2).
1. 章森, 宗成庆, 陈肇雄, 黄河燕. 语句拼音 – 汉字转换的智能处理机制分析[J]. 中文信息学报. 1997.12(2).
1. 郭进. 统计语言模型及汉语音字转换的一些新结果[J]. 中文信息学报. 1992.7(1).
1. 徐进霈, 高枚. 汉语文本读入中音字转换的知识集成模型和时间同步搜索算法[J]. 中文信息学报. 1993.8(1).
1. 高升, 王晓龙. 语句级汉字输入系统中语义规则研究[J]. 计算机工程与应用. 2003.
1. 王锡龙, 黄希琛, 邹志刚. 汉字输入中的重码自动区分理论[J]. 中文信息学报. 1990.4(1).
1. 吕强, 钱德培. 基于词组的智能化汉字输入系统CIIIS/2的设计[J]. 中文信息学报. 1991.6(1).
1. 赵雷, 吕强, 杨季文, 朱巧明. 汉字输入法类的设计与实现[J]. 中文信息学报. 1995.10(4).
1. 陈一凡, 朱亮. 汉字键盘输入智能处理软件综述[J]. 中文信息学报. 2002.17(2).
1. 刘长松, 伍振军, 乔春雷, 李元祥. 用统计方法实现汉字输入的智能联想[J]. 中文信息学报. 1999.14(1).
1. Zheng Chen, and Kai-Fu Lee. A new statistical approach to Chinese pinyin input[A]. ACL-2000[C]. Hong Kong. 2000.10.
1. Jianfeng Gao, Hai-Feng Wang, Mingjing Li, and Kai-Fu Lee. A unified approach to statistical language modeling for Chinese[A]. ICASSP2000[C]. Istanbul, Turkey. June 5 - 9, 2000.
1. 王永民. 五笔数码形声输入法及其键盘[P]. 中国. G06F3/023. 00124781.6. 2000-9-14.
1. 郑岩松. 左右数码汉字电脑输入法及其键盘[P]. 中国. G06F3/023. 02102272. 2002-2-1.
1. 罗康宁. 一种数码汉字输入法及其键盘[P]. 中国. G06F3/023. 03129316.6. 2003-12-10.
1. 肖水清. 汉字输入一日通[M]. 北京经济学院出版社. 1993.1.
1. 萧启宏. 全汉字编码输入系统启宏全息码[M]. 电子工业出版社. 1993.3.
1. 孟凯, 万国银, 许惠山. 汉字输入支持系统的设计特点[J]. 中文信息. 1992.(1).
1. 张玉华, 周克兰. 输入法码本前期处理工具的实现[J]. 微机发展. 2003.13(4).
1. 舒展羽, 胡勇新. 汉字编码辅助设计环境HCCAD[J]. 中文信息. 1992.(2).
1. 陈玉龙. 中文自动编码原理[J]. 中文信息学报. 1997.12(1).
1. 钱德培, 杨季文, 吕强, 朱巧明. 一个基于C/S模式的汉字词属性分析和重组系统的设计[J]. 中文信息学报. 1998.13(1).
1. 陆剑江, 钱培德. 汉字输入法码本自动更正设计研究[J]. 中文信息学报. 2001.16(6).
1. 吴娴, 吕相, 杨涛, 杨季文, 钱德培. 论汉字码本数据库管理技术[J]. 中文信息学报. 2002.17(2).
1. John G. Proakis. Digital Communications[M]. 3. 北京. 电子工业出版社. 1998.9.
1. C. E. Shannon. A Mathematical Theory of Communication[J]. The Bell System Technical Journal. 1984. (27).
1. Hyman e.Stimulus. Information as a Determinant of Reaction Time[J]. Journal of Experimental Psychology. Vol.45. No.3. 1953.
1. 丘菏生. 汉语双拼的标准键盘设计[J]. 中文信息. 1992.(2).
1. 杨道沅, 董小国, 董红, 陈丹. 《自然码》双拼键盘设计合理的研究[J]. 中文信息学报. 1992.8(1).
1. 杨道沅, 李棣. 汉字输入键盘设计方法的研究 – 兼论标准汉字双拼键盘的设计[J]. 中文信息学报. 1996.8(3).
1. 子厚. “全息码”风波的演变[J]. 中文信息. 1992.(2).
1. 余克艰. 戳穿电脑打字的“速度神话”[J]. 语文与信息. 1995.(6).
1. 陈和利. 专业录入员终究有一天会消失（转载）[J]. 语文与信息. 1995.(4).
1. 戴石麟. 文字式音形汉字输入法[P]. 中国: G06F, ZL 95111380.1, 1995.
1. 陈一凡, 张鹿, 周志农. 键位相关速度当量的研究[J]. 中文信息学报. 1990.4(4).
1. 陈一凡, 张鹿. 键位分布合理指数与动态平均码长综合指标的自动测定[J]. 中文信息学报. 1991.5(1).
1. Microsoft Corp. Microsoft Win32 Multilingual IME Overview for IME Development, Windows  DDK[R]. 
1. Microsoft Corp. Microsoft Win32 Multilingual IME Application Programming Interface for IME Development, Windows DDK[R].
1. Thomas Scovel. Psycholinguistics[M]. New York: Oxford University Press. 1998.
1. John Sinclair. Corpus, Concordance, Collocation[M]. New York: Oxford University Press. 1991.
1. Douglas, Susan Conrad, Randi Reppen. Corpus Linguistics[M]. Cambridge: Cambridge University Press. 1998.
1. Jeffrey D.Ullman, Jennifer Widom. A First Course in Database System[M]. Prentice Hall, Inc. 1997.
1. Ronald J. Norman. Object-Oriented Systems Analysis and Design[M]. Prentice Hall, Inc. 1996.
1. Bernard Kolman, Robert C. Busby, Sharon Ross. Discrete Mathematical Structure[M]. 3rd Edition. Prentice Hall, Inc. 1996.
1. Harry R. Lewis, Christos H. Papadimitriou. Elements of the Theory of Computation[M]. 2nd Edition. Prentice Hall, Inc. 1998.
1. William Ford, William Topp. Data Structures with C++[M]. Prentice Hall, Inc. 1996.
1. William Stallings. Operating Systems[M]. Prentice Hall, Inc. 1998.
1. Brian W. Kernighan, Dennis M. Ritche. The C Programming Language[M]. 2nd Edition. Prentice Hall, Inc. 1998.