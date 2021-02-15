import matplotlib.pyplot as plt
import numpy as np

plt.style.use("dark_background")
u=5
sigma=1
vals=u+sigma*np.random.randn(1000)
print(vals.shape)

plt.hist(vals,100)
plt.show()

vals=np.round(vals)
z=np.unique(vals,return_count=False)
print(z)

x=vals
y=np.zeroes(x.shape)


plt.scatter(x,y)
plt.show()