🤖 ROS 2 Humble WiFibot Indoor Autonomous Driving Simulation / Simulation de Conduite Autonome d'Intérieur pour WiFibot
🇨🇳 中文简介

本项目是一个基于 ROS 2 Humble 的室内移动机器人自动驾驶仿真系统。系统以 WiFibot 小车为底层平台，在 Gazebo 物理仿真环境中搭建了简易室内场景，并集成了 ZED2i 深度相机 的全功能传感器模拟。

系统核心特性包括：

    纯视觉定位与建图 (Pure Visual SLAM)： 基于 RTAB-Map 仅使用视觉信息进行室内环境的建图与高精度定位。

    自主路径规划 (Autonomous Path Planning)： 在简易环境中实现全局自主路线规划。

    路径跟随与局部避障 (Path Following & Local Obstacle Avoidance)： 通过自定义的路径跟随算法，结合传感器实时检测障碍物，实现动态重规划（Re-planning）与安全局部避障。

🇫🇷 Introduction en Français

Ce projet est un système de conduite autonome en intérieur pour robot mobile, développé sous ROS 2 Humble. Il utilise le robot WiFibot comme plateforme matérielle de base dans un environnement de simulation physique Gazebo (environnement intérieur simplifié), avec une simulation complète de la caméra de profondeur ZED2i.

Les principales fonctionnalités du système comprennent :

    SLAM Visuel Pur (Pure Visual SLAM) : Utilisation de RTAB-Map exploitant uniquement les données visuelles pour la cartographie et la localisation en intérieur.

    Planification de Trajectoire Autonome : Calcul d'itinéraires globaux autonomes dans l'environnement.

    Suivi de Trajectoire et Évitement d'Obstacles Locaux : Implémentation d'un algorithme de suivi de chemin associé à une détection d'obstacles en temps réel, permettant la replanification dynamique de trajectoire et l'évitement d'obstacles locaux.

系统架构 / Architecture du Système

    OS & Framework : Ubuntu Linux + ROS 2 Humble

    Simulation : Gazebo (Simulated Indoor Environment)

    Robot : WiFibot (Differential / Mobile Base)

    Sensor : ZED2i Stereo / Depth Camera (RGB-D)

    Core Stack : RTAB-Map (Visual SLAM), Custom A* / Path Planning, Path Follower, Dynamic Re-planning & Local Avoidance.


    💻 系统环境 / Environnement Système

本项目在以下开发与测试环境中验证通过：

    操作系统 / OS : Ubuntu 22.04.5 LTS (Jammy Jellyfish)

    ROS 2 版本 / Version ROS 2 : Humble Hawksbill

    仿真平台 / Simulateur : Gazebo 11.10.2

    编程语言 / Langage : Python 3.10.12

    🇨🇳 中文说明

为了确保项目能够正常编译和运行，建议在相同或兼容的软件版本下进行配置（尤其是 Ubuntu 22.04 配合 ROS 2 Humble）。
🇫🇷 Description en Français

Pour garantir le bon fonctionnement et la compilation du projet, il est fortement recommandé d'utiliser une configuration logicielle similaire ou compatible (en particulier Ubuntu 22.04 avec ROS 2 Humble).


📥 ROS 2 Humble 安装与验证 / Installation et Vérification de ROS 2 Humble
🇨🇳 中文说明

如果你是在全新系统上复现本项目，请按照以下标准步骤安装 ROS 2 Humble：
1. 设置本地语言环境

确保系统支持 UTF-8 编码：
Bash

locale  # 检查当前语言设置
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

2. 配置软件源与仓库

启用 Universe 软件源并添加 ROS 2 官方 GPG 密钥：
Bash

sudo apt install software-properties-common curl -y
sudo add-apt-repository universe
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

3. 安装 ROS 2 Humble 桌面版与开发工具

更新并安装桌面版及编译扩展工具：
Bash

sudo apt update && sudo apt upgrade -y
sudo apt install ros-humble-desktop python3-colcon-common-extensions python3-pip ros-humble-ros2cli-common-extensions -y

4. 设置环境变量

将 ROS 2 环境永久写入终端配置文件：
Bash

echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc

5. 验证安装

打开两个终端分别运行发布者和接收者测试通信：

    终端 A (Publisher)： ros2 run demo_nodes_cpp talker

    终端 B (Subscriber)： ros2 run demo_nodes_py listener

🇫🇷 Description en Français

Si vous configurez ce projet sur un système entièrement neuf, veuillez suivre ces étapes pour installer ROS 2 Humble :
1. Configuration de la locale
Bash

locale
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

2. Configuration des sources et dépôts
Bash

sudo apt install software-properties-common curl -y
sudo add-apt-repository universe
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

3. Installation de ROS 2 Humble Desktop et des outils de développement   
Bash

sudo apt update && sudo apt upgrade -y
sudo apt install ros-humble-desktop python3-colcon-common-extensions python3-pip ros-humble-ros2cli-common-extensions -y

4. Configuration de l'environnement
Bash

echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc

5. Vérification de l'installation

    Terminal A : ros2 run demo_nodes_cpp talker

    Terminal B : ros2 run demo_nodes_py listener


🌐 Gazebo Classic 11 与 ROS 2 桥接安装与验证 / Installation et Vérification de Gazebo Classic 11 et du Pont ROS 2
🇨🇳 中文说明

本项目依赖 Gazebo Classic 11 进行物理仿真。请按照以下步骤安装 Gazebo 及其与 ROS 2 Humble 的集成桥接包：
1. 安装 Gazebo Classic 11 主程序与开发库

更新系统并安装 Gazebo 11：
Bash

sudo apt update && sudo apt upgrade -y
sudo apt install gazebo libgazebo11 libgazebo-dev -y

2. 安装 ROS 2 与 Gazebo Classic 的集成桥接包

安装接口包以实现 ROS 2 与 Gazebo 的通信：
Bash

sudo apt install ros-humble-gazebo-ros-pkgs ros-humble-gazebo-dev -y

3. 验证安装是否成功

    验证独立运行（图形界面）：
    在终端中输入 gazebo，应成功弹出 3D 图形仿真界面且无报错。

    验证 ROS 2 桥接功能：
    运行空世界仿真：
    Bash

    ros2 launch gazebo_ros empty_world.launch.py

    打开新终端运行 ros2 node list，若输出 /gazebo 节点，说明桥接成功。

🇫🇷 Description en Français

Ce projet utilise Gazebo Classic 11 pour la simulation physique. Suivez les étapes ci-dessous pour installer Gazebo et ses composants de liaison avec ROS 2 Humble :
1. Installation de Gazebo Classic 11 et des bibliothèques de développement
Bash

sudo apt update && sudo apt upgrade -y
sudo apt install gazebo libgazebo11 libgazebo-dev -y

2. Installation du pont d'intégration ROS 2 et Gazebo Classic
Bash

sudo apt install ros-humble-gazebo-ros-pkgs ros-humble-gazebo-dev -y

3. Vérification de l'installation

    Vérification de l'interface graphique :
    Tapez gazebo dans le terminal. L'interface 3D doit s'ouvrir sans erreur.

    Vérification du pont ROS 2 :
    Lancez le monde vide :
    Bash

    ros2 launch gazebo_ros empty_world.launch.py

    Ouvrez un nouveau terminal et exécutez ros2 node list. Si le nœud /gazebo apparaît, la liaison est réussie.


为你将 Python 3.10.12 的安装与验证 部分也整理成了规范的中法双语对照版，可以直接接在前面的 Gazebo 安装指南后面：
中文 / Français
🐍 Python 3.10.12 安装与验证 / Installation et Vérification de Python 3.10.12
🇨🇳 中文说明

Ubuntu 22.04 原生支持 Python 3.10。如果需要重新安装、修复或指定安装到 Python 3.10.12 精确版本，推荐使用官方维护的 deadsnakes PPA 仓库：
1. 更新系统软件源
Bash

sudo apt update && sudo apt upgrade -y

2. 添加 Python 专用 PPA 仓库 (deadsnakes)
Bash

sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

3. 安装 Python 3.10.12 及其组件与 pip
Bash

sudo apt install python3.10 python3.10-dev python3.10-venv python3.10-distutils -y
curl -sS https://bootstrap.pypa.io/get-pip.py | sudo python3.10

4. 验证安装

    验证版本号： python3.10 --version（应输出 Python 3.10.12）

    验证 pip 绑定： python3.10 -m pip --version

🇫🇷 Description en Français

Ubuntu 22.04 intègre nativement Python 3.10. Si vous devez réinstaller, réparer ou cibler précisément la version Python 3.10.12, il est recommandé d'utiliser le dépôt PPA officiel deadsnakes :
1. Mise à jour des sources du système
Bash

sudo apt update && sudo apt upgrade -y

2. Ajout du dépôt PPA dédié à Python (deadsnakes)
Bash

sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

3. Installation de Python 3.10.12, de ses composants et de pip
Bash

sudo apt install python3.10 python3.10-dev python3.10-venv python3.10-distutils -y
curl -sS https://bootstrap.pypa.io/get-pip.py | sudo python3.10

4. Vérification de l'installation

    Vérification de la version : python3.10 --version (doit afficher Python 3.10.12)

    Vérification de pip : python3.10 -m pip --version


🗺️ RTAB-Map 视觉 SLAM 安装与验证 / Installation et Vérification de RTAB-Map (SLAM Visuel)
🇨🇳 中文说明

针对本项目使用的 ROS 2 Humble 环境，推荐通过 apt 直接安装官方维护的 rtabmap 二进制套件：
1. 更新本地软件源缓存

在安装前确保系统的包列表是最新的：
Bash

sudo apt update

    验证方法： 命令执行无网络或源错误，正常结束。

2. 一键安装 RTAB-Map 全套二进制组件

安装核心库、ROS 2 封装节点、可视化工具及 RViz 插件：
Bash

sudo apt install ros-humble-rtabmap ros-humble-rtabmap-ros ros-humble-rtabmap-viz -y

    验证方法： 安装过程无报错，所有依赖包均成功下载并解压。

3. 验证安装结果

    检查包列表：
    Bash

    dpkg -l | grep rtabmap

    验证标准：能够输出形如 ros-humble-rtabmap 等一系列以 ii 开头的软件包信息。

    独立启动可视化界面：
    确保已经加载 ROS 2 环境后运行：
    Bash

    source /opt/ros/humble/setup.bash
    rtabmap-viz

    验证标准：成功弹出 RTAB-Map 的独立图形界面 (Standalone GUI)。

🇫🇷 Description en Français

Pour l'environnement ROS 2 Humble utilisé dans ce projet, il est recommandé d'installer directement les suites binaires officielles de rtabmap via apt :
1. Mise à jour du cache des sources locales
Bash

sudo apt update

    Méthode de vérification : La commande s'exécute sans erreur réseau ni de source.

2. Installation des composants binaires complets de RTAB-Map
Bash

sudo apt install ros-humble-rtabmap ros-humble-rtabmap-ros ros-humble-rtabmap-viz -y

    Méthode de vérification : Installation sans erreur, tous les paquets sont téléchargés et décompressés avec succès.

3. Vérification du résultat de l'installation

    Vérification de la liste des paquets :
    Bash

    dpkg -l | grep rtabmap

    Critère : Affiche les informations des paquets commençant par ii (ex. ros-humble-rtabmap).

    Lancement de l'interface graphique :
    Après avoir chargé l'environnement ROS 2 :
    Bash

    source /opt/ros/humble/setup.bash
    rtabmap-viz

    Critère : L'interface graphique indépendante (GUI) de RTAB-Map s'ouvre avec succès.


📋 项目依赖 / Dépendances du Projet
🇨🇳 中文说明

本项目正常运行需要以下 Python 扩展库和 ROS 2 系统功能包支持：
1. Python 依赖库

通过 pip 安装项目所需的 Python 核心计算与图像处理库：
Bash

pip install numpy opencv-python pyyaml


2. ROS 2 Humble 系统功能包

通过 apt 安装项目所需的 ROS 2 消息与桥接组件：
Bash

sudo apt update
sudo apt install \
  ros-humble-cv-bridge \
  ros-humble-geometry-msgs \
  ros-humble-nav-msgs \
  ros-humble-sensor-msgs \
  ros-humble-launch-ros -y

🇫🇷 Description en Français

Le bon fonctionnement de ce projet nécessite les bibliothèques Python et paquets ROS 2 suivants :
1. Dépendances Python

Installez les bibliothèques de calcul et de traitement d'image via pip :
Bash

pip install numpy opencv-python pyyaml


2. Paquets système ROS 2 Humble

Installez les paquets de messages et composants nécessaires via apt :
Bash

sudo apt update
sudo apt install \
  ros-humble-cv-bridge \
  ros-humble-geometry-msgs \
  ros-humble-nav-msgs \
  ros-humble-sensor-msgs \
  ros-humble-launch-ros -y


📥 仓库下载与进入 / Clonage et Accès au Dépôt
🇨🇳 中文说明

打开终端，运行以下命令将本项目从 GitHub 克隆到本地，并进入工作空间根目录：
Bash

git clone https://github.com/BadMan987/wifibot_ws.git
cd wifibot_ws

🇫🇷 Description en Français

Ouvrez un terminal et exécutez la commande suivante pour cloner ce projet depuis GitHub sur votre machine locale, puis accédez au répertoire racine de l'espace de travail :
Bash

git clone https://github.com/BadMan987/wifibot_ws.git
cd wifibot_ws



🏗️ 工作空间编译 / Compilation de l'Espace de Travail
🇨🇳 中文说明

进入工作空间根目录，使用 colcon 工具进行编译。推荐加上 --symlink-install 参数，这样修改 Python 脚本或配置文件后无需重新编译即可直接生效：
Bash

cd ~/wifibot_ws
colcon build --symlink-install
source install/setup.bash

🇫🇷 Description en Français

Accédez au répertoire racine de l'espace de travail et compilez le projet à l'aide de l'outil colcon. L'utilisation du paramètre --symlink-install est recommandée, car elle permet de prendre en compte les modifications apportées aux scripts Python ou aux fichiers de configuration sans avoir à recompiler à chaque fois :
Bash

cd ~/wifibot_ws
colcon build --symlink-install
source install/setup.bash


🚀 启动仿真 / Lancement de la Simulation
🇨🇳 中文说明

在编译完成后，首先确保加载了 ROS 2 Humble 环境以及当前工作空间的环境变量，然后运行 Gazebo 仿真启动脚本：
Bash

source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash

ros2 launch wifibot_gazebo simulation.launch.py

🇫🇷 Description en Français

Une fois la compilation terminée, assurez-vous de charger l'environnement ROS 2 Humble ainsi que les variables d'environnement de votre espace de travail, puis lancez le script de simulation Gazebo :
Bash

source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash

ros2 launch wifibot_gazebo simulation.launch.py

<img width="1850" height="1053" alt="image" src="https://github.com/user-attachments/assets/c5daead3-fe3c-4a63-a9ab-229ae9d40f8d" />



💾 地图数据库配置与重置 / Configuration et Réinitialisation de la Base de Données de la Carte
🇨🇳 中文说明
1. 网盘下载 rtabmap.db

由于地图数据库文件 (rtabmap.db) 体积较大（通常达数 GB），因此未直接包含在本 Git 仓库中。你可以通过以下链接下载：

    Google Drive 下载地址： (https://drive.google.com/file/d/10x52tCdV76HGq51t29f5NSDp7LCilcUf/view?usp=sharing)点击此处下载 rtabmap.db

    放置路径： 下载完成后，请将 rtabmap.db 文件放置于工作空间的 src/wifibot_patrol/maps/indoor/ 目录下。

2. 制作与使用 rtabmap_clean.db（防止地图污染）

为了防止在后续测试中地图被错误修改或污染，建议保留一个干净的原始数据库副本 rtabmap_clean.db：

    制作方法： 将下载好的 rtabmap.db 复制一份并粘贴在同目录下，重命名为 rtabmap_clean.db。

    重置命令： 每次开始新的定位或测试前，执行以下命令用干净的模板覆盖主数据库：
    Bash

    cp ~/wifibot_ws/src/wifibot_patrol/maps/indoor/rtabmap_clean.db ~/wifibot_ws/src/wifibot_patrol/maps/indoor/rtabmap.db

🇫🇷 Description en Français
1. Téléchargement de rtabmap.db via Google Drive

Étant donné que le fichier de base de données de la carte (rtabmap.db) est volumineux (plusieurs Go), il n'est pas inclus directement dans ce dépôt Git. Vous pouvez le télécharger via le lien ci-dessous :

    Lien Google Drive : (https://drive.google.com/file/d/10x52tCdV76HGq51t29f5NSDp7LCilcUf/view?usp=sharing)Cliquez ici pour télécharger rtabmap.db

    Emplacement : Placez le fichier téléchargé dans le répertoire src/wifibot_patrol/maps/indoor/ de votre espace de travail.

2. Création et Utilisation de rtabmap_clean.db (Éviter la corruption de la carte)

Pour éviter que la carte ne soit corrompue lors des tests, il est recommandé de conserver une copie propre originale nommée rtabmap_clean.db :

    Méthode de création : Copiez le fichier rtabmap.db, collez-le dans le même dossier et renommez-le en rtabmap_clean.db.

    Commande de réinitialisation : Avant chaque nouveau test ou localisation, exécutez la commande suivante pour écraser la base de données principale avec le modèle propre :
    Bash

    cp ~/wifibot_ws/src/wifibot_patrol/maps/indoor/rtabmap_clean.db ~/wifibot_ws/src/wifibot_patrol/maps/indoor/rtabmap.db


为你将 重新建图流程（包含 RTAB-Map 建图、控制机器人移动以及 ROS 2 自带键盘控制指令） 整理成了规范的中法双语对照版，可以直接接在数据库说明的后面：
中文 / Français
🗺️ 重新建图流程（可选：适用于无 rtabmap.db 或更换环境） / Processus de Re-cartographie (Optionnel)
🇨🇳 中文说明

如果你在新的电脑上没有现成的 rtabmap.db，或者修改了 Gazebo 仿真地图，可以通过以下步骤从零开始重新构建地图：
1. 启动 Gazebo 仿真环境

打开终端 A，运行仿真：
Bash

source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash
ros2 launch wifibot_gazebo simulation.launch.py

2. 启动 RTAB-Map 建图节点

打开终端 B，运行建图命令（不加载旧数据库，让其自动新建）：
Bash

source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash

ros2 launch rtabmap_launch rtabmap.launch.py \
    rgb_topic:=/camera/zed2i/image_raw \
    depth_topic:=/camera/zed2i/depth/image_raw \
    camera_info_topic:=/camera/zed2i/camera_info \
    frame_id:=base_link \
    odom_topic:=/odom \
    subscribe_odom:=true \
    visual_odometry:=false \
    approx_sync:=true \
    use_sim_time:=true

3. 启动键盘控制节点驱动机器人

打开终端 C，运行 ROS 2 自带的键盘控制节点，控制小车在仿真环境中移动以构建全局地图：
Bash

source /opt/ros/humble/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard

(操作提示：根据终端提示按键（如 i 前进、u 左转、j 停止等）控制小车覆盖所有需要导航的区域。)
4. 保存并复制生成的地图数据库

建图完成后，RTAB-Map 默认会将生成的数据库保存在 ~/.ros/rtabmap.db。将其复制并重命名放到项目的对应路径下：
Bash

cp ~/.ros/rtabmap.db ~/wifibot_ws/src/wifibot_patrol/maps/indoor/rtabmap.db

🇫🇷 Description en Français

Si vous n'avez pas de fichier rtabmap.db sur une nouvelle machine ou si vous avez modifié l'environnement Gazebo, vous pouvez recréer la carte en suivant ces étapes :
1. Lancer l'environnement de simulation Gazebo

Ouvrez le terminal A :
Bash

source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash
ros2 launch wifibot_gazebo simulation.launch.py

2. Lancer le nœud de cartographie RTAB-Map

Ouvrez le terminal B :
Bash

source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash

ros2 launch rtabmap_launch rtabmap.launch.py \
    rgb_topic:=/camera/zed2i/image_raw \
    depth_topic:=/camera/zed2i/depth/image_raw \
    camera_info_topic:=/camera/zed2i/camera_info \
    frame_id:=base_link \
    odom_topic:=/odom \
    subscribe_odom:=true \
    visual_odometry:=false \
    approx_sync:=true \
    use_sim_time:=true

3. Lancer le nœud de contrôle au clavier

Ouvrez le terminal C pour piloter le robot et explorer l'environnement :
Bash

source /opt/ros/humble/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard

4. Sauvegarder et copier la base de données de la carte

Une fois la cartographie terminée, copiez et renommez le fichier généré vers le répertoire du projet :
Bash

cp ~/.ros/rtabmap.db ~/wifibot_ws/src/wifibot_patrol/maps/indoor/rtabmap.db


📍 启动 RTAB-Map 定位与导航 / Lancement de la Localisation et Navigation RTAB-Map
🇨🇳 中文说明

为了防止地图数据库被污染，建议在每次开始定位或测试前，使用干净的数据库模板（rtabmap_clean.db）覆盖主数据库文件：
Bash

cp ~/wifibot_ws/src/wifibot_patrol/maps/indoor/rtabmap_clean.db ~/wifibot_ws/src/wifibot_patrol/maps/indoor/rtabmap.db

随后，加载环境并运行正式的 RTAB-Map 启动命令进行定位与建图：
Bash

source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash

ros2 launch rtabmap_launch rtabmap.launch.py \
    database_path:=/home/yz0000/wifibot_ws/src/wifibot_patrol/maps/indoor/rtabmap.db \
    rgb_topic:=/camera/zed2i/image_raw \
    depth_topic:=/camera/zed2i/depth/image_raw \
    camera_info_topic:=/camera/zed2i/depth/camera_info \
    frame_id:=base_link \
    odom_topic:=/odom \
    subscribe_odom:=true \
    visual_odometry:=false \
    approx_sync:=true \
    use_sim_time:=true \
    map_always_update:=true \
    subscribe_depth:=true \
    rtabmap_args:="\
    --Mem/IncrementalMemory true \
    --Mem/InitWMWithAllNodes true \
    --RGBD/StartAtOrigin true \
    --Reg/Force3DoF true \
    --Optimizer/GravitySigma 0 \
    --Grid/Sensor true \
    --Grid/MaxObstacleHeight 1.5 \
    --Grid/MinObstacleHeight 0.05 \
    --Grid/RayTracing true \
    --Grid/FromDepth true"

📦 关于地图数据库 (rtabmap.db)

由于地图数据库文件 (rtabmap.db) 体积较大（通常达数 GB），因此未直接包含在本 Git 仓库中。如果你需要用于定位与导航，请使用干净的初始数据库（rtabmap_clean.db）或者通过外部网盘下载后放置于 src/wifibot_patrol/maps/indoor/ 目录下。
🇫🇷 Description en Français

Pour éviter la corruption de la base de données cartographique, il est recommandé de réinitialiser la base principale en la copiant depuis le fichier propre avant chaque lancement :
Bash

cp ~/wifibot_ws/src/wifibot_patrol/maps/indoor/rtabmap_clean.db ~/wifibot_ws/src/wifibot_patrol/maps/indoor/rtabmap.db

Ensuite, chargez l'environnement et lancez la commande RTAB-Map :
Bash

source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash

ros2 launch rtabmap_launch rtabmap.launch.py \
    database_path:=/home/yz0000/wifibot_ws/src/wifibot_patrol/maps/indoor/rtabmap.db \
    rgb_topic:=/camera/zed2i/image_raw \
    depth_topic:=/camera/zed2i/depth/image_raw \
    camera_info_topic:=/camera/zed2i/depth/camera_info \
    frame_id:=base_link \
    odom_topic:=/odom \
    subscribe_odom:=true \
    visual_odometry:=false \
    approx_sync:=true \
    use_sim_time:=true \
    map_always_update:=true \
    subscribe_depth:=true \
    rtabmap_args:="\
    --Mem/IncrementalMemory true \
    --Mem/InitWMWithAllNodes true \
    --RGBD/StartAtOrigin true \
    --Reg/Force3DoF true \
    --Optimizer/GravitySigma 0 \
    --Grid/Sensor true \
    --Grid/MaxObstacleHeight 1.5 \
    --Grid/MinObstacleHeight 0.05 \
    --Grid/RayTracing true \
    --Grid/FromDepth true"

📦 À propos de la base de données (rtabmap.db)

Étant donné que le fichier de base de données rtabmap.db est volumineux (plusieurs Go), il n'est pas inclus directement dans ce dépôt Git. Utilisez le modèle propre (rtabmap_clean.db) inclus ou placez votre fichier téléchargé dans le dossier src/wifibot_patrol/maps/indoor/.

🧭 运行 A* 路径规划测试 / Test de Planification de Trajectoire A*
🇨🇳 中文说明

如果你想单独测试或运行本项目中的 A* 路径规划算法脚本，可以在工作空间或对应源码路径下执行以下命令：
Bash

python3 ~/wifibot_ws/src/wifibot_patrol/wifibot_patrol/astar.py

🇫🇷 Description en Français

Si vous souhaitez tester ou exécuter indépendamment le script de planification de trajectoire A* de ce projet, exécutez la commande suivante :
Bash

python3 ~/wifibot_ws/src/wifibot_patrol/wifibot_patrol/astar.py


🛡️ 启动智能避障与路径重规划 / Lancement de l'Évitement Intelligent et de la Replanification
🇨🇳 中文说明

本项目核心的自动驾驶避障与导航巡航功能由 smart_bypass_guard.py 驱动。它内部会调用 path_follower.py 实现路径跟随，并在检测到障碍物时调用 astar.py 进行动态重规划，从而绕过障碍物。

启动该节点命令如下：
Bash

python3 ~/wifibot_ws/src/wifibot_patrol/wifibot_patrol/smart_bypass_guard.py

🇫🇷 Description en Français

La fonction centrale de conduite autonome, d'évitement d'obstacles et de navigation de ce projet est pilotée par le script smart_bypass_guard.py. En interne, il appelle path_follower.py pour le suivi de trajectoire et astar.py pour la replanification dynamique afin de contourner les obstacles détectés en temps réel.

Exécutez la commande suivante pour lancer ce nœud :
Bash

python3 ~/wifibot_ws/src/wifibot_patrol/wifibot_patrol/smart_bypass_guard.py

🎮 完整自动驾驶实操流程 / Guide Opérationnel Complet de Conduite Autonome
🇨🇳 中文说明

要在仿真环境中完整体验 WiFibot 的室内自动驾驶与智能避障巡航，请按照以下步骤在不同的终端中依次操作：
步骤 1：重置地图数据库（防止地图污染）

在每次运行定位和导航前，建议使用干净的模板重置主数据库文件：
Bash

cp ~/wifibot_ws/src/wifibot_patrol/maps/indoor/rtabmap_clean.db ~/wifibot_ws/src/wifibot_patrol/maps/indoor/rtabmap.db

步骤 2：启动 Gazebo 仿真环境（终端 A）

打开第一个终端，启动 Gazebo 物理仿真与 WiFibot 小车模型：
Bash

source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash
ros2 launch wifibot_gazebo simulation.launch.py

步骤 3：启动 RTAB-Map 视觉定位节点（终端 B）

打开第二个终端，加载环境并启动 RTAB-Map 进行纯视觉定位：
Bash

source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash

ros2 launch rtabmap_launch rtabmap.launch.py \
    database_path:=/home/yz0000/wifibot_ws/src/wifibot_patrol/maps/indoor/rtabmap.db \
    rgb_topic:=/camera/zed2i/image_raw \
    depth_topic:=/camera/zed2i/depth/image_raw \
    camera_info_topic:=/camera/zed2i/depth/camera_info \
    frame_id:=base_link \
    odom_topic:=/odom \
    subscribe_odom:=true \
    visual_odometry:=false \
    approx_sync:=true \
    use_sim_time:=true \
    map_always_update:=true \
    subscribe_depth:=true \
    rtabmap_args:="\
    --Mem/IncrementalMemory true \
    --Mem/InitWMWithAllNodes true \
    --RGBD/StartAtOrigin true \
    --Reg/Force3DoF true \
    --Optimizer/GravitySigma 0 \
    --Grid/Sensor true \
    --Grid/MaxObstacleHeight 1.5 \
    --Grid/MinObstacleHeight 0.05 \
    --Grid/RayTracing true \
    --Grid/FromDepth true"

步骤 4：运行 A* 算法选择目标点与方向（终端 C）

打开第三个终端，运行 astar.py 脚本：
Bash

source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash
python3 ~/wifibot_ws/src/wifibot_patrol/wifibot_patrol/astar.py

    操作交互提示： 运行后会弹出地图窗口：

    第一次点击： 选择小车巡航的目标位置（Goal Position）。

    第二次点击： 选择小车到达终点时的朝向方向（Target Orientation）。
步骤 5：启动智能避障与路径重规划巡航节点（终端 D）

打开第四个终端，运行核心巡航与避障控制脚本（内部自动调用 path_follower.py 与 astar.py 进行动态避障）：
Bash

source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash
python3 ~/wifibot_ws/src/wifibot_patrol/wifibot_patrol/smart_bypass_guard.py

🇫🇷 Description en Français

Pour tester l'ensemble du système de conduite autonome et d'évitement d'obstacles du WiFibot dans la simulation, veuillez suivre ces étapes dans des terminaux séparés :
Étape 1 : Réinitialiser la base de données de la carte

Avant chaque test, écrasez la base principale avec le modèle propre :
Bash

cp ~/wifibot_ws/src/wifibot_patrol/maps/indoor/rtabmap_clean.db ~/wifibot_ws/src/wifibot_patrol/maps/indoor/rtabmap.db

Étape 2 : Lancer la simulation Gazebo (Terminal A)

Ouvrez le premier terminal pour lancer la simulation physique :
Bash

source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash
ros2 launch wifibot_gazebo simulation.launch.py

Étape 3 : Lancer la localisation visuelle RTAB-Map (Terminal B)

Ouvrez le second terminal et exécutez la commande de localisation :
Bash

source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash

ros2 launch rtabmap_launch rtabmap.launch.py \
    database_path:=/home/yz0000/wifibot_ws/src/wifibot_patrol/maps/indoor/rtabmap.db \
    rgb_topic:=/camera/zed2i/image_raw \
    depth_topic:=/camera/zed2i/depth/image_raw \
    camera_info_topic:=/camera/zed2i/depth/camera_info \
    frame_id:=base_link \
    odom_topic:=/odom \
    subscribe_odom:=true \
    visual_odometry:=false \
    approx_sync:=true \
    use_sim_time:=true \
    map_always_update:=true \
    subscribe_depth:=true \
    rtabmap_args:="\
    --Mem/IncrementalMemory true \
    --Mem/InitWMWithAllNodes true \
    --RGBD/StartAtOrigin true \
    --Reg/Force3DoF true \
    --Optimizer/GravitySigma 0 \
    --Grid/Sensor true \
    --Grid/MaxObstacleHeight 1.5 \
    --Grid/MinObstacleHeight 0.05 \
    --Grid/RayTracing true \
    --Grid/FromDepth true"

Étape 4 : Sélectionner la destination et l'orientation via A* (Terminal C)

Ouvrez le troisième terminal et exécutez le script A* :
Bash

source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash
python3 ~/wifibot_ws/src/wifibot_patrol/wifibot_patrol/astar.py

    Instructions interactives :

    Premier clic : Définir la position de destination (Goal Position).

    Second clic : Définir l'orientation finale du robot à l'arrivée (Target Orientation).

Étape 5 : Lancer le nœud d'évitement et de patrouille (Terminal D)

Ouvrez le quatrième terminal pour exécuter le script de contrôle intelligent (qui gère le suivi de chemin et la replanification) :
Bash

source /opt/ros/humble/setup.bash
source ~/wifibot_ws/install/setup.bash
python3 ~/wifibot_ws/src/wifibot_patrol/wifibot_patrol/smart_bypass_guard.py
