#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    year = data[5]
    major = data[6]
    #print(data)
    abrMajor = convertMajor(major)
    abrYear = convertYear(year)
    #print(abrYear)
    student_id = makeID(first, last, idNum)
    output = last + "," + first + "," + student_id + "," + abrYear + "-" + abrMajor  + "\n"
    outFile.write(output)
    #print(student_id)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  #print(first, last, idNum)
  idLen = len(idNum)

  while len(last) < 5:
    last = last + "X"

  id = first[0] + last + idNum[idLen - 3: ]

  #print(id)
  return id 

def convertYear(year):
  if year == "Freshman":
    return "FR"
  elif year == "Sophomore":
    return "SO"
  elif year == "Junior":
    return "JR"
  elif year == "Senior":
    return "SR"
  else:
    return "UN"  # Unknown
  
def convertMajor(major):
  firstThree = major[:3]
  return firstThree

  




  

if __name__ == '__main__':
  main()
