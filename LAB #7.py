import numpy as np
from matplotlib import pyplot as plt
# x = np.array([1,2,3])
# y = np.array([1,2,3])

# labels = np.array(['cats', 'dogs'])
# perc = np.array([70,30])
#
# figure = plt.figure()
# axes = figure.add_axes([0.1,0.1,0.8,0.8])
# axes.pie(perc, labels=labels)
# # plt.plot(x,y, color = 'green', linestyle = '--')
# # plt.xlabel('t')
# # plt.ylabel('v')
# # plt.title('My plot!')
# plt.show()

data_arr = np.genfromtxt('voltage.csv', delimiter=',')
print(data_arr)
time = data_arr[:100, 0]
curr = data_arr[:100, 1]
volt = data_arr[:100, 2]
plt.subplot(1,2,1)
plt.plot(time, curr*50, 'b')
plt.subplot(1,2,2)
plt.plot(time, volt)
plt.show()