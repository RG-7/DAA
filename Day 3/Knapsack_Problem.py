# Day 3
# January 29, 2024
# Design & Analysis of Algorith

#Knap_Sack Problem

objects = []
values = []
weight = []

number_of_elements = int(input("Enter the total number of element you want to enter: "))

def input_all(objects,values,weight,elements):
  print('Enter elements in form of Objects, Values & Weight for each simultaneously : ')
  for i in range(0,elements):
    objects.append(float(input(f'Enter Objects[{i}]')))
    values.append(float(input(f'Enter valuess[{i}]')))
    weight.append(float(input(f'Enter weights[{i}]')))



input_all(objects,values,weight,number_of_elements)
