#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

RATE= 10
#Robot velociy
LIN_VEL = 0.2
#Reqired distance
distance= 1

class MoveForward:
    def __init__(self):
        #intializing the publisher
        self.cmd_pub=rospy.Publisher("/cmd_vel",Twist, queue_size=0)
        self.rate=rospy.Rate(RATE)

    def spin(self):
        #set up a twist message
        vel_msg= Twist()
        #set up the linear velocity of the robot to 0.2 m/sec
        vel_msg.linear.x=LIN_VEL
        #publishing the velocity message
        self.cmd_pub.publish(vel_msg)
        #start time of the robot
        t0 = rospy.Time.now().to_sec()
        #current distance of the robot
        current_distance = 0
        #Keep the robot on move until it reaches the required distance
        while(current_distance < distance):
            t1=rospy.Time.now().to_sec()
            current_distance= LIN_VEL*(t1-t0)
        #Stop the robot when it reaches the ultimate goal
        vel_msg.linear.x=0
        #Publish the zero velocity to stop the robot
        self.cmd_pub.publish(vel_msg)
        #wait in this while loop until termination
        while not rospy.is_shutdown():
            self.rate.sleep()

if __name__ == "__main__":
    #initialize a node to move forward
    rospy.init_node("move_forward")
    #Create an object from the MoveForward class
    r=MoveForward()
    #Sleep for 2 sec after the initialization step and before the excution
    rospy.sleep(2)
    r.spin()
