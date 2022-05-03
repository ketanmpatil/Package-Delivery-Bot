#!/usr/bin/env python3

# Import the necessary libraries

import rospy  # Python library for ROS
from sensor_msgs.msg import Image  # Image is the message type
from cv_bridge import CvBridge  # Package to convert between ROS and OpenCV Images
import cv2  # OpenCV library
import numpy as np
import pytesseract
import tf2_ros
import tf_conversions
import geometry_msgs
from std_msgs.msg import Int16
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

redLower = (0, 12, 12)
redUpper = (0, 213, 225)

cy = 240.5  # cy and cx are coordinates for center of camers
cx = 320.5
f = 554.387  # Focal length

img = None
dpt = None

# Colour codes for logging
GREEN = '\033[92m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

br = CvBridge()

broadcaster = tf2_ros.TransformBroadcaster()


def img_callback(msg):  # RGB Image callback function
    global img
    img = br.imgmsg_to_cv2(msg, 'bgr8')
    img = np.array(img)

def main():

    count_feed = rospy.Publisher(
        'perception', Int16,
        queue_size=10)  # Publisher node to publish count of tomatoes

    rospy.Subscriber("/image_raw", Image,
                     img_callback)  # Subscribe to camera topics

    # rate = rospy.Rate(10)  # 10Hz

    rospy.loginfo(
        f' {GREEN} {BOLD} {UNDERLINE}  Image Feed Recieved.... {END}')
    count_tom = Int16()
	
	while not rospy.is_shutdown():
		if (type(img) == np.ndarray) and (type(dpt) == np.ndarray):
			try:
				pass
			except:
				pass
if __name__ == '__main__':
    rospy.init_node('perception',
                    anonymous=True)  # "perception" node initilization

    main()