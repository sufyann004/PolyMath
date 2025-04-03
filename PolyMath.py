import cmath
import math
import time
import pygame
import os
pygame.init()
import math

#dictionary used for differentiation section ahead
dict1=dict({'sin':'cos', 'cos':'-sin', 'tan':'sec^2', 'cot':'-cosec^2'}) #Dictionary for trig  with functions as keys and their derivative as value
diff=''
resultlst=[]


#definition of all functions used:

def morse_gen(s):
    s_new = s.upper()
    code = ""
    morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',' ': '  ', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '!': '-.-.--',
    '.': '.-.-.-', '+': '-....--', '/': '-..-.', '=': '-...-', ':': '---...', '$': '...-..-', '?': '..--..', '@': '.--.-.',
    '&': '.-...', '"': '.-..-.', '_': '..--.-', '¡': '--...-¡', '-': '-.--.', '(': '-.--.-', ')': '-.--.-', ',': '--..--'
}
    #the dictionary above stores the morse code equivalents of English Alphabets and special characters
    for i in s_new:   #this loop is where the real magic happens. Morse code equivalents are found for each character used.
        code += morse_dict[i] + " " # A final string for encoded message is generated here.
    return code

def simple_integration():
    # Prompt the user for input
    expression_str = input("Enter the expression to integrate with respect to x: ")
    # Split the input into coefficient and the rest of the expression
    coefficient, rest = expression_str.split('x', 1)

    # Determine the power of x
    if rest:
        power = rest[1:] if rest[0] == '^' else '1'
    else:
        power = '1'

    # Define the variable and the expression
    x = 'x'
    expression = f"{expression_str}"

    # Perform symbolic integration
    integrated_power = f"{coefficient}/({int(power)+1})"
    integral_result = f"Integral of ({expression}) dx is: {integrated_power} * {x}^{int(power)+1} + C"

    # Display the result
    print(integral_result)



def differentiation(n):
     coeff=0 #Coefficient that will be taken as input
     eq='' #String to build the actual equation 
     tuple=() #Used so output is not changed 
     differential='' #String that takes the derivative of each variable
     lst=[]
     eqlst=[]
     
     for i in range(n,0,-1): #Loop for taking input and building equation. It is in reverse from n to 1 (inclusive) as it takes input of the highest degree first till the last variable (x^1)
         print('Enter the coefficient of x^'+str(i)+':') #Telling the user of what input is required
         coeff=int(input()) 
         if coeff!=0: #Checking condition to remove the variable if coefficient of the variable is zero
              eq+=str(coeff)+'x^'+str(i)+'+' #Building the actual equation for later use
              differential+=str(i*coeff)+'x^'+str(i-1)+'+' #Bulding the derivative
     print('Enter the constant')
     coeff=int(input()) #Taking the value of constant for the actual equation
     eq+=str(coeff)
     
     for i in range(len(differential)-1): #Appending all the values of derivative in list
         lst.append(differential[i])
     for j in range(len(lst)-1):
         if lst[j]=='+' and lst[j+1]=="-": #Using the list form of derivative to remove the +- sign together
             del lst[j] #Deleting the + sign as +- sign is present
         else:
             pass
         
     for i in range(len(eq)): #Appending all the values of eq in list
         eqlst.append(eq[i])
     for j in range(len(eqlst)-1):
         if eqlst[j]=='+' and eqlst[j+1]=="-": #Using the list form of eq to remove the +- sign together
             del eqlst[j] #Deleting the + sign as +- sign is present
         
     differential=''
     eq=''
     for i in lst:
         differential+=i #Forming the final  equation

     for j in eqlst:
         eq+=j #Forming the final original equation
     if 'x^0' in differential:
         differential=differential[:-3]
     elif differential[-1]=='+':
         differential=differential[:-1]
     tuple=(differential,eq) #Forming a tuple 
     return tuple


def productlaw(d):
    Udash=''
    final=''
    Vdash=''
    U=''
    V=''
    lst=[]
    if d==1: #Simple polynomial scenario
        print("Enter the highest degree of the expression")
        n=int(input())
        for i in differentiation(n):
            lst.append(i) #Appending the tuple of differentition func into a list
        U=lst[1] #1 is the actual equation
        Udash=lst[0] #0 is the derivative
    elif d==2: #Trignometric Scenario
        print("Input (write/type) a function from the following:")

        for i,j in dict1.items():
            print(i) #All the keys are printed so the user knows that what type of functions can this program derivate
        selection=str(input()) #Input of the trig function
        selection=selection.lower() #lowering all the cases as found in the dictionary. This is done to remove errors if the user enters the function in block letters.
        print("Enter the angle's (variable's) highest degree")
        n=int(input()) #Input for below function call
        for i in differentiation(n): #Calling function
            resultlst.append(i)
        diff=dict1[selection] #Value of the input trig function is stored in diff function 
        U=selection+'('+resultlst[1]+')' #Actual equation
        Udash='('+resultlst[0]+')'+diff+'('+resultlst[1]+')' #Derivative
    elif d==3: #Logarithmatic (ln) scenario
        print("Enter the highest degree of the expression")
        n=int(input())
        for i in differentiation(n):
            resultlst.append(i)
        U='ln('+resultlst[1]+')'
        Udash=resultlst[0]+'/'+'('+resultlst[1]+')' #Derivative of ln function
    else:
        print("Enter a valid input")
    #Entering into the second part. Same as above bur just for the second part of the equation.
    print("For equation's second part (V)\n Enter 1 if simple polynomial\n Enter 2 if trig \n Enter 3 if logarithmatic (ln) function")
    e=int(input()) #Choice of the input. 
    if e==1: 
        print("Enter the highest degree of the expression")
        n=int(input())
        for i in differentiation(n):
            lst.append(i)
        V=lst[1]
        Vdash=lst[0]
    elif e==2:
        print("Input (write) a function from the following:")

        for i,j in dict1.items():
            print(i)
        selection=str(input())
        selection=selection.lower()
        print("Enter the angle's (variable's) highest degree")
        n=int(input())
        for i in differentiation(n):
            resultlst.append(i)
        diff=dict1[selection]
        V=selection+'('+resultlst[1]+')'
        Vdash='('+resultlst[0]+')'+'('+diff+'('+resultlst[1]+'))'
    elif e==3:
        print("Enter the highest degree of the expression")
        n=int(input())
        for i in differentiation(n):
            resultlst.append(i)
        V='ln('+resultlst[1]+')'
        Vdash=resultlst[0]+'/'+'('+resultlst[1]+')'
    else:
        print("Enter a valid input")

    final='['+str(U)+']'+'['+str(Vdash)+'] + ['+str(Udash)+']'+'['+str(V)+']' #Printing the final derivative
    print(final)


def integrate_sin(a, b, angle):
    return f"-{a} * cos({b}x/{angle}) / ({b}/{angle})"

def integrate_cos(a, b, angle):
    return f"{a} * sin({b}x/{angle}) / ({b}/{angle})"

def integrate_sec2(a, b, angle):
    return f"{a / b} * tan({b}x/{angle})"

def integrate_csc2(a, b, angle):
    return f"-{a / b} * cot({b}x/{angle})"

def integrate_trigonometric():
    print("Choose a trigonometric function to integrate:")
    print("1. a * sin(bx/angle)")
    print("2. a * cos(bx/angle)")
    print("3. a * sec^2(bx/angle)")
    print("4. a * csc^2(bx/angle)")

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))



#definition of all functions ends right above.

#Right below the user is asked about which option he/she wants to choose. There are 4 possibilities.
while True:
    task = int(input("Enter \n 1 for morse code,\n 2 for quadratic calculator, \n 3 for differentiation, \n 4 for integration, \n 5 for factorial, \n  6 for EXIT: \n Enter the option:"))
    if task == 1: #morse code
        s = input("Enter your message: ")
        morse_code = morse_gen(s)
        pygame.mixer.init()
        dit_sound = pygame.mixer.Sound('dit2.wav')  #Here the .wav files used are passed through the pygame mixer and stored in their respective variables
        dah_sound = pygame.mixer.Sound('dah.wav')  
        final_code = ""
        for symbol in morse_code:    #This for loop is responsible for identifying dits, dahs and spaces in the encoded message. Spaces are represented by a silence.
            if symbol == '.':
                final_code += symbol
                print(final_code)
                dit_sound.play()
                time.sleep(0.2) #Responsible for making a brief pause between sounds generated.
            elif symbol == '-':
                final_code += symbol
                print(final_code)
                dah_sound.play()
                time.sleep(0.2)  
            elif symbol == ' ':
                final_code += symbol
                print(final_code)
                time.sleep(0.2) #Spaces are represented by a silence or delay of 0.2s).
    elif task == 2:
            #quadratic equation: ax^2 + bx + c
        a = int(input("Enter 'a' (where a != 0): "))
        b = int(input("Enter 'b': "))
        c = int(input("Enter 'c': "))      

        discrim = b**2 -(4*a*c)   #calculates discriminant and then decides whether the roots should be complex or normal.
        if discrim < 0:   #means complex roots will be generated
            root_one = (-b + cmath.sqrt((b**2 -(4*a*c)))) / (2*a)
            root_two = (-b - cmath.sqrt((b**2 -(4*a*c)))) / (2*a)
            # root_one = complex(round(root_one.real), round(root_one.imag))   #This line is where the real and imaginary part of each complex root is arranged in complex notation/form. (ie. a + bj)
            # root_two = complex(round(root_two.real), round(root_two.imag))
        else:  #non-complex roots to be generated
            root_one = (-b + math.sqrt((b**2 -(4*a*c)))) / (2*a)
            root_two = (-b - math.sqrt((b**2 -(4*a*c)))) / (2*a)
            root_one = round(root_one, 6)    #rounding-off of roots generated to 2 decimal points
            root_two = round(root_two, 6)

        print("Roots of the quadratic equation: ", "\n", 
        root_one , "\n" , root_two)
    elif task == 3:
        
        print('Enter 1 for simple polynomial differentiation \n Enter 2 for Trignometry differentiation \n Enter 3 for logarithamtic (ln function) differentiation \n Enter 4 for product law')
        choice=int(input())
        if choice==1: #Simple polynomial diff
            print('Enter the highest degree of the expression')
            n=int(input())
            print(differentiation(n)[0])
        elif choice==2: #SImple Trig diff
            print("Input (write) a function from the following:")
            for i,j in dict1.items():
                    print(i)
            selection=str(input())
            selection=selection.lower()
            print("Enter the angle's (variable's) highest degree")
            n=int(input())
            for i in differentiation(n):
                resultlst.append(i)
            diff=dict1[selection]
            print('('+resultlst[0]+')'+'('+diff+'('+resultlst[1]+'))')
        elif choice==3: #ln differentiation
            print('Enter 1 if the function is Simple Polynomial \n Enter 2 if the function is Trignometric')
            selectt=int(input()) #choice if ln function has simple or trig value
            if selectt==1:#simple polynomial ln function
                    print("Enter the highest degree of the expression")
                    n=int(input())
                    for i in differentiation(n):
                        resultlst.append(i)
                    print(resultlst[0]+'/'+'('+resultlst[1]+')')
            elif selectt==2:#trig ln func
                    print("Input (write/type) a function from the following:")
                    for i,j in dict1.items():
                        print(i)
                    selection=str(input())
                    selection=selection.lower()
                    print("Enter the angle's (variable's) highest degree")
                    n=int(input())
                    for i in differentiation(n):
                        resultlst.append(i)
                    diff=dict1[selection]
                    print(' ('+resultlst[0]+')['+diff+'('+resultlst[1]+')]') #Trying to output in a different way
                    print("---"*len(resultlst)*5) #Trying to output in a different way
                    print(" "+selection+'('+resultlst[1]+')') #Trying to output in a different way
        elif choice==4: #Product Law
                    print('Enter 1 if first part(U) is simple polynomial equation.\n Enter 2 if first part (U) is trig \n Enter 3 if first part (U) is logarithmatic (ln) function')
                    d=int(input())
                    productlaw(d)
        else: #If the input is not as expected
                print('Enter the number from the choices dude!')

    elif task == 4:
        print("1 for simple integration \n 2 for trig integration")
        choice=int(input())
        if choice == 1:
            # Prompt the user for input
            
            simple_integration()
        elif choice==2:
                print("Choose a trigonometric function to integrate:")
                print("1. a * sin(bx/angle)")
                print("2. a * cos(bx/angle)")
                print("3. a * sec^2(bx/angle)")
                print("4. a * csc^2(bx/angle)")
                choice = int(input("Enter your choice (1, 2, 3, or 4): "))
                a = float(input("Enter the coefficient 'a': "))
                b = float(input("Enter the coefficient 'b': "))
                angle = float(input("Enter the angle: "))

                if choice == 1:
                    result = integrate_sin(a, b, angle)
                elif choice == 2:
                    result = integrate_cos(a, b, angle)
                elif choice == 3:
                    result = integrate_sec2(a, b, angle)
                elif choice == 4:
                    result = integrate_csc2(a, b, angle)
                else:
                    print("Invalid choice. Exiting.")
                print(f"The integral of the selected trigonometric function is: {a} * ({result}) + C")
    elif task == 5:
        num = int(input("Enter number for factorial: "))
        print(str(num) +'!', "=", factorial(num))
    elif task == 6:
        print("Goodbye!")
        break
    else:
        print("This option doesn't exist!")