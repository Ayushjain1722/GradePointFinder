# GradePointFinder
A webapp that assigns grade points to a list of students according to their marks in a subject and sends the result file to user specified E-mail ID.

## Novelty
1.
2.

## Technologies Used
1. Flask (Backend) 

![image](https://user-images.githubusercontent.com/42894689/133317407-dc868f47-fbcb-4799-be73-b25313e65b0d.png)

2. HTML (Frontend)

![image](https://user-images.githubusercontent.com/42894689/133317464-d798e31b-8622-46be-909c-a264e34b7d31.png)

3. CSS (Frontend)

![image](https://user-images.githubusercontent.com/42894689/133317498-05875c94-9f66-47c4-b2d3-bc5a09d1361b.png)

4. Heroku (Hosting website)

![image](https://user-images.githubusercontent.com/42894689/133317602-42753fcb-f12e-45b5-8983-715964902754.png)

## Steps Involved:
1. User uploads the .csv or .txt files to the website.
2. The files are pre-processed(removed duplicates and invalid entries) and merged together to form the list of the complete institution.
3. The gpFinder.py script is run which calculates the grade and the grade point assigned to each student.
4. Final result.csv is made and user is asked to enter his/her email-id, providing which he/she will receive the file.

## UI Screenshots

## GIF showing process for one example:

## Input example:

## Output example:


## Challenges

## Future Scope

## Requirements

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

![image](https://user-images.githubusercontent.com/42894689/133393181-d7a2935f-1cd3-4995-b539-cd8e42279804.png)
