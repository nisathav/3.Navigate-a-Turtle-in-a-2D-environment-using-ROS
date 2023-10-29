#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist #find this using ros2 topic info /turtle1/cmd_vel
from rclpy.clock import Clock


class moveforward(Node):

    def __init__(self):
        super().__init__("x_movement") #node name
        #initialize publisher
        self.cmd_vel_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        #user input
        self.get_logger().info("Receving the user's input:")
        self.vel_= float(input("Input speed:"))
        self.distance_ = int(input("Type your distance:"))
        self.isForward_ = input("Foward?: ")#True or False

        #self.timer_ = self.create_timer(0.5,self.send_velocity_command)
        self.send_velocity_command()
        #print to screen
        self.get_logger().info("Movement in x-direction has been initiated")

    def send_velocity_command(self):
        msg = Twist()
        #use the following to find what to sent, ros2 interface show geometry_msgs/msg/Twist
        #Checking if the movement is forward or backwards
        if(self.isForward_ == "T"):
            msg.linear.x = self.vel_
        else:
            msg.linear.x = -(self.vel_)

        self.current_distance_ = 0
        while rclpy.ok():

        #Setting the current time for distance calculus
            t0 = self.get_clock().now()
            t0 = float(t0.nanoseconds/1e9)
            while(self.current_distance_ < self.distance_):
                #Publish the velocity
                self.cmd_vel_.publish(msg)
                #Takes actual time to velocity calculus
                t1= self.get_clock().now()
                t1 = float(t1.nanoseconds/1e9)
                #Calculates distancePoseStamped
                self.current_distance_= self.vel_* (t1-t0)
                self.get_logger().info("%.4f" %self.current_distance_)
            #After the loop, stops the robot
            msg.linear.x = 0.0
            #Force the robot to stop
            self.cmd_vel_.publish(msg)
            

def main(args=None):
    rclpy.init(args=args)
    node = moveforward()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()              
