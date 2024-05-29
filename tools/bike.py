# A Class to define the weather and calendar information to preview the quantity of bikes.


#Import
import joblib
import numpy as  np

#Class
class Bike:
    # The constructor
   def __init__(self, bikes):
       self.bikes = bikes

   def prepare(self):
       

      # Taking each item get from the application
       month = { 1 : 1 , 2 : 1 , 3 : 3 , 4 : 4 , 5 : 5 , 6 : 6 , 
                7 : 7 , 8 :8 , 9 : 9 , 10 : 10 , 11 : 11 , 12 : 12}
       
       day_of_week = {'Friday' : 13 , 'Monday' : 14 , 'Saturday' : 15 , 
                      'Sunday' : 16 , 'Thursday' : 17 , 'Tuesday' : 18 , 'Wednesday' : 19}
       
       functioning_day = {0 : 20, 1 : 21}
       
       holiday = {0 : 22 , 1 : 23}
       
       hour = {0 : 24 , 1 : 25 , 2 : 26 , 3 : 27 , 4 : 28 , 5 :29 , 6 :30 ,7 : 31, 8 : 32, 
               9 : 33, 10 : 34, 11 : 35, 12 : 36, 13 : 37 , 14 : 38 , 15 : 39 , 16 : 40 , 
               17 : 41, 18 : 42, 19 : 43 , 20 : 44 , 21 : 45, 22 : 46 , 23 : 47}
       
       seasons = {'Autum' : 48, 'Spring' : 49 , 'Summer' : 50 , 'Winter' : 51 } 
       
       rainfall_category = {'drizzle' : 52 , 'heavy rain' : 53 , 
                            'light rain' : 54 , 'moderate rain' : 55 , 'no rain' : 56}
       
       snow_category = {'light snow' : 57 , 'moderate snow' : 58 ,'no snow' : 59}
       
       wind_category = {'calm' : 60 , 'light breeze' : 61 , 'plowing' : 62, 'weak breeze' : 63}
       
       solar_radiation_category = {'moderate' : 64 , 'strong' : 65 , 'weak' : 66}
      
       visibility_category = {'bad' : 67 , 'moderate' : 68 , 'very bad' : 69}
       
       result = []
       result[0] = self.bikes[0] #TO DO temperature
       result[1] = self.bikes[1] #To DO dew point
       result[2] = self.bikes[2] #TO DO humidity
       



