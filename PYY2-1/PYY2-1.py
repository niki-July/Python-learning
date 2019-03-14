'''
#【2-1】用python实现下面的功能: 允许用txt文件定义一个 词典，内容为一系列词的解
释 如apple - food，每个词一行，你的python程序启动时加载一个词典，并开始接受命令
行输入。当输入词典中的词时输出释义。如输入apple -输出food。词典中没有的词则输出unknown。
#【2-2】词典的文件可以随时变，即使你的程序在运行过程中。我需要在你的程序不停地
前提下往那个词典里加东西--当TXT文本发生改变时，重新读取文本内容，你的程序要能认新加进去的东西。程序需要是长时间运行，
一轮输入输出后它会等待下一次输入。
#【2-3】在每次输出后面加一个你的程序花了多少时间计算出结果的描述。比如输入 apple
输出 food ( 0 ms )  用毫秒计时。未来我们需要追踪你这个游戏的反应有没有在变得太慢。
#【2-4】同时在启动程序的时候有一个参数控制要不要加这个时间。
比如 python PYY2-1.py --timerOn 你的程序就会一直显示这个时间，python PYY2-1.py 
就不会显示这个时间。相当于“开发者模式” 和“玩家模式”
#【2-5-todo】把你能想到的漏洞填一填，比如那个文件里有错，某一行只有光秃秃一个词怎么办？3个词
怎么办？词的释义里有空格也很正常？让它跑起来不会一不小心就出来很神奇的结果。如果某一行没对，就忽略
这一行，并给出提示哪行格式不对没加载。如果那个文件不存在怎么办？别直接挂掉，应该提示文件不存在请创建文件之类的。
'''

import sys
import time
import os

Filename = 'dict.txt'
last_time_filecheck = 0
last_time_filechange = 0

while True:
    local_time = time.time()
       
    if local_time - last_time_filecheck > 5:
        last_time_filecheck = local_time

        st_mtime = (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.stat(Filename).st_mtime)))
        if st_mtime != last_time_filechange:
            last_time_filechange = st_mtime

            #Python读取文本文档内容
            file_object = open(r"dict.txt",'r')
            lines = file_object.readlines()
            file_object.close( )
            print(lines)
                
            #去除list元素后的\n；并将字符串转换为单词保存
            keys = []
            values = []
            num = 0
            for i in range(len(lines)):
                lines[i] = lines[i].replace('\n','')
                div = lines[i].split(' - ')
                #print(div)
                if len(div) != 2:
                    print('The format in line %d is error, please check it later.' % num)
                elif div[0] == '':
                    print('The key in line %d is missing, please check it later.' % num)
                elif div[1] == '':
                    print('The value in line %d is missing, please check it later.' % num)
                else:
                    keys.insert(num, div[0])
                    values.insert(num, div[1])
                num+= 1

            #print(keys)
            #print(values)
            #将文本文档内容按要求存储在字典中
            dictionary = {}
            
            for i in range(len(keys)):
                dictionary[keys[i]] = values[i]
            #print(dictionary)
    
    word = input('Please input the word:')
    try:
        if sys.argv[1] == '--timerOn':
            start_time = time.time()
            print(dictionary.get(word,'unknown') + ' (' + str(int((time.time()-start_time)*1e6)) + 'us)')
        else:
            print(dictionary.get(word,'unknown'))
    except Exception as e:
            print(dictionary.get(word,'unknown'))
