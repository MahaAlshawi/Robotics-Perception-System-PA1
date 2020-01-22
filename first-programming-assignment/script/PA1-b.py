#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from visualization_msgs.msg import Marker
RATE= 10

class PlotState:
    def __init__(self):
        #Initialize a publisher
        self.marker_pub=rospy.Publisher("visualization_marker",Marker, queue_size=0)
        #Initialize a subscriber to read the x and y distance that the robot already moved
        self.scan_sub=rospy.Subscriber("/pose", PoseStamped, self.pose_callback, queue_size=1)
        #Set up rate for rospy
        self.rate=rospy.Rate(RATE)
        #Create a Marker object
        self.marker=Marker()

    def pose_callback(self, msg):
        #Set up all the information you need for the Marker topic
        self.marker.header.frame_id="odom"
        #This is an id to identify this Marker object
        self.marker.id=0
        #These are the x and y positions of the robot, read them from the pose topic and publish them to the Marker topic
        self.marker.pose.position.x=msg.pose.position.x
        self.marker.pose.position.y=msg.pose.position.y
        #Set up a scale for x,y and z coordinates
        self.marker.scale.x=1
        self.marker.scale.y=1
        self.marker.scale.z=1
        #Set up a color for the Marker
        self.marker.color.a=1
        #Choose the stamp to be the current time
        self.marker.header.stamp=rospy.Time.now()
        #Choose the Marker shape to be SPHERE
        self.marker.type=Marker.SPHERE
        self.marker.action=Marker.ADD
        #publish the marker object with all information set up
        self.marker_pub.publish(self.marker)

    def spin(self):
        #wait in this while loop until termination
        while not rospy.is_shutdown():
            self.rate.sleep()

if __name__ == "__main__":
        #Initiaizing a node for plotting
        rospy.init_node("plot")
        #Create an object of the PlotState class
        x=PlotState()
        #Sleep for a while before executing
        rospy.sleep(2)
        #The actual execution
        x.spin()
