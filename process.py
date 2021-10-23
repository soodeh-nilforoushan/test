from io import SEEK_CUR
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
from numpy.lib.function_base import piecewise
import seaborn as sns
import pandas as pd


filename="/Users/soudeh/Desktop/ditto-master/data/er_magellan/Structured/Fodors-Zagats/train.txt"
nonmatch_label=0
match_label=0
pair_number=0
record_number=0
words = []
match_words=[]
repeatition_of_each_word=[]
repeatition_of_match_word=[]
repeatitive=[]

empty_array=np.array([])
file = open(filename,'r')
count=0
with open(filename, 'r') as fp:
     while True:
        lines=fp.readline()
        if not lines:
             break
        pair_number+=1
        if (lines[-2]=="1"):
            match_label+=1
        elif (lines[-2]=="0"):
            nonmatch_label+=1
        # print(lines[-2])
        line_word=lines.split("\t")
        for w in line_word:  
            # if (w!="0\n" or w!="1\n"):
            if(lines[-2]=="1"):
               w2=w.strip('1\n')
               if (w2!=''):
                    match_words.append(w2)
                    # print(match_words)
            w1=w.strip('0\n').strip('1\n')
            if (w1!=''):
               words.append(w1) 
repeatition_of_each_word=[0]*len(words)
repeatition_of_match_word=[0]*len(match_words)
# print(match_words)



# for i in range(0, len(words)):  
#     repeatition_of_each_word[i] = words.count(words[i])
#     if(repeatition_of_each_word[i]==33):
#         print("here")
#         print(words[i])
# for i in range(0, len(repeatition_of_each_word)):  
#         print( repeatition_of_each_word[i])
for i in range(0, len(words)):  
    repeatition_of_each_word[i]=words.count(words[i])
for i in range(0, len(match_words)):  
    repeatition_of_match_word[i]=match_words.count(match_words[i])
    
for i in range(0, len(match_words)):  
    repeatition_of_match_word[i] = match_words.count(match_words[i])
    if(repeatition_of_match_word[i]==6):
        print("here")
        print(match_words[i])

c1=Counter(repeatition_of_each_word)
key_list=list(c1.keys())
val_list=list(c1.values())
for i in range(len(key_list)):
    (val_list[i])=int(val_list[i]/key_list[i])

c2=Counter(repeatition_of_match_word)
key_list_match=list(c2.keys())
val_list_match=list(c2.values())
for i in range(len(key_list_match)):
    (val_list_match[i])=int(val_list_match[i]/key_list_match[i])


print(f'first value shows the x-axis and the second value shows the y-axis:')
print("\n all records:")
for i in range(len(key_list)):
    print(f'{key_list[i]}:{val_list[i]}  ',end="")
print("\n match records: ")
for i in range(len(key_list_match)):
    print(f'{key_list_match[i]}:{val_list_match[i]}  ',end="")
print(f'\n number of match pairs:  {match_label}')
print(f'number of non-match pairs:  {nonmatch_label}')
print(f'number of records are: {len(Counter(words))}')      
print(f'number of pairs are:  {pair_number}')   


# sns.set()
# bins = np.linspace(0, 10, 100)
# data=np.random.multivariate_normal([val_list,key_list],[key_list_match,val_list_match],size=2000)
# data = pd.DataFrame(data, columns=['x', 'y'])
# for col in 'xy':
#     plt.hist(data[col], normed=True, alpha=0.5)

# plt.hist(val_list,bins=key_list,label='all records', alpha=0.5)
# plt.hist(val_list_match,bins=key_list_match, label='match records', alpha=0.5)


fig=plt.figure(figsize=[10,8])
ax1 = fig.add_subplot(111)

plt.grid(axis='y', alpha=0.75)
plt.grid(axis='x', alpha=0.75)
ax1.bar(key_list,val_list,alpha=0.5, label='all records')
ax1.bar(key_list_match,val_list_match,alpha=0.5, label='match records')
plt.legend(loc='upper right')
plt.ylabel('number of records with the frequency')
plt.xlabel('frequency of records appearing in a pair')
plt.title('wdc/cameras/train.txt.large')
plt.show()



