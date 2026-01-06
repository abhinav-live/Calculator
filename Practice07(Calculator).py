Equation = input("Equation [ODMAS]: ").replace(" ", "").lower()

#Functions

def isPresent(Str,List):
    if Str in List:
        return True

#Finding Numbers
digits= ["0","1","2","3","4",'5','6','7','8',"9"]
number = list()

#Equation LIST

Equation_list = list()

for i in range(0,len(Equation)+1):
    if i == len(Equation):
        number_string = ''.join(number)
        Equation_list.append(number_string)
        number = list()
        break

    elif Equation[i] in digits:
        number.append(Equation[i])
    elif Equation[i] not in digits:
        number_string = ''.join(number)
        if number_string != '':
            Equation_list.append(number_string)
        number = list()

    if Equation[i] == "+" or Equation[i] == "-" or (Equation[i] == "*" or Equation[i] == "/") :
        Equation_list.append(Equation[i])
        
    if (Equation[i] == "o" and Equation[i+1] == "f"):
        Equation_list.append("*")

    


#Calcultaions:-



while isPresent("+",Equation_list) or isPresent("-",Equation_list):
    for i in range(0,len(Equation_list)-1):
        if Equation_list[i] == "+" or Equation_list[i] == "-":
            Equation_list[i] = Equation_list[i] + Equation_list[i+1]
            Equation_list.pop(i+1)
            break
  


while isPresent("*",Equation_list) or isPresent("/",Equation_list):
    for i in range(0,len(Equation_list)-1):
        
        
        if Equation_list[i] == "/":
            Equation_list[i] = float(Equation_list[i-1]) / float(Equation_list[i+1])
            Equation_list.pop(i+1)
            Equation_list.pop(i-1)
            break
    
        if Equation_list[i] == "*":
            Equation_list[i] = float(Equation_list[i-1]) * float(Equation_list[i+1])
            Equation_list.pop(i+1)
            Equation_list.pop(i-1)
            break


while len(Equation_list) >1:
    Equation_list[0] = float(Equation_list[0]) + float(Equation_list[1])
    Equation_list.pop(1)
    
Solution = Equation_list[0]
print(Solution)
#noice
