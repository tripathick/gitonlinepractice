import matplotlib.pyplot as plt
import numpy as np


mean=np.array([5.0,6.0])
cov=np.array([[1,0],[0,1]])

mean2=np.array([5.0,6.0])
cov2=np.array([[1.3,0.8],[0.8,1.1]])

dist=np.random.multivariate_normal(mean,cov,500)
dist2=np.random.multivariate_normal(mean2,cov2,500)

plt.scatter(dist[:,0],dist[:,1])
plt.scatter(dist2[:,0],dist2[:,1])
plt.show()