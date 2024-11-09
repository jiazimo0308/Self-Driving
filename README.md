# Autonomous-Driving-Based-On-Deep-Learing
在智能车上实现自动行驶，红绿灯识别和避障

Realize automatic driving, traffic light recognition, and obstacle avoidance on smart cars

# 1.摘要（Abstract）
本文为实现自动驾驶系统，设计并实施了三个核心功能：自动行车、避障以及红绿灯识别，并最终将这三种功能进行分级合并。系统设计阶段，结合硬件环境，主要设计了智能车行驶、数据采集及模型部署系统。数据采集系统获取相机标定板数据以及行驶信息。经过深度处理，运用计算机视觉算法，处理得到可供模型训练的数据。自动行车系统的设计采用了两种深度学习模型和两种训练任务进行模型训练，并在比较分析的基础上，结合实际运行环境，优化训练结果。避障系统借助激光雷达扫描环境数据，确定车辆四个方向范围，并根据计算结果，指导智能车避障。红绿灯识别系统在新色彩空间下划分颜色区间并提取信号灯发光部分，进一步识别颜色，根据识别颜色控制车辆行动。将上述三种功能在已实现的情况下进行整合，设计功能优先级划分，根据实际硬件环境设计单独功能的运行逻辑。并根据最终设计的结果进行智能车实际部署以实现自动驾驶功能。

(In order to realize the auto drive system, this paper designs and implements three core functions: automatic driving, obstacle avoidance and traffic light recognition. Finally, these three functions are classified and combined. In the system design phase, combined with the hardware environment, the intelligent vehicle driving, data collection, and model deployment system were mainly designed. The data acquisition system obtains camera calibration board data and driving information. After deep processing, computer vision algorithms are used to obtain data that can be used for model training. The design of the automatic driving system adopts two deep learning models and two training tasks for model training, and optimizes the training results based on comparative analysis and actual operating environment. The obstacle avoidance system uses LiDAR to scan environmental data, determine the four directional ranges of the vehicle, and guide intelligent vehicles in obstacle avoidance based on the calculation results. The traffic light recognition system divides color intervals in the new color space and extracts the illuminated parts of the signal lights, further identifying colors and controlling vehicle movement based on the identified colors. Integrate the above three functions in the already implemented situation, design priority division of functions, and design the operation logic of individual functions based on the actual hardware environment. And based on the final design results, deploy the intelligent vehicle to achieve autonomous driving function.)

# 2.研究思路与方法（Research ideas and methods）
通过搭建场景平台，设置信号灯以及障碍物探究自动驾驶解决方法。重新设计符合智能车与场景平台下的操作系统，针对采集后的数据处理方法进行了深入的实验和测试。在搭建自动行驶系统中，选择两种符合当前计算资源下的小体量深度学习模型进行不同训练任务的测试，对比分析模型训练结果，并针对在实际情况部署所产生的问题进行解决和优化。设计智能车避障系统，利用智能车前端激光雷达扫描数据进行方向区间划分，将激光扫描到的区域划分成若干个小区间，并根据划分区间的计算结果使智能车实现避障。结合实际剩余计算资源设计红绿灯识别系统，根据不同颜色数值区间的差异性进行颜色识别。当上述三种功能完成时，设定三种功能优先等级，结合实际运行环境设计自动驾驶系统。
<div align=center>
<img width="400"  src="https://github.com/user-attachments/assets/cc7c1954-4396-4905-ab40-b5c04e42adda">
<img/></div>

（Explore solutions for autonomous driving by building a scene platform, setting up traffic lights and obstacles. Redesigned an operating system that is compatible with intelligent vehicles and scene platforms, and conducted in-depth experiments and tests on the data processing methods after collection.In building an autonomous driving system, two small-scale deep learning models that are suitable for the current computing resources are selected for testing different training tasks, and the training results of the models are compared and analyzed. Solutions and optimizations are made based on the problems arising from deployment in practical situations.Design an intelligent vehicle obstacle avoidance system that uses the front-end LiDAR scanning data of the intelligent vehicle to divide the direction interval, dividing the area scanned by the laser into several small intervals, and enabling the intelligent vehicle to achieve obstacle avoidance based on the calculation results of the divided intervals.Design a traffic light recognition system based on actual remaining computing resources, and recognize colors according to the differences in numerical ranges of different colors. When the above three functions are completed, set the priority of the three functions, and design the auto drive system in combination with the actual operating environment.）

# 3.实验环境与平台(Experimental environment and platform)
由于希望在实车平台上验证前文所训练的自动驾驶模型，以考验自动驾驶模型在实际 情况下的可靠性。为此搭建了专门面向自动驾驶工况场景的智能车平台。该平台由幻宇智 能车平台改装而来，软件控制基于机器人操作系统(Robot Operating System,ROS)。本章将 对使用到的硬件及软件部分进行介绍。之后在模拟场景下进行试验，以验证自动驾驶模型 的实际性能。

（Due to the desire to validate the previously trained autonomous driving model on a real vehicle platform, in order to test the reliability of the autonomous driving model in practical situations. We have built an intelligent vehicle platform specifically designed for autonomous driving scenarios. This platform is modified from the Huanyu Intelligent Vehicle Platform, and its software control is based on the Robot Operating System (ROS). This chapter will introduce the hardware and software components used. Afterwards, experiments will be conducted in simulated scenarios to verify the actual performance of the autonomous driving model.）

## 3.1 场景平台的搭建(Construction of scene platform)
为了实现自动驾驶的安全性和可靠性，大量的数据收集和测试是必不可少的。然而，在真实道路上进行数据收集和测试存在一些问题，例如高昂的成本、时间限制、安全风险等。因此，建立自动驾驶模拟环境成为了一种有效的解决方案。自动驾驶模拟环境是通过仿真技术来模拟现实世界中的各种场景和情况，以进行自动驾驶系统的开发和测试。在这个模拟环境中，可以利用虚拟的道路网络、车辆模型和传感器模拟真实道路上的交通情况。通过收集和分析模拟环境中的数据，可以评估自动驾驶系统在不同情况下的性能和稳定性。首先，进行自动驾驶模拟环境道路的设计，实现基本的道路行驶，智能车根据当前路况做出前进，后退，左转与右转动作
<div align=center>
<img width="400" alt="截屏2024-11-09 11 34 30" src="https://github.com/user-attachments/assets/ed445929-7c38-4b3d-824e-ddb650c4f61d">
<img/></div>

(In order to achieve the safety and reliability of autonomous driving, extensive data collection and testing are essential. However, there are some issues with data collection and testing on real roads, such as high costs, time constraints, safety risks, etc. Therefore, establishing an autonomous driving simulation environment has become an effective solution. The automatic driving simulation environment simulates various scenes and situations in the real world through simulation technology to develop and test the auto drive system. In this simulation environment, virtual road networks, vehicle models, and sensors can be used to simulate traffic conditions on real roads. By collecting and analyzing the data in the simulation environment, the performance and stability of the auto drive system in different situations can be evaluated.Firstly, the design of an autonomous driving simulation environment road is carried out to achieve basic road driving. The intelligent vehicle makes forward, backward, left turn, and right turn actions based on the current road conditions.)

所设计的自动驾驶模拟环境在宽度为420厘米长度460厘米的矩形上进行车道设计。为了进一步保证模拟实际行车情况所涉及到的路况，设计车道宽度为35厘米对应1.5倍车身宽度。并从两条黑色标记点开始以逆时针顺序运行。共有6个直角弯，1个回头弯，2个折角弯和7条直道组成。
<div align=center>
<img width="353" alt="截屏2024-11-09 11 03 18" src="https://github.com/user-attachments/assets/e79cd77c-63ba-4d45-8718-8e7cbd2095d6">
<img/></div>

(The designed autonomous driving simulation environment performs lane design on a rectangle with a width of 420 centimeters and a length of 460 centimeters. In order to further ensure the road conditions involved in simulating actual driving situations, the designed lane width is 35 centimeters, corresponding to 1.5 times the width of the vehicle body. And run in counterclockwise order starting from the two black marked points. There are a total of 6 right angle bends, 1 turn back bend, 2 corner bends, and 7 straight paths.)

## 3.2 智能车平台(Intelligent car platform)
自动驾驶智能车平台的搭建基于幻宇自研的一款配有麦克纳姆轮的四驱遥控车，其上安装的硬件系统结构如图11所示。其中主板选用NVIDIA Jetson B01开发版，该开发版采用ARM架构。搭载了四核心Cortex-A57处理器，具有128核Maxwell GPU及4GB LPCDDR内存。支持多种AI框架与算法，兼顾了小体型和大算力。下控制器选用幻宇自研主板，负责以串口通信的方式接收上方主板信号，并以PWM波的形式通过主板芯片传递给下游的四个编码电机，借此控制智能车底盘运动。直流12V编码驱动电机为智能车运行提供强大驱动力。对于感知模块，考虑到后期数据集所需数据的形式，通过使用板载的传感器方案，其中包括一个奥比中光所研发的具有感知景深的双目摄像头和一个用于辅助矫正的自带IMU以及思岚 A1 激光雷达。传感模块可给出车身纵向速度和角速度并将这两种状态量传递给主板。传感器模块可以做到10HZ的测量频率。其中12V锂电池通过下主板对上主板进行供电，电机主要由下主板的供电端口进行12V供电。车辆控制算法的软件编写基于ROS系统，其中车辆控制端主要通过geometry_msgs功能包和sensor_msgs功能包。控制模块的运算频率设定为10Hz。即在实际过程中智能车对前方路况的判断并做出行动的时间可以控制在100ms内，体现出自动驾驶算法的实时性。
<div align=center>
<img width="400" alt="截屏2024-11-09 13 17 58" src="https://github.com/user-attachments/assets/3ddacd6f-520e-435d-b267-4120e34751e5">
<img/></div>
<div align=center>
<img width="400" alt="截屏2024-11-09 11 17 12" src="https://github.com/user-attachments/assets/703ce7c2-3c8d-4856-b848-936718ca24b1">
<img/></div>

(The construction of the autonomous driving intelligent car platform is based on a four-wheel drive remote control car equipped with Mecanum wheels developed by Huanyu. The hardware system structure installed on it is shown in Figure 11. The motherboard uses NVIDIA Jetson B01 development version, which adopts ARM architecture. Equipped with a quad core Cortex-A57 processor, featuring a 128 core Maxwell GPU and 4GB LPCDDR memory. Supports multiple AI frameworks and algorithms, balancing small size and high computing power. The lower controller uses a self-developed motherboard from Huanyu, which is responsible for receiving signals from the upper motherboard through serial communication and transmitting them in the form of PWM waves to the four encoding motors downstream through the motherboard chip, thereby controlling the motion of the intelligent vehicle chassis. The DC 12V encoded drive motor provides powerful driving force for the operation of intelligent vehicles. For the perception module, considering the form of data required for the later dataset, an onboard sensor scheme is used, which includes a binocular camera with perception depth developed by Obi Zhongguang, a built-in IMU for auxiliary correction, and a Silan A1 laser radar. The sensing module can provide the longitudinal velocity and angular velocity of the vehicle body and transmit these two state variables to the motherboard. The sensor module can achieve a measurement frequency of 10Hz. The 12V lithium battery supplies power to the upper motherboard through the lower motherboard, while the motor is mainly powered by the 12V port on the lower motherboard. The software development of the vehicle control algorithm is based on the ROS system, where the vehicle control end mainly uses the geometriy_msgs and sensor-msgs function packages. The operating frequency of the control module is set to 10Hz. In the actual process, the time for intelligent vehicles to judge and take action on the road conditions ahead can be controlled within 100ms, reflecting the real-time performance of autonomous driving algorithms.)

## 3.3 计算平台（Computing platform）
由于本次实验的数据集主要由图像数据组成，其特点是数据量大、数据具有高维性或结构性。这对计算机的中央处理器以及图形处理器提出了较高的要求。为了满足对计算资源的需求，我们选择了两台高性能计算机进行数据处理与模型训练。首先，选用了一台搭载M2 PRO芯片的计算机，该机具有10核中央处理器和16核图形处理器，以及16GB四通道内存。这台计算机主要负责整体框架搭建，实验尝试性验证以及部分训练任务。M2 PRO芯片的强大计算能力和高效的内存管理，使得它能够快速处理大量的图像数据，提高实验效率。其次，选用了一台惠普Z600工作站，该工作站搭载了双核至强E5640中央处理器，双路DDR4 32GB内存和1TB固态硬盘，以及一块特斯拉丽台p100显卡，该卡拥有24GB的显存。这台工作站主要用于处理大规模的多维数据和模型训练的任务。双中央处理器和大容量的内存使工作站能够连续处理大规模的图像数据，1TB的固态硬盘则提供了足够的空间，保证了数据处理与模型训练的顺利进行，进一步保证了计算的可靠性。

(Due to the fact that the dataset used in this experiment is mainly composed of image data, which is characterized by a large amount of data and high dimensionality or structure. This places high demands on the central processing unit and graphics processor of computers. In order to meet the demand for computing resources, we selected two high-performance computers for data processing and model training. Firstly, a computer equipped with M2 PRO chip was selected, which has a 10 core central processing unit, a 16 core graphics processor, and 16GB of four channel memory. This computer is mainly responsible for overall framework construction, experimental trial verification, and some training tasks. The powerful computing power and efficient memory management of the M2 PRO chip enable it to quickly process large amounts of image data, improving experimental efficiency. Secondly, an HP Z600 workstation was selected, which is equipped with a dual core Xeon E5640 central processing unit, dual DDR4 32GB memory, 1TB solid-state drive, and a Tesla Lita P100 graphics card with 24GB of video memory. This workstation is mainly used for processing large-scale multidimensional data and model training tasks. The dual central processing units and large capacity memory enable the workstation to continuously process large-scale image data, while the 1TB solid-state drive provides sufficient space to ensure smooth data processing and model training, further ensuring computational reliability.)

# 4.车辆操控与数据处理(Vehicle handling and data processing)
## 4.1 操控系统设计(Control system design)
数据采集分为标定图像数据采和行驶图像与行驶速度的采集。由于不同部分对数据集的要求不同，所以按每种部分的要求分别设计智能车操控系统。并在次基础上设计了行驶轨迹，行车录像等功能，操作方式上主要尝试了电脑端操控与PS2手柄端操控，并最终找到最优的解决方案。

(Data collection is divided into calibration image data collection and collection of driving images and driving speed. Due to different requirements for the dataset in different parts, intelligent vehicle control systems are designed separately according to the requirements of each part. And based on this, we designed functions such as driving trajectory and driving video recording. In terms of operation, we mainly tried computer control and PS2 controller control, and finally found the optimal solution.)

### 4.1.1 操控系统的分析与选取(Analysis and selection of control system)
在本次试验基于机器人操作系统ROS上，采用Python语言对智能车的操作进行设计。分别设计了电脑键盘端智能车操控系统与PS2手柄端智能车操作系统。从而实现智能车前进，后退，左转，右转。并在此基础上实现相对应的数据采集功能。在电脑端，通过电脑端键盘中“w”,“s”,“a”,“d”键位实现对智能车的前进，后退，左转与右转。在实际搭建过程中使用到了pynput,pygame,curses等库进行测试，由于在实际运行中部分库只能在一个刷新频率下读取一个键盘输入值，因此在一个刷新周期中智能车只能进行一个动作，从而导致智能车运行卡顿不畅。为了保证智能车动作的连贯性，放弃电脑端的设计进而转向PS2手柄端的智能车操控系统。PS2手柄端正面共有13个键位。其中三个为内置功能，其余为可开发键位。为了更好的反应智能车实际的运行情况，选取两个遥感键位作为实现智能车前进，后退，左转，右转的真实运行情况。其余键位根据实际的数据采集需要进行合理的开发。首先确定每个键位在ROS系统中所代表的位置在哪里。根据ROS中的节点joy_node进行打印.
<div align=center>
<img width="400" alt="截屏2024-11-09 13 24 53" src="https://github.com/user-attachments/assets/217009c2-99e8-4a57-8308-fd4ddddab34d">
<img/></div>

(In this experiment, the operation of the intelligent car was designed using Python language based on the robot operating system ROS. We have separately designed a computer keyboard based intelligent car control system and a PS2 controller based intelligent car operating system. Thus achieving intelligent vehicle forward, backward, left turn, and right turn. And based on this, implement corresponding data collection functions. On the computer side, the "w", "s", "a", and "d" keys on the computer keyboard are used to move the smart car forward, backward, left, and right. In the actual construction process, libraries such as pynput, pygame, curses, etc. were used for testing. However, due to the fact that some libraries can only read one keyboard input value at one refresh rate during actual operation, the smart car can only perform one action in one refresh cycle, resulting in slow operation. In order to ensure the coherence of the actions of the intelligent car, the design of the computer end was abandoned and the direction shifted to the PS2 controller end of the intelligent car control system. There are a total of 13 key positions on the front of the PS2 controller end. Three of them are built-in functions, while the rest are playable keys. In order to better reflect the actual operation of the intelligent vehicle, two remote sensing key positions are selected to achieve the real operation of the intelligent vehicle's forward, backward, left turn, and right turn. The remaining key positions should be developed reasonably according to the actual data collection needs. Firstly, determine where each key position represents in the ROS system. Print based on the node joy_node in ROS.)

键位信息设计智能车的操控系统,实现智能车的前进，后退左转与右转以及智能车的三种运行速度的切换。在运行开始前,设置初始基础速度为0（base_speed=0）,遥感手柄的axes[7]左右两个按键为智能车实现三种运行速度的切换按键，左按键用于加速调节,右按键用于减速调节，且调节的最大值为3。智能车的前进力度与转弯力度由遥感手柄的axes[1]与axes[2]的两个参数linear_speed和angular_speed控制，最后通过速度综合控制函数得到最终行驶的线速度与角速度。
<div align=center>
<img width="400" alt="截屏2024-11-09 13 43 00" src="https://github.com/user-attachments/assets/49a34ec5-1953-423c-92b9-170ee68b634a">
<img/></div>

(Design a control system for intelligent vehicles based on key information, enabling the vehicle to move forward, backward, left turn, right turn, and switch between three different operating speeds. Before starting the operation, set the initial base speed to 0 (base_steed=0). The two buttons on the axes [7] of the remote sensing controller are used to switch between the three operating speeds of the smart car. The left button is used for acceleration adjustment, and the right button is used for deceleration adjustment, with a maximum adjustment value of 3. The forward and turning force of the smart car are controlled by two parameters, linear_speed and angular_steed, of the axes [1] and axes [2] of the remote sensing controller. Finally, the final linear and angular velocities of the vehicle are obtained through a speed synthesis control function.)

### 4.1.2 数据采集系统设计
#### 4.1.2.1 相机标定数据采集系统
标定图像对自动驾驶系统的精确感知和决策具有关键作用。通过打开roscore内核，joy_node节点以及基础启动环境进行相机标定数据采集系统的设计。通过建立ROS系统图像传输通路，订阅相机节点和操作手柄节点，设定并选取PS2操作手柄按键buttons[3]对图像拍照进行触发和保存。并在新的一轮的数据采集前清除掉上一次采集的数据保证数据不发生混乱提高数据在相同环境下的一致性。
<div align=center>
<img width="400" alt="截屏2024-11-09 13 44 31" src="https://github.com/user-attachments/assets/4174ff5d-8dc3-4995-98c7-e472574ab015">
<img/></div>

(The calibration image plays a key role in the accurate perception and decision-making of the auto drive system. Design a camera calibration data acquisition system by opening the roscore kernel, joy_node node, and basic startup environment. By establishing an image transmission path in the ROS system, subscribing to camera nodes and joystick nodes, setting and selecting the PS2 joystick buttons [3] to trigger and save image capture. And clear the previous data collection before the new round of data collection to ensure that the data is not chaotic and improve the consistency of the data in the same environment.)

#### 4.1.2.2 行车数据采集系统(Driving data collection system)
在实现自动驾驶过程中，图像是自动驾驶系统中最主要的感知信息来源。依托于智能车运行操作系统，进行智能车行车数据采集系统的实现。首先进行图像数据通路在ROS系统中的搭建，通过ROS系统中相机节点与操作系统节点，设定并选取PS2操作手柄按键axes[6]对行车图像数据进行采集，其中左按键为开始行车数据采集，右按键为结束行车数据采集并保存，与此同时发生的还有行车时间、行车线速度和角速度的数据采集。并在新的一轮数据采集之前清除掉上一次采集的数据。
<div align=center>
<img width="400" alt="截屏2024-11-09 13 45 25" src="https://github.com/user-attachments/assets/8a66ceb2-4c60-44fb-bff9-b4bdf2475d1a">
<img/></div>

(In the process of realizing automatic driving, images are the main source of perception information in the auto drive system. Based on the intelligent vehicle operating system, the implementation of an intelligent vehicle driving data collection system is carried out. Firstly, the image data pathway is established in the ROS system. Through the camera node and operating system node in the ROS system, the PS2 joystick button axes [6] is set and selected to collect driving image data. The left button is used to start driving data collection, and the right button is used to end and save driving data collection. At the same time, data collection of driving time, lane speed, and angular velocity also occurs. And clear the last collected data before the new round of data collection.)

#### 4.1.2.3 行车轨迹采集系统(Driving trajectory acquisition system)
不管是在行车数据采集时还是在进行模型的部署，都需要对智能车行驶的轨迹进行记录。由于ROS操作系统自带有智能车方位记录的功能，在实现智能车方位记录的过程中需要对智能车所在的坐标系进行转换，通过订阅Obom节点获得智能车当前的坐标以及四元组方向，四元组经过欧拉角的转换获得智能车相对于第一次位置所朝向的角度。通过数据的整合将智能车当前X轴、Y轴、Z轴以及智能车朝向角度W存储在文本文件中。
<div align=center>
<img width="400" alt="截屏2024-11-09 13 46 18" src="https://github.com/user-attachments/assets/26b68936-c63e-4f55-8a47-9628a16ccab2">
<img/></div>

(Whether it is during the collection of driving data or the deployment of models, it is necessary to record the trajectory of intelligent vehicle driving. Due to the built-in function of the ROS operating system for intelligent vehicle orientation recording, it is necessary to convert the coordinate system in which the intelligent vehicle is located during the process of implementing intelligent vehicle orientation recording. By subscribing to the Obom node, the current coordinates of the intelligent vehicle and the direction of the quadruple are obtained. The quadruple is then converted into Euler angles to obtain the angle of the intelligent vehicle relative to the first position. Store the current X-axis, Y-axis, Z-axis, and orientation angle W of the smart car in a text file through data integration.)

### 4.1.3 模型应用系统设计(Design of model application system)
当模型训练结束时，不仅要对模型进行测试集与验证集上的测试，还需要对模型进行实际应用的测试。通过实际应用测试得到在具体情况下此模型所产生的问题和运行效果，为了建立起模型与智能车之间的关系，设计模型应用系统为以后智能车自动驾驶整体系统的设计与实现奠定基础。在此系统中需要通过建立起图像数据通路，当系统开始运行获得图像数据时，需要使用与图像数据处理相同的处理方法，之后通过保存好的模型获得不同训练任务下的结果，根据不同训练任务下的结果进一步处理得到模型预测的操控数据，并在最后发布到智能车行驶的节点上，驱动智能车在不同情况下做出合理的运行行为，更加直观的反应出当前模型的训练效果。
<div align=center>
<img width="400" alt="截屏2024-11-09 13 46 59" src="https://github.com/user-attachments/assets/09459894-30db-43bf-8e97-70dec9e90742">
<img/></div>

(When the model training is completed, it is not only necessary to test the model on the test set and validation set, but also to test the model for practical applications. Through practical application testing, the problems and operational effects generated by this model in specific situations were obtained. In order to establish the relationship between the model and intelligent vehicles, a model application system was designed to lay the foundation for the design and implementation of the overall system of intelligent vehicle autonomous driving in the future. In this system, it is necessary to establish an image data path. When the system starts to obtain image data, the same processing method as image data processing needs to be used. Then, the saved model is used to obtain the results under different training tasks. Based on the results under different training tasks, the predicted control data of the model is further processed and published to the nodes where the intelligent vehicle travels. This drives the intelligent vehicle to make reasonable operating behaviors in different situations, which more intuitively reflects the training effect of the current model.)

## 4.2 数据采集(Aata acquisition)
### 4.2.1 标定数据采集(Calibration data collection)
本次相机标定采用张正友相机标定法，通过黑白棋盘格对相机进行标定。通过calib.io网站对标定所需的黑白棋盘格标定板进行设计。标定板由8行12列的小方格组成，每个小方格的边长大小为20mm。
<div align=center>
<img width="250" alt="截屏2024-11-09 13 47 39" src="https://github.com/user-attachments/assets/378b96b3-1efa-4b2c-9b34-c022f9cbc49c">
<img width="250" alt="截屏2024-11-09 13 48 16" src="https://github.com/user-attachments/assets/8f5b557c-949c-4f0c-9b7d-baaffaa65f08">
<img/></div>

(This camera calibration adopts the Zhang Zhengyou camera calibration method, which calibrates the camera through a black and white checkerboard pattern. Design the black and white checkerboard calibration board required for calibration through the calib.io website. The calibration board consists of 8 rows and 12 columns of small squares, each with a side length of 20mm.)

在对标定数据采集的过程中，将标定板与摄像头放置在多个不同的位置和角度，以确保从各个视角对相机进行全面的标定。提高标定的准确性与鲁邦性，避免引入新的误差。通过相机标定数据操控系统的操作，共拍摄了13张标定图片。

(During the process of collecting calibration data, the calibration board and camera are placed in multiple different positions and angles to ensure comprehensive calibration of the camera from various perspectives. Improve the accuracy and robustness of calibration to avoid introducing new errors. Through the operation of the camera calibration data control system, a total of 13 calibration images were captured.)

### 4.2.2 行车数据采集(Driving data collection)
在设计好的自动驾驶环境中进行数据采集，运行行车数据采集系统。通过PS2手柄的操控，从起始点以逆时针作为正方向进行智能车行驶的线速度与角速度数据以及摄像头数据采集。为了进一步保障采集数据的平衡化以起始点顺时针方向再一次进行数据采集。重复操作，直到采集到足够多的数据后停止并将需要的数据进行导出。
<div align=center>
<img width="400" alt="截屏2024-11-09 13 48 44" src="https://github.com/user-attachments/assets/dcceeab7-65d2-4b97-995a-db54019d77dd">
<img/></div>

(Collect data in the designed autonomous driving environment and operate the driving data collection system. By operating the PS2 controller, the linear and angular velocity data as well as camera data of the intelligent vehicle are collected from the starting point in a counterclockwise direction as the positive direction. In order to further ensure the balance of data collection, data collection is carried out again in a clockwise direction from the starting point. Repeat the operation until enough data is collected and stop exporting the required data.)

为了进一步提高数据采集量，将行车数据采集系统中的行车图像数据通过改变订阅节点进行压缩，并缩短采集周期从而提高采集频率。最终通过行车数据采集系统共采集到11560张行车数据图片，每一张行车数据图片以采集时间进行命名。行车过程中的线速度与角速度以采集时间，线速度，角速度的格式存储。且三列数据均为浮点数据类型。

(In order to further increase the amount of data collection, the driving image data in the driving data collection system is compressed by changing the subscription nodes, and the collection cycle is shortened to increase the collection frequency. Finally, a total of 11560 driving data images were collected through the driving data collection system, and each driving data image was named after the collection time. The linear velocity and angular velocity during driving are stored in the format of time, linear velocity, and angular velocity. And all three columns of data are of floating-point data type.)

## 4.3 数据处理(Data processing)
### 4.3.1 标定数据处理(Calidation data processing)
首先对采集的标定数据进行是否为空的判断，保证采集的标定数据集存在且路径正确，由于之后进行角点的寻找基于图像强度变化且不依赖于颜色信息，所以对图像进行灰度化处理，进一步突出图像形状、纹理和图案特征。其次根据标定板的行数和列数进行内脚点的确定，根据此次所使用的标定板的行数与列数分别为8行12列，所以得到内脚点的行数为7行11列，并建立起图像坐标系点。最后通过图像交点的寻找得到相机内部参数矩阵。
<div align=center>
<img width="400" alt="截屏2024-11-09 13 49 27" src="https://github.com/user-attachments/assets/18c3eab3-d421-4cf5-95ac-94466053c502">
<img/></div>

(Firstly, the collected calibration data is judged to be empty to ensure that the calibration dataset exists and the path is correct. As the subsequent search for corner points is based on changes in image intensity and does not rely on color information, the image is grayscale processed to further highlight its shape, texture, and pattern features. Secondly, based on the number of rows and columns of the calibration board, the inner foot points are determined. According to the number of rows and columns of the calibration board used this time, which are 8 rows and 12 columns respectively, the number of rows for the inner foot points is 7 rows and 11 columns, and an image coordinate system point is established. Finally, the camera's internal parameter matrix is obtained by searching for the intersection points of the images.)

通过张正友黑白棋盘标定法得到相机内部参数，分别为相机内部参数矩阵，相机畸变量，相机旋转量和相机平移量。根据相机标定计算得到的结果进行采集图片的畸变矫正。如图所示分别为采集得到的原图像和畸变矫正后的图像。
<div align=center>
<img width="250" alt="截屏2024-11-09 13 50 42" src="https://github.com/user-attachments/assets/04491845-d9cd-4b36-92c0-627b6a949372">
<img width="250" alt="截屏2024-11-09 13 51 19" src="https://github.com/user-attachments/assets/e0c75de2-2e05-42f8-9b7a-366362209759">
<img/></div>

(The internal parameters of the camera were obtained using Zhang Zhengyou's black and white chessboard calibration method, including the camera internal parameter matrix, camera distortion, camera rotation, and camera translation. Perform distortion correction on the captured images based on the results obtained from camera calibration calculations. As shown in the figure, they are the original image and the image after distortion correction obtained.)



### 4.3.2 行车数据处理(Driving data processing)
#### 4.3.2.1 行车图像处理(Driving image processing)
##### （1）行车图像数据分析(Driving image data analysis)
图像数据主要由智能车前的摄像头进行图像的捕捉，通常捕捉到的图像大小为480*640像素，并包含三个颜色通道（红色、绿色、蓝色）。如图25所示为智能车前摄像头捕捉到的行驶图像，图像中主要包含车道情况，周围光线以及部分周围环境。
<div align=center>
<img width="400" alt="截屏2024-11-09 13 51 49" src="https://github.com/user-attachments/assets/691a85b8-7726-4c46-836a-cd675330e33a">
<img/></div>

(The image data is mainly captured by the camera in front of the smart car. Usually, the size of the captured image is 480*640 pixels and contains three colour channels (red, green, blue). As shown in Figure 25, the driving image captured by the smart front camera mainly includes the lane situation, the surrounding light and part of the surrounding environment.)
通过预览行车数据采集系统所捕捉到的原始图像，发现采集的所有图像数据中主要存在三个问题分别为光线强度、路面纹理以及实验场地无关特征的加入。分别如图26,图27和图28所示。分别为采取原始图像中的光线强度，路面纹理以及无关场地特征。
<div align=center>
<img width="195" alt="截屏2024-11-09 13 52 56" src="https://github.com/user-attachments/assets/c1c1b42b-2c5a-48a8-95c2-c8ab35e23b2d">
<img width="195" alt="截屏2024-11-09 13 53 16" src="https://github.com/user-attachments/assets/c9064fbb-c7f4-49f5-afc0-9b2bc8de64b8">
<img width="195" alt="截屏2024-11-09 13 53 33" src="https://github.com/user-attachments/assets/e8813af4-5a8f-4f3d-ae7d-5ddc5e25a5ba">
<img/></div>

(By previewing the original images captured by the driving data acquisition system, it was found that there were three main problems in all the image data collected, namely the light intensity, the road surface texture and the addition of features unrelated to the experimental site. As shown in Figure 26, Figure 27 and Figure 28 respectively. They adopt the light intensity, road surface texture and irrelevant site features in the original image respectively.)

##### (2）行车图像数据增强处理(Driving image data enhancement processing)
针对以上在数据集中发现的问题进行相关的图像数据处理，使得图像数据集特征更加突出，提高此后模型训练的精确度。由于车道与车道周围颜色的对比度明显，进一步突出图像当前的特征，通过提高图像对比度进行图像数据增强处理，对比度增强的情况下与原始图像的对比.
<div align=center>
<img width="250" alt="截屏2024-11-09 13 57 21" src="https://github.com/user-attachments/assets/4e9b4b11-54f9-424f-a252-13e8ec200657">
<img width="250" alt="截屏2024-11-09 13 57 38" src="https://github.com/user-attachments/assets/a2b56891-1028-4540-8f1f-54d6306ed29e">
<img/></div>

(The relevant image data processing is carried out in response to the above problems found in the data set, which makes the characteristics of the image data set more prominent and improves the accuracy of subsequent model training. Due to the obvious contrast between the colours of the lane and the surrounding lane, the current characteristics of the image are further highlighted. The image data is enhanced by improving the image contrast, and the contrast is enhanced with the original image.)

通过增加对比度，使图像中最暗和最亮部分之间的差异变得更加明显，在原始图像与对比度处理后的图像中红色框可以看到光线强度在此发生了明显的削弱，几乎与光斑周围的颜色融为一体但还是存在并没有完全消除，蓝色框中的路面纹理由于图像对比度的增强变得愈加明显。可以清楚的看到路面纹理的走向，若以当前数据作为训练集则会对训练的模型造成一定影响，可能导致模型泛化能力降低，从而导致模型在实际部署中效果不佳。在无关特征中由于只是图像对比度的改变所以无关特征变化不大，在原始图像与对比度处理后的图像中由黄框所示。

(By increasing the contrast, the difference between the darkest and brightest parts of the image becomes more obvious. In the original image and the image after contrast processing, the red box can see that the light intensity has been significantly weakened here, which is almost integrated with the colour around the light spot, but still exists and has not been completely eliminated. In the blue box The texture of the road surface becomes more and more obvious due to the enhancement of the image contrast. The direction of the road surface texture can be clearly seen. If the current data is used as a training set, it will have a certain impact on the trained model, which may lead to a reduction in the generalisation ability of the model, resulting in poor performance of the model in actual deployment. Among the irrelevant features, because it is only a change in the contrast of the image, the irrelevant features do not change much, which is shown in the yellow box in the image after the original image and the contrast is processed.)

##### （3）行车图像数据高斯化与灰度化处理(Gaussian and greyscale processing of driving image data)
在当前情况下，为了进一步提高数据质量，减少图像中由于光线强度和路面纹理的影响，使用高斯模糊使图片减少噪声降低细节层次从而保留当前图像最主要的特征。由于当前图像分辨率较大，所以使用了较大的高斯核进行模糊化处理，高斯模糊处理后的结果如下。
<div align=center>
<img width="250" alt="截屏2024-11-09 13 58 48" src="https://github.com/user-attachments/assets/f509505c-8767-409f-b3fa-d35eca65db4c">
<img width="250" alt="截屏2024-11-09 13 59 07" src="https://github.com/user-attachments/assets/dea3b412-6127-44dc-baf6-b2ab5c0c3218">
<img/></div>

(In the current situation, in order to further improve the data quality and reduce the impact of light intensity and road surface texture in the image, Gaussian blur is used to reduce noise in the picture and reduce the detail layer to retain the main features of the current image. Due to the large resolution of the current image, a larger Gaussian kernel is used for blurring. The results of Gaussian blurring are as follows.)

由于车道在图像中占比了较大的部分所以通过高斯模糊化处理后，只是使光线强度与路面纹理发生了扩散，光线强度与路面纹理原本的轮廓并没有由于高斯模型与周围环境相融合，如图中红色框与蓝色框。通过高斯模糊使较远处的无关特征与周围环境的轮廓发生了融合，没有与原图像中无关特征的明显轮廓如图中黄色框所示。同时，通过图像的高斯模糊可以看到图像当前的主要特征如图中绿色线标注部分为车道边界线以及车道边界线的延伸。后针对以上所设计到的三种问题进行针对性处理。为了进一步解决上述所存在的问题，使原始图像从三通道图像转变为单通道图像，在保留图像主要特征完整度的前提下进一步优化图像处理效率，降低图像存储和使用的复杂程度，通过图像灰度化实现进一步的处理。在单通道图像下，图像主要特征边缘更加清晰且由于没有其他颜色的干扰使得黄色框中无关特征与周围环境的融合程度更高，红色框中光线强度的干扰得到了进一步的扩散，由于灰度化只是颜色强度的一种改变，所以路面纹理在图像灰度化中没有得到更好的处理如图中蓝色框所示。

(Because the lane accounts for a large part of the image, after Gaussian blur processing, it only diffuses the light intensity and the road surface texture. The original outline of the light intensity and the road surface texture is not due to the integration of the Gaussian model with the surrounding environment, such as the red box and the blue box in the figure. Gaussian blur merges the distant irrelevant features with the outline of the surrounding environment. The obvious contours without the irrelevant features in the original image are shown in the yellow box in the figure. At the same time, through the Gaussian blur of the image, the current main features of the image can be seen, such as the green line annotation part in the figure, which is the lane boundary line and the extension of the lane boundary line. Then carry out targeted treatment for the three problems designed above. In order to further solve the above problems, the original image is changed from a three-channel image to a single-channel image, the image processing efficiency is further optimised under the premise of retaining the integrity of the main features of the image, the complexity of image storage and use is reduced, and further processing is realised through image greyscale. Under the single-channel image, the edges of the main features of the image are clearer, and due to the interference of other colours, the integration of irrelevant features in the yellow box is higher with the surrounding environment. The interference of light intensity in the red box is further diffused. Because greyscale is only a change in colour intensity, the road surface texture is The greyscale of the image has not been better processed, as shown in the blue box in the figure.)

##### （4）行车图像数据二值化处理(Binarisation processing of driving image data)
在当前场景中，车道与车道周围所形成的强对比度，且光线强度与路面纹理同时处于浅色车道部分，车道周围为深色部分，二者颜色差异度较大，可以通过图像分割进行真实世界与图像世界的转换。由于车道与车道周围颜色结构相对单一故使用图像二值化方法进行图像分割。针对此选用了全局阈值法，自适应阈值法与OTSU二值化法分别实现对当前图像的分割。
<div align=center>
<img width="195" alt="截屏2024-11-09 13 59 34" src="https://github.com/user-attachments/assets/74afcaac-4095-4612-9dcf-5e6ef59da7c3">
<img width="195" alt="截屏2024-11-09 13 59 53" src="https://github.com/user-attachments/assets/7f76f744-b3d1-4312-9f4b-c05113ab1064">
<img width="195" alt="截屏2024-11-09 14 00 05" src="https://github.com/user-attachments/assets/3c570824-25b4-4de5-bb73-1007490f6e53">
 <img/></div>
 
 (In the current scene, the strong contrast formed between the lane and the area around the lane, and the light intensity and the road surface texture are in the light lane part at the same time, and the dark part around the lane is the dark part. The colour difference between the two is large, and the real world and the image world can be converted through image segmentation. Because the colour structure of the lane and the surrounding lane is relatively single, the image binary method is used for image segmentation. For this, the global threshold method is selected, and the adaptive threshold method and the OTSU binary method realise the segmentation of the current image respectively.)
 
由于场景平台不同方位光照强度的不统一情况，故在全局阈值法中进行了图像灰度的平均值计算，使用计算得到的灰度平均值作为全局阈值。在全局阈值法处理下相比于其他两种处理方法图像较远处的无关特征复杂度明显降低，其次是OTSU二值法，自适应阈值法由于分块计算，当一小块图像与周围图像灰度值较大时，将导致与灰度值较小的区域差别过大，故保留下了过多的无关特征，且在处理光线强度与路面纹理上也发生了此种问题。而其他两种算法由于是基于全局处理所以全局阈值法与OTSU二值法的效果要远远好于自适应阈值法。针对全局阈值法与OTSU二值法进行数据处理的相关验证与分析，避免由于在不同实验环境下算法的不稳定性，使得图像处理方案具有泛化能力。在较强的光线下的场景环境中进行图像数据的验证。
<div align=center>
<img width="195" alt="截屏2024-11-09 14 01 08" src="https://github.com/user-attachments/assets/7587b6a0-d434-4f92-a26b-978212a81180">
<img width="195" alt="截屏2024-11-09 14 01 18" src="https://github.com/user-attachments/assets/3e07d4c6-f5af-483c-b37c-43c5fbe64b75">
<img width="195" alt="截屏2024-11-09 14 01 25" src="https://github.com/user-attachments/assets/befe1a2d-fcf2-430f-8c6a-4a60d547de59">
<img/></div>

(Due to the inconsistence of the light intensity in different directions of the scene platform, the average value of the image greyscale is calculated in the global threshold method, and the calculated greyscale average is used as the global threshold. Under the global threshold method processing, compared with the other two processing methods, the complexity of the irrelevant features of the distant images is significantly reduced, followed by the OTSU binary method. Due to the block calculation, when a small piece of image and the surrounding image greyscale value is large, it will cause the area with a smaller greyscale value to be too large, so it is retained. Too many irrelevant features have been placed, and such problems also occur in the treatment of light intensity and road surface texture. Because the other two algorithms are based on global processing, the effect of the global threshold method and the OTSU binary method is much better than that of the adaptive threshold method. The relevant verification and analysis of data processing of the global threshold method and the OTSU binary method is carried out to avoid the instability of the algorithm in different experimental environments, so that the image processing scheme has the ability to generalise. Verify image data in a scene environment under strong light.)

通过全阈值法与OTSU二值法进行处理后，在全阈值法中由于光照较强导致阈值设置的较高，从而导致在全阈值法处理中图像主要特征表现不明显，如图中绿色标识。在距离智能车较近的地方全阈值法处理的结果相比于OTSU二值法处理的结果出现了较多非正确特征值，相比之下OTSU二值法保留了较多的特征信息。

(After processing through the full threshold method and the OTSU binary method, the threshold setting is high due to the strong lighting in the full threshold method, resulting in the inconspicuous performance of the main features of the image in the full threshold method processing, as shown in the green logo in the figure. Compared with the results of OTSU binary processing, there are more incorrect characteristic values in the results of the full threshold method processing close to the smart car. In contrast, the OTSU binary method retains more characteristic information.)

##### （5）行车图像数据的联通组件分析(Unicom component analysis of driving image data)
通过实际部署发现，数据在经过二值化处理后，仍然会存在一些处理不充分的特征，如下图39所示，即使后期通过了数据图像的裁剪，但也会导致由于在原始数据上存在难以处理的无关特征。在二值化处理后，使得赛道与赛道周围的差异性不断增大，由于此原因，故使用基于联通组件分析的方法对数据进行图像主体提取，并在图像主体提取后，根据图像主体重新制作新的数据集。从二值化以后的图像中，右上角部分（红色椭圆圈内）由于在原始图像中为周围墙壁与道路周围环境的交界处属于客观存在不可避免的无关特征，为了减小这些客观无关特征的干扰，进行联通组件分析的方法对图像主体特征进行提取，提取结果如图所示，根据提取出的图像按照原图像尺寸进行生成，最终形成图所示的新图像数据。
<div align=center>
<img width="195" alt="截屏2024-11-09 14 01 35" src="https://github.com/user-attachments/assets/1b61e1fd-3c7f-4973-a7ac-f4f5cd41d0fa">
<img width="195" alt="截屏2024-11-09 14 01 43" src="https://github.com/user-attachments/assets/15b2da94-0807-4b1b-96c5-fba10fa2cedb">
<img width="195" alt="截屏2024-11-09 14 01 49" src="https://github.com/user-attachments/assets/1a47b482-dddc-4647-a40d-d0e67ad4bd56">
<img/></div>

(Through actual deployment, it is found that after binary processing, the data will still have some insufficiently processed characteristics. As shown in Figure 39 below, even if the data image is cropped in the later stage, it will lead to irrelevant features that are difficult to process on the original data. After binary processing, the difference between the track and the around the track continues to increase. For this reason, the image body of the data is extracted based on Unicom component analysis, and after the image body is extracted, a new data set is remade according to the image subject. From the binary image, the upper right part (in the red ellipse) is an objective and inevitable irrelevant features at the junction of the surrounding wall and the surrounding environment of the road in the original image. In order to reduce the interference of these objectively irrelevant features, the method of connecting component analysis is carried out on the main features of the image. Extract, the extraction results are shown in the figure. According to the extracted image, it is generated according to the original image size, and finally the new image data shown in the figure is formed.)

##### （6）行车图像数据的裁剪与缩放(Cropping and scaling of driving image data)
最后对当前的处理结果进行图像的裁剪与缩放，在保证图像保留当前主要特征的前提下对图像无关特征进行裁剪。裁剪图像上半部分三分之一比例，从原图像480*640比例，裁剪到320*640比例，并在图像裁剪后对图像进行缩放，以提高模型训练效率与存储空间结构的优化。裁剪后的图像如图42所示，保留了当前图像数据中主要特征进一步帮助模型理解图像并使用图像进行模型部署。
<div align=center>
<img width="250" alt="截屏2024-11-09 14 02 01" src="https://github.com/user-attachments/assets/f38d2b2b-3748-40f0-a90e-2f386f05b9a0">
<img width="250" alt="截屏2024-11-09 14 02 08" src="https://github.com/user-attachments/assets/8a7e90c9-fcbe-4150-b029-c7658c7e3165">
<img/></div>

(Finally, crop and scale the image of the current processing results, and crop the irrelevant features of the image under the premise of ensuring that the image retains the current main features. Crop one-third of the upper half of the image, from the 480*640 scale of the original image to the 320*640 scale, and scale the image after cropping the image to improve the efficiency of model training and optimise the storage space structure. The cropped image is shown in Figure 42, which retains the main features of the current image data to further help the model understand the image and use the image for model deployment.)

最后将图像进行等比缩放，裁剪图像由原来320*640比例，等比缩放到100*200比例相比于原始图像数据在内存中缩小了11.25倍。并由后续所建立的行车数据处理系统与行车速度等数据进行打包，最终形成训练集与测试集。

(Finally, the image is scaled isoportionally. The cropped image is scaled from the original 320*640 scale to 100*200 scale. Compared with the original image data, it is reduced by 11.25 times in memory. And it is packaged by the subsequent driving data processing system, driving speed and other data, and finally form a training set and test set.)

#### 4.3.2.2 行车速度数据处理(Driving speed data processing)
行车数据速度标签主要由时间，线速度，角速度构成。在进行收集的过程中，将采集到的数据存储在文本文档中，对此后的数据预处理会造成一定阻碍，所以将文本数据转换为表格格式，方便后续在行车速度数据上的数据处理。转换后的原数据如表2所示。

(The driving data speed tag is mainly composed of time, line speed and angular speed. In the process of collection, the collected data is stored in the text document, which will cause certain obstacles to the subsequent data preprocessing. Therefore, the text data is converted into table format to facilitate the subsequent data processing on the driving speed data. The converted original data is shown in Table 2.)

表2 部分速度数据转换结果（截取部分)
|时间|	线速度|	角速度|
|:---:| :---: | :---: |
|1706265089.13|	0.002917931	|0|
|1706265094.68|	0.125	|0.231022313|
|1706265099.25|	0.00156066	|0.25|
|1706265099.28|	0.005632472	|-0.25|
|1706265189.36|	0.06124844	|0|
|1706265189.39|	0.065320253	|0|

由于线速度与角速度由正负表示方向，数值表示大小，不够直观和解释，所以对采集的线速度与角速度进行速度的分解，使展现的速度更加细化。若线速度数值为正则车辆向前行驶，反之，向后行驶。同理若角速度为正则车辆向左侧转向，反之，向右侧转向。根据上述原理，在原始数据中加入前进，后退，左转，右转四个方向的分动作标签从而更加直观的展现出动作的组成部分。如表3所示为差分后的速度标签。

(Because the linear velocity and angular velocity are represented by positive and negative, and the numerical representation of the size is not intuitive and explained, the collected linear velocity and angular velocity are decomposed to make the displayed speed more refined. If the line speed value is regular, the vehicle will drive forward, and vice versa, drive backward. Similarly, if the angular velocity is regular, the vehicle will turn to the left, and vice versa, it will turn to the right. According to the above principle, four directions of forward, backward, left and right are added to the original data to show the components of the action more intuitively. As shown in Table 3, it is the speed label after the difference.)

表3 差分后的速度标签
|动作|标签|动作|标签|
|:---:| :---: | :---: |:---: |
|静止	|0000|	向左后行驶|	0101|
|前进	|1000|	向右后行驶|	0110|
|向左前行驶	|1010|	逆时针旋转|	0010|
|向右前行驶|1001|	顺时针旋转|	0001|
|倒车/刹车|0100|	

在速度差分后的标签表示下，使智能车当前的状态表示更加的直观，但速度差分标签在计算机存储的情况下包含所有位信息，所以对存储资源可能会造成一定的浪费，由于智能车实现的功能量大以及有限的计算资源，在可以表示当前智能车动作的情况下，进一步优化标签形式提高计算资源的使用效率。根据智能车行驶的九个行驶状态，进行行驶标签的设定。将智能车行驶分为9种变长标签类别。优化传输或存储资源的使用效率，且在智能车实际行驶过程中对前方道路的识别具有高频率的动态变化特性，相对于速度差分编码简化的行驶状态编码更能直观的反应当前智能车行驶状态，方便更好的分辨智能车在当前环境下路况识别的准确性。如表4所示为根据智能车行驶的九个状态对行驶状态标签的设定。

(Under the label representation after the speed difference, the current state representation of the smart car is more intuitive, but the speed difference label contains all the bit information in the case of computer storage, so it may cause a certain waste of storage resources. Due to the large number of functions and limited computing resources realised by the smart car, it can be represented In the current situation of intelligent car operation, the label form is further optimised to improve the efficiency of computing resources. The driving label is set according to the nine driving states of the smart car. Smart car driving is divided into 9 categories of variable-length labels. Optimise the use efficiency of transmission or storage resources, and the identification of the road ahead in the actual driving process of smart cars has the characteristics of high-frequency dynamic change. Compared with the speed difference code, the simplified driving status code can more intuitively reflect the current driving status of the smart car, which is convenient to better distinguish the road of smart cars in the current environment. The accuracy of situational recognition. As shown in Table 4, the driving status label is set according to the nine states of the smart car.)

表4 根据运行状态划分的标签（进行了变长标签补齐）
|动作|标签|动作|标签|
|:---:| :---: | :---: |:---: |
|静止|000000001|	向左后行驶|	000100000|
|前进|000000010|	向右后行驶|	001000000|
|向左前行驶|000000100|逆时针旋转|010000000|
|向右前行驶|000001000|顺时针旋转|100000000|
|倒车/刹车|000010000|

根据运行状态划分的标签可在分类模型中使用，由于线速度与角速度的绝对值都处于0到1之间故不做过多的数据处理，线速度与角速度可在回归模型中使用。在采集到的所有数据中由于智能车无线通讯系统由于并行处理其他任务而可能产生智能车反应缓慢，对于PS2手柄所发出的指令不能及时执行，从而使智能车存在静止状态，对此，在数据采集过程中对线速度与角速度标签全为0的数据进行删除。在实际采集状态下，智能车可能与异常值产生原因相同的原因和实际客观因素的影响下造成数据采集量的不同，为了避免后期模型在训练时由于先前数据集所存在的问题造成模型的过拟合或在实际部署过程中存在模型对实际运行环境感知错误的情况，所以对数据进行均衡化处理，使各个状态标签下的数据不产生数据量差距过大的情况，保证模型训练时训练数据的水平化，不造成模型训练结果的偏失。

(Labels divided according to the operating state can be used in the classification model. Because the absolute values of linear velocity and angular velocity are between 0 and 1, too much data is not processed, and linear velocity and angular velocity can be used in the regression model. In all the data collected, because the wireless communication system of the smart car may respond slowly to the intelligent car due to the parallel processing of other tasks, the instructions issued by the PS2 handle cannot be executed in time, so that the smart car is in a stationary state. In this regard, in the process of data collection, the line speed and angular velocity labels are all The data of 0 is deleted. In the actual acquisition state, the intelligent car may cause different data acquisition volume under the same reason as the abnormal value and under the influence of actual objective factors. In order to avoid the over-fitting of the model or the actual operation of the model during the actual deployment process due to problems in the previous data set during the actual deployment of the later model The environment perceives the wrong situation, so the data is balanced and processed, so that the data under each state label does not produce too much data volume gap, so as to ensure the horizontalisation of the training data during model training, and does not cause the deviation of the model training results.)

#### 4.3.2.3 行车数据处理系统(Driving data processing system)
结合上述行车图像处理与行车数据处理的处理方法，设计行车数据处理系统，方便由于不确定因素从而进行多次采样后的数据处理情况。图像数据与速度数据相互依赖又相互约束。设计行车数据并行处理系统流程
<div align=center>
<img width="400" alt="截屏2024-11-09 14 05 26" src="https://github.com/user-attachments/assets/43a18026-b28c-4726-881b-700170e14acb">
<img/></div>

(Combined with the above-mentioned processing methods of driving image processing and driving data processing, the driving data processing system is designed to facilitate the data processing after multiple sampling due to uncertainties. Image data and speed data are interdependent and constrained. Design the process of parallel processing system for driving data.)

当数据采集时，由于ROS系统与各个自身功能部件的协调使得在数据采集过程中图像数据与行车速度数据大致重合但还不精确，为了避免由于时间差问题从而导致模型训练时误差的累积，故在读取标签文本数据并进行四类标签转换和行车图像数据后，首先进行两者数据量的对比，并进行时间一致性检验，保留都为在同一时刻发生的数据，并在此时获取行车图像路径索引。并处理速度为0的无效数据以及数据均衡化处理。在整个智能车行驶中占比最高的为前进，向左前行驶和向右前行驶的数据，由于在数据采集过程中，存在智能车在进入弯道前的位置不适宜接下来的弯道行驶，需要原地对智能车的位置进行调整，所以才存在了占比较小的倒车/刹车，顺时针旋转和逆时针旋转的数据。由于这三种标签占比量较小，而且在三大标签进行速度交接时可以起到润滑平滑换的作用故保留当前三种标签，对占比较大的三类标签进行标签处理。得到的结果如表5所示。

(When data is collected, due to the coordination between the ROS system and each functional component of its own, the image data and the driving speed data roughly coincide but are not accurate during the data acquisition process. In order to avoid the accumulation of errors in model training due to the time difference problem, the label text data is read and four types of labels are carried out. After converting and driving image data, first compare the amount of data between the two, and carry out a time consistency test, retain the data that occurs at the same time, and obtain the driving image path index at this time. And process invalid data with a speed of 0 and data equalisation processing. The data that accounts for the highest proportion of the whole intelligent car driving is forward, driving to the left and driving to the right. Because in the data acquisition process, the position of the intelligent car before entering the curve is not suitable for the next curve, and the position of the intelligent car needs to be adjusted in place, so there is a relatively small reverse/ Data of braking, clockwise rotation and counterclockwise rotation. Because the proportion of these three labels is relatively small, and they can play a role in lubricating and smoothing when the three labels are handed over quickly, the current three labels are retained, and the three types of labels, which account for a relatively large proportion, are labelled. The results obtained are shown in Table 5.)

表5 数据均衡化处理前与处理后数据量对比
|动作|	处理前|	处理后|	动作	|处理前|	处理后|
|:---:| :---: | :---: |:---: | :---: |:---: |
|前进|4325|3304|倒车/刹车|9|9|
|向左前行驶|3484|3298|顺时针旋转|12|12|
|向右前行驶|3698|3300|逆时针旋转|32|32|

根据表5所示的占比最高的标签在数据均衡化后数据量相差不大，数据量基本均衡。数据均衡化的结果在经过需要删除数据名称的筛选和无效数据进行合并。在得到无效数据和均衡化要删除的图像名称后，图像根据无效数据和均衡化要删除的图像名对图像数据进行删除，删除后并再次进行两者数据量的比较和又一次的数据一致性检验。在此之后，图像数据进行数据增强，高斯模糊与灰度化，二值化与等比缩放，速度数据则根据标签进行分层抽样，并进行数据的划分得到速度数据的训练集与测试集，而后图像数据根据划分得到的训练集与测试集进行图像训练集与测试集的分类，在每组数据中进行分层抽样操作，并抽取30%作为测试集与剩下70%的数据作为训练集，最后将训练集与测试集进行打包形成最终的训练数据集与测试数据集。

(According to the label with the highest proportion shown in Table 5, the data volume is not much different after data equalisation, and the data volume is basically balanced. The results of data equalisation are merged after filtering of data names that need to be deleted and invalid data. After obtaining the invalid data and the image name to be deleted by equalisation, the image deletes the image data according to the invalid data and the image name to be deleted by equalisation. After deletion, the amount of data between the two is compared and another data consistency test is carried out again. After that, the image data is enhanced, Gaussian blur and greyscale, binary and isometric scaling, the speed data is stratified and sampled according to the label, and the training set and test set of the speed data are divided into data, and then the image data is trained according to the training set and test set obtained by the division. Classify with the test set, carry out hierarchical sampling in each set of data, and extract 30% as the test set and the remaining 70% of the data as the training set. Finally, the training set and test set are packaged to form the final training data set and test data set.)

# 5.自动驾驶功能实现与整合(Realisation and integration of autonomous driving function)
## 5.1 自动行车系统的设计与实现(Design and realisation of automatic driving system)
由于在实际的模型部署中，智能车运用模型对当前路况进行合理且快速的判断。因此建立起的自动行车模型架构不宜过大，模型应具备模型体量小且训练效果较好的特点，根据实际应用情况，本章节介绍了针对行车数据的分析以及英伟达端到端模型和LeNet-5模型的训练并选择最优模型作为智能车自动行驶模型解决方案。

(Because in the actual model deployment, the intelligent car uses the model to make a reasonable and fast judgement of the current road conditions. Therefore, the architecture of the established automatic driving model should not be too large. The model should have the characteristics of small model volume and good training effect. According to the actual application, this chapter introduces the analysis of driving data and the training of NVIDIA end-to-end model and LeNet-5 model, and selects the optimal model as an intelligent vehicle. Dynamic driving model solution.)

### 5.1.1 行车数据分析(Driving data analysis)
通过分析行车数据进一步提高模型训练的合理性，提高模型的准确率。首先行车数据采集围绕场景平台进行，通过获取PS2操控手柄的信号使智能车绕场景平台中的道路行驶，借助ROS平台中Obom功能包对智能车运行的足迹进行绘制.
<div align=center>
<img width="300" alt="截屏2024-11-09 14 06 56" src="https://github.com/user-attachments/assets/28de603c-9a4a-4c2a-9670-a9f90fe392c2">
<img/></div>

(By analysing driving data, the rationality of model training is further improved and the accuracy of the model is improved. First of all, the driving data collection is carried out around the scene platform. By obtaining the signal of the PS2 control handle, the intelligent car drives around the road in the scene platform, and the footprint of the intelligent car operation is drawn with the help of the Obom function package in the ROS platform.)

由于智能车只凭借Obom功能包进行方位采集，所以在进行数据可视化时产生了一定的误差。但在整体上，智能车完整的绕场景平台的道路进行行驶，没有产生在行车数据采集中由于没有完整的行驶而导致的数据偏颇。在模型开始训练前对行车图像数据进行归一化处理同时除以255以便减轻计算平台压力进一步提高训练效率，对于行车速度数据则需要选择适合的数据类型，通过将采集的一组行车速度数据进行可视化.
<div align=center>
<img width="300" alt="截屏2024-11-09 14 07 13" src="https://github.com/user-attachments/assets/7358d2f2-707a-40bd-89c2-212402219bef">
<img/></div>

(Because smart cars only rely on the Obom function package for amuth acquisition, there are certain errors in data visualisation. However, on the whole, the intelligent car drives completely around the road of the scene platform, and there is no data bias caused by the lack of complete driving in the driving data collection. Before the model starts training, the driving image data is normalised and divided by 255 to reduce the pressure of the computing platform and further improve the training efficiency. For the driving speed data, it is necessary to select a suitable data type and visualise the collected set of driving speed data.)

通过可视化下的行车速度可以更加直观的看到在行车速度数据集中线速度与角速度的分布情况。由于在设定线速度与角速度时，设定的基础速度为0.25与0.5所以使得线速度与角速度在图像存在上界，又由于设定的速度并不激进以及智能车大部分情况为前进运行，所以在线速度上没有出现负值。在角速度上由于存在弯道等运行情况或者由于默认速度设置相对保守使得转弯半径过大就会出现线速度为0从而只有角速度原地调整智能车车头朝向。在出弯道调整或正常行驶过程中发生车辆发生偏移从而修正车身，通过修正的幅度大小而导致了角速度相比于线速度有更多的随机性。线速度与角速度都由PS2操作手柄进行控制其遥杆量的大小为线形分布，但在可视化线速度与角速度图中由于基础速度设定的限制也可看作是智能车四个方向速度的分解只不过智能车动作幅度的大小取决于每个方向上速度存在的时间。针对上述两种情况分别建立对应的回归模型与分类模型进行验证并在择优的基础上进行进一步的优化。

(Through the visualisation of the driving speed, the distribution of line speed and angular speed in the driving speed data set can be seen more intuitively. Because when setting the linear speed and angular velocity, the set basic speed is 0.25 and 0.5, so the linear speed and angular velocity have an upper bound in the image. Because the set speed is not radical and the intelligent car is running forward in most cases, there is no negative value on the online speed. In terms of angular velocity, due to the existence of curves and other operating conditions, or because the default speed setting is relatively conservative, the turning radius is too large, the line speed will be 0, so that only the angular velocity can adjust the front direction of the intelligent car in place. During the curve adjustment or normal driving, the vehicle shifts and the body is modified. Through the size of the correction, the angular velocity is more random than the linear speed. The linear speed and angular velocity are both controlled by the PS2 operating handle. The size of the remote bar is linearly distributed, but in the visual linear speed and angular velocity diagram, due to the limitation of the basic speed setting, it can also be regarded as the decomposition of the four-direction speed of the smart car, but the size of the action amplitude of the smart car depends on the existence of the speed in each direction. The time of. For the above two situations, the corresponding regression model and classification model are established for verification and further optimisation is carried out on the basis of selection.)

### 5.1.2 行车模型的建立(The establishment of driving models)
#### 5.1.2.1 英伟达端到端模型(NVIDIA end-to-end model)
英伟达端到端模型（NVIDIA end-to-end Model）是通过整合硬件和软件来实现人工智能任务端到端优化，且建立在英伟达GPU架构上利用并行计算能力加速深度学习、机器学习等任务的一种模型。在英伟达端到端模型中神经网络输入的为原始图片，神经网络输出的为直接控制指令。由于在神经网络中每一个部分对于系统都起特征提取和控制的作用使得特征提取层和控制输出层的分界不明显。英伟达端到端模型其基本的模型结构由卷基层与全链接层组成。在基本结构中神经网络的第一层使用归一化层对输入的数据进行归一化操作，对输入数据的每一个纬度都除以255并加上负0.5，将所有元素归一到负0.5到正0.5中，第一层不涉及学习过程。而后共有五个卷积层，其中前三层有的卷积核个数逐层增加分别是24个，36个和48个，选择了大小为5的卷机核和大小为2的步长，后两层每层共有64个卷积核选择了大小为3的卷积核但没有设定步长大小。后三层为全连接层每一层神经元个数分别是250个，50个和2个。其中除最后一层的激活函数以外，其余层的激活函数都为指数线性单元激活函数（elu）,关于卷积核与步长的设定英伟达并没有做过多的解释。在实际应用中针对典型参数进行尝试并选择效果较好的参数，但可能无法给出合理的解释。由于卷积核数量逐层增多使得提取出的图像特征越通用，进一步保留图像的准确特征，方便图像的进一步训练。
<div align=center>
<img width="400" alt="截屏2024-11-09 14 07 24" src="https://github.com/user-attachments/assets/47ab6a99-70f4-4dc2-972e-e5bf5318ddf0">
<img/></div>

(NVIDIA end-to-end Model is a model that realises end-to-end optimisation of artificial intelligence tasks by integrating hardware and software, and uses parallel computing power to accelerate deep learning, machine learning and other tasks based on NVIDIA GPU architecture. In the NVIDIA end-to-end model, the neural network inputs the original picture, and the neural network outputs the direct control instructions. Because each part of the neural network plays the role of feature extraction and control for the system, the boundary between the feature extraction layer and the control output layer is not obvious. The basic model structure of the NVIDIA end-to-end model consists of a volume base and a full link layer. In the basic structure, the first layer of the neural network uses the normalisation layer to normalise the input data. Each latitude of the input data is divided by 255 and minus 0.5 is added to normalize all elements from negative 0.5 to positive 0.5. The first layer does not involve the learning process. Then there are five convolutional layers, of which the number of convolutional nuclei in the first three layers increases by layer to 24, 36 and 48 respectively. The winding nucleus with a size of 5 and the step length of 2 are selected. There are a total of 64 convolutional nuclei in each layer of the latter two layers. The convolutional core with a size of 3 is selected but the step length size is not set. The last three layers are fully connected layers, and the number of neurons in each layer is 250, 50 and 2 respectively. Among them, except for the activation function of the last layer, the activation functions of the remaining layers are exponential linear unit activation functions (elu), and NVIDIA has not explained much about the setting of convolutional nucleus and step length. In practical application, try to target the typical parameters and select the parameters with better effect, but it may not be possible to give a reasonable explanation. Due to the increase in the number of convolutional nuclei layer by layer, the more general the extracted image features are, which further preserves the accurate features of the image and facilitates the further training of the image.)

以英伟达端到端模型为基础进一步改进此模型，使改进的模型更好的适用于行车图像数据。由于模型结构在较为复杂的情况下造成模型的过拟合现象，又由于全连接神经网络中参数较多容易导致发生模型过拟合。所以在最后一层卷积层后加入了抛弃率为50%的Dropout层，并将三层的全连接神经网络去除中间一层的隐藏层，根据模型实际的任务情况对最后一层的输出层神经元个数与激活函数进行更改。

(This model is further improved based on the NVIDIA end-to-end model, so that the improved model is better applicable to driving image data. Because the model structure causes the over-sitting phenomenon of the model under relatively complex circumstances, and because there are more parameters in the fully connected neural network, it is easy to cause the over-sitting of the model. Therefore, after the last convolution layer, the Dropout layer with an abandonment rate of 50% is added, and the three-layer fully connected neural network removes the hidden layer of the middle layer, and the number of output layer neurons and activation functions of the last layer are changed according to the actual task situation of the model.)

### 5.1.2.2 LeNet-5模型(LeNet-5 model)
LeNet-5模型是一种早期的卷积神经网络模型，由Yann Lecun等人于1990年开发，起初LeNet-5模型主要用于手写数字识别任务，但由于其具有很好的任务分类效果，后广泛使用于图像识别任务中。LeNet-5模型是深度学习和计算机视觉领域的里程碑之一，其结构为后来的深度学习提供了重要参考。在手写数字识别中，LeNet-5模型架构共有7层。第一层为卷积层，共有6个大小为5的卷积核,第二层为池化层，平均池化层大小设定为2。第三层同样为卷积层，卷积层由16个大小为5的卷积核构成。第四层由大小为2的平均池化层构成。第五层由120个大小为5的卷积核构成，最后两层大小分别为84和10的全连接层构成。通过不断的进行卷积操作以及池化操作使得模型尽最大可能使图像特征保留下来，提高图像特征提取效果，帮助模型进行训练,其中除最后输出层以外，都为修正线性单元激活函数（relu）。LeNet-5模型结构如图。
<div align=center>
<img width="400" alt="截屏2024-11-09 14 07 32" src="https://github.com/user-attachments/assets/5599400b-b99b-4d22-8d84-3936e2d33a45">
<img/></div>

(The LeNet-5 model is an early convolutional neural network model developed by Yann Lecun and others in 1990. At first, the LeNet-5 model was mainly used for handwritten digital recognition tasks, but because of its good task classification effect, it was later widely used in image recognition tasks. The LeNet-5 model is one of the milestones in the field of deep learning and computer vision, and its structure provides an important reference for later deep learning. In handwritten digital recognition, the LeNet-5 model architecture has a total of 7 layers. The first layer is a convolutional layer, with a total of 6 convolutional nuclei with a size of 5. The second layer is a pooled layer, and the average pooled layer size is set to 2. The third layer is also a convolutional layer, which is composed of 16 convolutional nuclei of size 5. The fourth layer is composed of an average pooled layer of 2 in size. The fifth layer is composed of 120 convolutional nuclei of size 5, and the last two layers are composed of full connection layers of size 84 and 10 respectively. Through continuous convolution operation and pooling operation, the model can retain the image features as much as possible, improve the image feature extraction effect, and help the model train. In addition to the final output layer, the linear unit activation function (relu) is modified. The structure of the LeNet-5 model is shown in the figure.)

根据当前所要进行的分类任务与回归任务对模型结构进行改造。图像经过数据处理中等比缩放的变换，大小从480*640转换到150*200，根据当前图像大小适当扩大了每一层卷积核的个数。第一层卷积核从原先6个增加为16个，第三层卷积核从原先16个减少到64个。后在实际训练过程中根据不同的训练任务对最后一层的输出神经元个数与激活函数进行更改。

(Transform the model structure according to the current classification tasks and regression tasks. The image is transformed by medium ratio scaling in data processing, and the size is converted from 480*640 to 150*200, and the number of convolutional nuclei of each layer is appropriately expanded according to the current image size. The first convolutional nucleus increased from the original 6 to 16, and the third convolutional nucleus decreased from the original 16 to 64. Later, during the actual training process, the number of output neurons and activation functions of the last layer are changed according to different training tasks.)

### 5.1.3 行车模型的训练(Training of driving models)
#### 5.1.3.1 英伟达端到端回归模型的训练(Training of NVIDIA's end-to-end regression model)
构建英伟达端到端回归模型并训练，由于训练数据为回归任务，将模型最后一层输出神经元个数设置为两个，激活函数选用线性回归单元激活函数(linear)。为了方便评判模型回归的拟合程度所以将损失函数设定为均方误差，优化器选用自适应矩估计(adam)作为最小化损失函数并选用平均绝对误差作为模型的评估指标。设定模型学习率为0.000001，对数据集进行600次迭代，每次迭代的样本大小为300，并用测试集的数据与标签计算模型效果。根据测试集的平均绝对误差作为模型早停依据，避免模型发生过拟合，提高训练效率。如图49和图50分别为回归模型训练时的损失值与平均绝对误差的变化情况。
<div align=center>
<img width="250" alt="截屏2024-11-09 14 07 48" src="https://github.com/user-attachments/assets/e48f3b8e-2f69-4316-8013-6dbb22ef2203">
<img width="250" alt="截屏2024-11-09 14 07 57" src="https://github.com/user-attachments/assets/5f0ae770-9cdd-4022-8b0b-22f0b8646efb">
<img/></div>

(Build an end-to-end regression model of NVIDIA and train it. Since the training data is a regression task, the number of output neurons in the last layer of the model is set to two, and the activation function selects the linear regression unit activation function (linear). In order to facilitate the judgment of the fit of the model regression, the loss function is set to the mean square error. The optimiser selects the adaptive moment estimate (adam) as the minimum loss function and the average absolute error as the evaluation index of the model. Set the model learning rate to 0.000001, perform 600 iterations on the data set, the sample size of each iteration is 300, and calculate the model effect with the data and labels of the test set. Based on the average absolute error of the test set as the basis for the early stop of the model, avoid the fitting of the model and improve the training efficiency. For example, Figure 49 and Figure 50 are the changes in the loss value and the average absolute error during regression model training respectively.)

根据回归模型损失值变化与回归模型平均绝对误差变化可以看到，在训练过程中由于使用自适应矩估计作为优化函数，模型在开始训练后验证集与测试集的损失值快速下降，且在前50次训练中测试集的损失值下降幅度远远大于训练集的下降幅度。训练集与测试集在50次训练后二者下降趋势变缓，但整体为下降趋势。在平均绝对误差中，测试集与训练集的下降趋势与损失值变化相同，训练集与测试集的平均绝对误差随着训练模型下降速度变缓，并最终达到模型早停设定条件，模型训练结束。

(According to the change of the loss value of the regression model and the change of the average absolute error of the regression model, it can be seen that during the training process, due to the use of adaptive moment estimation as the optimisation function, the loss value of the verification set and the test set of the model decreased rapidly after the start of the training, and the loss value of the test set in the first 50 trainings decreased much greater than The decline of the training set. The downward trend of the training set and the test set slowed down after 50 training sessions, but the overall trend was downward. In the average absolute error, the downward trend and loss value of the test set and the training set are the same. The average absolute error of the training set and the test set slows down with the speed of decline of the training model, and finally reaches the setting conditions set by the model early stop, and the model training ends.)

#### 5.1.3.2 英伟达端到端分类模型的训练(Training of NVIDIA's end-to-end classification model)
构建英伟达端到端分类模型并训练，标签为多分类任务的九维数组，且训练任务为分类任务，所以将模型最后一层输出层的神经元个数设置为9，激活函数选用归一化指数函数(softmax)。模型损失函数选用分类交叉熵，由于随机梯度下降算法在实际表现中不如亚当优化算法(adam)，所以优化器选用亚当优化算法并约束学习率为0.000001。模型评估指标选用准确率作为判断依据，对数据集进行600次迭代，样本批次大小设定为600，并用测试集的数据与标签计算模型效果，为保证模型训练不发生过拟合现象故加入早停使模型在训练达到验证集准确率最高的情况下暂停训练。
<div align=center>
<img width="250" alt="截屏2024-11-09 20 17 18" src="https://github.com/user-attachments/assets/a6ab18b2-1125-4a45-b771-ae9227385c24">
<img width="250" alt="截屏2024-11-09 20 17 26" src="https://github.com/user-attachments/assets/31de86d4-a228-4409-b05e-0358f9b78f18">
<img/></div>

(Build an end-to-end classification model of NVIDIA and train it. The label is a nine-dimensional array of multi-classification tasks, and the training task is a classification task. Therefore, the number of neurons in the last output layer of the model is set to 9, and the activation function selects the normalised exponential function (softmax). The model loss function selects classified cross-entropy. Because the stochastic gradient descent algorithm is not as good as the Adam optimisation algorithm (adam) in actual performance, the optimiser chooses the Adam optimisation algorithm and constrains the learning rate to 0.000001. The model evaluation index selects the accuracy rate as the basis for judgement. The data set is iterated 600 times, the sample batch size is set to 600, and the model effect is calculated with the data and labels of the test set. In order to ensure that the model training does not have a fitting phenomenon, early stop is added to make the model achieve the highest accuracy rate of the verification set in training. Moreover, the training is suspended.)

根据分类模型损失值变化与准确率变化可知，在训练过程中分类模型的损失值在第50次训练左右降低到最小。在准确率变化中，测试集的准确率在第6次左右训练达到了一个小高峰，而后模型不断的训练使测试集的准确率下降并最终随着训练不断上升，最终达到最高值，训练集的准确率则是随训练次数的不断训练逐渐上升，并在最终达到稳定不在发生较大变化。由于模型设置了训练早停使的在第50次训练后停止训练，测试集准确率不在发生变化。模型训练结束。

(According to the change of the loss value and accuracy of the classification model, it can be seen that the loss value of the classification model is reduced to the minimum around the 50th training during the training. In the change of accuracy rate, the accuracy rate of the test set reached a small peak around the 6th training, and then the continuous training of the model reduced the accuracy of the test set and finally reached the highest value with the continuous training. The accuracy rate of the training set gradually increased with the continuous training of the number of trainings, and finally reached There is no major change in stability. Because the model sets the training to stop early and stop training after the 50th training, the accuracy rate of the test set does not change. The model training is over.)

#### 5.1.3.3 LeNet-5回归模型的训练(Training of LeNet-5 regression model)
构建LeNet-5回归模型并训练，由于训练结果为连续型变量。模型最后一层输出层的个数应为两个神经元，且激活函数为线性激活函数(linear)。模型设置损失函数为均方误差，优化器选用亚当优化算法，为了避免学习速度过快而造成过拟合现象，故将优化器的学习率设定为0.000001，模型训练效果选用平均绝对误差作为判断依据。并对模型进行600次训练，每次训练样本大小设定为300。并用测试集的数据与标签计算模型效果，并根据测试集的平均绝对误差设置模型早停条件。
<div align=center>
<img width="250" alt="截屏2024-11-09 20 17 34" src="https://github.com/user-attachments/assets/a91b58c7-dc3d-4505-bbab-473f81de03dc">
<img width="250" alt="截屏2024-11-09 20 17 41" src="https://github.com/user-attachments/assets/660cf8b1-24e7-4862-ac66-366db15dc3fa">
<img/></div>

(Build and train the LeNet-5 regression model, because the training results are continuous variables. The number of output layers in the last layer of the model should be two neurons, and the activation function should be linear. The model sets the loss function as the mean square error, and the optimiser chooses the Adam optimisation algorithm. In order to avoid the over-fitting phenomenon caused by too fast learning speed, the learning rate of the optimiser is set to 0.00000, and the average absolute error of the model training effect is selected as the basis for judgement. And the model is trained 600 times, and the sample size of each training is set to 300. And calculate the effect of the model with the data and labels of the test set, and set the early stop conditions of the model according to the average absolute error of the test set.)

根据训练历史的可视化可以看到，由于模型在训练过程中加入早停，使得当训练集的平均绝对误差达到最低并持续一段时间后模型停止训练。其中训练集与测试集的损失函数不断下降，下降率随着不断训练逐渐变缓直到停止训练。训练集与测试集的平均绝对误差也伴随训练不断下降，并在最后达到最
低。平均绝对误差下降率也随着不断训练逐渐变缓直到停止训练，模型训练结束。

(According to the visualisation of the training history, it can be seen that because the model adds early stop during the training process, when the average absolute error of the training set reaches the lowest and lasts for a period of time, the model stops training. Among them, the loss function of the training set and the test set continues to decline, and the decline rate gradually slows down with continuous training until the training is stopped. The average absolute error of the training set and the test set also decreases with the training and reaches the minimum in the end. The average absolute error decrease rate also gradually slows down with continuous training until the training is stopped and the model training is over.)

#### 5.1.3.4 LeNet-5分类模型的训练(Training of LeNet-5 classification model)
构建LeNet-5分类模型的训练，每组标签为九维数组。根据标签纬度将最后一层设定为9个输出神经元，选用归一化指数函数(softmax)作为激活函数，由于标签属于多分类类型，故使用分类交叉熵作为损失函数，为了避免模型在训练过程中发生过拟合现象，设置模型训练早停，以测试集准确率的最大值作为早停依据，并采用亚当优化算法作为优化函数，设置学习率为0.000001。模型评估指标选用准确率作为判断依据，对数据集进行600次迭代，故每次迭代的样本批次大小设定为600，并用测试集的数据与标签计算模型效果从而体现模型训练的准确度。
<div align=center>
<img width="250" alt="截屏2024-11-09 20 18 05" src="https://github.com/user-attachments/assets/135c2264-ee0a-45f5-98f9-19db610b4739">
<img width="250" alt="截屏2024-11-09 20 18 12" src="https://github.com/user-attachments/assets/4e5bbcf0-3d84-4571-a103-ac277c0cfb2a">
<img/></div>

(The training of building a LeNet-5 classification model, each group of labels is a nine-dimensional array. According to the label latitude, the last layer is set to 9 output neurons, and the normalised exponential function (softmax) is selected as the activation function. Because the label belongs to the multi-classification type, the classification cross-entropy is used as the loss function. In order to avoid the fitting phenomenon of the model during the training process, the model training is set up. Early stop, take the maximum value of the accuracy of the test set as the basis for early stop, and use the Adam optimisation algorithm as the optimisation function, and set the learning rate to 0.000001. The model evaluation index selects the accuracy rate as the basis for judgement, and the data set is iterated 600 times. Therefore, the sample batch size of each iteration is set to 600, and the data and labels of the test set are used to calculate the model effect to reflect the accuracy of model training.)

在LeNet-5分类模型的训练中，当训练集的准确率达到最高并持续一段时间的情况下为了避免发生过拟合的现象，训练发生早停。在LeNet-5分类模型损失值变化中，测试集的变化情况与训练集相同，并随训练次数的不断增加二者的损失值不断下降。在LeNet-5分类模型准确率变化中模型在训练到第10次左右时模型在测试集与训练集的准确率快速增高，并在第30次左后测试集和训练集的准确率上升到较高位置，上升速度逐渐变缓，且二者变化情况相同，测试集与训练集的准确率随着不断的训练逐渐增高并保持，模型训练结束。

(In the training of the LeNet-5 classification model, when the accuracy of the training set reaches the highest and lasts for a period of time, in order to avoid the phenomenon of fitting, the training stops early. In the change of the loss value of the LeNet-5 classification model, the change of the test set is the same as that of the training set, and the loss value of the two decreases with the increase of the number of trainings. In the change of the accuracy rate of the LeNet-5 classification model, when the model is trained to about the 10th time, the accuracy rate of the test set and the training set of the model increases rapidly, and the accuracy rate of the left test set and training set rises to a higher position in the 30th time. The rise rate gradually slows down, and the change of the two is the same. The test set and The accuracy of the training set gradually increases and is maintained with continuous training, and the model training ends.)

### 5.1.4 行车模型的选取(Selection of driving models)
#### 5.1.4.1 模型评判依据(The basis for model judgement)
在线速度与角速度回归任务中，选用平均绝对误差(Mean Absolute Error, MAE)和均方误差(Mean Squared Error, MSE)作为回归任务的主要评判标准。其中平均绝对误差可以帮助评估回归模型的准确性，得到预测结果与实际观测值之间的平均绝对偏差，且对异常值的鲁棒性表象较好，不会因为某个极端异常值的存在而使误差值被放大。均方误差通过计算预测值与实际观测值之间的平方差的平均值来衡量预测误差的大小，方便模型根据均方误差结果进行参数调整，但对于异常值比平均绝对误差较敏感，从而对结果造成影响。在速度差分的分类任务中，选用准确率(Accuracy，Acc)作为模型评判的依据。准确率对于分类任务是常用评估标准之一，通过更加直观的反应正确预测的样本数量占总样本数量的比例使得人们可以更快的理解，在整体表现上反应模型的准确率，通过准确率的比较从而选择最佳模型。

(In the online speed and angular velocity regression tasks, Mean Absolute Error (MAE) and Mean Squared Error (MSE) are selected as the main judgement criteria for the regression task. Among them, the average absolute error can help to evaluate the accuracy of the regression model, obtain the average absolute deviation between the predicted results and the actual observation value, and the robustness of the outlier value is better, and the error value will not be amplified due to the existence of an extreme outlier. The mean square error measures the size of the predicted error by calculating the average of the square difference between the predicted value and the actual observed value, which is convenient for the model to adjust the parameters according to the mean square error results, but the abnormal value is more sensitive than the average absolute error, thus affecting the result. In the classification task of speed difference, accuracy (Accuracy, Acc) is selected as the basis for model judgement. Accuracy is one of the common evaluation criteria for classification tasks. Through a more intuitive response, the proportion of the number of samples correctly predicted to the total number of samples enables people to understand faster. In terms of overall performance, the accuracy of the model is reflected, and the best model is selected through the comparison of accuracy.)

#### 5.1.4.2 模型评判(Model judgement)
基于英伟达端到端模型和LeNet-5模型两种基本模型分别根据不同训练任务进行了模型的训练。分别训练出了两种任务，两种架构的四种模型。为了进一步选择出实现智能车自动行驶的最优模型，将对这四种模型结合模型判断依据中的标准以及训练时间，模型大小，模型实际效果等几个纬度对模型进行比较。在英伟达端到端回归模型和LeNet-5回归模型训练中，在保证参数相似，训练环境相同的情况下进行两种模型的比较，英伟达端到端回归模型与LeNet-5回归模型训练结果如表所示。

(The two basic models based on the NVIDIA end-to-end model and the LeNet-5 model are trained according to different training tasks. Two tasks and four models of two architectures have been trained respectively. In order to further select the optimal model to realise the automatic driving of intelligent vehicles, these four models will be compared with the standards in the basis of model judgement and several latitudes such as training time, model size, and actual effect of the model. In the training of NVIDIA's end-to-end regression model and LeNet-5 regression model, the two models are compared under the condition that the parameters are similar and the training environment is the same. The training results of NVIDIA's end-to-end regression model and LeNet-5 regression model are shown in the table.)

表6 两种回归类模型的训练结果比较
|模型类别|MSE|MAE|训练批次占比|
|:---:| :---: | :---: |:---: | 
|英伟达端到端回归模型|0.010790275|0.046966029|158/600|
|LeNet-5回归模型|0.011214698|0.052184216|340/600|

在两种回归类模型的训练比较中，LeNet-5回归模型的均方误差为0.011214698大于英伟达端到端回归模型的均方误差值0.010790275，而在平均绝对误差中LeNet-5回归模型也大于英伟达端到端回归模型的结果，在每批训练时间相似的情况下，英伟达端到端回归模型的训练时间要远远小于LeNet-5回归模型的训练时间。在英伟达端到端分类模型和LeNet-5分类模型训练中，在保证参数相似，训练环境相同的情况下进行两种模型的比较，英伟达端到端分类模型与LeNet-5分类模型训练结果如表所示。

(In the training comparison of the two regression models, the mean square error of the LeNet-5 regression model is 0.011214698, which is greater than the mean square error value of the NVIDIA end-to-end regression model is 0.010790275, and in the average absolute error, the LeNet-5 regression model is also greater than the NVIDIA end. As a result of the end-to-end regression model, under the condition that the training time of each batch is similar, the training time of the NVIDIA end-to-end regression model is much less than the training time of the LeNet-5 regression model. In NVIDIA's end-to-end classification model and LeNet-5 classification model training, the two models are compared under the condition that the parameters are similar and the training environment is the same. The training results of NVIDIA's end-to-end classification model and LeNet-5 classification model are shown in the table.)

表7 两种分类模型的训练结果的比较
|模型类别|ACC|训练批次占比|
|:---:| :---: | :---: |
|英伟达端到端分类模型|0.97969496|52/600|
|LeNet-5分类模型|0.94803104|41/600|

在英伟达端到端分类模型与LeNet-5分类模型的比较中，LeNet-5分类模型的准确率为0.94803104小于英伟达端到端分类模型的准确率0.97969496。且两种模型单次训练时间相似，其中LeNet-5分类模型的训练批次占比小于英伟达端到端分类模型，LeNet分类模型的训练速度更快。由于智能车所存在的算力资源一定的情况下，占用计算资源较小的模型会提高计算频率从而提高识别效率，针对四种模型进行内存资源占用上的比较。

(In the comparison of NVIDIA's end-to-end classification model and LeNet-5 classification model, the accuracy rate of LeNet-5 classification model is 0.94803104, which is less than that of NVIDIA's end-to-end classification model.0.97969496. And the single training time of the two models is similar. Among them, the proportion of training batches of the LeNet-5 classification model is smaller than that of the NVIDIA end-to-end classification model, and the training speed of the LeNet classification model is faster.Due to the certain amount of computing power resources in intelligent vehicles, models that occupy less computing resources will increase the computing frequency and thus improve the recognition efficiency, and compare the memory resource occupation of the four models.)

表8 四种模型内存空间占比
|模型类别|内存占比|模型类别|内存占比|
|:---:| :---: | :---: |:---: | 
|英伟达端到端回归模型|41.20MB|英伟达端到端分类模型|43.13MB|
|LeNet-5回归模型|83.66MB|LeNet-5分类模型|83.67MB|

根据表8中的数据可以清晰的看到，LeNet-5为基础的模型比英伟达端到端为基础的模型内存占用高，在相同任务的情况下，LeNet-5模型要比英伟达端到端模型多大约40MB内存空间，这主要由于模型架构的区别，当模型架构相似时，更多的卷积层可以使数据快速降低纬度，数据在通往后续的全连接层时，全连接层训练所需的参数数量相应减少。且在基础模型相同的情况下，分类模型由于最后一层的神经元个数比回归多，分类模型的内存占用比回归模型高，在LeNet-5的分类模型与回归模型的比较中，分类模型只比回归模型内存占用多0.01MB。但在英伟达端到端模型中，分类模型比回归模型内存占用多1.93MB。

(According to the data in Table 8, it can be clearly seen that the LeNet-5-based model occupies more memory than the NVIDIA end-to-end-based model. In the same task, the LeNet-5 model has about 40MB more memory space than the NVIDIA end-to-end model, which is mainly due to the area of the model architecture. No, when the model architecture is similar, more convolutional layers can make the data quickly reduce the latitude. When the data leads to the subsequent full connection layer, the number of parameters required for full connection layer training is correspondingly reduced. And under the same condition that the basic model, because the number of neurons in the last layer of the classification model is more than that of regression, the memory occupation of the classification model is higher than that of the regression model. In the comparison between the classification model of LeNet-5 and the regression model, the classification model only occupies 0.01MB more memory than that of the regression model. However, in the NVIDIA end-to-end model, the classified model occupies 1.93MB more memory than the regression model.)

### 5.1.5 行车模型的实现与改进(The realisation and improvement of the driving model)
#### 5.1.5.1 行车模型的实现(The realisation of the driving model)
在进行了模型训练结果的数据对比与分析下，为了进一步加强对模型实际场景下的验证，分别将四种模型进行实际部署，通过行车轨迹采集系统对四种模型再一次的进行比较，车辆轨迹可以很好的反应出智能车在实际情况中的运行状态。更好的体现出智能车模型识别的稳定性与准确性。
<div align=center>
<img width="250" alt="截屏2024-11-09 20 20 48" src="https://github.com/user-attachments/assets/efafbd9f-d805-4eb3-a455-0a0ed35faf82">
<img width="250" alt="截屏2024-11-09 20 20 56" src="https://github.com/user-attachments/assets/01621c82-e072-46d2-924e-4ee41e221e3f">
<img/></div>
<div align=center>
<img width="250" alt="截屏2024-11-09 20 21 07" src="https://github.com/user-attachments/assets/ef0ef135-8225-47f9-a018-031a6261b0e1">
<img width="250" alt="截屏2024-11-09 20 21 13" src="https://github.com/user-attachments/assets/b63a205a-bd5f-40b3-a642-f717a11d861c">
<img/></div>

(Under the data comparison and analysis of the model training results, in order to further strengthen the verification of the actual scenario of the model, the four models are actually deployed respectively, and the four models are compared again through the driving trajectory acquisition system. The vehicle trajectory can well reflect the operation of intelligent vehicles in the actual situation. Line status. It better reflects the stability and accuracy of intelligent car model recognition.)

车轨迹采集系统为单传感器收集数据，所以在智能车车头朝向会存在误差，由于车头朝向数据的偏差，导致起始位置与结束位置不重合。但智能车在实际车道中的表现并没有由于误差而造成消失。模型部署的实际效果主要是智能车在直行车道中的稳定性以及智能车在行驶弯道时的表现，主要评判标准为在直行车道中智能车蛇形运动幅度的大小，造成蛇形运动的产生主要分为两个方面，其一是在进行数据处理时缩小了感受域，导致模型只针对处理后的感受域做出判断，不能结合未来道路的变化进行提前的判断来及时修正车身，使车身修正幅度过大。其二，智能车在道路行驶所占据的位置很大程度上决定了智能车是否修正当前车身。当出现弯道时，智能车入弯位置很大程度上决定了智能车出弯位置，当智能车在不合适的出弯位置时，智能车这时就会进行车身姿态的修正，由于在实际计算平台中需要结合智能车有限的算力进行判断，所以识别频率受到限制，导致智能车在修正车身后不能及时的辨别智能车当前位置，使辨别速度与实际情况产生滞后效果，最终使智能车陷入不断的车身姿态修正过程中。在上图四种模型中，红色圈内是智能车在不同模型模型下的行驶轨迹。其中英伟达端到端类模型中，回归模型比分类模型所产生的轨迹更加平滑。但结合真实的汽车行驶情况中，车辆在道路上行驶与车道的位置事实上并不是保持相对单一的位置，而是根据实际情况下对车辆在车道中的位置进行实时的修正。这种修正会随着速度的变化导致修正幅度的改变。在低速行驶中，车辆可以在很短的时间内实现很大幅度的修正范围，但在高速行驶中，车辆要实现与低速行驶中相同的修正幅度，需要的修正时间要远远大于车辆在低速下修正所需的时间。出于安全考虑的真实情况下，虽然两种算法都达到了可判断自行行驶的效果，但英伟达端到端分类模型的实际行驶效果要优于英伟达端到端回归模型。英伟达端到端分类模型的调整次数少且幅度小，调整精确。LeNet-5模型中，LeNet-5回归模型在直行道路的稳定性明显优于LeNet-5分类模型。LeNet-5回归模型的调整幅度更小且调整次数明显小于LeNet-5分类模型。英伟达端到端模型总体优于LeNet-5模型行驶的轨迹。智能车对弯道的识别行驶也是评判四种模型识别道路准确性的参考依据，智能车在行驶弯道中所呈现的轨迹越平滑，表明模型在合适的入弯位置识别并做出了正确的判断。在绿色圈内，为一个连续弯道，连续的弯道可以反应出模型对于快速变化的路况是否可以做出及时的正确调整，如果智能车处于不利于进入弯道的位置，则会导致智能车在通过弯道时驶出车道，或使智能车在弯道中进行调整造成时间的浪费。根据上图中四个模型在连续弯道中的表现，英伟达端到端回归模型的轨迹相比于英伟达端到端分类模型轨迹更加平滑，但智能车在通过第一个弯道后，在进入第二个弯道时，英伟达端到端回归模型车头指向性不如英伟达端到端分类模型车头的指向性更加清晰。而在LeNet-5模型中，LeNet-5回归模型在连续弯道的行驶轨迹比LeNet-5分类模型的行驶轨迹更加平滑，且LeNet-5分类模型在第一个弯道中进行车头非平滑的调整，虽然使智能车最终保持到了车道内，但因此浪费了更多的时间。最终在行驶到第二个弯道时，LeNet-5分类模型车头的指向不如LeNet-5回归模型车头指向性明确。英伟达端到端分类模型和LeNet-5回归模型轨迹明显优于剩余的两种模型。 

(The vehicle trajectory acquisition system collects data for a single sensor, so there will be an error in the direction of the front of the intelligent car. Due to the deviation of the front direction data, the starting position and the end position do not coincide. However, the performance of smart cars in the actual lane has not disappeared due to errors. The actual effect of the model deployment is mainly the stability of the intelligent car in the straight lane and the performance of the intelligent car in the curve. The main criterion for judging is the magnitude of the snake-shaped movement of the intelligent car in the straight lane. The resulting snake-shaped movement is mainly divided into two aspects, one is to narrow the feeling during data processing. As a result, the model only makes judgements based on the processed sensing domain, and cannot make advance judgements in combination with future road changes to correct the car body in time, so that the body correction is too large. Second, the position occupied by the intelligent car on the road greatly determines whether the intelligent vehicle modifies the current body. When a curve appears, the cornering position of the intelligent car largely determines the cornering position of the intelligent car. When the intelligent car is in an inappropriate cornering position, the intelligent car will correct the body posture at this time. Because it needs to be judged in combination with the limited computing power of the intelligent car in the actual computing platform, the recognition frequency is limited. As a result, the intelligent car cannot distinguish the current position of the intelligent car in time after modifying the body, which causes the discrimination speed and actual situation to have a lag effect, and finally makes the intelligent car fall into the process of continuous body posture correction. Among the four models in the figure above, the red circle is the driving trajectory of the intelligent car under different models. Among them, in NVIDIA's end-to-end class model, the regression model is smoother than the trajectory generated by the classification model. However, in combination with the actual driving situation of the car, the position of the vehicle on the road and the lane does not actually maintain a relatively single position, but corrects the position of the vehicle in the lane in real time according to the actual situation. This kind of correction will lead to a change in the amplitude of the correction with the change of speed. In low-speed driving, the vehicle can achieve a large correction range in a short time, but in high-speed driving, the vehicle needs to achieve the same correction amplitude as in low-speed driving, and the correction time required is much longer than the vehicle to correct at low speed. In the real situation for safety reasons, although both algorithms have achieved the effect of judging self-driving, the actual driving effect of NVIDIA's end-to-end classification model is better than that of NVIDIA's end-to-end regression model. The number of adjustments of NVIDIA's end-to-end classification model is small and the magnitude is small, and the adjustment is accurate. In the LeNet-5 model, the stability of the LeNet-5 regression model on the straight road is obviously better than that of the LeNet-5 classification model. The adjustment range of the LeNet-5 regression model is smaller and the number of adjustments is significantly less than that of the LeNet-5 classification model. The NVIDIA end-to-end model is generally superior to the LeNet-5 model. The recognition of curves by intelligent vehicles is also a reference basis for judging the accuracy of the four models of road recognition. The smoother the trajectory presented by intelligent vehicles in driving curves indicates that the model recognises and makes correct judgements in the appropriate cornering position. In the green circle, it is a continuous curve. The continuous curve can reflect whether the model can make timely and correct adjustments to the rapidly changing road conditions. If the smart car is in a position that is not conducive to entering the curve, it will cause the smart car to drive out of the lane when passing through the curve, or make the smart car to adjust in the curve. A waste of time. According to the performance of the four models in the above figure in continuous curves, the trajectory of the NVIDIA end-to-end regression model is smoother than that of NVIDIA's end-to-end classification model, but after the intelligent car passes the first curve and enters the second curve, the front directionality of the NVIDIA end-to-end regression model is not as good as that of NVIDIA's end-to-end division. The direction of the front of the model car is clearer. In the LeNet-5 model, the driving trajectory of the LeNet-5 regression model in continuous curves is smoother than that of the LeNet-5 classification model, and the LeNet-5 classification model makes non-smooth adjustments to the front of the car in the first curve, although the smart car is finally maintained in the lane. Inside, but more time was wasted because of it. Finally, when driving to the second curve, the pointing of the front of the LeNet-5 classification model is not as clear as that of the front of the LeNet-5 regression model. NVIDIA's end-to-end classification model and LeNet-5 regression model trajectory are obviously better than the remaining two models.)

#### 5.1.5.2 行车模型的改进(Improvement of the driving model)
在行车模型的实现结果中，可以发现在四种模型的实际部署中都存在在直行车道中车身发生了一定幅度的抖动最终产生蛇形现象。抖动程度的大小取决于很多影响因素，比如智能车计算资源有限所导致计算频率降低，从而导致智能车反应不及时。或者在数据采集时，由于车道存在非传统弯道而导致了智能车在出弯时不能处于合适位置，从而造成模型计算错误。为了避免由于以上所存在的问题导致智能车在行驶过程中出现的蛇行现象。通过缩小智能车在行驶过程中的感受野，训练模型进行当前道路的判断，进而合理抑制智能车在直行道路行驶过程中的蛇形现象。在真实驾车行驶过程中，车辆在直行道路行驶过程中也并非始终保持道路中间，期间也有驾驶人员的不断修正，通过驾驶员的不断修正来使得车辆保持在道路中间位置。修正波长越长则反馈的体感强度越小，震荡感越轻微。修正波长越短则反馈的体感越强，震荡感越明显。因此减小车辆自身行驶修正强度至关重要。驾驶员通常做出决策并不局限于远处视野路况，而是进行远近的路况扫描，并最终做出行驶决策。根据此缩小智能车的感受视野，对当前这部分感受视野进行路况判断。通过对路况的判断再结合正常自动行驶模型所需要的原始感受野，最终输出车辆在当前路况下合理的行驶速度。
<div align=center>
<img width="400" alt="截屏2024-11-09 20 27 10" src="https://github.com/user-attachments/assets/5f9b31a9-e7fe-43d4-9598-c88f6e0679f4">
<img/></div>

(In the realisation results of the driving model, it can be found that in the actual deployment of the four models, there is a certain amount of shaking of the car body in the straight lane, resulting in a snake-shaped phenomenon. The magnitude of the degree of jitter depends on many influencing factors, such as the limited computing resources of smart cars, resulting in a decrease in the calculation frequency, resulting in untimely response of smart cars. Or when collecting data, due to the non-traditional curves in the lane, the smart car cannot be in the right position when cornering, resulting in model calculation errors. In order to avoid the meandering phenomenon of intelligent vehicles in the process of driving due to the above problems. By narrowing the feeling field of intelligent vehicles in the process of driving, the training model to make a judgement of the current road, and then reasonably suppress the snake-shaped phenomenon of intelligent vehicles in the process of driving straight roads. In the process of real driving, the vehicle does not always stay in the middle of the road in the process of driving straight on the road. During this period, there is also a continuous correction by the driver to keep the vehicle in the middle of the road through the continuous correction of the driver. The longer the modified wavelength, the smaller the physical strength of the feedback and the milder the shock. The shorter the correction wavelength, the stronger the feedback and the more obvious the shock. Therefore, it is very important to reduce the intensity of the vehicle's own driving and correction. Drivers usually make decisions not limited to the road conditions in the distance, but scan the road conditions far and near, and finally make driving decisions. According to this, narrow the sensing field of view of the smart car, and judge the road condition of the current part of the feeling field of view. Through the judgement of the road conditions and combined with the original sensing field required by the normal automatic driving model, the reasonable driving speed of the vehicle under the current road conditions is finally output.)

通过行车数据图像处理的结果进行道路识别感受野的划分，道路识别感受野通过道路识别模型识别出当前道路情况，而处理后的行测数据则通过自动行车模型计算出当前需要的线速度与角速度。若道路识别出当前道路为直行车道，自动行车预测的角速度值过大，则进行智能车角速度的抑制；若道路识别出当前道路为弯道，自动行车预测的角速度值则不受到抑制。并获得最终角速度与线速度使智能车进行行驶。通过对行车数据采集处理后的数据进行路况判断的感受野范围的提取，以原图像中间为界限，向上向下提取原图像高度的20%。并通过人工分类的方法对图像进行分类。共分为弯道与直道两种类别，每种类别共1253张图片.
<div align=center>
<img width="400" alt="截屏2024-11-09 20 28 38" src="https://github.com/user-attachments/assets/4d1efc3b-8abb-4961-b49b-c53ff16d9f90">
<img/></div>

(The road recognition sensing field is divided through the results of driving data image processing. The road identification sensing field identifies the current road situation through the road recognition model, and the processed road measurement data calculates the current required linear speed and angular velocity through the automatic driving model. If the road recognises that the current road is a straight lane and the angular velocity value predicted by automatic driving is too large, the intelligent angular velocity is suppressed; if the road recognises that the current road is a curve, the angular velocity value predicted by automatic driving is not inhibited. And obtain the final angular velocity and linear velocity to make the smart car run. By extracting the sensing range of the road condition judgement of the data after the driving data is collected and processed, 20% of the height of the original image is extracted up and down with the middle of the original image as the boundary. And classify images through manual classification. It is divided into two categories: curves and straight roads, with a total of 1,253 pictures in each category.)

为了减小道路识别模型对智能车计算资源的占用，提高模型的计算速度，这里使用广义线性回归对模型进行训练。将数据集划分为测试集与训练集，其中测试集占原数据集个数的20%，其余为训练集。根据划分后的数据对模型进行训练。模型训练后在测试集上的准确率达到了0.94076923，在测试集上模型训练的准确率为0.93406593。且训练速度为23秒，模型占用内存为10MB。模型训练结果较好。在实际部署过程中，模型可以根据当前感受野对路况进行分辨，并控制自动行驶模型计算到的角速度进行调控。如图为遇到不同路况时道路识别模型识别到的结果。
<div align=center>
<img width="250" alt="截屏2024-11-09 20 28 45" src="https://github.com/user-attachments/assets/07543959-1792-4bc4-a5be-7f21f69db39a">
<img width="250" alt="截屏2024-11-09 20 28 54" src="https://github.com/user-attachments/assets/13a82aa9-9605-47af-b5dc-7941529bb9bd">
<img/></div>
<div align=center>
<img width="400" alt="截屏2024-11-09 20 29 00" src="https://github.com/user-attachments/assets/1854643e-dd73-4800-8497-812281961d3d">
<img/></div>

(In order to reduce the occupation of intelligent vehicle computing resources by the road recognition model and improve the calculation speed of the model, generalised linear regression is used to train the model here. The data set is divided into test set and training set, of which the test set accounts for 20% of the original data set, and the rest is the training set. Train the model according to the divided data. After model training, the accuracy rate on the test set reaches 0.94076923, and the accuracy rate of model training on the test set is 0.93406593. And the training speed is 23 seconds, and the model occupies 10MB of memory. The model training results are relatively good. In the actual deployment process, the model can distinguish the road conditions according to the current sensing field, and control the angular velocity calculated by the automatic driving model to regulate. The figure shows the results recognised by the road recognition model when encountering different road conditions.)

通过加入道路识别辅助智能车行驶，避免智能车在行驶过程中产生的蛇形运动。通过道路识别结果可以看到道路识别模型对当前道路识别的结果，若识别为直行车道则把识别区域的白色车道填充为绿色，若识别结果为弯道，则把识别区域的白色车道填充为红色。根据不同颜色车道的标注从而更好的让智能车识别当前的车道情况。后应用于智能车自动行驶中，如图65改进后智能车行驶轨迹所示，图中行驶轨迹相较于四个自动行驶模型轨迹更加顺滑，且在直行车道中虽能体现出智能车在车道中的调整但调整频率与调整次数明显下降。智能车运行的稳定性与蛇行现象明显提升与减少。

(By adding road recognition to assist the driving of intelligent vehicles, it avoids the snake-shaped movement generated by intelligent vehicles during driving. Through the road identification results, we can see the results of the road identification model's current road recognition. If it is identified as a straight lane, the white lane in the identification area will be filled with green. If the identification result is a curve, the white lane in the identification area will be filled in red. According to the labelling of different colour lanes, intelligent cars can better recognise the current lane situation. Then it is applied to the automatic driving of intelligent vehicles, as shown in the improved driving trajectory of intelligent vehicles in Figure 65. The driving trajectory in the figure is smoother than that of the four automatic driving models, and although it can reflect the adjustment of intelligent vehicles in the lane in the straight lane, the adjustment frequency and number of adjustments are significantly reduced. The stability and serpentine phenomenon of intelligent vehicle operation have been significantly improved and reduced.)

## 5.2 避障系统的设计与实现(Design and realisation of obstacle avoidance system)
在自动驾驶中，当车辆遇到车道突然侵入时，车辆的避障显得尤为重要。本章将分析智能车前方的激光雷达所采集到的车辆周围数据，设计智能车避障算法进行智能车周围障碍的判断，并对当前障碍做出反应最终实现智能车的避障动作。

(In autonomous driving, it is especially important to avoid obstacles when the vehicle encounters a sudden intrusion of the lane. This chapter will analyse the data around the vehicle collected by the lidar in front of the intelligent vehicle, design an intelligent vehicle obstacle avoidance algorithm to judge the obstacles around the intelligent vehicle, and respond to the current obstacles to finally realise the obstacle avoidance action of the intelligent vehicle.)

### 5.2.1 激光雷达数据分析(Lidar data analysis)
激光雷达收集到的数据来自于智能车所搭载的思岚A1雷达。激光雷达设定扫描频率为5.5HZ设定为标准工作模式。激光雷达所扫描的数据结构主要分为9个部分，分别为头部分，角度最大值，角度最小值，每次扫描的角度差，每次扫描的时间差，总扫描时间，距离最大值，距离最小值和距离列表。根据起始部分的角度最大值和角度最小值以及每次扫描角度差可以计算出在距离列表中每一个距离所对应的旋转角。旋转角和距离经过极坐标系与笛卡尔坐标系的转换得到当前车辆周围的环境状态。且每次扫描坐标原点为智能车点位。
<div align=center>
<img width="400" alt="截屏2024-11-09 20 31 38" src="https://github.com/user-attachments/assets/ace2a20a-b182-4995-b350-c40f440baf81">
<img/></div>

(The data collected by the lidar comes from the Silan A1 radar carried by the smart car. The scanning frequency of the lidar is set to 5.5HZ and the standard working mode is set. The data structure scanned by lidar is mainly divided into 9 parts, which are the head part, the maximum angle value, the minimum angle value, the angle difference of each scan, the time difference of each scan, the total scanning time, the maximum distance value, the minimum distance value and the distance list.The rotation angle corresponding to each distance in the distance list can be calculated according to the maximum angle and minimum angle of the starting part and the angle difference of each scan. The rotation angle and distance are converted through the polar coordinate system and the Cartesian coordinate system to obtain the current environmental state around the vehicle. And the origin of the coordinates of each scan is the intelligent car point.)

### 5.2.2 避障系统的设计(The design of the obstacle avoidance system)
为了避免当车辆遇到障碍物后继续前进，与障碍物距离不断减小，当距离障碍物过近时无法完成完整的避障动作，所以根据此种情况设定大于车辆中心到边缘距离的最大预警值。当车辆到障碍物的距离小于最大预警值时进行避障。实现前进，后退，左转与右转四个方向的运动，避免与障碍物发生接触。为了增强车辆对周围环境的感知能力，根据车辆尺寸分别对智能车正前方向，智能车正后方向，智能车正左方向以及智能车正右方向的障碍物进行划分，在智能车正前方以及正右方向和正左方向划分的区间上找到与智能车最近障碍物的距离。
<div align=center>
<img width="400" alt="截屏2024-11-09 20 31 44" src="https://github.com/user-attachments/assets/1efc455f-f86b-42f4-ad17-c4cba5524ba9">
<img/></div>

(In order to avoid moving forward when the vehicle encounters an obstacle, the distance from the obstacle is constantly decreasing, and the complete obstacle avoidance cannot be completed when the obstacle is too close, the maximum warning value greater than the distance from the centre of the vehicle to the edge is set according to this situation. Avoid obstacles when the distance between the vehicle and the obstacle is less than the maximum warning value. Realise the four-way movement of forward, backward, left and right, and avoid contact with obstacles. In order to enhance the vehicle's ability to perceive the surrounding environment, the obstacles in the front direction of the smart car, the rear direction of the smart car, the left direction of the smart car and the right direction of the smart car are divided according to the size of the vehicle, and the nearest obstacles to the smart car are found in the front of the smart car and the right and left direction. The distance of the obstacle.)

当智能车与障碍物的距离达到设定的最大预警值时，车辆线速度将设置为0，并根据车辆正左侧与正右侧与障碍物距离的大小进行车辆运行方向的调整。若车辆左侧距离大于车辆右侧距离则智能车将向左侧以设定的速度进行左侧转向；若车辆右侧的距离大于车辆左侧距离则智能车将向右侧以设定的速度进行右侧转向。当智能车与障碍物的距离大于设定的最大预警值时则停止转向并以设定的默认线速度向前前进。
<div align=center>
<img width="400" alt="截屏2024-11-09 20 31 52" src="https://github.com/user-attachments/assets/9ffa1025-99a6-410b-b135-d41f84960d97">
<img/></div>

(When the distance between the smart car and the obstacle reaches the set maximum warning value, the vehicle line speed will be set to 0, and the running direction of the vehicle will be adjusted according to the size of the distance between the left and right side of the vehicle and the obstacle. If the distance from the left side of the vehicle is greater than the distance from the right side of the vehicle, the smart car will turn to the left at the left at the set speed; if the distance from the right side of the vehicle is greater than the distance from the left side of the vehicle, the smart car will turn to the right at the right at the set speed. When the distance between the smart car and the obstacle is greater than the set maximum warning value, stop steering and move forward at the set default line speed.)

### 5.2.3 避障系统的实现(The realisation of obstacle avoidance system)
根据避障逻辑从而实现智能车的行车避障，如图69所示智能车处于开始行驶时刻，如图紫色代表智能车所在的位置，绿色部分代表设定的智能车预警值距离，若障碍物在智能车预警值距离内则标记为红色，而蓝色代表通过坐标变换激光所扫描到的障碍物。由于智能车正前方距离障碍物的距离大于预警值范围，所以在智能车以默认线速度前进到避障过程B所在的位置如图70所示。当在次位置扫描到前方障碍物的距离小于等于智能车预警值距离时，智能车停止前进。由于激光雷达测得智能车左侧距离大于右侧距离时，智能车进行默认角速度向左选择到避障过程C所在的位置如图71所示。当智能车正前方距离再一次大于设定的预警距离时，智能车停止转向并恢复默认线速度向前行驶到达避障过程D所在位置如图所示。从而完成智能车整个避障过程。
<div align=center>
<img width="400" alt="截屏2024-11-09 20 32 04" src="https://github.com/user-attachments/assets/06e022e3-39e4-4e23-84fa-24167732fd01">
<img/></div>

(According to the obstacle avoidance logic, the driving avoidance of intelligent vehicles is realized. As shown in Figure 69, the intelligent vehicle is at the starting point of operation. As shown in the figure, purple represents the location of the intelligent vehicle, and the green part represents the set warning value distance of the intelligent vehicle. If the obstacle is within the distance of the intelligent vehicle warning value, it is marked in red, and blue represents the coordinates. Transform the obstacles scanned by the laser. Because the distance of the obstacle in front of the smart car is greater than the warning value range, the smart car moves forward at the default line speed to the position of obstacle avoidance process B as shown in Figure 70. When the distance scanned to the obstacle in front of the sub-position is less than or equal to the distance of the warning value of the smart car, the smart car stops moving forward. Because the lidar measures that the distance on the left side of the smart car is greater than the distance on the right side, the default angular speed of the smart car selects the position of obstacle avoidance process C to the left, as shown in Figure 71. When the distance in front of the smart car is once again greater than the set warning distance, the smart car stops steering and restores the default line speed to drive forward to the position of obstacle avoidance process D as shown in the figure. So as to complete the whole obstacle avoidance process of smart cars.)

## 5.3 红绿灯识别系统的设计与实现(Design and realisation of traffic light identification system)
在实际行车过程中，红绿灯在日常行车场景中是占比最多的一种行车状况。本章主要分析了红绿灯的基本参数，并结合当前车辆运行环境设计红绿灯颜色的识别以及距离的判断。从而在一定条件下使智能车对当前信号灯进行正确判断，进一步完善智能车自动驾驶能力。

(In the actual driving process, traffic lights account for the largest proportion of driving situations in daily driving scenarios. This chapter mainly analyzes the basic parameters of traffic lights, and designs the identification of traffic light colors and the judgment of distance in combination with the current vehicle operating environment. So that under certain conditions, intelligent vehicles can correctly judge the current traffic lights and further improve the autonomous driving ability of intelligent vehicles.)

### 5.3.1 红绿灯数据分析(Traffic light data analysis)
红绿灯主要由红，黄，绿三种二极管显示颜色，并加入红绿灯倒计时屏幕。运行电压为3V。其中红灯和绿灯时间都为9秒黄灯时间为3秒，整个红绿灯高为8cm。当红绿灯开始运行时，每一次先从绿色灯开始，然后再到黄色灯最后到红色灯显示，且在每种灯显示的后3秒，灯的显示形式从长亮变为每1秒闪烁四下直至下一个颜色的灯亮起。
<div align=center>
<img width="400" alt="截屏2024-11-09 20 35 11" src="https://github.com/user-attachments/assets/f1dfda4b-710f-4498-a259-870fbee6cc36">
<img/></div>

(The traffic light is mainly composed of three diodes, red, yellow and green, and the traffic light countdown screen is added. The operating voltage is 3V. Among them, the red light and green light time are 9 seconds, the yellow light time is 3 seconds, and the whole traffic light is 8cm high. When the traffic light starts to run, each time it starts from the green light, then the yellow light and finally to the red light display, and in the last 3 seconds of each light display, the display form of the lamp changes from long light to flashing four times every 1 second until the next color light lights up.)

智能车前方行驶的路况图像主要由前方摄像头进行拍摄。摄像头距离地面高度为18cm。由于摄像头拍摄的角度，智能车行驶道路的宽度以及红绿灯本身大小的限制。所以将红绿灯设置在行驶车道的右侧。方便摄像头的捕捉与识别，确保摄像头的视野范围内存在完整的红绿灯信号。摄像头拍摄得到的图像长度为640像素高度为480像素，图像通道为RGB三通道。

(The images of the road conditions in front of the smart car are mainly taken by the front camera. The camera is 18cm above the ground. Due to the angle shot by the camera, the width of the smart car's road and the size of the traffic light itself are limited. Therefore, the traffic light is set on the right side of the driving lane. It is convenient for camera capture and recognition, and ensures that there is a complete traffic light signal within the field of view of the camera. The image taken by the camera is 640 pixels long and the height is 480 pixels, and the image channel is RGB three-channel.)

### 5.3.2 红绿灯识别系统的设计(Design of traffic light identification system)
当智能车行驶到有红绿灯所在的路段时，为了达到与现实世界相同的逻辑判断，实现智能车遇到红灯时停止行驶，绿灯时开始行驶的功能，首先建立ROS图像的传输通道并对摄像头所拍摄的图像进行色彩颜色的转换，使图像原本的RGB颜色转换成HSV颜色范围。当红灯、绿灯或黄灯亮起时光线由于灯的周围的白色覆盖件使灯周围呈现较多的白色，针对由于光线所产生的白色范围进行提取并获得当前对应的遮罩层。结合相机标定数据对遮罩层图像进行图像畸变矫正，在此基础上结合所识别出红绿灯在图像中的具体位置，通过运用相似三角形的原理，计算出智能车当前位置与红绿灯之间的距离。若当前距离大于设定的距离，则让智能车保持继续的形式；若当前距离小于等于设定距离，则对具体信号进行识别。对遮罩中最大的区域进行图像的裁剪并进行HSV图像颜色空间的转换。通过设定红色，绿色和黄色的颜色范围进一步确定红绿灯当前为哪一种信号。当检查出的信号为绿灯或空时保持智能车继续行驶，若检查出的信号为红灯或黄灯时则使智能车停止行驶直到信号灯变为绿色。
<div align=center>
<img width="400" alt="截屏2024-11-09 20 35 25" src="https://github.com/user-attachments/assets/494f47d5-d2d0-405f-9ad2-b9f70e7c0315">
<img/></div>

(When the smart car drives to the section where the traffic light is located, in order to achieve the same logical judgment as the real world, to realize the function of the smart car stopping driving when it encounters a red light and starting to drive when the green light, first establish a transmission channel of the ROS image and convert the color of the image taken by the camera, so that the image Ben's RGB color is converted to HSV color range. When the red light, green light or yellow light is on, the light shows more white around the lamp due to the white covering around the lamp, and the current corresponding mask layer is extracted for the white range generated by the light. Combine the camera calibration data to correct the image distortion of the mask layer image. On this basis, combine the specific position of the traffic light in the image, and calculate the distance between the current position of the smart car and the traffic light by using the principle of similar triangles. If the current distance is greater than the set distance, let the smart car continue; if the current distance is less than or equal to the set distance, the specific signal will be identified. Crop the image of the largest area in the mask and convert the color space of the HSV image. Further determine which signal the traffic light is currently by setting the color range of red, green and yellow. When the detected signal is green or empty, keep the smart car running. If the checked signal is red or yellow, stop the smart car until the signal light turns green.)

### 5.3.3 红绿灯识别系统的实现(Realisation of traffic light identification system)
为了更好的验证红绿灯系统的可行性，依托于相机标定数据采集系统采集包括三种红绿灯信号的共13张图片进行验证。根据红绿灯识别系统的设计，由于不同颜色的灯光所在红绿灯周围的覆盖件上反光都为白色。因此，通过转换原始图像的色域对白色区域进行图像提取。根据图75和图76可以清晰的看到灯珠由于发光导致周围颜色为近似白色。并进行白色区域的边缘检测得到面积最大的白色区域。所对应的面积最大的白色区域也就为当前具体哪一个颜色的信号灯在使用。
<div align=center>
<img width="195" alt="截屏2024-11-09 20 35 34" src="https://github.com/user-attachments/assets/aefcb5f7-8520-44ad-8a90-75eac3e4123c">
<img width="195" alt="截屏2024-11-09 20 35 41" src="https://github.com/user-attachments/assets/da592bbd-4cef-4de4-9349-e6d1fdfa4b2b">
<img width="195" alt="截屏2024-11-09 20 35 47" src="https://github.com/user-attachments/assets/f822a516-76a0-4d77-a466-2ede0795cd00">
<img/></div>

(In order to better verify the feasibility of the traffic light system, a camera calibration data acquisition system was used to collect a total of 13 images including three types of traffic light signals for verification. According to the design of the traffic light recognition system, the reflection on the covering around the traffic light is white due to the presence of lights of different colors. Therefore, white areas are extracted from the image by converting the color gamut of the original image. According to Figures 75 and 76, it can be clearly seen that the light bead emits light, causing the surrounding color to be approximately white. And perform edge detection on the white area to obtain the largest white area. The white area with the largest area corresponds to which specific color of signal light is currently in use.)

当具体识别到信号时，根据图77的识别结果，将所框选的区域进行截取，截取出具体的信号类别，之后再次使用颜色范围提取的方法，划分红色，黄色以及绿色范围进行颜色判断，若红色范围大于黄色与绿色则为红灯，若黄色颜色范围大于红色与绿色则为黄灯，绿色亦然，根据此判断得到具体的信号标识。如图78，图79，图80所示为截取到的红灯，黄灯与绿灯。
<div align=center>
<img width="195" alt="截屏2024-11-09 20 35 54" src="https://github.com/user-attachments/assets/2da1f79f-f6c1-41f4-8c61-9ebbec30ab4a">
<img width="195" alt="截屏2024-11-09 20 35 59" src="https://github.com/user-attachments/assets/ffaeb248-5ce7-4aba-923d-b3879dadcea3">
<img width="195" alt="截屏2024-11-09 20 36 05" src="https://github.com/user-attachments/assets/a62c5dae-71ae-4e53-b853-e1d07a850648">  
<img/></div>

(When a specific signal is recognized, according to the recognition result in Figure 77, the selected area is cropped to extract the specific signal category. Then, the color range extraction method is used again to divide the red, yellow, and green ranges for color judgment. If the red range is larger than the yellow and green ranges, it is a red light. If the yellow range is larger than the red and green ranges, it is a yellow light, and the same goes for green. Based on this judgment, the specific signal identifier is obtained. The red, yellow, and green lights captured are shown in Figures 78, 79, and 80.)

通过截取到的不同颜色的信号灯进行当前智能车与信号灯之间距离的判断。根据针孔成像原理所知真实时间与相机世界比例呈相似三角形关系。通过已知的红绿灯高度和相机内参数焦距和图像呈现的像素点可以得到智能车距离红绿灯的大致距离。通过红绿灯的距离进而判断智能车的停车位置。如图为红绿灯的识别结果。红色字代表智能车识别红绿灯的信号种类，蓝色代表智能车距离红绿灯的距离。
<div align=center>
<img width="400" alt="截屏2024-11-09 20 36 12" src="https://github.com/user-attachments/assets/54a12ee6-438b-4383-a6ca-aa07c0dbd53f">
<img/></div>

(Determine the distance between the current smart car and the signal lights by capturing different colored signal lights. According to the pinhole imaging principle, it is known that the real time has a similar triangular relationship with the camera world ratio. The approximate distance between the intelligent vehicle and the traffic light can be obtained by knowing the height of the traffic light, the focal length of the camera parameters, and the pixel points presented in the image. Determine the parking position of the smart car based on the distance between traffic lights. The recognition result of traffic lights is shown in the picture. The red text represents the type of traffic light signal recognized by the intelligent vehicle, and the blue text represents the distance between the intelligent vehicle and the traffic light.)

## 5.4 自动驾驶整体系统的设计与实现(Design and realisation of the overall system of autonomous driving)
### 5.4.1 自动驾驶整体系统的设计(The design of the overall system of autonomous driving)
根据已实现的功能对其整合从而实现自动驾驶整体体系。在自动驾驶众多传感器中，设定传感器功能控制优先级至关重要。这将取决当车辆周围出现情况时，车辆会依据最高级别传感器进行行为决策，如当行驶至红绿灯路口时前方信号灯变为红色，突然冲出非机动车。此时，车辆周围毫米波雷达就作为最高优先级。行车电脑会对其进行数据分析并做出决策，当威胁消除时在进行红绿灯最高优先级的判断。根据本文所要实现的三个功能进行功能优先级的化分。根据设定的模型行车环境从远到近进行智能车功能等级的排序，分别是红绿灯等级大于避障系统等级，避障系统等级大于自动行车系统。
<div align=center>
<img width="400" alt="截屏2024-11-09 20 39 44" src="https://github.com/user-attachments/assets/84352889-caa9-4be9-af52-177915a61ba3">
<img/></div>

(Integrate it based on the implemented functions to achieve the overall system of autonomous driving. Among the numerous sensors in autonomous driving, setting the priority of sensor function control is crucial. This will depend on the behavior decisions made by the vehicle based on the highest level sensors when there are situations around the vehicle, such as when the traffic light turns red at the intersection and suddenly rushes out of a non motorized vehicle. At this point, millimeter wave radar around the vehicle is given the highest priority. The onboard computer will analyze the data and make decisions, and when the threat is eliminated, it will determine the highest priority for traffic lights. Prioritize the three functions to be implemented in this article. According to the set model driving environment, the intelligent vehicle function levels are sorted from far to near, with the traffic light level being higher than the obstacle avoidance system level and the obstacle avoidance system level being higher than the automatic driving system level.)

当自动驾驶整体系统启动时，首先通过激光雷达数据通路和ROS图像传输通道获得智能车前方激光雷达扫描数据与摄像头捕捉图像。当红绿灯识别系统识别到红绿灯后对具体信号进行判断。若此时红绿灯信号为不可通行时则等到可通行信号的开放。当红绿灯识别系统反馈的信号为可通行或无信号灯时，则避障系统运行结果有效。当避障系统检查到前方有障碍物时则启动避障算法直到障碍物在所设置的阈值之外。在避障系统没有检测到障碍物时自动行车系统接管智能车控制并完成整体的车辆运行，达到最终的自动驾驶整体系统的建立。

(When the overall autonomous driving system is started, the intelligent vehicle's front LiDAR scanning data and camera captured images are first obtained through the LiDAR data path and ROS image transmission channel. The traffic light recognition system determines the specific signal after recognizing the traffic light. If the traffic light signal is not passable at this time, wait for the passable signal to open. When the signal feedback from the traffic light recognition system is passable or no signal light, the obstacle avoidance system operation result is valid. When the obstacle avoidance system detects an obstacle ahead, it starts the obstacle avoidance algorithm until the obstacle is outside the set threshold. When the obstacle avoidance system does not detect any obstacles, the automatic driving system takes over the control of the intelligent vehicle and completes the overall vehicle operation, achieving the establishment of the final automatic driving system.)

### 5.4.2 自动驾驶整体系统的实现(The realisation of the overall system of autonomous driving)
自动驾驶整体系统的实现是依托于以上自动行车系统，避障系统以及红绿灯识别系统所实现的。为了更好的达到各个系统的完美融合，所以在初始场景的设定下加入障碍物与信号灯。在原有场景下设置避障环境和红绿灯识别环境。激光雷达通过扫描周围环境，智能车通过避障系统实现智能车在当前设置的环境下通过障碍区域。通过智能车前置摄像头识别当前信号灯的类别，智能车通过判断信号灯的类别做出相应的动作。根据加入的避障区域与红绿灯识别区域划分出不同环境下智能车的功能区间。
<div align=center>
<img width="400" alt="截屏2024-11-09 20 39 53" src="https://github.com/user-attachments/assets/8db21d09-273d-4806-bb33-67357b3a0b01">
<img/></div>

(The implementation of the overall autonomous driving system relies on the above automatic driving system, obstacle avoidance system, and traffic light recognition system. In order to achieve a perfect integration of various systems, obstacles and traffic lights are added to the initial scene settings.Set up obstacle avoidance environment and traffic light recognition environment in the original scene. Lidar scans the surrounding environment, and intelligent vehicles use obstacle avoidance systems to pass through obstacle areas in the current set environment. By using the front camera of the smart car to identify the category of the current signal light, the smart car takes corresponding actions by judging the category of the signal light. Divide the functional zones of intelligent vehicles in different environments based on the added obstacle avoidance areas and traffic light recognition areas.)

智能车测试环境部署结束后，根据自动驾驶整体系统的设计的功能优先级进行整体系统的实现。为了使各部分传感器协调工作，避免由于各个功能在运行时对计算资源的占用而发生系统阻塞，内存溢出的问题。以及个功能部件的响应时间不一致导致智能车不能及时做出反应的问题。进一步优化由于硬件不足而导致的计算错误，由于ROS系统本身自带服务(Services)来进行并行数据交互，所以将各个功能部件进行单独计算并将各部分计算结果返回给处理整体数据的部分，经过计算，运行行驶算法，得到智能车运行速度，并最终实现智能车的正确行驶。
每一个智能车功能都进行独立于其他功能的运行，自动行驶系统会根据当前路况进行数据处理，运行模型得到的速度，并最终将智能车行驶所需要的角速度与线速度发布到主节点上，红绿灯识别系统，则根据红绿灯处理算法，订阅前置摄像头图片进行红绿灯信号的识别，并将识别到的信号发布到主节点上。避障系统则通过订阅避障节点，进行数据坐标的转换，并计算出四个方向需要的数据，将四个方向的数据发布到主节点上。最后，通过订阅上面每一个功能节点输出的数据，结合自动驾驶整体系统的设计的功能优先级对障碍，信号和速度进行整体的判断，并将最终得到的速度发布到智能车速度节点上实现智能车的运行。
<div align=center>
<img width="400" alt="截屏2024-11-09 20 40 03" src="https://github.com/user-attachments/assets/c6955384-f578-4a2a-8e52-0838403cf48a">
<img/></div>

(After the deployment of the intelligent vehicle testing environment is completed, the overall system implementation is carried out according to the functional priority of the design of the autonomous driving system. In order to coordinate the operation of various sensors and avoid system blocking and memory overflow issues caused by the occupation of computing resources by various functions during runtime. And the problem of inconsistent response times of various functional components, which leads to the inability of smart cars to respond in a timely manner. Further optimize the calculation errors caused by insufficient hardware. As the ROS system itself comes with services for parallel data exchange, each functional component is calculated separately and the calculation results of each part are returned to the part that processes the overall data. After calculation, the driving algorithm is run to obtain the running speed of the intelligent vehicle, and ultimately achieve the correct driving of the intelligent vehicle.
Each intelligent vehicle function operates independently of other functions. The automatic driving system processes data based on the current road conditions, calculates the speed obtained by running the model, and finally publishes the angular velocity and linear velocity required for the intelligent vehicle to travel to the main node. The traffic light recognition system, based on the traffic light processing algorithm, subscribes to front camera images for traffic light signal recognition and publishes the recognized signals to the main node. The obstacle avoidance system converts data coordinates by subscribing to obstacle avoidance nodes, calculates the required data in four directions, and publishes the data in all four directions to the main node. Finally, by subscribing to the data output from each functional node above, combined with the priority of the designed functions of the autonomous driving system, the overall judgment of obstacles, signals, and speed is made, and the final speed is published on the intelligent vehicle speed node to achieve the operation of the intelligent vehicle.)

根据设计的自动驾驶整体系统与智能车测试环境完成以后，对智能车进行实际测试，以验证智能车各个功能部件运行的完整度和自动驾驶整体系统决策的正确性，实现智能车在实际测试中的自动行驶，障碍避障和信号识别。将智能车放到起始位置，启动自动行驶整体系统以及智能车轨迹记录系统和智能车摄像系统，对智能车在测试过程中遇到的路况以及行驶轨迹进行记录，不仅方便智能车在测试过程中自动行驶模型对当前路况判断准确性的评估比较，还进一步记录了第三视角智能车实际的行驶轨迹，以更加直观的视角方便对智能车行驶情况进行整体评估。在自动行驶整体系统启动以后，智能车将自行对识别到的路况产生相应的判断，对信号灯信息进行判别和对障碍物进行避障动作，依托于以上三种运行功能构建智能车自动行驶系统。如图为智能车在测试环境下的行驶轨迹。
<div align=center>
<img width="250" alt="截屏2024-11-09 20 40 10" src="https://github.com/user-attachments/assets/f6a58ef7-b5d9-41f0-b03e-8cc1f493b40a">
<img width="250" alt="截屏2024-11-09 20 40 15" src="https://github.com/user-attachments/assets/7151ffb3-4b68-4016-a053-d81b2f5635e4">
<img/></div>
<div align=center>
<img width="400" alt="截屏2024-11-09 20 40 21" src="https://github.com/user-attachments/assets/524edfe1-ec58-44be-b740-cee06fadfa51">
<img/></div>

(After the completion of the designed autonomous driving system and intelligent vehicle testing environment, actual testing of the intelligent vehicle is carried out to verify the integrity of the operation of various functional components of the intelligent vehicle and the correctness of the overall decision-making of the autonomous driving system, achieving automatic driving, obstacle avoidance, and signal recognition of the intelligent vehicle in actual testing. Place the smart car in the starting position, activate the overall automatic driving system, intelligent car trajectory recording system, and intelligent car camera system, and record the road conditions and driving trajectories encountered by the smart car during the testing process. This not only facilitates the evaluation and comparison of the accuracy of the current road conditions by the automatic driving model of the smart car during the testing process, but also further records the actual driving trajectory of the smart car from a third perspective, providing a more intuitive perspective for the overall evaluation of the smart car's driving situation. After the overall automatic driving system is started, the intelligent vehicle will make corresponding judgments on the recognized road conditions, distinguish signal light information, and take obstacle avoidance actions. Based on the above three operating functions, an intelligent vehicle automatic driving system will be constructed. The driving trajectory of the intelligent vehicle in the testing environment is shown in the figure.)

根据智能车在测试环境下的运行轨迹。可以看到，智能车在整体运行中，随着从起始位置开始逐渐到结束位置，智能车的轨迹的颜色不断的加深。在智能车自动行驶部分中，智能车不论是在直行道路与弯道轨迹都表现的非常光滑，只有在一小部分场景下智能车才进行了车身姿态的修正，在红绿灯识别系统的情况下由于智能车检测到前方信号灯为红色信号时进行了停车操作如图85红绿灯识别停车，才使在红绿灯识别位置产生了明显的颜色差异。在行驶到避障系统中时如图激光雷达避障，由于小车运行避障系统如图86，避障系统设置默认速度过慢才导致了避障的范围内智能车行驶轨迹的颜色的快速加深，由于智能车需要时时刻刻对周围环境进行数据采集并进行计算判断，所以在进行避障的第一个右转过程中，智能车表现出对周围环境的判断，并没有过快的执行行驶策略。而是进一步调整车身姿态，以最优的计算结果驱动智能车决策从而使智能车通过避障行驶区域。后根据自动行驶系统的计算结果引导智能车返回开始起点。因此在此环境下实现了智能车的自动行驶，红绿灯识别以及避障行驶和分级控制功能的集合。

(Based on the running trajectory of the intelligent vehicle in the testing environment. As can be seen, during the overall operation of the smart car, the color of its trajectory gradually deepens from the starting position to the ending position. In the automatic driving part of the intelligent vehicle, the intelligent vehicle performs very smoothly on both straight and curved roads. Only in a small number of scenarios does the intelligent vehicle correct its body posture. In the case of the traffic light recognition system, the intelligent vehicle performs a parking operation when it detects that the signal ahead is a red signal, as shown in Figure 85, which results in a significant color difference at the traffic light recognition position. When driving to the obstacle avoidance system, as shown in Figure 86, the laser radar obstacle avoidance system was used. Due to the slow default speed set by the obstacle avoidance system, the color of the intelligent vehicle's driving trajectory within the obstacle avoidance range quickly deepened. As the intelligent vehicle needs to constantly collect data from the surrounding environment and make calculations and judgments, it showed judgment of the surrounding environment during the first right turn of the obstacle avoidance process and did not execute the driving strategy too quickly. Instead, it further adjusts the body posture to drive intelligent vehicle decisions with the optimal calculation results, thereby enabling the intelligent vehicle to pass through obstacle avoidance driving areas. Then, based on the calculation results of the automatic driving system, guide the intelligent vehicle back to the starting point. Therefore, in this environment, the automatic driving, traffic light recognition, obstacle avoidance driving, and graded control functions of intelligent vehicles have been achieved.)

# 6.结论(Conclusion)
本文自动驾驶项目成功实现了自动行驶、红绿灯识别、避障以及智能车道路判断等关键功能。尽管这些功能各自独立，但在构建自动驾驶系统的过程中，它们都是必不可少的。在自动行驶功能的实现过程中，初期阶段的行车数据获取至关重要，因为一个优质的数据集对后续的模型训练起到了决定性的作用。本次实验的环境设置为理想状态，道路周围颜色较深，包含直角弯道、回头弯道、直行道和斜弯道等多种路况。然而，由于硬件运行频率的不同，数据采集过程中的速度与图像存在时间差，这可能导致车辆无法及时做出判断。在模型训练过程中，选择了小体量模型以避免内存阻塞，但由于时间限制，模型的选择与测试还不够充分，无法实现准确可靠的运行结果。在避障系统的构建中，只对智能车周围四个方向的数据进行了分析，避障算法设计较为简单，基本实现了智能车在有障碍物下的避障行驶。未来的改进中，可以从更复杂的方向和层次进行智能车周围环境的判断，进一步提高智能车对障碍物的判断力和决策正确性。
在红绿灯识别系统中，我们使用了颜色空间的转换，但这种方法在非特定环境下可能会造成红绿灯信号的识别错误。未来，可以考虑加入Yolo V5,transformer，内容识别等模型，以提高系统在真实环境下的泛化能力。此外，本次自动驾驶系统主要依赖于以上三种功能的整合，但各个系统之间的协调也是至关重要的。在本项目中，我们主要采用纵向优先级的方式对自动行驶系统中的功能进行分级划分。然而，在实际情况中，自动驾驶系统需要在不同路况下进行相应优先级的调整，同时在优先级下，自动驾驶各种传感器的数据需要相互流通。处理单元需要对这一时刻下的数据进行并行计算，才能保证决策思路与优先级发挥出相应的作用。总的来说，通过本次实验，实现了自动驾驶的一小部分功能，并通过实际测试得到了预期的结果。在智能车自动驾驶的搭建过程中，软件与硬件的协同工作至关重要。未来，将继续优化和完善自动驾驶系统，以实现更多的功能，并提高系统的稳定性和可靠性。随着技术的不断进步，自动驾驶将会在未来的交通出行中发挥越来越重要的作用。

(The autonomous driving project in this article has successfully achieved key functions such as automatic driving, traffic light recognition, obstacle avoidance, and intelligent vehicle road judgment. Although these functions are independent, they are indispensable in the process of building the auto drive system. In the implementation process of automatic driving function, obtaining driving data in the initial stage is crucial, as a high-quality dataset plays a decisive role in subsequent model training. The environment for this experiment is set to an ideal state, with darker colors around the road, including various road conditions such as right angle curves, turning curves, straight lanes, and diagonal curves. However, due to the different operating frequencies of hardware, there is a time difference between the speed of data acquisition and the image, which may cause the vehicle to be unable to make timely judgments. During the model training process, a small-scale model was selected to avoid memory blocking, but due to time constraints, the model selection and testing were not sufficient to achieve accurate and reliable running results. In the construction of the obstacle avoidance system, only data from four directions around the intelligent vehicle were analyzed, and the obstacle avoidance algorithm design was relatively simple, basically achieving obstacle avoidance driving of the intelligent vehicle under obstacles. In future improvements, the judgment of the surrounding environment of intelligent vehicles can be carried out from more complex directions and levels, further improving the judgment and decision-making accuracy of intelligent vehicles towards obstacles.
In the traffic light recognition system, we use color space conversion, but this method may cause recognition errors in traffic light signals in non-specific environments. In the future, models such as Yolo V5, transformer, and content recognition can be considered to improve the system's generalization ability in real-world environments. In addition, this auto drive system mainly depends on the integration of the above three functions, but the coordination between various systems is also crucial. In this project, we mainly adopt a vertical priority approach to classify and divide the functions in the automatic driving system. However, in reality, the auto drive system needs to adjust the corresponding priority under different road conditions, and at the same time, under the priority, the data of various sensors of autopilot needs to flow with each other. The processing unit needs to perform parallel computing on the data at this moment in order to ensure that the decision-making ideas and priorities play a corresponding role. Overall, a small portion of the functions of autonomous driving have been achieved through this experiment, and the expected results have been obtained through actual testing. The collaborative work of software and hardware is crucial in the construction process of intelligent vehicle autonomous driving. In the future, the auto drive system will continue to be optimized and improved to achieve more functions and improve the stability and reliability of the system. With the continuous advancement of technology, autonomous driving will play an increasingly important role in future transportation.)






 Thank you for reading and correcting .Feel free to ask question.
Created by Jia zimo(yiwei)/Zhang peihua. E-mail:15832120175@163.com


