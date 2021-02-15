import matplotlib.pyplot as plt
import numpy as np

x=np.arange(10)
y1=x**2
y2=x**2+3

print(x)
print(y1)
print(y2)

#now plot the curves of two line

themes=plt.style.available
print(themes)

plt.plot(x,y1,color='red',label="Apple",marker='*')
plt.plot(x,y2,color='green',label='KIWI',linestyle="dashed",marker='o')

plt.xlabel("Time")
plt.ylabel("Price of Apple and Kiwi")

plt.title("Price of Fruits Overtime")
plt.legend()
plt.show()

