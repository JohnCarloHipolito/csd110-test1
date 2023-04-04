def validate_month(mm):
    if mm < 1 or mm > 12:
        return False
    else:
        return True


def validate_day(mm, dd):
    if dd < 1:
        valid = False
    elif (dd > 28) and (mm == 2):  # Assumes February has 28 days
        valid = False
    elif (dd > 30) and ((mm == 4) or (mm == 6) or (mm == 9) or (mm == 11)):  # Check months with 30 days
        valid = False
    elif dd > 31:  # Check months with 31 days
        valid = False
    else:
        valid = True

    return valid


def validate_year(year_str):
    yy = int(year_str)
    if len(year_str) != 2:  # Use the raw input to handle 00-09 years
        valid = False
    elif yy < 0 or yy > 99:
        valid = False
    else:
        valid = True
    return valid


def print_err_and_exit_if_invalid(valid, message):
    if not valid:
        print(message)
        exit()


# main flow

# MONTH
month = int(input("Enter the month in the numeric form: "))
valid_month = validate_month(month)
print_err_and_exit_if_invalid(valid_month, 'Month: "Error: Invalid Month Input"')

# DAY
day = int(input("Enter the day in numeric form: "))
valid_day = validate_day(month, day)
print_err_and_exit_if_invalid(valid_day, 'Day: "Error: Invalid Day Input"')

# YEAR
year = input("Enter the year as two numerical digits: ")
valid_year = validate_year(year)
print_err_and_exit_if_invalid(valid_year, 'Year: "Error: Invalid Year Input"')

# Valid, print the date in m/d/yy
print("Success: Congratulations! you entered the correct date.")
print("The date is ", month, "/", day, "/", year)
