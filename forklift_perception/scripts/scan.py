#!/usr/bin/env python3

# import rospy
import cv2 as cv
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge
import numpy as np
# from std_msgs.msg import Int16

GREEN = '\033[92m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'
YELLOW = '\033[93m'

feed = None

# def callback(data):
#     global feed
#     feed = data.data

def main():
    # global img_store
    # rospy.init_node('perception')
    # pub = rospy.Publisher("Destination", Int16, queue_size=10) 
    # rospy.Subscriber("Destination", Int16, callback)
    video = cv.VideoCapture(0)
            # load the dictionary that was used to generate the markers
    dictionary = cv.aruco.Dictionary_get(cv.aruco.DICT_4X4_1000)

    # initializing the detector parameters with default values
    parameters =  cv.aruco.DetectorParameters_create()
    # rate = rospy.Rate(20)

    # while not rospy.is_shutdown():
    # while not rospy.is_shutdown():
    while True:

        ret, frame = video.read()
        corners, ids, rejectedCandidates = cv.aruco.detectMarkers(frame, dictionary, parameters=parameters)
        # msg = Int16()
        if ids:
            # msg.data = int(ids[0][0])
            print(f' {GREEN} {BOLD} {UNDERLINE} QR Scan Complete. Scanned ID: {ids} {END}')
            # pub.publish(msg)
            # rospy.sleep(0.5)
            

        # rate.sleep()

        

if __name__ == "__main__":
    main()