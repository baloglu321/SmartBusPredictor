# Bus Occupancy Rate Prediction

The project has basically been developed to run both database and machine learning algorithms on the same server, as well as to design an interface that displays these outputs to the user. Mongo db is selected for to be database app. It was used because it has docker images that can run on the Mongo db server and it will work efficiently. The data read from Mongo db with using python and pandas was sent to a library with machine learning algorithms. Among these machine learning algorithms, the one with the most suitable was selected and it was made to predict according to the days of the week and day in hour. Outputs from the machine learning model will estimate based on the current day/time, predicting how full the bus is. It will display the predictions on the website using the Django framework. It will make this estimation as 18 different periods for 10 different buses.
 
*To review the machine learning algorithm: https://github.com/baloglu321/Patika_Practicum/blob/main/BusCapPred/Home/bus_cap_pred.py

Attention, This code specifically created for this data. You should rewrite code for different dataset.

Installation steps
----------------------

First of all, you must install docker and mongoDb on your server. 

*For install docker on your server (my recommended OS is ubuntu): https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04

Run mongodb on top of docker


    docker run -d --network=host -v /opt/data:/data/db mongo
  
  
And import your dataset from this mongodb server.

*For more information on this:https://github.com/baloglu321/Spark_Workspaces/blob/main/Mongo_server_data_upload.ipynb

Clone this repository to run on the server

    git clone https://github.com/baloglu321/Patika_Practicum.git
    
Go inside the folder and isntall requirements


    cd Patika_Practicum
    pip3 install -r requirements.txt
    
    
#Warning: pip can be pip or pip3 depending on python installation

Go inside the folder and edit to settings.py

    cd BusCapPred/BusCapPred
    nano settings.py
    
    
In ALLOWED_HOSTS = ['*'] on line 29, replace "*" with the dimming server ips

Save settings.py and back to old folder

    cd ..
    
And run it...

        python3 manage.py runserver 0.0.0.0:8000
        
        

