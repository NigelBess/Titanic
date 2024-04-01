
import os
import pandas as pd

dataFolder = os.path.join(os.getcwd(),"Data")
trainFilePath = os.path.join(dataFolder,'train.csv')
trainData = pd.read_csv(trainFilePath)
trainData.head()