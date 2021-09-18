# GradePointFinder

A webapp that assigns grade points to a list of students according to the marks of overall batch in a subject and sends the result file to user specified E-mail ID.

## Live Link

https://gp-finder.herokuapp.com/

## Novelty

1. Designed the complete frontend and backend.
2. Creted dummy dataset for testing purpose.
3. Merging multiple files into a single csv file, removing duplicate entries and invalid entries.
4. Sending email to multiple accounts with the result file attached. 
5. Able to attach multiple files at once.
6. Only certain extensions allowed so that no invalid file has to be processed.
7. Live project that can be accessed from anywhere. 
8. Implementation novelty: a) Different files for each feature (modular approach). 
                           b) Making standard template for HTML files to remove redundancy in code.

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
4. Final result.csv is made and user is asked to enter his/her email-id(s), providing which he/she will receive the file.

## UI Screenshots

![image](https://user-images.githubusercontent.com/42894689/133873132-5037c83b-fcf3-41e4-970e-f2ac81b04e24.png)

![image](https://user-images.githubusercontent.com/42894689/133873136-d988d0f7-896e-43d0-af20-24016befea85.png)

![image](https://user-images.githubusercontent.com/42894689/133873151-a0b05fa9-90d8-4152-87b4-bb51e7268756.png)

![image](https://user-images.githubusercontent.com/42894689/133873369-36dee141-44eb-40fb-a78f-64e84d2a8e39.png)


## GIF showing process for one example:

## Input example:

![image](https://user-images.githubusercontent.com/42894689/133873866-991ccd4e-15b2-4def-a470-a0bc1c6b5823.png)

![image](https://user-images.githubusercontent.com/42894689/133873892-91684f35-768f-43d8-8708-dbd9d6a57489.png)![image](https://user-images.githubusercontent.com/42894689/133873951-7cc75ca7-7e55-4848-95a9-47e0ed80bdbd.png)


## Output example:

![image](https://user-images.githubusercontent.com/42894689/133873803-c3861250-856d-426a-a65a-2880475e1b5d.png)

![image](https://user-images.githubusercontent.com/42894689/133873777-5e40c0d4-5f46-4bce-a255-ae5f05b129c0.png)


## Challenges

1. Google Authentication for third party apps: Allow access in security settings of your account.
2. File upload error for invalid files: Only allow certain extensions to be uploaded.
3. HTML template was not getting extended to other pages correctly: Use "{% block .. %}" and "{% endblock %}" to rectify.

## Future Scope

1. Account authentication for different users who use this website.

## Requirements

1. Working Internet connection (around 2 Mbps)
2. Mail account where you will receive the result.


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
