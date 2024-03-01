print("MARK SHEET")

print("ENTER YOUR NAME")
name=input()

print("ENTER YOUR CLASS")
className=input()

print("ENTER YOUR SECTION")
sec=input()

print("ENTER YOUR ROLL NO:")
rollNo=int(input())

print("ENTER YOUR MARKS IN MATHS")
mathMarks=int(input())

print("ENTER YOUR MARKS IN ENGLISH")
englishMarks=int(input())

print("ENTER YOUR MARKS IN URDU")
urduMarks=int(input())

print("ENTER YOUR MARKS IN  PHYSICS")
phyMarks=int(input())

print("ENTER YOUR MARKS IN CHEMISTRY")
chemMarks=int(input())

obtainedMarks= mathMarks + englishMarks + urduMarks + phyMarks + chemMarks

totalMarks= 500

percentage= (obtainedMarks / totalMarks) * 100

print("PERCENTAGE :" , percentage)

if(percentage>=40):
  print("PASS")

else:
    print("FAIL")



