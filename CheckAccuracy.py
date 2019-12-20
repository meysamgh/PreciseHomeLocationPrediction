#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 23:44:26 2019

@author: meysam
"""

import csv
import numpy as np
import time

y=[]
user=[]
pred=[]

with open('TEST.csv', 'r') as csvfile:
        reader=csv.DictReader(csvfile)
        records=[]
        for row in reader:
            t=[]            
            records.append(int(row['Rec']))
            user.append(int(row['user_id']))
#            t=row['Pred']
#            t=t.split('[')
#            t=t[1].split(']')
#            pred.append(float(t[0]))
            if row['is_home']=='FALSE':
                    y.append(0)
            else:
                    y.append(1)
#                    print(t[0])
                    
with open('outpurregressionIt200.csv', 'r') as csvfile:                    
#with open('outpurregressionDropout60.csv', 'r') as csvfile:
        reader=csv.DictReader(csvfile)
        records=[]
        for row in reader:
            t=row['Pred']
            t=t.split('[')
            t=t[1].split(']')
            pred.append(float(t[0]))
            



   
        
true=0
false=0
user1=-1
counter=0
falses=[]
predvalues=[]
records=[]
maxval=0


for i in range (1, 1269):
    maximum=0
    correct=0
    for j in range (0,len(y)):
        if user[j]==i and pred[j]>maximum:
            maximum=pred[j]
        if y[j]==1 and user[j]==i:
            correct=pred[j]
    if maximum==correct:
        true=true+1
#    else:
#        print("WRONG DETECTION ", i, maximum, correct)
#        time.sleep(5)
        

print("TRUE: ", true)
print("ACCURACY TOTAL: ", true/(1268))
true=0

for i in range (1, 1269):
    maximum=0
    maximum2=0
    correct=0
    for j in range (0,len(y)):
        if user[j]==i and pred[j]>maximum:
            if maximum>maximum2:
                maximum2=maximum
            maximum=pred[j]
        if y[j]==1 and user[j]==i:
            correct=pred[j]
            
    if maximum==correct and (abs(maximum-maximum2)/maximum>0.1) :
        true=true+1
    if maximum!=correct and (abs(maximum-maximum2)/maximum>0.1):
        false=false+1
#    if maximum!=correct and (((maximum-correct)/maximum<0.15 and (maximum-correct)/maximum>0) or ((correct-maximum)/maximum<0.15 and (correct-maximum)/maximum>0)):
#        false=false+1
        
#    else:
#        print("WRONG DETECTION ", i, maximum, correct)
#        time.sleep(5)
        
        
print("FALSE: ", false)
print("TRUE: ", true)
print("ACCU: ", true/(true+false))  
print("PERCENTAGE: ", (true+false)/1268*100)      
        
        
c=[]
print("________________________________________________")
threshold=0.98    
with open('outpurcategorical-3.csv', 'r') as csvfile:
    reader=csv.DictReader(csvfile)
    records=[]
    for row in reader:
        t=row['PredY']
        c.append(float(t))
true=0
false=0

for i in range (1, 1269):
    maximum=0
    maximum2=0
    correct=0
    idxmax=0
    for j in range (0,len(y)):
        if user[j]==i and pred[j]>maximum:
            if maximum>maximum2:
                maximum2=maximum
            maximum=pred[j]
            idxmax=j
        if y[j]==1 and user[j]==i:
            correct=pred[j]
            
    if maximum==correct and (abs(maximum-maximum2)/maximum>0.1)  and c[idxmax]>threshold:
        true=true+1
    if maximum!=correct and (abs(maximum-maximum2)/maximum>0.1) and c[idxmax]>threshold:
        false=false+1
#    if maximum==correct and  c[idxmax]>threshold:
#        true=true+1
#    if maximum!=correct  and c[idxmax]>threshold:
#        false=false+1


print("ACCU Combined: ", true/(true+false))  
print("PERCENTAGE Combined: ", (true+false)/1268*100)  

true=0
false=0

for i in range (1, 1269):
    maximum=0
    maximum2=0
    correct=0
    idxmax=0
    for j in range (0,len(y)):
        if user[j]==i and pred[j]>maximum:
            if maximum>maximum2:
                maximum2=maximum
            maximum=pred[j]
            idxmax=j
        if y[j]==1 and user[j]==i:
            correct=pred[j]
            
#    if maximum==correct and (abs(maximum-maximum2)/maximum>0.1)  and c[idxmax]>threshold:
#        true=true+1
#    if maximum!=correct and (abs(maximum-maximum2)/maximum>0.1) and c[idxmax]>threshold:
#        false=false+1
    if maximum==correct and  c[idxmax]>threshold:
        true=true+1
    if maximum!=correct  and c[idxmax]>threshold:
        false=false+1

#    if maximum!=correct and (((maximum-correct)/maximum<0.15 and (maximum-correct)/maximum>0) or ((correct-maximum)/maximum<0.15 and (correct-maximum)/maximum>0)):
#        false=false+1
        
#    else:
#        print("WRONG DETECTION ", i, maximum, correct)
#        time.sleep(5)
        
        
#print("FALSE combined: ", false)
#print("TRUE combined: ", true)
print("ACCU Single: ", true/(true+false))  
print("PERCENTAGE Single: ", (true+false)/1268*100)           
        
        
 
#true=0
#false=0
#for i in range (1, 1269):
#    maximum=0
#    correct=0
#    for j in range (0,len(c)):
#        if user[j]==i and (c[j]+pred[j])/2>maximum:
#            maximum=(c[j]+pred[j])/2
#        if y[j]==1 and user[j]==i:
#            correct=(c[j]+pred[j])/2
#    if maximum==correct:
#        true=true+1   
#print("TRUE CLASSIFICATION: ", true)
#print("ACCU CLASSIFICATION: ", true/1268)
        
