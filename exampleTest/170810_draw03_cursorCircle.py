import time, math, win32api

radius = 100
period, dt = 0.5, 0.01
steps = int(period / dt)

mouseX, mouseY = win32api.GetCursorPos()[0], win32api.GetCursorPos()[1]

for i in range(steps+1):
    time.sleep(dt)
    x = mouseX + int(radius - radius * math.cos(i * 4*math.pi/steps))
    y = mouseY - int(radius * math.sin(i * 4*math.pi/steps))
    win32api.SetCursorPos((x,y))