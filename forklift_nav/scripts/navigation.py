#!/usr/bin/env python3

# Import the necessary libraries

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import *
import std_msgs

# Colour codes for logging
GREEN = '\033[92m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'
YELLOW = '\033[93m'

coordinates = [[3.45, 5.50, -0.00, 0, 0.70433, 0.70986],
[1.18, 5.95,-0.00, 0, 0.70433, 0.70986],
[-0.466, 5.50,-0.00, 0, 0.70433, 0.70986],
# [3.45, 5.50, -0.00, -8.24, 0.70433, 0.70986]
]

feed = None

def destination_callback(data):
    global feed
    feed = data.data

def nav():
    global feed
    '''
    Uses the waypoint to take the Agribot to across the greenhouse.
    Also updates the manipulation node.
    '''

    rospy.init_node('navigation', anonymous=True)  # Node Initialisation

    nav = rospy.Publisher(
        'Destination', std_msgs.msg.Int16,
        queue_size=10)  # Navigation Feedback: Whether Agribot is stationary
        

    dest_msg = std_msgs.msg.Int16()  # Navigation feedback msg

    rospy.Subscriber(
        'Destination', std_msgs.msg.Int16,
        destination_callback)  # Subscriber for returning feedback from manipulation

    ac = actionlib.SimpleActionClient(
        'move_base', MoveBaseAction)  # Starting move_base action client

    while (not ac.wait_for_server(rospy.Duration(5))):
        rospy.loginfo(
            f' {YELLOW} {BOLD} {UNDERLINE}  WAITING FOR THE SERVER TO START {END}'
        )  # Wait until the server is ready.

    rate = rospy.Rate(5)  # 10Hz

    goal = MoveBaseGoal()

    idx = 0  # Index

    goal.target_pose.header.frame_id = 'map'  # Frame Id
    goal.target_pose.header.stamp = rospy.Time.now()

    dest_msg.data = 0


    rospy.loginfo(f' {GREEN} {BOLD} {UNDERLINE} Started Run! {END}')

    while not rospy.is_shutdown():
        nav.publish(dest_msg)
        # print(feed)
        try:
            if (type(feed)) == int and (feed > 0):

                rospy.loginfo(f' {GREEN} {BOLD} {UNDERLINE} Package Ready! {END}')
                print(feed)

                # Position
                if feed == 0:
                    feed = 3
                goal.target_pose.pose.position.x = coordinates[int(feed-1)][0]
                goal.target_pose.pose.position.y = coordinates[int(feed-1)][1]
                goal.target_pose.pose.position.z = 0.1

                # Orientation
                goal.target_pose.pose.orientation.x = coordinates[int(feed-1)][2]
                goal.target_pose.pose.orientation.y = coordinates[int(feed-1)][3]
                goal.target_pose.pose.orientation.z = coordinates[int(feed-1)][4]
                goal.target_pose.pose.orientation.w = coordinates[int(feed-1)][5]

                # Sending goal to server
                ac.send_goal(goal)
                ac.wait_for_result(rospy.Duration(120))  # Wait for 60sec

                
                print(ac.get_goal_status_text())
                if (ac.get_state() == GoalStatus.SUCCEEDED):
                    dest_msg.data = 0
                    nav.publish(dest_msg)  # Update to manipulation node
                    rospy.loginfo(f' {GREEN} {BOLD} {UNDERLINE} Package Delivered!!! {END}')
                    rospy.sleep(0.5)
                    rospy.signal_shutdown("Done Code")
                    

                else:
                    rospy.loginfo(
                        f" {GREEN} {BOLD} {UNDERLINE}  THE BOT DIDN'T REACH ITS DESTINATION, RETRYING {END}"
                    )

                
        except:
            raise

    rate.sleep()


if __name__ == "__main__":
    nav()
