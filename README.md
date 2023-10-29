# 3.Navigate-a-Turtle-in-a-2D-environment-using-ROS
Moving turtle using inputs from the user in the 2D environment

I have created three different motions in this project. 
1. Linear Motion (xmovement.py)
2. Rotational Motion
3. Moving to a user input point

The 1 and 2 can be done simply assigning the velcoity, angular velocity, 
distance and angular distance values input by the user to the relevant variable. 

but to move the robot to a specified position. Proportional 
controller has been used
1. linear velocity V^*= K_v √(〖(x^*-x)〗^2+〖(y^*-y)〗^2 )
2. steering anle 〖theta〗^x= 〖tan〗^(-1)   (y^*-y)/(x^*-x)
3. proportional controller gemma = constant * (theta)*
   
