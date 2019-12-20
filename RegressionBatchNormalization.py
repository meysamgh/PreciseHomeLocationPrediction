#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 23:20:29 2019

@author: meysam
"""

import csv
from keras.models import Sequential
from keras.layers import Dense,Dropout
import math
import numpy as np
import time
import random
import keras
import pandas as pd
from keras.layers.normalization import BatchNormalization
from keras import optimizers, regularizers
from keras.utils import to_categorical
batchsize=64

#with open('RandomForestOutput.csv', 'r') as csvfile:
#        reader=csv.DictReader(csvfile)
#        targetrecords=[]
#        for row in reader:                      
#            targetrecords.append(int(row['Rec']))


x=[]
x2=[]
y=[]
recall=0
y2=[]
falsedetections=[]
with open('training__set.csv', 'r') as csvfile:
        reader=csv.DictReader(csvfile)
        records=[]
        for row in reader:
            t=[]            
            records.append(int(row['Rec']))
            if 1==1:
#            if int(row['Rec']) in targetrecords:
                t.append(float(row['checkin_ratio']))
                t.append(float(row['daily_total_checkin_rate']))
                t.append(float(row['end_of_day_ratio']))
                y2.append(float(row['end_of_day_ratio']))
                t.append(float(row['end_of_inactive_day_ratio']))
                t.append(float(row['kilometer_distance_to_most_checked_in']))
                t.append(float(row['midnight_ratio']))
                t.append(float(row['num_of_total_checkins']))
                t.append(float(row['number_of_checkins_at_this_location']))
                t.append(float(row['page_rank']))
                t.append(float(row['reverse_page_rank']))
                x.append(t)
                t2=[]
                t2.append(float(row['checkin_ratio']))
                t2.append(float(row['daily_total_checkin_rate']))
                t2.append(float(row['end_of_day_ratio']))
                t2.append(float(row['end_of_inactive_day_ratio']))
                t2.append(float(row['kilometer_distance_to_most_checked_in']))
                t2.append(float(row['midnight_ratio']))
                t2.append(float(row['num_of_total_checkins']))
                t2.append(float(row['number_of_checkins_at_this_location']))
                t2.append(float(row['page_rank']))
                t2.append(float(row['reverse_page_rank']))
                #x.append(t)
                #test=t
                t2.append(int(row['user_id']))
                x2.append(t2)
                        
                if row['is_home']=='FALSE':
                    y.append(0)
                else:
                    y.append(1)
tx=[]
tx2=[]
ty=[]
ty2=[]                  
with open('test_set.csv', 'r') as csvfile:
        reader=csv.DictReader(csvfile)
        records=[]
        for row in reader:
            t=[]            
            records.append(int(row['Rec']))
            if 1==1:
#            if int(row['Rec']) in targetrecords:
                t.append(float(row['checkin_ratio']))
                t.append(float(row['daily_total_checkin_rate']))
                t.append(float(row['end_of_day_ratio']))
                ty2.append(float(row['end_of_day_ratio']))
                t.append(float(row['end_of_inactive_day_ratio']))
                t.append(float(row['kilometer_distance_to_most_checked_in']))
                t.append(float(row['midnight_ratio']))
                t.append(float(row['num_of_total_checkins']))
                t.append(float(row['number_of_checkins_at_this_location']))
                t.append(float(row['page_rank']))
                t.append(float(row['reverse_page_rank']))
                tx.append(t)
                t2=[]
                t2.append(float(row['checkin_ratio']))
                t2.append(float(row['daily_total_checkin_rate']))
                t2.append(float(row['end_of_day_ratio']))
                t2.append(float(row['end_of_inactive_day_ratio']))
                t2.append(float(row['kilometer_distance_to_most_checked_in']))
                t2.append(float(row['midnight_ratio']))
                t2.append(float(row['num_of_total_checkins']))
                t2.append(float(row['number_of_checkins_at_this_location']))
                t2.append(float(row['page_rank']))
                t2.append(float(row['reverse_page_rank']))
                #x.append(t)
                #test=t
                t2.append(int(row['user_id']))
                tx2.append(t2)
                        
                if row['is_home']=='FALSE':
                    ty.append(0)
                else:
                    ty.append(1)
#                    recall=recall+1
#print("RECALL: ", recall/1267)
# Prepare the training and test set


y3=[]



xtrainpos=[]
ytrainpos=[]
xtestcheck=[]
y3=[]
x_train1=[]
y_train1=[]
x_test1=[]
y_test1=[]
   
#    for i in range (number1,number2):
#        y3.append(y2[i])
for i in range (0,len(x)):
    x_train1.append(x[i])
    y_train1.append(y[i])
    if y[i]==1:
        xtrainpos.append(x[i])
        ytrainpos.append(y[i])
#    x_test1.append(x[i])
#    y_test1.append(y[i]) 

    #if y[i]==1:
     #   for j in range (0,40):
      #      x_train1.append(x[i])
       #     y_train1.append(y[i])   
            
#for i in range (number+1,len(y)-1):
tmpx=[]
tmpy=[]
counter=0
for i in range(0,len(x_train1)):
    tmpx.append(x_train1[i])
    tmpy.append(y_train1[i])
    if i % batchsize ==0:
#            print("TEST", i, counter,batchsize)
        #counter=0
        if i > 0:
            for j in range (counter,batchsize):
                t=random.randint(0,len(xtrainpos)-1)
#                    print("APPEND")
                tmpx.append(xtrainpos[t])
                tmpy.append(ytrainpos[t])
        counter=0
    if y_train1[i]==1:
        counter=counter+1
    
#    print(tmpy)
#    print("++++++++++++++++++++++++++++++++++++++++++++++")
                
            
 output=[]   
x_train1=tmpx
y_train1=tmpy
    
for i in range (0,len(tx)):
    x_test1.append(tx[i])
    y_test1.append(ty[i])

x_train=np.array(x_train1)
y_train=np.array(y_train1)
x_test=np.array(x_test1)
y_test=np.array(y_test1)

model = Sequential()
model.add(Dense(5, input_dim=10, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.20))
model.add(Dense(20, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.20))

model.add(Dense(10, activation='tanh'))
model.add(BatchNormalization())
model.add(Dropout(0.20))

#    model.add(Dense(20, activation='relu'))
#    model.add(BatchNormalization())
#    model.add(Dropout(0.20))

model.add(Dense(10, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.20))
#model.add(Dense(1, activation='tanh'))
#    model.add(Dense(1, activation='sigmoid'))
#    
#    sgd = optimizers.SGD(lr=0.01, decay=0.00001, momentum=0.99, nesterov=True)
#    model.compile(loss='mean_squared_error', optimizer='SGD', metrics=['accuracy'])
#    #model.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['accuracy'])


model.add(Dense(1, activation='sigmoid'))
model.add(BatchNormalization())

sgd = optimizers.SGD(lr=0.01, decay=0.00001, momentum=0.99, nesterov=True)
model.compile(loss='mean_squared_error', optimizer='rmsprop', metrics=['accuracy'])
#    model.compile(loss='mean_squared_error', optimizer='SGD', metrics=[keras.metrics.sparse_categorical_accuracy(y_train, y)])




print(model.summary())
model.fit(x_train, y_train, epochs=50, batch_size=batchsize*2, shuffle=False)

scores = model.evaluate(x_train, y_train, verbose=0)
print("Baseline Error: %.2f%%" % (100-scores[1]*100))
y2=model.predict(x_test)
for i in range (0,len(y2)):
    y3.append(y2[i])
    output.append(y2[i])
user1=-1
true=0
false=0
predvalues=[]
for i in range (0,len(y2)-1):
#        t=xtestcheck[i]
    t=x2[i+number1]
    user=t[10]
    if user==user1:
        predvalues.append(y3[i])
    else:
        user1=user
        if len(predvalues)>0:
            if y_test1[i-len(predvalues)+np.argmax(predvalues)]==1:
                true=true+1
                predvalues=[]                    
            else:
                false=false+1
                predvalues=[]
print("ACCURACY: ", true/(true+false))
#    with open("outpurregression.csv") as csv:
with open('outpurregressionIt50.csv', 'w') as csvfile:
    csvwriter=csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Rec", "Pred"])
    for k in range (0,len(x2)):
        csvwriter.writerow([x2[k],output[k]])
