def calc_gst(number):
    number *= 1.15
    return number


# Main

number_ = float(input("Input price: $"))
print(f"${number_} + gst = ${calc_gst(number_)}")
