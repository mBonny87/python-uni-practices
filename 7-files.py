# Write a Python program that opens two given txt files in read mode and combines each line from the first file with the corresponding line in the second file. 
# It writes each combined line to another output file.

def merge_files(f1,f2):
  first = []
  second = []
  merged = open("7-merge.txt", 'w')

  for line in open(f1, 'r'):
    first.append(line)

  for line in open(f2, 'r'):
    second.append(line)

  max_index = len(first) - 1
  for i in range(len(second) - 1):
    if(max_index > i):
      first[i] = str(first[i]).replace("\n", "") + second[i]
    else:
      first.append(second[i])

  for line in first:
    merged.write(line)
  print(first)



merge_files("7-text1.txt", "7-text2.txt")