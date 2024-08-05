# A Class to define the weather and calendar information to preview the quantity of bikes.


#Import
import sys
sys.path.append('D:\Projetos\ML\Seoul_bikes')
import joblib
import numpy as  np
import pandas as pd
from tools.encoders import CategoricalVaribleEncoder
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("CategoricalVaribleEncoder importado com sucesso")

#Class
class Bikes:
    # The constructor
   def __init__(self, bikes):
       
       self.bikes = bikes
       
       

   def prepare(self):

       result = {}

      # Taking each item get from the application
       month_columns = { "1" : 0, "2" : 1 , "3" : 2 , "4" : 3 , "5" : 4 , "6" : 5 , 
               "7" : 6 , "8" :7 , "9" : 8 , "10" : 9 , "11" : 10 , "12" : 11}
       
       month = { "onehot__x0_1" : '0', "onehot__x0_2" : '0' , "onehot__x0_3" : '0' , "onehot__x0_4" : '0' , "onehot__x0_5" : '0' , "onehot__x0_6" : '0' , 
               "onehot__x0_7" : '0' , "onehot__x0_8" :'0', "onehot__x0_9" :'0', "onehot__x0_10" : '0' , "onehot__x0_11" : '0' , "onehot__x0_12" : '0'}
       month_index = self.bikes[0]
       month[month_index] = '1'
          
              
       #result['month'] = [str(self.bikes[0])]
      
       day_of_week_columns = {'0' : 12 , '1' : 13 , '2' : 14 , 
                      '3' : 15 , '4' : 16 , '5' : 17 , '6' : 18}
       
       day_of_week = {'onehot__x1_0' : '0' , 'onehot__x1_1' : '0' , 
                      'onehot__x1_2' : '0' , 'onehot__x1_3' : '0' , 
                      'onehot__x1_4' : '0' , 'onehot__x1_5' : '0' , 
                      'onehot__x1_6' : '0'}
       
       day_index = self.bikes[1]
       day_of_week[day_index] = 1
       #result['day_of_week']=[str(self.bikes[1])]
       
       functioning_day_columns = {'0' : 19, '1' : 20}
       functioning_day = {'onehot__x2_0':'0','onehot__x2_1':'0'}

       functionin_day_index = self.bikes[2]
       functioning_day[functionin_day_index] = 1
       #result['functioning_day']=[str(self.bikes[2])]
       
       holiday_columns = {'0' : 21 , '1' : 22}
       holiday = {'onehot__x3_0':'0','onehot__x3_1':'1'}

       holiday_index = self.bikes[3]
       holiday[holiday_index] = 1
       #result['holiday']=[str(self.bikes[3])]
       
       hour_columns = {'0' : 23 , '1' : 24 , '2' : 25 , '3' : 26 , '4' : 27 , '5' :28 , '6' :29 ,'7' : 30, '8' : 31, 
               '9' : 32, '10' : 33, '11' : 34, '12' : 35, '13' : 36 , '14' : 37 , '15' : 38 , '16' : 39 , 
               '17' : 40, '18' : 41, '19' : 42 , '20' : 43 , '21' : 44, '22' : 45 , '23' : 46}
       
       hour = {'onehot__x4_0' : 0 , 
               'onehot__x4_1' : 0 , 
               'onehot__x4_2' : 0 , 
               'onehot__x4_3' : 0 , 
               'onehot__x4_4' : 0 , 
               'onehot__x4_5' : 0 , 
               'onehot__x4_6' : 0 ,
               'onehot__x4_7' : 0, 
               'onehot__x4_8' : 0, 
               'onehot__x4_9' : 0, 
               'onehot__x4_10' : 0, 
               'onehot__x4_11' : 0, 
               'onehot__x4_12' : 0, 
               'onehot__x4_13' : 0 , 
               'onehot__x4_14' : 0 , 
               'onehot__x4_15' : 0 , 
               'onehot__x4_16' : 0 , 
               'onehot__x4_17' : 0, 
               'onehot__x4_18' : 0, 
               'onehot__x4_19' : 0 , 
               'onehot__x4_20' : 0 , 
               'onehot__x4_21' : 0, 
               'onehot__x4_22' : 0 , 
               'onehot__x4_23' : 0}


       hour_index = self.bikes[4]
       hour[hour_index] = '1'
       #result['hour']=[str(self.bikes[4])]
       
       seasons_columns = {'Autumn' : 47, 'Spring' : 48 , 'Summer' : 49 , 'Winter' : 50 } 
       seasons = {'onehot__x5_Autumn' : '0', 'onehot__x5_Spring' : '0' , 
                  'onehot__x5_Summer' : '0' , 'onehot__x5_Winter' : '0' }
       season_index = self.bikes[5]
       seasons[season_index] = '1'
       #result['seasons']=[str(self.bikes[5])]

       #result['temperature(°c)'] =[float(self.bikes[6])]
       #result['dew_point_temperature(°c)'] = [float(self.bikes[7])]
       #result['humidity(%)'] = [float(self.bikes[8])]
       

       rainfall_category_columns = {'1_no rain' : 51 , '2_drizzle' : 52 , 
                            '3_light rain' : 53 , '4_moderate rain' : 54 , 
                            '5_heavy rain' : 55}
       
       rainfall_category = {'onehot__x6_1_no rain' : '0' , 'onehot__x6_2_drizzle' : '0' , 
                            'onehot__x6_3_light rain' : '0' , 'onehot__x6_4_moderate rain' : '0' , 
                            'onehot__x6_5_heavy rain' : '0'}
       

       rainfall_category_index = self.bikes[9]
       rainfall_category[rainfall_category_index] = 1
       #result['rainfall_category'] = [str(self.bikes[9])]
       
       snow_category_columns = {'1_no snow' : 56 , '2_light snow' : 57 ,'3_moderate snow' : 58}
       snow_category = {'onehot__x7_1_no snow' : '0' , 'onehot__x7_2_light snow' : '0' ,
                        'onehot__x7_3_moderate snow' : '0'}

       snow_category_index =  self.bikes[10]
       snow_category[snow_category_index] = 1
       #result['snow_category']=[str(self.bikes[10])]
       
       wind_category_columns = {'1_calm' : 59 , '2_plowing' : 60 , '3_light breeze' : 61, '4_weak breeze' : 62}
       wind_category = {'onehot__x8_1_calm' : '0' , 'onehot__x8_2_plowing' : '0' , 
                        'onehot__x8_3_light breeze' : '0', 'onehot__x8_4_weak breeze' : '0'}
       wind_category_index = self.bikes[11]
       wind_category[wind_category_index] = 1
       #result['wind_category'] = [str(self.bikes[11])]

       solar_radiation_category_columns = {'1_weak' : 63 , '2_moderate' : 64 , '3_strong' : 65}
       solar_radiation_category = {'onehot__x9_1_weak' : '0' , 'onehot__x9_2_moderate' : '0' , 
                                   'onehot__x9_3_strong' : '0'}
       solar_radiation_category_index = self.bikes[12]
       solar_radiation_category[solar_radiation_category_index] = 1
       #result['solar_radiation_category'] = [str(self.bikes[12])]
      
       visibility_category_columns = {'1_very bad' : 66 , '2_bad' : 67 , '3_moderate' : 68}
       visibility_category = {'onehot__x10_1_very bad' : '0', 'onehot__x10_2_bad' : '0' , 'onehot__x10_3_moderate' : '0'}

       visibility_category_index =  self.bikes[13]
       visibility_category[visibility_category_index] = 1
       #result['visibility_category'] = [str(self.bikes[13])]


       temperature = {}
       temperature['temperature(°c)'] =[float(self.bikes[6])]

       dew_point = {}
       dew_point['dew_point_temperature(°c)'] = [float(self.bikes[7])]

       humidity = {}
       humidity['humidity(%)'] = [float(self.bikes[8])]
       
       
       #result[69] = float(self.bikes[11]) 
       #result[70] = float(self.bikes[12]) 
       #result[71] = float(self.bikes[13]) 

       colunas=[month,day_of_week,functioning_day,holiday,
                 hour, seasons, rainfall_category, snow_category,
                 wind_category, solar_radiation_category, visibility_category,
                 temperature, dew_point, humidity]
       
       for col in colunas:
           result.update(col)
       

       return result

   def predict(self, result):
        bikes_to_predict = (result)
        quantity_bikes_to_predict = pd.DataFrame(data = bikes_to_predict)
        #categorical_features=['month','day_of_week', 'functioning_day', 'holiday', 'hour', 'seasons', 
        #                      'rainfall_category', 'snow_category','wind_category', 'solar_radiation_category', 'visibility_category']

        categorical_features = ['onehot__x0_1', 
                                'onehot__x0_2',
                                'onehot__x0_3',
                                'onehot__x0_4',
                                'onehot__x0_5',
                                'onehot__x0_6',                                 
                                'onehot__x0_7',
                                'onehot__x0_8',
                                'onehot__x0_9',
                                'onehot__x0_10',
                                'onehot__x0_11',
                                'onehot__x0_12',
                                'onehot__x1_0', 
                                'onehot__x1_1', 
                                'onehot__x1_2', 
                                'onehot__x1_3', 
                                'onehot__x1_4', 
                                'onehot__x1_5', 
                                'onehot__x1_6', 
                                'onehot__x2_0', 
                                'onehot__x2_1', 
                                'onehot__x3_0', 
                                'onehot__x3_1', 
                                'onehot__x4_0',
                                'onehot__x4_1', 
                                'onehot__x4_2', 
                                'onehot__x4_3', 
                                'onehot__x4_4', 
                                'onehot__x4_5', 
                                'onehot__x4_6',
                                'onehot__x4_7', 
                                'onehot__x4_8', 
                                'onehot__x4_9', 
                                'onehot__x4_10', 
                                'onehot__x4_11', 
                                'onehot__x4_12',
                                'onehot__x4_13', 
                                'onehot__x4_14', 
                                'onehot__x4_15', 
                                'onehot__x4_16', 
                                'onehot__x4_17', 
                                'onehot__x4_18',
                                'onehot__x4_19', 
                                'onehot__x4_20', 
                                'onehot__x4_21', 
                                'onehot__x4_22', 
                                'onehot__x4_23', 
                                'onehot__x5_Autumn',
                                'onehot__x5_Spring', 
                                'onehot__x5_Summer', 
                                'onehot__x5_Winter', 
                                'onehot__x6_1_no rain', 
                                'onehot__x6_2_drizzle',
                                'onehot__x6_3_light rain', 
                                'onehot__x6_4_moderate rain', 
                                'onehot__x6_5_heavy rain', 
                                'onehot__x7_1_no snow',
                                'onehot__x7_2_light snow',
                                'onehot__x7_3_moderate snow',
                                'onehot__x8_1_calm', 
                                'onehot__x8_2_plowing', 
                                'onehot__x8_3_light breeze',
                                'onehot__x8_4_weak breeze',
                                'onehot__x9_1_weak',
                                'onehot__x9_2_moderate',
                                'onehot__x9_3_strong',
                                'onehot__x10_1_very bad',
                                'onehot__x10_2_bad',
                                'onehot__x10_3_moderate',
 ]
 

        quantity_bikes_to_predict[categorical_features] = quantity_bikes_to_predict[categorical_features].astype('category')
       
               
        #encoder = CategoricalVaribleEncoder(categorical_features)
        #quantity_bikes_to_predict_encoded = encoder.fit_transform(quantity_bikes_to_predict)

        model = joblib.load('modelo/model.pkl')
        predicted_bikes_quantities = model.predict(quantity_bikes_to_predict)
        predicted_bikes_quantities = np.ceil(predicted_bikes_quantities).astype(int)
        
        if predicted_bikes_quantities[0] <= 0:
            predicted_bikes_quantities = np.clip(predicted_bikes_quantities, a_min=0, a_max=None)
            value = predicted_bikes_quantities[0]
        else:
            value = predicted_bikes_quantities[0]
                       
        
        return value
       



