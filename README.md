# PARC-Engineers-League
PARC Engineer's League Competition Package

# Setup
### Setup ROS workspace
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
```

### Clone the repository
```
cd ~/catkin_ws/src
git clone --recurse-submodules https://github.com/PARC-Robotics/PARC-Engineers-League.git
```
Or if you already have cloned the repo without submodules, run command `git submodule update --init --recursive` to update them.

### Install dependencies
```
cd ~/catkin_ws
sudo apt update
rosdep install --from-paths ./src --ignore-src -y
```

### Compile
```
cd ~/catkin_ws
catkin_make
```

**NOTE:** There is a known issue while compiling, ` Intel RealSense SDK 2.0 is missing`
To solve, update the file `realsense-ros/realsense_camera/CMakeLists.txt`,line: 43 to `find_package(realsense2 2.36.0)`
i.e. downgrade the required version of `realsense2` to `2.36.0`


## Run
### Task 1
Run the following command in one Terminal
```
source ~/catkin_ws/devel/setup.bash
roslaunch parc-robot task1.launch
```

And Run the following command in another terminal
```
source ~/catkin_ws/devel/setup.bash
roslaunch parc-robot teleop.launch
```

Now keeping the second terminal on top (teleop.launch) press `i` to move the robot forward, you can see the robot moving in "RViz" and "Gazebo" windows.
you can use the keys shown below to move the robot and `k` key to stop the movement.
```
Moving around:
   u    i    o
   j    k    l
   m    ,    .
```
