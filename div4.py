import matplotlib.pyplot as plt
import numpy as np

plt.style.use("dark_background")
subjects=["Maths","Chemistry","English","Physics"]

weightage=[20,15,10,5]
plt.pie(weightage,label=subjects,explode=[0.2, 0, 0, 0],shadow=True)

plt.show()