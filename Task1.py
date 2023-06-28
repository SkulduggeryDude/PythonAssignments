from turtle import *



#Vertical line
#Loop for drawing the circle, range is length of line as circles
lt(90)
for x in range(10):
  begin_fill()
  circle(10)
  end_fill()
  pu()
  fd(20)
  pd()
#Resets position for drawing next line
#Home is bottom of the K
pu()
home()
pd()

#Bottom right of K
#Moving position to the middle of the K to start new line
lt(90)
pu()
fd(80)
rt(135)
pd()
#Loop for drawing the circle, range is length of line as circles
for x in range(7):
  begin_fill()
  circle(10)
  end_fill()
  pu()
  fd(20)
  pd()
#Resets position for drawing next line
pu()
home()
pd()

#Top Right of K
#Moving position to the middle of the K to start new line
lt(90)
pu()
fd(80)
pd()
rt(45)

#Loop for drawing the circle, range is length of line as circles
for x in range(7):
  begin_fill()
  circle(10)
  end_fill()
  pu()
  fd(20)
  pd()

#Resets position for drawing next line
pu()
home()
pd()
