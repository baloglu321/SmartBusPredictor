# SmartBus: Predictive Occupancy Analysis  for Optimized Commutes

Our project is designed to run both database and machine learning algorithms on the same server, and present the resulting outputs to users through an intuitive interface. We chose Mongo DB as our database application, as it provides efficient Docker images for our server needs. After retrieving data from Mongo DB using Python and Pandas, we implemented a library of machine learning algorithms. After evaluating several models, we selected the most suitable algorithm, which we trained to predict bus occupancy based on time and day of the week. The machine learning model produces predictions for 18 time periods across 10 different buses, which we display on our website using the Django framework. Our system is optimized to provide accurate occupancy predictions, enabling users to plan their journeys accordingly.
 
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
    
    
In ALLOWED_HOSTS = ['---'] on line 29, replace '---' with the dimming server ips

Save settings.py and back to old folder

    cd ..
    
And run it...

        python3 manage.py runserver 0.0.0.0:8000
        
        

