#!/bin/python3

import os
import rospy
import pcl
import ros_numpy
import cv2
from sensor_msgs.msg import PointCloud2, Image
from cv_bridge import CvBridge

# Constants
SAVE_FOLDER = "pcl_img_pairs_may2nd"
MAX_PAIRS = 15

# Global variables
pair_counter = 1
bridge = CvBridge()
point_cloud_data = None
image_data = None

# Callback for receiving point cloud data
def point_cloud_callback(msg):
    global pair_counter, point_cloud_data, image_data
    if pair_counter > MAX_PAIRS:
        rospy.loginfo("Reached maximum number of pairs. Exiting...")
        rospy.signal_shutdown("Maximum pairs reached")
        return

    if image_data is not None:
        filename = f'pair_{pair_counter}'
        point_cloud_filename = f'{filename}.pcd'
        image_filename = f'{filename}.png'

        # Process and save point cloud
        pc_data = pcl.PointCloud()
        points = ros_numpy.point_cloud2.pointcloud2_to_array(msg)
        pc_data.from_list([(p['x'], p['y'], p['z']) for p in points])
        pcl.save(pc_data, os.path.join(SAVE_FOLDER, point_cloud_filename))

        # Process and save image in RGB format
        cv_image = bridge.imgmsg_to_cv2(image_data, desired_encoding='bgr8')
        cv2.imwrite(os.path.join(SAVE_FOLDER, image_filename), cv_image)

        # Increment pair counter
        pair_counter += 1

        # Reset image data
        image_data = None

# Callback for receiving image data
def image_callback(msg):
    global image_data
    image_data = msg

    # Inspect image properties
    print("Image Encoding:", image_data.encoding)
    print("Image Height:", image_data.height)
    print("Image Width:", image_data.width)

# Initialize ROS node
rospy.init_node('pcl_img_save_node', anonymous=True)

# Subscribe to point cloud and image topics
rospy.Subscriber('/cepton/points', PointCloud2, point_cloud_callback)
rospy.Subscriber('/usb_cam/image_raw', Image, image_callback)

# Create PCL save folder if it doesn't exist
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

# Spin
rospy.spin()
