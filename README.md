# LiveSensor-MachineLearning-MongoDB-project


Problem Statement:-
Air Pressure System is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefit of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a binary classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class indicates that the failure was caused by something else.

Solution Proposed:-
In this project, the system in focus is the Air pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as breaking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.
The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.

## 1)Problem statement.
Data: Sensor Data
Problem statement:
The system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.
-The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.

The total cost of a prediction model the sum of 'Cost_1' multiplied by the number of instances with type 1 failure and 'Cost_2' with the number of instances with type 2 failure, resulting in a 'Total_cost'. In this case 'Cost_1' refers to the cost that an unnecessary check needs to be done by an mechanic at an workshop, while 'Cost_2' refer to the cost of missing a faulty truck, which may cause a breakdown.
'Total-cost=Cost_1"No_instances + Cost_2" No_instances.'

-From the above problem statement we could observe that, we have to reduce false positives and false negatives. More importantly we have to ""reduce false negatives, since cost incurred due to false negative is 50 times higher than the false positives"".

---------------------------
Tools Installation:-
---------------------------
Inital steps

Softwares required to run the code editor and other softwares to begin the project
 
 Anaconda
 Python 
 Visual Studio Code Editor(VS Code) Software
 VS Code Extensions:-  
 GIT cli software
 Github
_______________________________________________________________________________
This Project includes python and machine learning and mongo db database is used. Live Sensor data is collected and stored in MongoDB database and end-to-end-machine-learning-project........ a complete machine learning project is implemented

-----------------------
# Project Execution:
First step: 

git clone https://github.com/chandrasai-Durgapu/LiveSensor-MachineLearning-MongoDB-project.git

1. create virtual environment
 conda create -p venv python=3.13.5

2. Activate Virtual environment
conda activate F:\DataScienceProjects\SENSORLIVE\venv

3. run setup.py
 python setup.py install

 4. install requirements.txt
 pip install -r requirements.txt

 added content

 EDA
 Exploratory Data Analysis ....file added partially....few steps of EDA was updated(full steps were pending)


run these commands in terminal:-
pip install -r requirements.txt

mongodb certificate issue
pip install --upgrade cryptography pymongo pyopenssl

pip install --upgrade pymongo cryptography pyopenssl

pip install --upgrade pymongo cryptography



pip install PyYAML
pip install dill


pip show python-dotenv pymongo certifi

where python
python -m site

python main.py

flowcharts folder

git add .
git commit -m "files added"
git push origin main
git config --global http.postBuffer 524288000
git lfs track "*.zip"



git remote set-url origin git@github.com:chandrasai-Durgapu/LiveSensor-MachineLearning-MongoDB-project.git



git remote set-url origin https://github.com/chandrasai-Durgapu/LiveSensor-MachineLearning-MongoDB-project.git


ssh-keygen -t rsa -b 4096 -C "chandrasekharcse522@gmail.com"

-------------------------


