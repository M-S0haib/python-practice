print("MARK SHEET")

print("ENTER YOUR NAME")
name=input()

print("ENTER YOUR CLASS")
className=input()

print("ENTER YOUR SECTION")
sec=input()

print("ENTER YOUR ROLL NO:")
rollNo=input()

print("ENTER YOUR MARKS IN MATHS")
mathMarks=input()

print("ENTER YOUR MARKS IN ENGLISH")
englishMarks=input()

print("ENTER YOUR MARKS IN URDU")
urduMarks=input()

print("ENTER YOUR MARKS IN  PHYSICS")
phyMarks=input()

print("ENTER YOUR MARKS IN CHEMISTRY")
chemMarks=input()

obtainedMarks= int(mathMarks) + int(englishMarks) + int(urduMarks) + int(phyMarks) + int(chemMarks)

totalMarks= 500

percentage= (obtainedMarks / totalMarks) * 100

print(percentage)

if(percentage>=40):
  print("PASS")

else:
    print("FAIL")



