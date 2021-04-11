import streamlit as st
import pickle
import pandas as pd 
import numpy as np
import datetime
import time

st.title("RAKSHIT FLIGHT SERVICE PRICE PREDICTION")

st.sidebar.header(" FLIGHT TIMING DETAILS ")
st.sidebar.subheader(" Departure Timings ")

month = pd.to_datetime("today").month
day = pd.to_datetime("today").day
year = pd.to_datetime("today").year


depart = st.sidebar.date_input("Date" , datetime.date(year,month,day))
if depart is not None:
    mon_dep = depart.month
    day_dep = depart.day
    
hour_dep = st.sidebar.selectbox("Hour", list(range(0,24)))
minute_dep = st.sidebar.selectbox("Minute", list(range(0,60)))

st.sidebar.subheader("Arrival_details:")
arrival = st.sidebar.date_input("Date:" , datetime.date(year,month,day))
if arrival is not None:
    
    mon_arr = arrival.month
    day_arr = arrival.day
        
        

hour_arr = st.sidebar.selectbox("Hour:", list(range(0,24)))
minute_arr = st.sidebar.selectbox("Minute:", list(range(0,60)))



st.subheader("Departure Timing :")
x = "2020" + "/"  +str(mon_dep) + "/" + str(day_dep) + " " + str(hour_dep) + ":" + str(minute_dep)
if x is not None:
        
    tim = pd.to_datetime(x)
    if tim is not None:
        st.write(tim)
       
st.subheader("Arrival Timing :")
y= "2020"+"/"+str(mon_arr)+"/"+str(day_arr)+" "+str(hour_arr)+":"+str(minute_arr)
if y is not None:
    lol= pd.to_datetime(y)
    if lol is not None:
        st.write(lol)

st.subheader("FROM :")
city=st.selectbox("",["Delhi","Kolkata","Banglore","Mumbai","Chennai"])
if city=="Delhi":
    source_inp=0
elif city=="Kolkata":
    source_inp=1
elif city=="Banglore":
    source_inp=2
elif city=="Mumbai":
    source_inp=3
else:
    source_inp=4
    
st.subheader("TO :")
dest = st.selectbox("" , ['Bangalore', 'Cochin', 'Hyderabad','Delhi',"New Delhi",'Kolkata'])
if dest == "Bangalore":
    dest_inp = 2
elif dest == "Cochin":
    dest_inp = 3
elif dest == "Delhi":
    dest_inp = 0
elif dest == "Hyderabad":
    dest_inp = 4
elif dest == "Kolkata":
    dest_inp = 1
else:
    dest_inp=5
    
st.subheader("Select Airline")
airline = st.selectbox("  " , ["Indigo","Air India","Jet Airways","SpiceJet","Multiple Carriers","Go Air","Vistara","Vistara Premium Economy","Jet Airways Business","Multiple carriers Premium Economy","Trujet"])

if airline == "Indigo":
    air_inp = 0
elif airline == "Air India":
    air_inp = 1
elif airline == "Jet Airways":
    air_inp = 2
elif airline == "SpiceJet":
    air_inp = 3
elif airline == 'Multiple Carriers':
    air_inp = 4
elif airline == "Go Air":
     air_inp = 5
elif airline == "Vistara":
     air_inp = 6
elif airline == "Vistara Premium Economy":
     air_inp = 7
elif airline=="Jet Airways Business":
    air_inp =8
elif airline =='Multiple carriers Premium Economy':
    air_inp=9
else:
    air_inp=10
    
st.subheader("No of Stops")
stops=st.selectbox("",[0,1,2,3])

if stops==0:
    stop_inp=0
    
elif stops==1:
    stop_inp=1
    
elif stops==2:
    stop_inp=2
   
elif stops==3:
    stop_inp=3
    
else:
    stop_inp = 4
    

      
tim2 = str(lol-tim)
if tim2 is not None:
    hr = int(tim2.split(':')[0][-2:])
    mini = int(tim2.split(':')[1])
   
st.subheader("Duration")
if lol is not None:
    a=str(lol-tim)+"------------->"+str(hr)+" Hours and "+str(mini)+" Minutes "
    st.write(a)
    
    
    
model = pickle.load(open("flightpred.pkl","rb"))

    #prediction

par = [air_inp , source_inp , dest_inp ,stops ,day_dep, mon_dep,hour_arr,minute_arr, hour_dep , minute_dep, mini,hr,]
arrays=np.array(par,dtype="int64")
    
    
if st.checkbox("PREDICT"):
    pred = model.predict([arrays])[0]
    st.write("Your Fare Price is : " , round(pred ,3)  , "INR")
    
