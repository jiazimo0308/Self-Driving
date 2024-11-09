# Autonomous-Driving-Based-On-Deep-Learing
在智能车上实现自动行驶，红绿灯识别和避障

Realize automatic driving, traffic light recognition, and obstacle avoidance on smart cars

# 1.摘要（ABSTRACT）
本文为实现自动驾驶系统，设计并实施了三个核心功能：自动行车、避障以及红绿灯识别，并最终将这三种功能进行分级合并。系统设计阶段，结合硬件环境，主要设计了智能车行驶、数据采集及模型部署系统。数据采集系统获取相机标定板数据以及行驶信息。经过深度处理，运用计算机视觉算法，处理得到可供模型训练的数据。自动行车系统的设计采用了两种深度学习模型和两种训练任务进行模型训练，并在比较分析的基础上，结合实际运行环境，优化训练结果。避障系统借助激光雷达扫描环境数据，确定车辆四个方向范围，并根据计算结果，指导智能车避障。红绿灯识别系统在新色彩空间下划分颜色区间并提取信号灯发光部分，进一步识别颜色，根据识别颜色控制车辆行动。将上述三种功能在已实现的情况下进行整合，设计功能优先级划分，根据实际硬件环境设计单独功能的运行逻辑。并根据最终设计的结果进行智能车实际部署以实现自动驾驶功能。

(In order to realize the auto drive system, this paper designs and implements three core functions: automatic driving, obstacle avoidance and traffic light recognition. Finally, these three functions are classified and combined. In the system design phase, combined with the hardware environment, the intelligent vehicle driving, data collection, and model deployment system were mainly designed. The data acquisition system obtains camera calibration board data and driving information. After deep processing, computer vision algorithms are used to obtain data that can be used for model training. The design of the automatic driving system adopts two deep learning models and two training tasks for model training, and optimizes the training results based on comparative analysis and actual operating environment. The obstacle avoidance system uses LiDAR to scan environmental data, determine the four directional ranges of the vehicle, and guide intelligent vehicles in obstacle avoidance based on the calculation results. The traffic light recognition system divides color intervals in the new color space and extracts the illuminated parts of the signal lights, further identifying colors and controlling vehicle movement based on the identified colors. Integrate the above three functions in the already implemented situation, design priority division of functions, and design the operation logic of individual functions based on the actual hardware environment. And based on the final design results, deploy the intelligent vehicle to achieve autonomous driving function.)

# 2.研究思路与方法（Research ideas and methods）
通过搭建场景平台，设置信号灯以及障碍物探究自动驾驶解决方法。重新设计符合智能车与场景平台下的操作系统，针对采集后的数据处理方法进行了深入的实验和测试。在搭建自动行驶系统中，选择两种符合当前计算资源下的小体量深度学习模型进行不同训练任务的测试，对比分析模型训练结果，并针对在实际情况部署所产生的问题进行解决和优化。设计智能车避障系统，利用智能车前端激光雷达扫描数据进行方向区间划分，将激光扫描到的区域划分成若干个小区间，并根据划分区间的计算结果使智能车实现避障。结合实际剩余计算资源设计红绿灯识别系统，根据不同颜色数值区间的差异性进行颜色识别。当上述三种功能完成时，设定三种功能优先等级，结合实际运行环境设计自动驾驶系统。

<img width="400" alt="截屏2024-11-08 22 55 16" src="https://github.com/user-attachments/assets/cc7c1954-4396-4905-ab40-b5c04e42adda" div align=center />

（Explore solutions for autonomous driving by building a scene platform, setting up traffic lights and obstacles. Redesigned an operating system that is compatible with intelligent vehicles and scene platforms, and conducted in-depth experiments and tests on the data processing methods after collection.In building an autonomous driving system, two small-scale deep learning models that are suitable for the current computing resources are selected for testing different training tasks, and the training results of the models are compared and analyzed. Solutions and optimizations are made based on the problems arising from deployment in practical situations.Design an intelligent vehicle obstacle avoidance system that uses the front-end LiDAR scanning data of the intelligent vehicle to divide the direction interval, dividing the area scanned by the laser into several small intervals, and enabling the intelligent vehicle to achieve obstacle avoidance based on the calculation results of the divided intervals.Design a traffic light recognition system based on actual remaining computing resources, and recognize colors according to the differences in numerical ranges of different colors. When the above three functions are completed, set the priority of the three functions, and design the auto drive system in combination with the actual operating environment.）

# 3.实验环境与平台
由于希望在实车平台上验证前文所训练的自动驾驶模型，以考验自动驾驶模型在实际 情况下的可靠性。为此搭建了专门面向自动驾驶工况场景的智能车平台。该平台由幻宇智 能车平台改装而来，软件控制基于机器人操作系统(Robot Operating System,ROS)。本章将 对使用到的硬件及软件部分进行介绍。之后在模拟场景下进行试验，以验证自动驾驶模型 的实际性能。

（Due to the desire to validate the previously trained autonomous driving model on a real vehicle platform, in order to test the reliability of the autonomous driving model in practical situations. We have built an intelligent vehicle platform specifically designed for autonomous driving scenarios. This platform is modified from the Huanyu Intelligent Vehicle Platform, and its software control is based on the Robot Operating System (ROS). This chapter will introduce the hardware and software components used. Afterwards, experiments will be conducted in simulated scenarios to verify the actual performance of the autonomous driving model.）

## 3.1 场景平台的搭建
为了实现自动驾驶的安全性和可靠性，大量的数据收集和测试是必不可少的。然而，在真实道路上进行数据收集和测试存在一些问题，例如高昂的成本、时间限制、安全风险等。因此，建立自动驾驶模拟环境成为了一种有效的解决方案。自动驾驶模拟环境是通过仿真技术来模拟现实世界中的各种场景和情况，以进行自动驾驶系统的开发和测试。在这个模拟环境中，可以利用虚拟的道路网络、车辆模型和传感器模拟真实道路上的交通情况。通过收集和分析模拟环境中的数据，可以评估自动驾驶系统在不同情况下的性能和稳定性。
首先，进行自动驾驶模拟环境道路的设计，实现基本的道路行驶，智能车根据当前路况做出前进，后退，左转与右转动作

(In order to achieve the safety and reliability of autonomous driving, extensive data collection and testing are essential. However, there are some issues with data collection and testing on real roads, such as high costs, time constraints, safety risks, etc. Therefore, establishing an autonomous driving simulation environment has become an effective solution. The automatic driving simulation environment simulates various scenes and situations in the real world through simulation technology to develop and test the auto drive system. In this simulation environment, virtual road networks, vehicle models, and sensors can be used to simulate traffic conditions on real roads. By collecting and analyzing the data in the simulation environment, the performance and stability of the auto drive system in different situations can be evaluated.Firstly, the design of an autonomous driving simulation environment road is carried out to achieve basic road driving. The intelligent vehicle makes forward, backward, left turn, and right turn actions based on the current road conditions.)

![轨道详细数据](https://github.com/user-attachments/assets/0db7cf7a-73d3-442d-8b69-8137887bd3a6)

所设计的自动驾驶模拟环境在宽度为420厘米长度460厘米的矩形上进行车道设计。为了进一步保证模拟实际行车情况所涉及到的路况，设计车道宽度为35厘米对应1.5倍车身宽度。并从两条黑色标记点开始以逆时针顺序运行。共有6个直角弯，1个回头弯，2个折角弯和7条直道组成。

(The designed autonomous driving simulation environment performs lane design on a rectangle with a width of 420 centimeters and a length of 460 centimeters. In order to further ensure the road conditions involved in simulating actual driving situations, the designed lane width is 35 centimeters, corresponding to 1.5 times the width of the vehicle body. And run in counterclockwise order starting from the two black marked points. There are a total of 6 right angle bends, 1 turn back bend, 2 corner bends, and 7 straight paths.)

<img width="385" alt="截屏2024-11-08 23 14 58" src="https://github.com/user-attachments/assets/760d7d55-adda-479f-be52-e114ccbccebd">





