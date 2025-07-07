
# Flow Control: if, elif, else

'''   Basic Syntax
if condition1:
    # code A
elif condition2:
    # code B
else:
    # code C     '''


def check_age(age):
    if age < 18:
      return  "Minor"
    elif age < 60:
       return "Adult"
    else :
       return "Senior"

a = check_age(43)
print(a)
