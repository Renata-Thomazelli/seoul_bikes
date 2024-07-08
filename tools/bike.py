# A Class to define the weather and calendar information to preview the quantity of bikes.


#Import
import joblib
import numpy as  np

#Class
class Bikes:
    # The constructor
   def __init__(self, bikes):
       self.bikes = bikes

   def prepare(self):

       result = np.zeros(72)

      # Taking each item get from the application
       month = { "1" : 0, "2" : 1 , "3" : 2 , "4" : 3 , "5" : 4 , "6" : 5 , 
                "7" : 6 , "8" :7 , "9" : 8 , "10" : 9 , "11" : 10 , "12" : 11}
       
       day_of_week = {'0' : 12 , '1' : 13 , 2 : 14 , 
                      '3' : 15 , '4' : 16 , '5' : 17 , '6' : 18}
       
       functioning_day = {'0' : 19, '1' : 20}
       
       holiday = {'0' : 21 , '1' : 22}
       
       hour = {'0' : 23 , '1' : 24 , '2' : 25 , '3' : 26 , '4' : 27 , '5' :28 , '6' :29 ,'7' : 30, '8' : 31, 
               '9' : 32, '10' : 33, '11' : 34, '12' : 35, '13' : 36 , '14' : 37 , '15' : 38 , '16' : 39 , 
               '17' : 40, '18' : 41, '19' : 42 , '20' : 43 , '21' : 44, '22' : 45 , '23' : 46}
       
       seasons = {'Autum' : 47, 'Spring' : 48 , 'Summer' : 49 , 'Winter' : 50 } 
       
       rainfall_category = {'1_no rain' : 51 , '2_drizzle' : 52 , 
                            '3_light rain' : 53 , '4_moderate rain' : 54 , '5_heavy rain' : 55}
       
       snow_category = {'1_no snow' : 56 , '2_light snow' : 57 ,'3_moderate snow' : 58}
       
       wind_category = {'1_calm' : 59 , '2_plowing' : 60 , '3_light breeze' : 61, '4_weak breeze' : 62}
       
       solar_radiation_category = {'1_weak' : 63 , '2_moderate' : 64 , '3_strong' : 65}
      
       visibility_category = {'1_very bad' : 66 , '2_bad' : 67 , '3_moderate' : 68}
       
       
       result[69] = float(self.bikes[69]) 
       result[70] = float(self.bikes[70]) 
       result[71] = float(self.bikes[71]) 

       return result

   def predict(self, car):
        quantity_bikes_to_predict = [bikes]
        model = joblib.load('modelo/modelo.pkl')
        predicted_bikes_quantities = model.predict(quantity_bikes_to_predict)
        value = predicted_bikes_quantities[0]
        return value
       



