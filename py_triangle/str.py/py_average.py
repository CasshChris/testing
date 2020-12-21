#find the grade average of both the math & english grades
#first; prompt for the math grade
#second; prompt for the english grade
#third; calculate the averag (named EpMa) then print it

math_str = input("Enter Math grade: ")
math_float = float(math_str)
eng_str = input("Enter English grade: ")
eng_float = float(eng_str)

EpMa = (math_float + eng_float) / 2

print("The average of Math & English is ", EpMa)