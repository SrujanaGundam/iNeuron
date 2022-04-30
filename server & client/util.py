from typing import List
import numpy as np
import json
import pickle
import datetime

__weather_encoder={}
__model=None
def get_estimated_traffic(holiday,weather,time,date,temp,clouds):

  #holiday
  if(holiday=='Yes'):
    holiday_in=[1]
  else:
    holiday_in=[0]

  #time
  time_t=int(time.split(":")[0])
  time_in=[0]*24
  time_in[time_t]=1

  #date
  # year,month,date=[int(x) for x in date.split('-')]
  year=int(date.split('-')[0])
  yr1=year
  month=int(date.split('-')[1])
  m1=month
  date=int(date.split('-')[2])
  d1=date
  month_in=[0]*12
  month_in[month-1]=1
  year_in=[0]*7
  year_in[year-2012]=1
  #print(type(year))


 #day
 #date formatting
  date1=datetime.date(yr1,m1,d1)
  week=date1.weekday()
  #week=convert.weekday()
  print(week)
  week_in=[0]*7
  week_in[week]=1


 #temp
  temp_in=[temp]

 #clouds_all
  clouds_in=[float(clouds/100)]

 #weather_main
  weather_dict=weather_to_number(weather)
  weather_in=[weather_dict]


  input_x=np.array(holiday_in + temp_in + clouds_in + weather_in + week_in + time_in +month_in + year_in).reshape(1,-1)

  return list(__model.predict(input_x))



def weather_to_number(weather_name):
    return __weather_encoder[weather_name]
def load_artifacts():  #opening the folder to acces model
    print("loading saved atrifacts..start")
    global __weather_encoder


    with open("./artifacts/weather.json","r") as f:
        __weather_encoder=json.load(f)


    global __model
    if __model is None:
        with open("./artifacts/saved__model.pickle","rb") as f:
            __model=pickle.load(f)
    print("loading saved artifacts..done")


if __name__=='__main__':
    load_artifacts()
    print(get_estimated_traffic('Yes','Fog','12:00','2013-05-2',288.6,50)[0])
    print(get_estimated_traffic('No', 'Mist', '2:00', '2014-06-12', 277.6,45)[0])
