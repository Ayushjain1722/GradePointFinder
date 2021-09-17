import pandas as pd
import sys
import time
import os

def preprocessing(path, files, index):
  #Reading the csv file
  dataset = pd.read_csv(path + files[index])
  #Renaming the columns
  dataset = dataset.rename(columns={dataset.columns[1]:"RollNo", dataset.columns[2]:"Marks"})
  #Removing NA Values
  dataset = dataset.fillna(0)
  #Removing invalid input
  for i in range(dataset.shape[0]):
    try:
      marks = int(dataset.iloc[i,2])
    except:
      dataset.iloc[i,2] = 0
  dataset.drop(dataset.columns[0],axis=1,inplace=True)
  return dataset

def mergeMain():
  files = os.listdir('./uploads')
  path = './uploads/'

  #Initializing the dataset with one value
  mainDataset = preprocessing(path, files, 0)

  for i in range(1, len(files)):
    #Get the preprocessed dataset by calling the function
    df = preprocessing(path, files, i)
    mainDataset = pd.concat([mainDataset, df], ignore_index=True)

  #Removing duplicate values
  mainDataset = mainDataset.drop_duplicates(subset="RollNo", keep="last")

  for file in files:
    os.remove(path+file)

  mainDataset.to_csv('./output/preprocessed.csv')