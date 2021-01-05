import time
import sys
import os
import re
sys.path.append(os.path.abspath("SO_site-packages"))
import pyperclip  # 引入模块
print("文献复制中英结合版")
print("literaturecopy_both english and chinese")
print("version 0.2")
print("by TophTab")
print("support me via Alipay:15279108805,even $1 is big support to author.")
print("赞助请转账支付宝：15279108805，即使是一元也是对作者的支持")
recent_value = ""
tmp_value="" # 初始化（应该也可以没有这一行，感觉意义不大。但是对recent_value的初始化是必须的）
E_pun = u',.!?()<>"\''
C_pun = u'，。！？（）《》“‘'
table_CtoE= {ord(f):ord(t) for f,t in zip(C_pun,E_pun)}
table_EtoC= {ord(f):ord(t) for f,t in zip(E_pun,C_pun)}
    

def English(recent_value):
    changed_1= re.sub(r"\s{2,}", " ", recent_value) 	#将文本的换行符去掉，变成一个空格
    changed_2=changed_1.translate(table_CtoE)
    pyperclip.copy(changed_2)					     #将修改后的文本写入系统剪切板中
    print("\n英文_值变为: %s" % str(changed_2))  	# 输出已经去除换行符的文本
    time.sleep(0.1)

def Chinese(recent_value):
    changed_1= re.sub(r"\s", "", recent_value) 	#将文本的换行符去掉，变成一个空格
    changed_2=changed_1.translate(table_EtoC)
    pyperclip.copy(changed_2)						     #将修改后的文本写入系统剪切板中
    print("\n中文_值变为: %s" % str(changed_2))  	# 输出已经去除换行符的文本
    time.sleep(0.1)

while True:
    tmp_value = pyperclip.paste() 			# 读取剪切板复制的内容
    try:
        if tmp_value != recent_value:		#如果检测到剪切板内容有改动，那么就进入文本的修改
            recent_value = tmp_value
            if re.search("[\u2E80-\u9FFF]+",tmp_value) is not None:
                Chinese(recent_value)
            else:
                English(recent_value)
    except KeyboardInterrupt:  # 如果有ctrl+c，那么就退出这个程序。
        break
