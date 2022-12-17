import random

print("Hello qiuqiu")
i = print("nihao")
print("i")
dir(__builtins__)

i = 456
print(i)

x = 2
y = 5
print(x,y)
y = x
print(y)
x = 2
y = 5
x,y=y,x
print(x,y)

print('go')
print("let's go")
print("\"let\'s go\"")
print("i love python\ni love pychram")
print("白菜菊花")

#反斜杠和原始字符r
print("D:\three\two\one\now")
print("D:\\three\\two\one\\now")
print(r"D:\three\two\one\now")

#换行字符
poetry = """
泥鳅可以欧端午
泥鳅下一个新池60发出完
泥鳅蟹黄下一锅一定成
"""
print(poetry)

print(12+34)
print('12' + '34')
print("1234\n" * 5)

print(3 < 3)
print(3 == 3)
print(3 > 1)
print(3 != 1)

import _random

counts = 1
i = random.randint(1,100)
while counts > 0:
  b = input("猜一下一等奖是数字几：")
  a = int(b)
  if a == i:
    print("恭喜你猜对了")
    break
  else:
      if a < i:
          print("小啦")
      else:
          print("大啦")
  counts  = counts - 1

print("游戏结束")



i = 0
while i < 1:
    i = i + 0.1
    print(i)

i = print("九九乘法表")







