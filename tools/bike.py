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
       result = []

      # Taking each item get from the application
       result[0] = self.bikes[0] #Month TO DO months list
       result[1] = self.bikes[1] #Day of week TO DO Days of the week list
       result[2] = self.bikes[2] #Functioning Day TO DO list
       result[3] = self.bikes[3] #Holiday TO Do List
       result[4] = int16(self.bikes[4]) #Hour of the Day TO Do List
       result[5] = self.bikes[5] #Season TO Do List TO Do List
       result[6] = np.float(self.bikes[6])# Temperature °C 
       result[7] = np.float(self.bikes[7])#Dew Point Temp °C 
       result[8] = np.int(self.bikes[8]) #humidity 
       result[9] = self.bikes[9] #Rainfall TO Do List
       result[10] = self.bikes[10] #Snowfall TO Do List
       result[11] = self.bikes[11] #Wind Speed TO Do List
       result[12] = self.bikes[12] #Solar Radiation TO Do List
       result[13] = self.bikes[13] #Visibility TO Do List




