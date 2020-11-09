# Guidelines

Github.com 
    - Account
        - Repositories
            - Code files

Case sensitive
    - abc ABC (both are different)
    
1. git clone <>
What it means?
PythonOnline repository -> source code - in your local machine

2. cd PythonOnline -> main | master (root branch)

3. git checkout -b Mohita
What it means?
a. Create new branch (-b)
    - Mohita
b. local (not in github.com)

4. git status
What it means?
View all the changed files
Complete file path including file name
e.g. 
    PythonLearning/PythonOnline/test.py
    PythonLearning/PythonOnline/validate.py
    PythonLearning/PythonOnline/checkversion.py

5. git add .
What it means?
a. Stage your changes
b. For specific file to add
    git add <path of the changed file separated with space>
    e.g.
    git add PythonLearning/PythonOnline/test.py PythonLearning/PythonOnline/validate.py

6. git commit -m "Started learning python"
What it means?
All staged changed files commited

7. git push origin Mohita
What it means?
Changes pushed to github account respository

8. git status

