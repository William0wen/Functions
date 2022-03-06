# Function to print name given number of times

def print_name(name, number):
    for item in range(0, number):
        print(name)


# Main

name_ = input("Name to print: ")
number_ = int(input("Times to print: "))

print_name(name_, number_)
