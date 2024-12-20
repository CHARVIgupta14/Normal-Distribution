import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_excel(r'C:\Users\gupta\python\pandas\data_of_hours.xlsx')
print(data)

data.to_csv("normal_distrubution.csv")
numbers_of_hours_slept=data["Number of hours slept before maths's exam (MTT)"].tolist()
mean =sum(numbers_of_hours_slept)/ len(numbers_of_hours_slept)

print(mean)
p=[]
for x in numbers_of_hours_slept:
    d=x-mean
    p.append(d)

variance=((sum(p))**2)/len(p)
print(variance)    



x=numbers_of_hours_slept

y = [
    (1 / ((2 * 3.14 * variance) ** 0.5)) * (2.71 ** (-((xi - mean) ** 2) / (2 * variance)))
    for xi in x
]



plt.plot(x, y ,label="normal_distribution",color="blue")
 
plt.hist(numbers_of_hours_slept,bins =10,density=True,alpha=0.6,label="histogram of data",color="orange",edgecolor="pink")

plt.title("normal distribution")
plt. xlabel("numbers_of_hours_slept")
plt.ylabel("probability density")
plt.legend()
plt.savefig("normal_distributionn.png")
plt.show()



