# Wifibot WS (ROS 2 Humble)

这是一个基于 **NVIDIA Jetson AGX Orin** 和 **ROS 2 Humble** 移动机器人开发的工作空间。项目集成了 **Wifibot 四驱底盘驱动** 以及 **Stereolabs ZED 2i 双目深度相机**，实现了基于视觉里程计（Visual Odometry）与 RTAB-Map 的 2D 平面栅格地图构建（SLAM），为后续的 Nav2 自主导航巡航提供底层基础。

---

## 🛠️ 硬件架构与依赖
- **移动底盘**: Wifibot 4WD 机器人底盘 (通过 `/dev/ttyUSB0` 串口通信)
- **主控芯片**: NVIDIA Jetson AGX Orin
- **传感器**: Stereolabs ZED 2i 深度相机 (依赖 ZED SDK v4.x 及 CUDA 驱动)
- **操作系统**: Ubuntu 22.04 LTS
- **ROS 版本**: ROS 2 Humble Hawksbill

---

## 📦 工作空间结构

```text
wifibot_ws/
└── src/
    ├── wifibot_control/       # Wifibot 底盘串口驱动、状态反馈与控制节点
    ├── zed_components/       # ZED 相机底层核心组件
    ├── zed_wrapper/          # ZED 相机 ROS 2 官方标准封装层
    └── zed_ros2/             # ZED 接口与自定义消息类型

🚀 编译与环境部署
1. 补齐系统依赖
在首次克隆此工作空间后，请先确保安装了必要的 SLAM 基础组件：
Bash
sudo apt update
sudo apt install -y ros-humble-rtabmap-ros ros-humble-nav2-map-server ros-humble-teleop-twist-keyboard


2. 编译工作空间
在工作空间根目录下，使用 colcon 进行符号链接编译：
Bash
cd ~/wifibot_ws
colcon build --symlink-install --cmake-args=-DCMAKE_BUILD_TYPE=Release

🎬 运行与实时 2D 建图指南
为了在实验室 Wi-Fi 环境下实现多端或单端稳定通信，项目统一锁定了网络通信频段：
Bash
export ROS_DOMAIN_ID=0

步骤 1：启动小车底盘硬件串口节点 (终端 1)
确保底盘已上电并连接 USB 串口线，赋予权限后运行：
Bash
sudo chmod 777 /dev/ttyUSB0
source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash
export ROS_DOMAIN_ID=45
ros2 run wifibot_control wifibot_node

步骤 2：启动 ZED 2i 深度相机驱动 (终端 2)
相机初次启动时，ZED SDK 将自动调用 TensorRT 核心进行后台神经网络模型（NEURAL LIGHT 模式）的编译与硬件加速优化，请耐心等待至日志输出 SUCCESS。
Bash
source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash
export ROS_DOMAIN_ID=45
ros2 launch zed_wrapper zed_camera.launch.py \
  camera_model:=zed2i \
  publish_tf:=true \
  pos_tracking.publish_tf:=false \
  pos_tracking.publish_map_tf:=false \
  odom_frame:="zed_unused_odom"

步骤 3：开启 RTAB-Map 建图与可视化大屏 (终端 3)
此命令通过将 ZED 2i 采集到的 3D 稠密点云在内部实时切片投影，直接输出用于自主巡航的 2D 栅格地图（Occupancy Grid），同时联动唤醒 RViz2。
Bash
source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash
export ROS_DOMAIN_ID=45

ros2 launch rtabmap_launch rtabmap.launch.py \
  rgb_topic:=/zed/zed_node/rgb/image_rect_color \
  depth_topic:=/zed/zed_node/depth/depth_registered \
  camera_info_topic:=/zed/zed_node/rgb/camera_info \
  odom_topic:=/odom \
  visual_odometry:=false \
  subscribe_odom:=true \
  subscribe_odom_info:=false \
  frame_id:=base_link \
  odom_frame_id:=odom \
  approx_sync:=true \
  approx_sync_max_interval:=0.3 \
  topic_queue_size:=50 \
  sync_queue_size:=50 \
  qos:=2 \
  Grid/3D:=false \
  rviz:=true \
  rtabmap_viz:=false \
  rtabmap_args:="--delete_db_on_start --RGBD/LinearUpdate 0.05 --RGBD/AngularUpdate 0.05 --wait_for_transform 0.8 --Mem/DepthCompressionFormat .png"
💡 RViz2 查看配置：由于 RTAB-Map 采用持久化 QoS 历史策略，请在 RViz2 添加 Map 显示项后，将 Topic 强制指定为 /rtabmap/map，并把其属性中的 Durability Policy 改为 Transient Local。

步骤 4：键盘遥控小车扫描地图 (终端 4)
保持在该终端视窗内，使用 i, ,, j, l 键慢速平稳遥控小车移动，直至周围环境的黑白线条闭合拼装完毕。
Bash
source /opt/ros/humble/setup.bash
export ROS_DOMAIN_ID=45
ros2 run teleop_twist_keyboard teleop_twist_keyboard
