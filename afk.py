import pyautogui
import math

SIZE_X = 100
SIZE_Y = 100

pyautogui.FAILSAFE = False

minutes = input("How many minutes? ")


# Number of steps is equal to minutes * 60 * 10 - ten steps for each second
steps = minutes * 60 * 10

# Start in cricle
print "Going for " + str(minutes) + " minutes and " + str(steps) + " steps."
pyautogui.moveTo(0, 0, duration=0)

for i in range(0, steps):
	# print str(i) + ": " + str(((math.cos(i) + 1)*100) + 50) + " | " + str(((math.sin(i) + 1)*100)+ 50)
	pyautogui.moveTo(((math.cos(i) + 1 )*100) + 50, ((math.sin(i) + 1)*100) + 50, duration=0.1)