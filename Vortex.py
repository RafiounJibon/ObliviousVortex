from JibonFunctions import *
turtle.tracer(False)

for times in range(40):
    jump(0,0)
    vortex(35)
    vortex(30)
    
for times in range(40):
    spike2(35)
    spike2(30)
    jump(-760,400)

for times in range(40):
    spike3(35)
    spike3(30)
    jump(760,-400)

for times in range(40):
    spike4(35)
    spike4(30)
    jump(-760,-400)

for times in range(40):
    spike5(35)
    spike5(30)
    jump(760,400)
    
turtle.tracer(True)
