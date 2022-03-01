import MeCab
import japanize_matplotlib
import collections
import seaborn as sns
from matplotlib import pyplot as plt

# データセット===================================

text_original="""
メロスは激怒した。34歳。必ずかの邪智暴虐の王を除かなければならぬと決意した。メロスには政治がわからぬ。メロスは激怒した。メロスには政治がわからぬ。
"""

# データ処理=====================================

text=text_original.strip()

# 形態素解析=====================================

t = MeCab.Tagger()
node = t.parseToNode(text)

# 形態素解析後、目的のもののみ取り出す=====================================

words=[]
while node:
    hinshi = node.feature.split(",")[0]
    if hinshi in ["名詞","動詞","形容詞"]:
        origin = node.feature.split(",")[6]
        print(node.feature)
        words.append(origin)
    node = node.next
# print(words)

#不要な＊の消去=======================================================-

for n in range(0,len(words))[::-1]:
    if words[n]=="*":
        words.pop(n)

#単語の数カウント===============================================

c = collections.Counter(words)

#グラフ描画===================================================

sns.countplot(y=words,order=[i[0] for i in c.most_common(20)])
plt.show()