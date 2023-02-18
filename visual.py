import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import utils

fig = plt.figure()

outline = 100
crosssize = 10

# 중앙선
lw = 5
plt.plot([-outline,-crosssize], [0, 0], 'y', linewidth = lw)
plt.plot([crosssize,outline], [0, 0], 'y', linewidth = lw)
plt.plot([0, 0] , [-outline,-crosssize], 'y', linewidth = lw)
plt.plot([0, 0] , [crosssize,outline], 'y', linewidth = lw)

# 차선 생성
lw = 0.5
plt.plot([-outline,-crosssize], [+5, +5], 'k', linewidth = lw)
plt.plot([crosssize,outline], [+5, +5], 'k', linewidth = lw)

plt.plot([-outline,-crosssize], [-5, -5], 'k', linewidth = lw)
plt.plot([crosssize,outline], [-5, -5], 'k', linewidth = lw)

plt.plot([-5, -5], [-outline, -crosssize], 'k', linewidth = lw)
plt.plot([-5, -5], [crosssize, +outline], 'k', linewidth = lw)

plt.plot([+5, +5], [-outline, -crosssize], 'k', linewidth = lw)
plt.plot([+5, +5], [crosssize, +outline], 'k', linewidth = lw)

# 바깥 경계 생성
lw = 3
plt.plot([-outline,0], [+10, +10], 'k', linewidth = lw)
plt.plot([crosssize,outline], [+10, +10], 'k', linewidth = lw)
plt.plot([-outline,-crosssize], [-10, -10], 'k', linewidth = lw)
plt.plot([0,outline], [-10, -10], 'k', linewidth = lw)
plt.plot([-10, -10], [-outline, 0], 'k', linewidth = lw)
plt.plot([-10, -10], [crosssize, +outline], 'k', linewidth = lw)
plt.plot([+10, +10], [0, +outline], 'k', linewidth = lw)
plt.plot([+10, +10], [-outline, -crosssize], 'k', linewidth = lw)

ax = plt.axis([-outline,outline,-outline,outline])

car_1 = utils.Vehicle(1, [0.1, 0], [-100, -2.5])
car_2 = utils.Vehicle(2, [0, 0.1], [2.5, -100])

car_no_1_dot, = plt.plot([], [], 'ro')
car_no_2_dot, = plt.plot([], [], 'bo')

def animate(_):
    car_1.time_passed_dt()
    car_2.time_passed_dt()
    car_no_1_dot.set_data(car_1.whereiscar())
    car_no_2_dot.set_data(car_2.whereiscar())
    
    return car_no_1_dot, car_no_2_dot

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(10), \
                                      interval=1, blit=True, repeat=True)

plt.show()