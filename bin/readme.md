## 文件结构

* src
  * stringmatch.py
  * stringmatch_gui.py
  * ui.py
* bin
  * requirement.txt
  * readme.md
* report.pdf
* hw10.pdf

## 各个文件的作用

`stringmatch.py` 实现了`naive`，`kmp`，`bm` 三种字符串匹配算法，提供了便捷的命令行控制

`python stringmatch.py [-h] [-itf INPUT_TEXT_PATH] [-ipf INPUT_PATTERN_PATH] [-it INPUT_TEXT] [-ip INPUT_PATTERN] [-o OUTPUT_FILE]`

使用时，选择从文件或者直接在命令行中输入 `text` 和 `pattern` 

`-itf` 输入 text 的路径或者 `-it` 直接输入 text

`-ipf` 输入 pattern 的路径或者 `-ip` 直接输入 pattern

需要注意的是，有些特殊符号直接输入在命令行中会导致命令行参数解析错误，此时使用文件输入就能解决这个问题

`-o` 是可选参数，若输入某个文件的路径，将会把程序执行的结果保存到该文件中

程序会在命令行输出三行，分别表示三个算法的结果是否一致，匹配成功的位置以及三个算法分别使用的时间

`stringmatch_gui.py` 实现了图形界面，使用方式 `python stringmatch_gui.py` 

在图形界面中输入 `text` 和 `pattern` 后点击 `match` 就会显示出总共成功匹配的个数，text 和 pattern 的长度，匹配成功的位置以及三个算法分别使用的时间，同时会在 match 中将匹配成功的高亮显示

点击 `reset` 会清空所有输入，可以继续进行匹配

增加了快捷键 `ctrl + M` ，`ctrl + L`，`ctrl + Q` 分别对应 `match`，`clear` 和关闭程序

`requirement.txt` 中是所依赖的库

`report.pdf` 是实验报告

`hw10.pdf` 是证明题

附上程序支持的字母表列表：

```python
['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~', '\n', ' ', '—','\t','＂','＃','＄','％','＆','＇','（','）','＊','＋','，','－','／','：','；','＜','＝','＞','＠','［','＼','］','＾','＿','｀','｛','｜','｝','～','｟','｠','｢','｣','、','〃','〈','〉','《','》','「','」','『','』','【','】','〔','〕','〖','〗','〘','〙','〚','〛','〜','〝','〞','〟','〰','–','—','‘','’','‛','“','”','„','‟','…','‧','﹏','﹑','﹔','·','！','？','｡','。']
```

