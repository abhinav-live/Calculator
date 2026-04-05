def calculation(Equation_input:str):

    Equation = Equation_input.replace(" ", "").lower()

    #Functions

    def isPresent(Str,List):
        if Str in List:
            return True

    def do_add_sub(Equation_list):
        while isPresent("+",Equation_list) or isPresent("-",Equation_list):
            for i in range(0,len(Equation_list)-1):
                if Equation_list[i] == "-":
                    Equation_list[i] = Equation_list[i] + Equation_list[i+1]
                    Equation_list.pop(i+1)
                    break
                if Equation_list[i] == "+":
                    Equation_list.pop(i)
                    break
  
    def op_op(Equation_list):
        while not set(Equation_list).isdisjoint(op_op_list):
            for i in range(0,len(Equation_list)-1):
                if Equation_list[i] == "++" or Equation_list[i] == "--":
                    Equation_list[i] = "+"
                    break
            for i in range(0,len(Equation_list)-1):
                if Equation_list[i] == "+-" or Equation_list[i] == "-+":
                    Equation_list[i] = "-"
                    break
            for i in range(0,len(Equation_list)-1):
                if Equation_list[i] == "+*" or Equation_list[i] == "+/" or Equation_list[i] == "-/" or Equation_list[i] == "-*":
                    raise Exception("operator error found")
                
       
    def exp(Equation_list):
        while "^" in Equation_list:
            for i in range(len(Equation_list)-2, 0, -1):
                if Equation_list[i] == "^":
                    Equation_list[i] = power(float(Equation_list[i+1]),str(Equation_list[i-1]))
                    Equation_list.pop(i+1)
                    Equation_list.pop(i-1)
                    break    


            
    def multi_divi(Equation_list):
        while isPresent("*",Equation_list) or isPresent("/",Equation_list):
            for i in range(len(Equation_list)-1):
                if str(Equation_list[i]) in "*/" and str(Equation_list[i+1]) in "*/":
                    raise Exception("operator error found")    

            for i in range(1,len(Equation_list)-1):

                if Equation_list[i] == "/" and float(Equation_list[i+1]) == float("0"):
                    raise Exception("Zero division not possible")
        
                elif Equation_list[i] == "/":
                    Equation_list[i] = float(Equation_list[i-1]) / float(Equation_list[i+1])
                    Equation_list.pop(i+1)
                    Equation_list.pop(i-1)
                    break
    
                if Equation_list[i] == "*":
                    Equation_list[i] = float(Equation_list[i-1]) * float(Equation_list[i+1])
                    Equation_list.pop(i+1)
                    Equation_list.pop(i-1)
                    break



    def Calc(Equation_list):
        while len(Equation_list) >1 and not set(Equation_list).isdisjoint(op_list):
            
            if not set(Equation_list).isdisjoint(add_sub_list):
                do_add_sub(Equation_list)
            exp(Equation_list)
            if not set(Equation_list).isdisjoint(op_op_list):
                op_op(Equation_list)
            if not set(Equation_list).isdisjoint(multi_divi_list) and set(Equation_list).isdisjoint(op_op_list) and set(Equation_list).isdisjoint(add_sub_list):
                multi_divi(Equation_list)

        while len(Equation_list) >1:
                Equation_list[0] = float(Equation_list[0]) + float(Equation_list[1])
                Equation_list.pop(1)
    
        return Equation_list
    

    #Finding Numbers
    digits= ["0","1","2","3","4",'5','6','7','8',"9","."]
    op_list = ["++","+-","--","-+","/+","-/","+/","/-","*/","/*","*+","+*","*-","-*","+","-","/","*","^"]
    opbr_list = ["++","+-","--","-+","/+","-/","+/","/-","*/","/*","*+","+*","*-","-*","+","-","/","*","(",")","^"]
    op_op_list = ["++","+-","--","-+","/+","-/","+/","/-","*/","/*","*+","+*","*-","-*"]
    add_sub_list = ["+","-"]
    multi_divi_list =["*","/"]
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
    
        if Equation[i] in "([}{])":
            Equation_list.append(Equation[i])

        if Equation[i] == "+" or Equation[i] == "-" or (Equation[i] == "*" or Equation[i] == "/") :
            Equation_list.append(Equation[i])
        if Equation[i] == "÷":
            Equation_list.append("/")
        if Equation[i] == "×":
            Equation_list.append("*")
        if Equation[i] == "−":
            Equation_list.append("-")            
        if i < len(Equation)-1 and (Equation[i] == "o" and Equation[i+1] == "f"):
            Equation_list.append("*")
        if Equation[i] == "^":
            Equation_list.append("^")


    if Equation_list[-1] == "":
        Equation_list.pop(-1)

    #Bracket Control
    Equation_list_main = Equation_list.copy()   
    bracket_list = list()
    try_again_bracket = True
    number_of_OB = 0
    number_of_CB = 0

    def Bracketing():
        try_again_bracket = True


        while try_again_bracket == True:
            try_again_bracket = False
            number_of_OB = 0
            number_of_CB = 0
            for x in range(0,len(Equation_list_main)):
                if Equation_list_main[x] in "([{":
                    Equation_list_main[x] = "("
                    number_of_OB += 1
                elif Equation_list_main[x] in ")]}":
                    Equation_list_main[x] = ")"
                    number_of_CB += 1
                    if number_of_CB > number_of_OB:
                        Equation_list_main.insert(0, "(")
                        number_of_OB += 1
                        try_again_bracket = True
                        break



        if number_of_OB > number_of_CB:
            for _ in range(number_of_OB - number_of_CB):
                Equation_list_main.append(")")
        elif number_of_OB < number_of_CB:
            for _ in range(number_of_CB - number_of_OB):
                Equation_list_main.insert(0, "(")
   


        for x in range(0,len(Equation_list_main)):
            if Equation_list_main[x] in "()":
                bracket_list.append(Equation_list_main[x])



    Bracketing()


    #Error Catch

    if Equation_list[-1] in "*+-/" and Equation_list[-1] not in "()":
        raise Exception("Last Value Can not be an Operator")
    if Equation_list[0] in "*/":
        raise Exception("Expression cannot start with * or /")

    #Calcultaions:-



    try_again_calc = True
    number_bracket = int(len(bracket_list))
    while number_bracket > 0 and try_again_calc:

        try_again_calc = False
        Equation_list = Equation_list_main.copy()


  
        for x in range(0,len(Equation_list_main)+1):
            if Equation_list_main[x] == ")":
                for y in range(x,-1,-1):
                    if Equation_list_main[y] == "(":

                        Main_eq = list()
                        for z in range(y+1,x):
                            Main_eq.append(Equation_list_main[z])
                        Value = Calc(Main_eq)


                        if x+1 != len(Equation_list_main):
                            if Equation_list_main[x+1] not in opbr_list:
                                Equation_list_main[x] = "*"
                                Remove_x = False
                                x -= 1
                            elif Equation_list_main[x+1] in opbr_list: Remove_x = True
                        elif x+1 == len(Equation_list_main): Remove_x = True



                        if y != 0:
                            if Equation_list_main[y-1] not in opbr_list:
                                Equation_list_main[y] = "*"
                                Remove_y = False

                            elif Equation_list_main[y-1] in opbr_list: Remove_y = True
                        elif y == 0: Remove_y = True 
                                       
                    

                        if Remove_x:
                            Equation_list_main.pop(x)
                            x -= 1
               

                        if Remove_y:
                            while x-y > 0:
                                Equation_list_main.pop(y+1)
                                x -= 1
                        elif Remove_y == False:
                            while x-y > 1:
                                Equation_list_main.pop(y+1)
                                x -= 1

                                           
                    
                        if Remove_y: 
                            Equation_list_main[y] = str(Value[0])
                        elif Remove_y == False:
                            Equation_list_main[y+1] = str(Value[0])


                        number_bracket = number_bracket - 2
                        try_again_calc = True
                        break
            if try_again_calc == True:break
    
    Solution = None
    Equation_list = Equation_list_main.copy()
    
    if number_bracket == 0:
        Calc(Equation_list)
        Solution = Equation_list[0]


    Solution = float(Solution)
    if float(int(Solution)) == Solution:
        return int(Solution)
    else: return Solution 

            
def power(exponent:float,base:str):

    base = float(calculation(base))

    Solution = base**exponent
   
    if float(int(Solution)) == Solution:
        return int(Solution)
    else: return Solution 


def factorial(Value:int):
    if Value < 0:
        raise Exception("[-ve] factorial is undefined")
    Solution = 1
    for i in range(1,Value+1):
        Solution = i * Solution
    
    if float(int(Solution)) == Solution:
        return int(Solution)
    else: return Solution 
                        

def factor(Value:int):
    if Value < 0:
        Value = -Value
    if Value == 0:
        return ("Every non-Zero are factors of 0")
    
    Factors = list()
    for i in range(1,int(Value**0.5)+1):
        if Value % i == 0:
            Factors.append(i)
            if Value != Value//i:
                Factors.append(Value//i)
    for i in range(0,len(Factors)):
        Factors.append(-Factors[i])
    
    return Factors


def isPrime(Value:int):
    if Value < 1:
        raise Exception("Only Natural numbers can be Prime")
    if Value == 1:
        raise Exception("1 is not a prime number")
    for i in range(2,int(Value**0.5)+1):
        if Value % i == 0 and Value != i:
            return False
    return True
