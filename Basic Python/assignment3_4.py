quiz=int(input("Enter quiz marks: "))
if quiz<=20:
    quizw = (quiz / 20) * 15
elif quiz>20:
    print("Invalid marks {0}>20".format(quiz))
elif quiz<=0:
    print("Invalid marks {0}<0".format(quiz))

exam=int(input("Enter exam marks: "))
if exam<=100:
   examw=(exam/100)*40
elif exam>100:
    print("Invalid marks {0}>100".format(exam))
elif exam<=0:
    print("Invalid marks {0}<0".format(exam))

assignment=int(input("Enter assignment marks: "))
if assignment<=100:
   assignmentw=(assignment/100)*20
elif assignment>100:
    print("Invalid marks {0}>100".format(assignment))
elif assignment<=0:
    print("Invalid marks {0}<0".format(assignment))

project=int(input("Enter project marks: "))
if project<=50:
   projectw=(project/50)*25
elif project>50:
    print("Invalid marks {0}>50".format(project))
elif project<=0:
    print("Invalid marks {0}<0".format(project))

gpa=(quizw+examw+assignmentw+projectw)/10
r=round(gpa,2)
print(r)