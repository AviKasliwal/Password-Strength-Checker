#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Mon Jan 27 12:23:48 2020
    
    @author: Avi Kasliwal
    ML Project -> Check Password Strength
    This is a py script to fetch data for strong passwords.
"""

import requests

MIN_LENGTH = 8
MAX_LENGTH = 14

count = 1

for length in range(MIN_LENGTH, MAX_LENGTH + 1):
    fout = open("./Data/tsvFiles/strong.tsv", "a+")
    for i in range(140):
        url = f"https://passwordwolf.com/api/?length={length}&exclude=%3F!%3C%3Eli1I0OB8%60&repeat=128"
        print(count, url)
        count += 1
        passwords = requests.get(url).json()
        
        for p in passwords:
            password = p['password']
            password = password + '\t2\n'
            fout.write(password)
    fout.close()
