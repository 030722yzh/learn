# i = 0
# j = 0
# while j < 10:
#     print(f'{i}*{j}={i*j}',end='\t')
#     j = j + 1
#     while i < 9:
#         if i < 9:
#             print(i * j)
#             i = i + 1


# 1*9=9     1*8=8	1*7=7	1*6=6	1*5=5	1*4=4	1*3=3	1*2=2	1*1=1
# 2*9=18	2*8=16	2*7=14	2*6=12	2*5=10	2*4=8	2*3=6	2*2=4
# 3*9=27	3*8=24	3*7=21	3*6=18	3*5=15	3*4=12	3*3=9
# 4*9=36	4*8=32	4*7=28	4*6=24	4*5=20	4*4=16
# 5*9=45	5*8=40	5*7=35	5*6=30	5*5=25
# 6*9=54	6*8=48	6*7=42	6*6=36
# 7*9=63	7*8=56	7*7=49
# 8*9=72	8*8=64
# 9*9=81


counts = 10
i = 1
j = 1
z = i + j
print('1.1.', end='')
while counts > 0:
    print('%d' % (z), end='.')
    i = j
    j = z
    z = i + j
    counts = counts - 1








