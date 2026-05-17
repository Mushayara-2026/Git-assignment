# Mini Calculator Project

## Overview
This is a simple Python project created as part of a Git assignment.  
The project demonstrates basic Git workflow — initialization, commits, and pushing code to a remote repository — while also including a small interactive calculator program.

## Features
- Addition
- Subtraction
- Multiplication
- Division (with error handling for division by zero)

## How to Run
Clone the repository:
   ``bash
git clone https://github.com/Mushayara-2026/Git-assignment.git

**Question 1: Setting up Repository**

Created a folder **Git-assignment** in VS Code.

<img width="223" height="55" alt="image" src="https://github.com/user-attachments/assets/60d054f1-d935-4262-82af-5d0d2a1c05d6" />

Initialized Git using **git init**, Added a Python file **app.py** with sample calculator code and Checked status with **git status**.

<img width="470" height="187" alt="image" src="https://github.com/user-attachments/assets/87e31201-093e-40a4-b47e-34ba471093f7" />

<img width="471" height="294" alt="image" src="https://github.com/user-attachments/assets/d3c964bf-8f91-4e51-bcec-71ef54fcb195" />


Staged file using **git add app.py** and committed with message **"Initial commit: add app.py"**.

<img width="395" height="120" alt="image" src="https://github.com/user-attachments/assets/b0309302-4eec-43d2-81bc-3d5c5358f356" />

Created a remote repository on GitHub, linked remote using **git remote add origin** and Verified remote with **git remote -v**.

<img width="475" height="345" alt="image" src="https://github.com/user-attachments/assets/7486c239-60b4-4fdd-8ae3-262fe40b02e3" />

Pushed code using **git push origin master**

<img width="459" height="191" alt="image" src="https://github.com/user-attachments/assets/6217475d-ee6a-4860-9837-7c33bc81b378" />

After pushing in repository 

<img width="470" height="218" alt="image" src="https://github.com/user-attachments/assets/65e239e5-3adf-40cb-b3c5-c54d56035b15" />


**Question 2: Working with Changes & History**

Modified app.py by adding a new function square(a)

<img width="431" height="343" alt="image" src="https://github.com/user-attachments/assets/5ddf7ae5-9580-456f-a52d-8fcb490a8620" />

Checked changes with **git status**.

<img width="410" height="146" alt="image" src="https://github.com/user-attachments/assets/abf56b9a-3074-4551-b29e-ad60a58b716d" />

Viewed differences using **git diff app.py.** (green colour text shows the chages)

<img width="431" height="350" alt="image" src="https://github.com/user-attachments/assets/d47ad49b-0f43-4261-9689-20655fec4e22" />

Staged specific changes interactively using **git add app.py** and committed with message **"Add square function to calculator"**.

<img width="380" height="125" alt="image" src="https://github.com/user-attachments/assets/20a46640-c410-469f-8e3a-7e299f55cc4a" />

Modified app.py again to add power(a, b) function.

<img width="334" height="287" alt="image" src="https://github.com/user-attachments/assets/50c8d254-d042-45d3-b678-fb158917fb23" />

Checked for for difference. Staged all changes using **git add app.py** and committed with message **"Add power function to calculator".**

<img width="290" height="323" alt="image" src="https://github.com/user-attachments/assets/d96d8293-001c-4304-8477-bd9a0ddd7da2" />

Viewed commit history using **git log** and viewed compact commit history using **git log --oneline**.

<img width="324" height="303" alt="image" src="https://github.com/user-attachments/assets/65f8464b-f849-4d2e-b9f3-a182d794d2cc" />

**Question 3: Branching & Feature Development**

Created a new branch feature-update using **git branch feature-update** and Switched to the branch using **git checkout feature-update**.

<img width="319" height="80" alt="image" src="https://github.com/user-attachments/assets/9b7c9a17-da57-48a5-b0a7-9ef9e097ac0b" />

Modified app.py by adding a new function modulus(a, b) and integrated it with elif choice == "modulus".

<img width="353" height="350" alt="image" src="https://github.com/user-attachments/assets/d1a49574-907d-4d0b-854d-ba80000513f5" />

Staged and committed changes with message **"Add modulus function to calculator"**.

<img width="319" height="31" alt="image" src="https://github.com/user-attachments/assets/0a6b96da-2d34-43a8-a2a8-7263c3d0eb50" />

<img width="310" height="44" alt="image" src="https://github.com/user-attachments/assets/5be31fe8-12f8-492e-81c3-b2d3904d8fa5" />

Switched back to master branch using **git checkout master**, merged the feature branch into master using **git merge feature-update**, 
verified changes were merged using **git log --oneline** and Deleted the branch safely using **git branch -d feature-update**.

<img width="360" height="217" alt="image" src="https://github.com/user-attachments/assets/803e089c-ec9c-4e33-b7d7-ea8236436185" />

Created a dummy branch temp-branch and force deleted it using **git branch -D temp-branch**.

<img width="299" height="80" alt="image" src="https://github.com/user-attachments/assets/8e857bbc-1e61-40fb-871c-0e4fbd941987" />

**Question 4: Handling Errors (Stash, Reset, Revert)**

Made changes to app.py but did not commit, Stashed the changes (including untracked files) using **git stash -u**, Checked the stash list with git stash list, 
applied the stashed changes back using **git stash apply** and committed the applied changes with a clear message.

<img width="383" height="265" alt="image" src="https://github.com/user-attachments/assets/4c6a207e-a5f9-4aea-951d-099f52723cd7" />

Made another commit with incorrect code, undid the last commit using **git reset --hard HEAD~1**.

<img width="394" height="215" alt="image" src="https://github.com/user-attachments/assets/d514a17e-fe90-4977-ae77-2e43d5beae9f" />

Made another commit with corrected code.

<img width="383" height="152" alt="image" src="https://github.com/user-attachments/assets/bfab4e52-0cd8-4254-9e26-62d31da1adf8" />

Undid a commit using **git revert <commit_id>** (saved and exited the editor) and verified the commit history using **git log --oneline.**

<img width="377" height="199" alt="image" src="https://github.com/user-attachments/assets/523a12e0-2b34-4663-806b-0bd2bc1c49c6" />

Finally pushed the final code to master branch repository

<img width="350" height="138" alt="image" src="https://github.com/user-attachments/assets/e9bdbcf6-9751-46d4-a26f-9080f368618e" />
