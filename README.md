# Password Strength Checker
Intro text.

## 1. Data Collection and Data Preprocessing.
- Data Collection
    - Krish Naik's repository. [LINK]
    - Common passwords. [LINK]
        - common_passwords.py -> script to read common passwords file line by line and create a new file (.tsv) which has the password and its strength (0 in this case.)
    - Strong Passwords. [LINK]

- Data Preprocessing.
    - Jumble the passwords in strong.tsv
    - remove duplicates from the new files created.
    - extract common passwords from original data and add the new common passwords.
	- Sample up, sample down.
	- tf-idf vectorization of passwrods.

## 2. Building different tree classifiers.
	- Decission Tree.
