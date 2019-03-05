#【2-1】用python实现下面的功能: 允许用txt文件定义一个 词典，内容为一系列词的解释 如apple - food，每个词一行，你的python程序启动时加载一个词典，并开始接受命令行输入。当输入词典中的词时输出释义。如输入apple -输出food。词典中没有的词则输出unknown。

#Python读取文本文档内容
file_object = open(r"dict.txt",'r')
try:
     lines = file_object.readlines()
finally:
     file_object.close( )
print(lines)
#去除list元素后的\n
for i in range(len(lines)):
     lines[i] = lines[i].replace('\n','')
print(lines)


#将文本文档内容按要求存储在字典中
dictionary = {}
num = 0
for word in lines:
    #if word != '\n':
     num+= 1
     if num % 2:    #偶数为key，奇数为value
          dictionary[lines[num-1]] = lines[num]
print(dictionary)

#dict中插入一个元素，试验一下
dictionary['respect'] = 'emotion'
print(dictionary['respect'])
#用法待学习
for key in dictionary.keys():
    print('key = {}'.format(key))

for value in dictionary.values():
    print('value = {}'.format(value))

for key,value in dictionary.items():
    print('{key} : {value}'.format(key = key, value = value))


#接受命令行输入，当输入词典中的词时输出释义。词典中没有的词则输出unknown。
word = input('Please input the word：')
print(dictionary.get(word,'unknown'))
