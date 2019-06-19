import codecs
import re
import sys
import os
import numpy as np
import pymysql
from snownlp import SnowNLP
import matplotlib.pyplot as plt
from snownlp import sentiment
from snownlp.sentiment import Sentiment

def snowanalysis(self):
	# sentimentslist = []
	neg = 0
	pos = 0
	for li in self:  # 实参不要有空串
		non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

		# 正则表达式取所需文本
		# print(li)
		# print('above is li')
	# re_words = re.compile(u"[\u4e00-\u9fa5]+")
	# m =  re_words.search(li, 0)
		# print(m)
		# print('---------below is m.group()')
		# 按理说不能有空串，这里先用if-break混过去
	# if m == None:
	# 	break
		# print(m.group())

	# text = m.group()
		# cn    [\u4E00-\u9FA5\\s]+
		text = re.sub(r'((?=[\x21-\x7e]+)[^A-Za-z0-9])', ',', li)
		text = text.translate(non_bmp_map)
		# print("text")
		# print(text)
		s = SnowNLP(text)
		# print("s.sentiments")
		# print(s.sentiments)
		if s.sentiments < 0.71:  # 调成0.7试试
			neg += 1
		else:
			pos += 1
	print(str(neg) + "\t" + str(pos))
	return neg,pos


root_dir = "F:\\CoursesMaterials\\DATA Ana\\data"  # 存放待分析txt的文件夹名
dirList = os.listdir(root_dir)
ylist = []
index = []
inx = 0
for i in range(0,len(dirList)):
	path = os.path.join(root_dir, dirList[i])
	if os.path.isfile(path):
		# print(path)
		comment = []
		with open(path, "r", encoding="utf-8") as f:  # 注意编码
			rows = f.readlines()
			print(rows)
			for row in rows:
				# 根据数据样式做定向剔除
				comment.append(row)
		print(comment)  # 存入列表的一篇文档信息
		# comment 未调整，直接用rows
		neg,pos = snowanalysis(rows)
		snownlpResult = open("Z:\\snownlpResult07.txt", "a", encoding="utf-8")  # 分析结果存放位置
		if (neg+pos) == 0:
			break
		snownlpResult.write(str(pos/(neg+pos)) + '\n')
		snownlpResult.close()
		ylist.append(pos/(neg+pos))
		index.append(inx)
		inx += 1
		# print(result)

plt.xlabel("time")
plt.ylabel("sentiment")
plt.legend()
plt.plot(index, ylist)
# plt.scatter(index, ylist, s=20, c="#ff1212")
plt.title('Sentiment from 0401 to 0530')
plt.show()
print("finish")

# snowanalysis(comment)
