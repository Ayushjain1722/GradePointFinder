import pandas as pd
import os

def assignGrade(dataset, index):
  # A Grade
  top10Percent = int(dataset.shape[0] / 10)
  if index <= top10Percent:
    return 'A'
  noOfStudentsFailing = len(dataset[dataset['Marks'] < 33])
  remainingStudents = dataset.shape[0] - top10Percent - noOfStudentsFailing
  if index > top10Percent and index <= top10Percent + remainingStudents/6:
    return 'A-'
  elif index > top10Percent + remainingStudents/6 and index <= top10Percent + 2*remainingStudents/6:
    return 'B'
  elif index > top10Percent + 2*remainingStudents/6 and index <= top10Percent + 3*remainingStudents/6:
    return 'B-'
  elif index > top10Percent + 3*remainingStudents/6 and index <= top10Percent + 4*remainingStudents/6:
    return 'C'
  elif index > top10Percent + 4*remainingStudents/6 and index <= top10Percent + 5*remainingStudents/6:
    return 'C-'
  elif index > top10Percent + 5*remainingStudents/6 and index < top10Percent + remainingStudents:
    return 'E'
  else:
    return 'F'

def gpMain(name):
    dataset = pd.read_csv("./output/"+name, usecols=[1,2])
    gradePoints = []
    grades = []
    dataset = dataset.sort_values(by="Marks", ascending=False)
    n = dataset.shape[0]
    for i in range(n):
        mark = dataset.iloc[i,1]
        grade = assignGrade(dataset, i)
        grades.append(grade)
        if grade == 'A':
            gradePoints.append(10)
        elif grade == 'A-':
            gradePoints.append(9)
        elif grade == 'B':
            gradePoints.append(8)
        elif grade == 'B-':
            gradePoints.append(7)
        elif grade == 'C':
            gradePoints.append(6)
        elif grade == 'C-':
            gradePoints.append(5)
        elif grade == 'E':
            gradePoints.append(4)
        else:
            gradePoints.append(0)
    dataset['grades'] = grades
    dataset['gradePoint'] = gradePoints
    os.remove('./output/preprocessed.csv')
    dataset.to_csv('./output/results.csv')