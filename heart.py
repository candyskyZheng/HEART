import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib


x_value1 = list(range(10, 100))
y_value1 = [-x+110 for x in x_value1]

x_value2 = list(range(101,190))
y_value2 = [x - 90 for x in x_value2]

x_value3 = list(range(10, 100))
y_value3 = [(45**2 - (x-55)**2)**(1/2)+100 for x in x_value3]

x_value4 = list(range(101,190))
y_value4 = [(45**2 - (x-145)**2)**(1/2)+100 for x in x_value4]

# x_values = x_value1 + x_value2 
# y_values = y_value1 + y_value2 
# plt.scatter(x_values, y_values, c = y_values,cmap = plt.cm.summer, s=5)


for x in range(10,100):
	y_value5 = list(range(-x+110, int((45**2 - (x-55)**2)**(1/2)+100)))
	n = len(y_value5)
	x_value5 = [x]*n
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	plt.scatter(x_value5, y_value5, c = y_value5,cmap = plt.cm.cool, s=20)


for x in range(101,190):
	y_value6 = list(range(x - 90, int((45**2 - (x-145)**2)**(1/2)+100)))
	n = len(y_value6)
	x_value6 = [x]*n
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	plt.scatter(x_value6, y_value6, c = y_value6,cmap = plt.cm.cool, s=20)



plt.show()
