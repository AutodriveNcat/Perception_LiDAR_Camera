# Perception_LiDAR_Camera
To install LiDAR drivers do the following:

1- Make an empty foler and an emtpy src fodler inside of it.

2- Inside the src folde, clone their repository using the following command:

  git clone https://github.com/ceptontech/cepton_sdk_redist.git
  
3- Inside the cepton_sdk_redist folder, open the "CMakeLists.txt" file and edit line 13 to be the following:

  set(CMAKE_CXX_STANDARD 14)

4- In the file "cepton_sdk_util.inc" located in cepton_sdk_redist/ros/third_party/cepton_sdk/include/cepton_sdk_impl comment lines 114-117, the part about VISTA_X15 

5- Now go abck to the main folder (the one that contains the src folder) and run the following command:

  catkin_make

6- If there are errors in the command line, stop the execution (ctrl + c) and read the error. It is possible that you will need to repeat step 4 and comment a different part of the file

7- Now you are ready to use the drivers.


To use the drivers and start getting data from the LiDAR, opena terminal and use the following commadn to start the ROS master:

  roscore

Then in a different terminal, run the following command:

  roslaunch cepton_ros demo.launch

Now you should be recieving the data from the LiDAR
