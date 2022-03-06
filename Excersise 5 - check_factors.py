def check_factor(big_num, small_num):
    return big_num % small_num == 0


# Main

big = int(input("Enter a big number: "))
small = int(input("Enter a small number: "))

if check_factor(big, small):
    print(f"{small} is a factor of {big}")
else:
    print(f"{small} is not a factor of {big}")

