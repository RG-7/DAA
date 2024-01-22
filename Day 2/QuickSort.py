# Day 2
# January 22, 2024
# Design & Analysis of Algorithm

# Array = list(input("Enter a list of Element"))
Array = [12,13,11,4,3,19,17,2,1,21]
starting_index = 0
ending_index = len(Array)-1
# print(f'{Array}\n{starting_index}\n{ending_index}')

def swap(Array,index1,index2):
  temp = Array[index1]
  Array[index1] = Array[index2]
  Array[index2] = temp

def Partition(Array,p_index,e_index):
  index = p_index
  pviot_value = Array[index]

  for j in range(index+1,e_index+1):
    if Array[j] < pviot_value:
      index += 1
      swap(Array,j,index)
  swap(Array,index,p_index)
  return index


def QuickSort(Array,s_index,e_index):
    if(s_index < e_index):
      partition_index = Partition(Array,s_index,e_index)
      QuickSort(Array,s_index,partition_index-1)
      QuickSort(Array,partition_index+1,e_index)

print(f'Before: {Array}')
QuickSort(Array,starting_index,ending_index)
print(f'After : {Array}')
