# GradePointFinder
A webapp that assigns grade points to a list of students according to their marks in a subject and sends the result file to user specified E-mail ID.

## Creating dummy dataset to test the code
```
#Creating a csv
rollNumbers = []
marks = []
for i in range(0,357):
  if len(str(i)) == 1:
    rollNumbers.append('10180368' + str(i))
  elif len(str(i)) == 2:
    rollNumbers.append('1018037' + str(i))
  else:
    rollNumbers.append('101803' + str(i))
  marks.append(random.randrange(30, 100))

data = {}
data['roll'] = rollNumbers
data['marks'] = marks

finalDataset = pd.DataFrame.from_dict(data)
finalDataset.to_csv('scores.csv')
```