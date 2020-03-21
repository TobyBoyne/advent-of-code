import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

class Star:
	def __init__(self, *args):
		self.x, self.y, self.x_vel, self.y_vel = args
	def move(self, t):
		return self.x + t * self.x_vel, self.y + t * self.y_vel

stars = []
with open("day10.txt", 'r') as f:
	for l in f:
		args = [int(l[10:16]), -int(l[17:24]), int(l[36:38]), -int(l[40:42])]
		stars.append(Star(*args))

# pyplot
fig = plt.figure()
ax_t = plt.axes([0.25, 0, 0.65, 0.03])
ax_stars = plt.axes([0.1, 0.2, 0.8, 0.65])

x = [star.x for star in stars]
y = [star.y for star in stars]

plt.axes = ax_stars
plt.scatter(x, y)
time = Slider(ax_t, 't', 10000, 10200, valinit=0, valstep=1)

def update(val):
	x=[star.move(val)[0] for star in stars]
	y=[star.move(val)[1] for star in stars]
	ax_stars.clear()
	plt.scatter(x,y)
	fig.canvas.draw_idle()

time.on_changed(update)
plt.show()