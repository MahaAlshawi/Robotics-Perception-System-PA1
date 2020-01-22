There is two python scripts in this project. The first is PA1_a which moves the robot a specific distance which is (1 meter in this case), and the second is to subscribe to the robot pose and then publish it to the Marker Topic. We then can visualize the x and y movements of the robot in rviz.

Steps that you need to do to run these scripts:

1- Add the first_programming_assignment package to src folder in your rosbot's catkin workspace.

2- Then Catkin_make while you are in catkin_ws folder in terminal. Don't forget to source devel/setup.bash while you are in catkin_ws.

3- Run: roscore in a new screen in rosbot.

4- Run: rosrun rosbot_webui serial_bridge.sh in another screen.

5- In another screen, run rosrun first_programming_assignment PA1-a.py     or     run rosrun first_programming_assignment PA1-b.py depending on whether you want to run the first script or the second one.
