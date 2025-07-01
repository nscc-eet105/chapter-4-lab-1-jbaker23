#My name is Jacob Baker and this is Chapter 4 Lab 1 which I am completing on June 24.

def far_to_cel(f):
    return (f - 32) / 1.8 
#this converts fahrenheit to celsius    

def cel_to_far(c):
    return (c * 1.8) +32
#this converts celsius to fahrenheit
     


def main():
    temp=float (input("What is the current temperature? "))
    degree=input("Did you enter the temperature in (c)elsius or (f)ahrenheit?")


    if degree == "c":
        cel_to_far(temp)
        answer = cel_to_far(temp)
        print (f" The current temperature is {temp} Celsius. The converted value is {answer: .2f} Fahrenheit.")
    elif degree == "f":
        far_to_cel(temp)
        answer = far_to_cel(temp)
        print (f" The current temperature is {temp} Fahrenheit. The converted value is {answer: .2f} Celsius.")
    else:
        print ("The value is invalid")



main()







    

    
