# BLINKAH
### Parker Van Roy, Ayush Upneja, William Pine, Ritam Das, Raghurama Bukkarayasamudram

BLINKAH is a behavior-based insurance system that uses Computer Vision to analyze other drivers on the road as well as providing directions and safety notifications, as well as delivers a data analysis dashboard for enterprise insurance customers.

#### Boston University Computer Engineering Senior Design Project 2020-2021

## Frontend Run Instructions

-   Install NodeJs from  [NodeJs Official Page](https://nodejs.org/en/?ref=creativetim)
-   Open Terminal
-   Go to your file project (where you've unzipped the product)
-   Navigate to frontend
-   Run in terminal
    
    ```
    npm install
    ```
    
-   Then run
    
    ```
    npm start
    ```
    
    If you have an error something containing
    
    ```
    Module not found
    ```
    
    You should check if in your root project folder you have a file named  `.env`.  
    If you do not have it, then create it and add this line in it:  `NODE_PATH=./src`  
    If that does not work, you need to do the following
    
    ```
    npm install --g cross-env
    ```
    
    then change the  `script`  inside  `package.json`  by adding  `NODE_PATH=./src`  inside it. For example, the start script would be changed from
    
    ```
    "start": "react-scripts start",
    ```
    
    to
    
    ```
    "start": "NODE_PATH=./src react-scripts start",
    ```
## Backend Run Instructions

## Server Setup Instructions

## OpenALPR Setup Instructions
We decided to use OpenALPR, an open-source Automatic License Plate Recognition library software to handle the bulk of our computer vision and machine learning processes. It is based in C++ with dependencies available in python3, so we are using OpenCV as well as tesseract to handle the translation of license plates to text.
Since OpenALPR is based on windows and ubuntu linux, we decided to set it up on an ubuntu OS. We simply install the required prerequisites and the actual OpenALPR from the github, set up a build directory, and compile an environment. Once that is set up, we can compile the library, and install the binaries to the local machine and test. https://github.com/openalpr/openalpr/wiki/Compilation-instructions-(Ubuntu-Linux)


## Introduction
In this section we shall introduce the motivation for the introduction of BLINKAH. The supporting evidence presented henceforth will be with reference to entries 1&2 in the bibliography

### Need

With the current state of society in the context of the the #BlackLivesMatter movement, it has become apparent that racial minorities are facing incredible hardship. One of the most prominent forms of profiling and targeting comes in the form of traffic stops performed by the police. 

A study published in Nature in May 2020 analyzed a dataset of 100 million traffic stops conducted across the country, finding that “black drivers were less likely to be stopped after sunset, when a ‘veil of darkness’ masks one’s race, suggesting bias in stop decisions.” This bias is important to contextualize the horrific statistics and videos that have surfaced over the last few decades of police overreach and abuse with regard to traffic stops of racial minorities. 

In the same study, the data showed that the bar for searching black and Latino drivers was much lower, as search rates were 4.3% for black drivers, 41.% for Hispanic drivers, and 1.9% for white drivers. The threshold test calculates that the bar for searching black (5.0%) and Hispanic drivers (4.6%) is much lower than for white drivers (10.0%). The analysis that this is unjust is substantiated by the fact that the bar is so low that the difference in the contraband possession rate between white and Latino drivers is a whopping 10%. 

In a world where Machine Learning and Artificial Intelligence are expanding everyday, there is no need for a simple outdated registration, or broken taillight should result in police brutality on the highway. 

Through Blinkah, we provide mechanisms through which non emergency concerns can be solved directly through proper entities (insurance, RMV, etc), and therefore reducing the risk of racial profiling and targeting, resulting in rampant police brutality. We additionally solve for the large rate of unsafe driving habits which cause accidents in the country, severely contributing to loss of human life, by notifying nearby drivers of any unsafe activity near them.

### Problem Statement

There are two major concerns with the current system in society. Firstly, according to the CDC road crashes are the leading cause of death in the country, and therefore the status quo is ineffective at deterring unsafe driving habits. Secondly, racial profiling and targeting have spiraled completely out of control, resulting in major police brutality at minor traffic stops which could be solved directly through the relevant entities themselves. Thus we ask the question, how can we create a fairer system for road safety?

We solve this problem with three major deliverables.

The first deliverable is the Blinkah Hardware Unit. This unit contains a camera, and integrates with your phone to get your latitude and longitude for notification purposes. This hardware unit acts as a dashcam, constantly recording, compressing, and uploading footage to the cloud. It also has a display attached to the head unit, which has both audio and video notifications for nearby unsafe drivers.

The second deliverable is the software algorithm. This algorithm is completed completely in the cloud, in which we process all of the data using computer vision algorithms to analyze the video source. We aim to have > 50% erratic driver identification accuracy, in < 5 minutes of processing time.

The final deliverable is the dashboard and backend API. After the completion of our software algorithm and a hit on any traffic violation or unsafe driving, we have multiple API endpoints to send the relevant traffic violation or notification of nearby unsafe driving to relevant entities. This allows for us to directly communicate with insurance companies, State RMVs, or even police. We also securely store database driver history records.

## Product
In this section, we will make clear the goals and general design of BLINKAH as a product in order to facilitate the engineering requirements.

### Deliverables
We solve the paradoxical road safety problem with the BLINKAH project, which consists of three major deliverables: The first deliverable is the BLINKAH Hardware Unit. This unit contains a camera, and integrates with your phone to get your latitude and longitude for notification purposes. This hardware unit acts as a dashboard camera, constantly recording, compressing, and uploading footage to the cloud. It also has a display attached to the head unit, which has both audio and video notifications for nearby unsafe drivers. 

The second deliverable is the software algorithm. This algorithm is completed completely in the cloud, in which we process all of the data using computer vision algorithms to analyze the video source. We aim to have > 50% erratic driver identification accuracy, in < 5 minutes of processing time. 

The final deliverable is the dashboard and backend API. After the completion of our software algorithm and a hit on any traffic violation or unsafe driving, we have multiple API endpoints to send the relevant traffic violation or notification of nearby unsafe driving to relevant entities. This allows for us to directly communicate with insurance companies, State RMVs, or even police. We also securely store database driver history records.

### Visualization
Fig. 1. A drawing of the BLINKAH unit in a vehicle. Note the BLINKAH head unit in yellow and the proprietary dashboard camera in red. 

Picture this: you are driving and approach a busy intersection. From your left, a car runs the red light and cuts you off within centimeters! You honk your horn to alert other drivers in the area to beware, but the car is out of sight in seconds, weaving traffic. A few minutes later, you pass a car accident on the side of the road involving the very same vehicle. 

This is an easily avoidable situation given modern technology, and it doesn’t require everyone to use a self-driving car! With BLINKAH, everyone is made safer on the road. Here’s the same situation played out with BLINKAH: 

You are driving and approach a busy intersection. As you approach, you receive a notification from your BLINKAH device warning you of an erratic, dangerous driver approaching from your left, so you slow down at the intersection. From your left, a car runs the red light! Your BLINKAH unit then sends data to the BLINKAH cloud and alerts other drivers up the road of the danger. A few minutes later, you receive a notification that you have recieved a bonus for helping to report dangerous drivers on the road!

### Competitors

Creating an effective solution to ineffective policing, limiting traffic stops, and disincentivizing reckless driving are not new ideas; however, there are no viable remedies out there addressing all of these issues at once like BLINKAH intends to. BLINKAH falls into the driver safety/traffic monitoring industry where there are no shortage of companies but rather a shortage of innovative solutions addressing the real problems faced by many in society. Waze and police radar manufacturers attempt to alert you of police locations, but they have been proven to be highly inaccurate and unreliable. Tesla’s autonomous driving system does an excellent job of using computer vision in realtime to determine potential safety threats and direct the vehicle. However, they lack the proprietary algorithm we will be using to detect erratic drivers. Several insurance companies offer safe driver discounts to incentivize safe driving, but that doesn’t enforce safe driving nor address the issue of ineffective policing. Many cars come with a built-in safety service such as OnStar, but this addresses safety concerns after you have been in an accident. BLINKAH is more of a preventative measure rather than reactive feature. These are all relevant technologies in driver safety, but the most directly competitive brands for BLINKAH are: Telematics, Nexar, and GoTrueMotion. 

Telematics technology determines your driving pattern using GPS, accelerometers, gyroscopes, and more. They are one of our main competitors since their goal is to improve driver safety by incentivizing drivers to save on their insurance premiums. Geotab is one such company utilizing this technology along with Internet of Things and the Cloud. Geotab aims to innovate in the areas of: traffic prediction, performance benchmarking, and general safety. This information is stored in the cloud and accessed by mobile or desktop devices in the form of reports. Our main differentiating feature is that we do not rely on a telematics based technology, and instead depend on a real-time dashcam that analyzes driving patterns. While Geotabs technology allows users and companies to get very in-depth information about their driving, it does not have a major impact real-time aside from alerting on nearby accidents of police. 

Gotrue motion is another potential competitor that relies on using phone sensor data to score your driving. Using the phone is a convenient way to get rough estimates, but real, in-depth traffic analysis requires a more real Nexar is another company that produces dash-cams providing real time traffic and accident information through an app. This follows the WAZE style of reporting traffic data, but claims to upload information anonymously. While similar to our concept, its focus on purely traffic makes it more of an add on for ride-sharing with some emphasis on driver safety. BLINKAH applies our machine learning algorithm in real time to observe OTHER drivers on the road to determine if they are erratic allowing you to know who to avoid. Additionally, BLINKAH aims to avoid traffic-related stops by informing drivers of basic information. BLINKAH can go the route of targeting insurance companies, car dealerships, or possibly state services.


## Engineering Requirements
In this section, we will dive deeper in depth into our system in designing BLINKAH for senior design and beyond. The design details, system overview, and general timeline are described.

### Constraints
After reviewing the possible hardware modules and peripherals against our objectives and constraints, we identified the following hardware configuration to suit our needs: 
1) The hardware prototype will utilize the Nvidia Jetson Nano board, running Linux, for on-board interfacing and processing of camera data. 
2) The hardware prototype will utilize a single camera, recording footage at a minimum of 720p resolution and 15 frames per second. 
3) The camera will interface with the Jetson Nano via USB connection. Although a CSI bus connection would result in better performance, its distance limitation of less than 10 cm would make it incompatible with our project. 
4) The camera’s enclosure or mounting must be able to dampen vehicle-produced vibrations to some degree, as jitter may interfere with data processing. 
5) The Jetson Nano will interface with a color LCD display of at least 480p resolution, which is able to display text and images, and a speaker which is able to generate clearly audible alerts produced by the on-board software. 

Regarding the on-board software, the following requirements were identified, in order for the project to meet its objectives: 
1) The computer vision algorithm must be able to identify at least 50% of clearly visible erratic drivers in the camera’s field of view. 
2) The computer vision algorithm must not take longer than 300 seconds in returning a result after initial data acquisition. 
3) The on-board software must be able to successfully uplink results from the algorithm to a cloud server, receiving positive acknowledgement of transmission. 
4) The on-board software must be able to listen for and receive incoming data from the cloud server. 
5) The on-board software must be able to parse incoming data into alerts and notifications to be presented to the driver in a non-distracting manner. 

Regarding the cloud software and backend API, the following requirements were identified, in order for the project to meet its objectives: 
1) The server software must be able to listen for and receive uplinked data from several different ground units. 
2) The server software must be able to classify incoming data, store it, and relay it to the relevant entities, such as insurance providers or the local department of motor vehicles. 
3) The server software must be able to identify other users in the vicinity of a possible hazard which was identified through uplinked data. 
4) The server software must be able to send alerts and notifications to users in the vicinity of a possible hazard, and receive positive acknowledgement of transmission. 
5) The server software must be able to present its data and system status through a protected web-based dashboard

### System Overview

Fig. 2. Initial System Overview Diagram Displayed in figure 2 is an overview of the BLINKAH system. Here are some details: 
- The BLINKAH Head Unit development model is an nVidia Jetson with capabilities to communicate over bluetooth with a user cellphone, has a touchscreen display for directions and notifications, has audio notifications, and connects to a proprietary dashboard camera. It communicates over cellular data to the BLINKAH Cloud. 
- The BLINKAH Cloud is a cluster of servers that operate to create a seamless API-based system for other components. The intent is to deliver BLINKAH Cloud using OpenShift for scalability. The operations include Computer Vision Servers that operate on individual cameras, Road Analysis Servers that render what occurs on the roads, multiple databases to store data of different types, Distribution Servers to distribute output information, a Directions Server to serve directions to users, and a Notification Server to distribute user notifications. 
- The BLINKAH Dashboard is a data visualization tool and API endpoint for accessing the compiled information from the BLINKAH Cloud. The intent is to deliver data analysis to insurance companies, notify emergency services when relevant, and report minor vehicle infractions such as broken tail lights to local government, bypassing the police.

### Timeline

Fig. 3. Timeline Checkpoints Displayed in figure 3 is the main completion checkpoints of the BLINKAH project and a ray displaying the relative style of production. Here is some more detail: 
- Proposal: This phase has been completed. It involved the initial ideation of the project and ended with the project proposal submission. 
- Design: This phase is completed with the submission of this paper. It consisted of base design questions, an Informal Design Review, a PDRR presentation, and a ‘Shark Tank’ session with alumni. 
 - Device: The IoT device creation is a priority in this project. Although it will still be subject to change, completing the IoT Hardware of the BLINKAH project is a priority as it will allow for more fluid work in an agile, software-based environment. 
 - Dashboard: The software sided Dashboard component of this project will be the final phase. It is an API and data visualization tool for enterprise level use.
 - Note that the BLINKAH Cloud has not been mentioned; this is because as we progress towards an agile workflow it will be a necessity to have completed in minor components throughout other parts of the project.
 - The goal is to progressively progress form a Waterfall engineering design style to an agile environment consisting of software sprints.



## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
