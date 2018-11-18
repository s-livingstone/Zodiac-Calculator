# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 13:35:34 2018

@author: Shannon
"""
#program to determine zodiac sign based on birthday inputed by user
#    
print("Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec")


month = input("Please write the first three letters of the chosen birth month exactly as shown")
if month == ("Jan"):
    print ("You might be a Capricorn or Aquarius")
    day= int(input("Please write the birth day"))
    if day>=1 and day<=19 :
        print("You are a Capricorn")
    elif day>=20 and day<=31:
        print("You are an Aquarius")
    else:
        print("You may have wrote invalid integers.Try program again.")
        

if month == ("Feb"):
    print ("You might be an Aquarius or Pisces")
    day= int(input("Please write the birth day"))
    if day>=1 and day<=18 :
        print("You are an Aquarius")
    elif day>=19 and day<=28:
        print("You are a Pisces")
    else:
        print("You may have wrote invalid integers, if so try program again. \nIf you were born on the 29th of Feb, I am sorry.")
        
        
if month == ("Mar"):
    print ("You might be a Pisces or Aries")
    day= int(input("Please write the birth day"))
    if day>=1 and day<=20 :
        print("You are a Pisces")
    elif day>=21 and day<=31:
        print("You are an Aries")
    else:
        print("You may have wrote invalid integers.Try program again.")


if month == ("Apr"):
    print ("You might be an Aries or Taurus")
    day= int(input("Please write the birth day"))
    if day>=1 and day<=19 :
        print("You are an Aries")
    elif day>=20 and day<=30:
        print("You are a Taurus :) (like me!)")
    else:
        print("You may have wrote invalid integers.Try program again.")
        
        
        
if month == ("May"):
    print ("You might be a Taurus or Gemini")
    day= int(input("Please write the birth day"))
    if day>=1 and day<=20 :
        print("You are a Taurus :) (like me!)")
    elif day>=21 and day<=31:
        print("You are a Gemini")
    else:
        print("You may have wrote invalid integers.Try program again.")
        
        
        
if month == ("Jun"):
    print ("You might be a Gemini or Cancer")
    day= int(input("Please write the birth day"))
    if day>=1 and day<=20 :
        print("You are a Gemini")
    elif day>=21 and day<=30:
        print("You are a Cancer")
    else:
        print("You may have wrote invalid integers.Try program again.")
        
        
        
if month == ("Jul"):
    print ("You might be a Cancer or Leo")
    day= int(input("Please write the birth day"))
    if day>=1 and day<=22 :
        print("You are a Cancer")
    elif day>=23 and day<=31:
        print("You are a Leo")
    else:
        print("You may have wrote invalid integers.Try program again.")
 
if month == ("Aug"):
    print ("You might be a Leo or Virgo")
    day= int(input("Please write the birth day"))
    if day>=1 and day<=22 :
        print("You are a Leo")
    elif day>=23 and day<=31:
        print("You are a Virgo")
    else:
        print("You may have wrote invalid integers.Try program again.")
        
if month == ("Sep"):
    print ("You might be a Virgo or Libra")
    day= int(input("Please write the birth day"))
    if day>=1 and day<=22 :
        print("You are a Virgo")
    elif day>=23 and day<=30:
        print("You are a Libra")
    else:
        print("You may have wrote invalid integers.Try program again.")
        
        
if month == ("Oct"):
    print ("You might be a Libra or Scorpio")
    day= int(input("Please write the birth day"))
    if day>=1 and day<=23 :
        print("You are a Libra")
    elif day>=20 and day<=31:
        print("You are a Scorpio")
    else:
        print("You may have wrote invalid integers.Try program again.")

if month == ("Nov"):
    print ("You might be a Scorpio or Sagittarius")
    day= int(input("Please write the birth day"))
    if day>=1 and day<=21 :
        print("You are a Capricorn")
    elif day>=22 and day<=30:
        print("You are a Sagittarius")
    else:
        print("You may have wrote invalid integers.Try program again.")
        
if month == ("Dec"):
    print ("You might be a Sagittarius or Capricorn")
    day= int(input("Please write the birth day"))
    if day>=1 and day<=21 :
        print("You are a Capricorn")
    elif day>=22 and day<=31:
        print("You are an Aquarius")
    else:
        print("You may have wrote invalid integers.Try program again.")

    
    
   
