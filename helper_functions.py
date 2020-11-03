import csv
import sys
import Tkinter as tk
from Tkinter import *
import tkMessageBox
import sys
import os
import boto3

#The below parameters should generally be stored in a config file along with other configurations

working_dir='/home/ec2-user/test/'
local_employee_file = './employee.txt'
role_file='./role_file.txt'

#The GetUsers() function is used to read the employee file from S3 into a dictionary.

def GetUsers():

    s3=boto3.resource(u's3')
    bucket=s3.Bucket(u'myfirstbucketms')
    obj = bucket.Object(key=u'employee.txt')
    response = obj.get()
    lines = response['Body'].read().decode('utf-8').split()
    #lines = response[u'Body'].read().split()
    employee_data = []
    employee_col_id = {}
    employee_dtl = {}
    for rec in csv.DictReader(lines):
        employee_data.append(rec)


    return employee_data

#This function is used by add user UI to populate the rolenames
def GetRoles():

    role_file = csv.DictReader(open(role_file,'r'),delimiter=delim)
    role_data = []
    role_dtl = {}
    for rec in role_file:
        role_data.append(rec)
    print(role_data)
    return role_data

# This function is used to get the existing maxId from the employee file, which is evetually required to populate the new Id is the add_user screen
def getMaxId():
    id_val=0
    employee_data = GetUsers()
    for employee_col_id in employee_data:
        for j,k in employee_col_id.items():
             if j == "Id" and id_val < int(k):
                id_val = int(k)
    return id_val

# This function is used to get the subordinate details in the search user screen
def getSubOrdinates(user_name):
    employee_date = []
    employee_dtl = []
    employee_col_id = {}
    employee_data = GetUsers()
    for employee_col_id in employee_data:
        for j,k in employee_col_id.items():
             if j == "Name" and user_name.replace(" ","") == k.replace(" ",""):
                 employee_dtl = employee_col_id
                 break;


#    print(employee_dtl["Role"])

    result_set=[]

    if employee_dtl:
        for x in range(0,len(employee_data)):
             if(int(employee_data[x]["Role"]) > int(employee_dtl["Role"])):
                result_set.append(employee_data[x])

    print(result_set)

    return result_set

#This function writes the data provided by add user screen into the employee file

def writeUserToFile(FirstName,LastName, roleName,roleData_lst):
    #The max id is pulled from the employee file and incremented by 1 for the new joinee
    maxId = getMaxId()
    maxId = maxId +1
    space_char = " "
    #The rolename is passed to the function as that is what is visible to the UI user, From the roleName, roleId is derived using the role file
    try:
     for x in range(0,len(roleData_lst)):
        if roleData_lst[x]["Name"] == roleName:
            roleId = roleData_lst[x]["id"]
            break
        else:
            roleId=''
     #The return codes decide the message that is displayed to the UI user
     if FirstName in( None,'') or LastName  in(None,'') or str(roleId) in (None,''):
      return 1

      #The record is added to the employee file
     else:
        FullName = str(FirstName) + str(space_char) + str(LastName)
        rec=','.join([str(maxId),FullName,str(roleId)])
        rec_newline = "\n"                                   #Writing newline to the record
        employee_file = open('/home/ec2-user/test/employee.txt','a')
        employee_file.write(rec)
        employee_file.write(rec_newline)
        employee_file.close()
     return 0

    except:
        print('An error occured. Please check')

#if __name__ == "__main__": getSubOrdinates('Emily Employee')
        #if __name__ == "__main__": writeUserToFile('Simon', 'Jones','Employee', list([{'objRole': 'ObjRole1', 'id': '4', 'Name': 'Employee', 'Parent': '3'}]))
                                                                                                                                                      116,1-8       Bot
