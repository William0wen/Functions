def calc_fines(days_overdue):
    base_charge = 0.50
    daily_charge = 0.80
    max_charge = 30
    gross_charge = base_charge + (days_overdue * daily_charge)
    if gross_charge > max_charge:
        fine = max_charge
    else:
        fine = gross_charge
    return fine


# Main

days_overdue_ = int(input("Enter days overdue: "))
print(f"For {days_overdue_} days, the fine is ${calc_fines(days_overdue_):.2f}.")
