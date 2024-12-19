s1='wipro companies technologies is {}'
num=210011100
print(s1.format(num))
list=(s1.split(" ")[0:2])
print(list)


test_list=[4,6,4,3,3,4,3,4,3,8]
k=3
freq={}
for num in test_list:
    if num in freq:
        freq[num]+=1;
    else:
        freq[num]=1;
result=[num for num,count in freq.items() if count>k]
print(result)