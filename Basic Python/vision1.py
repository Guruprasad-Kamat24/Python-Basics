quiz=int(input("Enter quiz marks: "))
quizw=(quiz/20)*15
exam=int(input("Enter exam marks: "))
examw=(exam/100)*40
assignment=int(input("Enter assignment marks: "))
assignmentw=(assignment/100)*20
project=int(input("Enter project marks: "))
projectw=(project/50)*25
gpa=(quizw+examw+assignmentw+projectw)/10
r=round(gpa,2)
print(r)