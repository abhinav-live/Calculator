Equation = input("Equation [ODMAS]: ").replace(" ", "").lower()

#Funtions

def multiply(String1,String2):
    return (int(String1) * int(String2))
def divide(String1,String2):
    return (int(String1) / int(String2))
def add(String1,String2):
    return (int(String1) + int(String2))
def subtract(String1,String2):
    return (int(String1) - int(String2))

def isPresent(Str,List):
    if Str in List:
        return True
    
def Calculate(symbol,function):
    while isPresent(symbol,Symbols):
        for i in range(0,len(Symbols)):
            if Symbols[i] == symbol:
                n = function(numbers[i],numbers[i+1])
                numbers[i] = n
                numbers.pop(i+1)
                break
        for i in range(0,len(Symbols)):
            if Symbols[i] == symbol:
                Symbols.pop(i)    
                break 


#Finding Symbols
Symbols = list()
for i in range(0,len(Equation)):
    if (Equation[i] == "+" or Equation[i] == "-" or Equation[i] == "*" or Equation[i] == "/"):
        Symbols.append(Equation[i])
        
    elif (Equation[i] == "o" and (Equation[i+1] == "f")):
        Symbols.append("*")
        
#Finding Numbers
digits= ["0","1","2","3","4",'5','6','7','8',"9"]
numbers = list()
number = list()
for i in range(0,len(Equation)+1):
    if i == len(Equation):
        number_string = ''.join(number)
        numbers.append(number_string)
        number = list()

    elif Equation[i] in digits:
        number.append(Equation[i])

    else:
        number_string = ''.join(number)
        if number_string != '':
            numbers.append(number_string)
        number = list()


#Calcultaions:-

Calculate("*",multiply)
Calculate("/",divide)
Calculate("+",add)
Calculate("-",subtract)


print(numbers[0])

#noice