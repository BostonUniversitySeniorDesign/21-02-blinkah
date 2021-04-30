# BLINKAH User Manual

#### Boston University Computer Engineering Senior Design Project 2020-2021

Team Members:

Raghurama Bukkarayasamudram rbukka@bu.edu

Ritam Das ritamdas@bu.edu

William Pine wpine@bu.edu

Ayush Upneja upneja@bu.edu

Parker Van Roy parkervr@bu.edu





## Executive Summary

WE ARE BLINKAH: Revolutionizing the Road
	
BLINKAH is a leader in lateral thinking with our disruptive behavior-based-insurance-as-a-service (BBI-AAS) platform that engineers solutions to urgent pain points in our society. We enhance road safety and eliminate statistically proven policing biases. Leveraging proprietary edge computing machine learning algorithms in an IoT system with 4G LTE telecommunications, BLINKAH Dashcam Head Units are able to identify erratic drivers in real time, aggregate contextual information, and send reports to the BLINKAH Cloud. Using these key performance indicators, the BLINKAH Cloud conducts deep behavioral analysis on drivers in a robust big data computing environment and distributes these findings to insurance companies, emergency services, and other relevant entities through a REST API and data visualization tool known as the BLINKAH Computational Frontend (BCF). BLINKAH makes a social impact by incentivizing safe driving and solving non-emergency concerns through appropriate organizations, thus, reducing the risk of racial profiling that results in rampant police brutality and reinforcing road safety. “USE YAH BLINKAH!”

## Introduction

Racial profiling and targeting in the form of police traffic stops has been a persistent theme in American culture. The events of summer 2020 regarding the #BlackLivesMatter movement brought such grim issues to a national spotlight and sparked a much more rapid change in public perception of those who are enforcing road safety. A study published by Stanford in May 2020 analyzed a dataset of 100 million traffic stops conducted across the country, finding that “black drivers were less likely to be stopped after sunset, when a ‘veil of darkness’ masks one’s race, suggesting bias in stop decisions.” This bias is important to contextualize the horrific statistics and videos that have surfaced over the last few decades of police overreach and abuse with regard to traffic stops of racial minorities.

In the same study, the data showed that the bar for searching black and Latino drivers was much lower, as search rates were 4.3% for black drivers, 4.1% for Hispanic drivers, and 1.9% for white drivers. The threshold test calculates that the bar for searching black (5.0%) and Hispanic drivers (4.6%) is much lower than for white drivers (10.0%). This suggests significant amounts of bias and prejudice in the police force, as such a severe difference in threshold amongst all drivers certainly depicts a dystopian reality in our society.

In the ever-expanding fields of Machine Learning and Artificial Intelligence, there is no reason a simple outdated registration, broken taillight, or any minor infraction should result in police brutality. This is where BLINKAH plans to step in.

Our goal is to incentivize safe driving and solve non-emergency concerns through the appropriate organizations, thus, reducing the risk of racial profiling and reinforcing road safety.

In terms of hardware, there are BLINKAH head units composed of a dashcam, speaker, and touchscreen all running on the Nvidia Jetson Nano. These will be the edge computing dash cameras that will leverage computer vision and proprietary algorithms to analyze and report other vehicles on the road. 
The BLINKAH head units utilize 4G communication to the BLINKAH Cloud + Computational Frontend (BCF), where we analyze the aggregated data from our head units and keep records of vehicle/driver behavior. This enables BLINKAH to create reports of erratic drivers based on a variety of unsafe driving metrics and report such information to insurance providers and other drivers in the vicinity. 

Through BLINKAH, we provide mechanisms that can solve non emergency concerns directly through proper entities (insurance, DMV, etc) without the need to involve emergency/police services, and therefore reduce the risk of racial profiling and targeting, which leads to police brutality. We additionally solve for the large rate of unsafe driving habits which severely contribute to vehicle fatality rates. This is done by detecting erratic drivers in the vicinity of the user and notifying the user and other nearby drivers of any unsafe activity near them. The intention is to have a large network of head units on the road all monitoring each other to recreate road safety enforcement without any personal bias. Ultimately, BLINKAH eliminates irrelevant entities in traffic stops and reinforces safe driving habits.

Following this introduction to BLINKAH, you will find:

A system overview and installation detailing the technical installation, setup, and support instructions
Operational Modes and Safety Issues
An in-depth description of the technical components of the product
Head Unit
BLINKAH Cloud + Computational Frontend
Engineering standards relevant to BLINKAH implementation
Cost Breakdown & Expense Sheet
Appendix
Specifications
The BLINKAH Team
 








## System Overview and Installation
BLINKAH is a behavior-based-insurance as-a-service platform. The BLINKAH system consists of two user-facing components - the BLINKAH Head Unit, and the BLINKAH Computational Frontend. These components have separate users. While the relation between these two users is determined as a business need, they do not have technical overlap and exist as independent operators. The BLINKAH system has been streamlined in deployment and operation for all users with a simplified user experience.
 
### Overview Block Diagram

Systemdiagram.png 
DESCRIPTION

### User Interface

The user interface is twofold. The first component of the user interface is the BLINKAH Head Unit. 

The Head Unit interface is simple - there is a landing page and a camera feed page. While the BLINKAH operates automatically, the display can be changed to activate a live feed of the computer vision analysis. Reports will display a symbol on the screen and play audio over a speaker so as to not distract the driver. A small clock is displayed on the BLINKAH Head Unit for user convenience.




The second component of the user interface is the BLINKAH Computational Frontend. This user interface is deployed on Firebase and offers secure login for BLINKAH Admins. On this dashboard, admins can look up histories associated with specific license plates in addition to visualizing report data on a heatmap. 

Admin Dashboard with license plate lookup, generated statistics, and navbar


Heatmap visualization of generated Boston incident data


Splash page featuring BCF logo and OAuth

### Physical Description



		Head Unit & Dashcam vehicle mockup

			1998 Volvo XC70 Testing Setup for Alpha Unit BLINKAH0 
### Installation, setup, and support

BLINKAH Head Unit


Displayed is a set of Dash Camera Electrical hookup components. These kits provide 5V 2A DC power. A kit similar to this is expected to be prepared by the user for the BLINKAH Head Unit installation. 

assembled_mount.png
Displayed is an assembled version of the BLINKAH Head Unit Mount that should be installed in user vehicles, showing successful operation of basic object detection on the screen.


3d_components.png
Displayed is a collection of the 3D-printed components involved in the mounting of the BLINKAH Head Unit for the Beta version. These components are printed in ABS Plastic.


For installation purposes, it is assumed that the user has prepared a sufficient Dash Cam Hardwire in their vehicle as pictured in (IMG ABOVE). It is also assumed that the BLINKAH Head Unit is delivered to recipients completely assembled and simply needs to be mounted with 3M Mounting Tape or with the provided mounting holes + screws, however, if this is not the case, the user will be provided with sufficient 10x2.5M screws and the cables required to connect internal peripherals to the Jetson Nano.



## BLINKAH Computational Frontend
Visit https://BLINKAH.net and log in with an SSO option!


## Operation of the Project 

### Operating Mode 1: Normal Operation

In a normal operating mode, a user will interact with the BLINKAH Head Unit as follows:
The user turns the device on, and the Head Unit automatically analyzes vehicles in front of the user’s car
The user will drive their vehicle and the BLINKAH Head Unit will scan automatically
If an erratic driver is recognized, the device will upload a full report with relevant details to the BLINKAH Cloud, in addition to supporting evidence
The driver will receive a visual and audio notification if there is an erratic driver nearby through the BLINKAH Head Unit


### Operating Mode 2: Abnormal Operations
Abnormal operations include the Jetson Nano crashing, power outage due to external automobile electric failure, and mechanical failure in any circumstance.

To exit this state of abnormal operations, the user can simply restart the device, and ensure that all connections are attached properly before enabling the erratic driver detection.

### Safety Issues

It is important to not get distracted by the notifications or the display screen. Users should not be driving with anything other than the given UI on the head unit. Additionally, the current installation is quite rudimentary, and as a result any mechanical failure involving components getting disconnected should be swiftly resolved by pulling over, and resetting the device. Users must also pay attention to not overdraw power and make sure that any converters are deemed safe for the automobile.

## Technical Background
BLINKAH Head Unit

The BLINKAH Head Units are driven by Nvidia Jetson Nano 4G Developer Boards running JetPack 4.5.1 (A fork of Ubuntu 18.04). The Head Unit uses Python 3.6 and QtPy5 to run it’s frontend software, which is displayed on a 1024x600 7” HDMI/USB LCD Touchscreen. The Head Unit computer vision module involves MobileNet v2 for object detection, OpenALPR for license plate optical character recognition, and proprietary algorithms for lane detection and composite erratic driver detection. Video is captured from a  8MP IMX219-160 CSI Camera with GStream and the JetCam library, and are buffered in jpeg format in the filesystem. CVLC and a USB Speaker are used to play audio notifications. A Hologram 4G modem and sim card are used for telecommunication, and a GPS module is attached for location tracking. The software is containerized with Buildah and deployed in Podman.

BLINKAH Cloud

The BLINKAH Cloud, in its current form, consists of a single DigitalOcean droplet server running Ubuntu 20.04. On top of this Ubuntu installation, we are running our backend server code using Python, Django, and the Django REST framework, wrapped in a Python virtual environment for easy dependency management. The Django backend code is responsible for defining the database model schema and exposing REST endpoints to interact with the database, including operations such as reading, adding, modifying, and destroying data, as well as filtering. The database itself is an SQLite database for prototyping purposes, with future intentions to upgrade to PostgreSQL if scaling demands necessitate it. The exposed REST endpoints provided by the Django backend are used by both the individual head units, for submitting reports and polling for notifications, and by the BLINKAH computational frontend.

BLINKAH Computational Frontend




## Relevant Engineering Standards

Some of the relevant engineering standards that BLINKAH utilizes include REST API’s, SSO/OAuth authentication, HTML syntax, the JPEG image format, and the JSON data format.

BLINKAH Head Unit Standards

For the head unit hardware, it utilizes the USB, CSI, and HDMI standards for communicating with other hardware components, including the speaker, 4G modem, camera, and touchscreen display. The JPEG image format is used to capture frames from the head unit’s dashcam, and feed it through our machine learning pipeline, which detects individual vehicles, crops them, and sends a report to the server with a cropped JPEG.

BLINKAH Cloud (Backend & Frontend Standards)

The REST API standard is used for communication between the Jetson head units and Blinkah Computational frontend, and with the cloud backend. SSO/OAuth authentication is used for signing into the computational frontend. HTML syntax is obviously used in the frontend, and JSON is used for sending and receiving data via the REST standard. The MP3 audio storage format is utilized for generating audio notifications via IBM Watson on the backend server, and downloading and playing them back on the individual head units Containers were built in an OCI-compliant standard. Furthermore, the Python 3 and JavaScript ECMA language standards were used in developing the software.


	In terms of Engineering Management, the project is developed with an upstream development process with Git. Conventional open source pull request code review standards and lgtm messages are used to create upstream builds that are merged based on agile weekly goals.
## Cost Breakdown


Per-Unit Project Costs for Production of Beta Version (Next Unit after Prototype)
Item
Description
Unit Cost
1
 Jetson Nano 4G + SD Card
 115
2
 Hologram 4G Modem / SIM / GPS
80 
3
 Camera + Lens 
 25
4
 7” LCD Touchscreen + Speaker
65
5
 Casing + Mounting
 10
Beta Version-Per-Unit Total Cost
295




## Appendices

Appendix A - Specifications

In spec sheet

Appendix B - Team Information

Raghurama Bukkarayasamudram
Developed the BLINKAH Cloud Notifications Service and REST API with IBM Watson Text-to-Speech and integrated it in the BLINKAH Head Unit. Created the Jetson Nano Speaker Framework. Designed the BLINKAH Head Unit Frontend. Assisted in working on the lane detection and erratic driver detection algorithms.

Ritam Das
Designed and developed the BLINKAH Computational Frontend primarily. Assisted on backend REST API and endpoints as well as object, lane, and erratic driver detection algorithms.

William Pine
Worked primarily on the BLINKAH Cloud’s backend REST API and endpoints. Also assisted with work on lane detection and erratic driver detection code which runs directly on the Jetson head unit.

Ayush Upneja
Worked primarily on the BLINKAH Computational Frontend and the BLINKAH Cloud. Will be working as a Software Engineer for Citrix Systems after graduation.

Parker Van Roy
Worked on the BLINKAH Cloud Rest API and Python Services and BLINKAH Head Unit. Wrote the Head Unit QtPy5 Application, proprietary lane detection algorithm, and developed the erratic driver detection code. Compiled and integrated various services on the Jetson Nano.

















