# My name is Jacob Baker and this is Chapter 4 Lab 1 which I am completing on June 24.
#I revised this lab on July 3 and added a loop to keep it running and changed the celsius to a void function
def far_to_cel(f):
    return (f - 32) / 1.8


# this converts fahrenheit to celsius

def cel_to_far(c):
    answer = (c * 1.8) + 32
    print(f" The current temperature is {c} Celsius. The converted value is {answer: .2f} Fahrenheit.")


# this converts celsius to fahrenheit


def main():
    while True:
        temp = float(input("What is the current temperature? "))
        degree = input("Did you enter the temperature in (c)elsius or (f)ahrenheit?")

        if degree == "c":
            cel_to_far(temp)
        elif degree == "f":
            answer = far_to_cel(temp)
            print(f" The current temperature is {temp} Fahrenheit. The converted value is {answer: .2f} Celsius.")
        else:
            print("The value is invalid")

main()
