# Used the following conversion rate
CANADA = "Canada"
USA = "USA"
UK = "United Kingdom"
CAMBODIA = "Cambodia"

RICH = 'rich'
POOR = 'poor'

EURO_TO_CAD = 1.47 #Current conversion rate from google
EURO_TO_USD = 1.18
EURO_TO_GBP = 0.91
EURO_TO_KHR = 4847.30

UK_AVERAGE = 35423
USA_AVERAGE = 56516
CANADA_AVERAGE = 64000
CAMBODIA_AVERAGE = 5649856


def a_valid_country(country):
    return (country == CANADA) or (country == USA) or (country == UK) or (country == CAMBODIA)


def convert_salary(euro, country):
    if country == CANADA:
        salary = euro * EURO_TO_CAD
    elif country == USA:
        salary = euro * EURO_TO_USD
    elif country == UK:
        salary = euro * EURO_TO_GBP
    else:
        salary = euro * EURO_TO_KHR

    return salary


def living_status(salary, country):
    if country == CANADA:
        status = POOR if (salary < CANADA_AVERAGE) else RICH
    elif country == USA:
        status = POOR if salary < USA_AVERAGE else RICH
    elif country == UK:
        status = POOR if salary < UK_AVERAGE else RICH
    else:
        status = POOR if salary < CAMBODIA_AVERAGE else RICH

    return status

def print_status(status, country, salary):
    print("You will be", status ,"in", country ,"with a salary of", round(salary, 2))


# Main flow
euro_salary = int(input("Please enter your salary in Germany: "))
target_country = input("Enter the country you want to migrate to: ")

if not a_valid_country(target_country):
    print("Invalid country:", target_country)
else:
    converted_salary = convert_salary(euro_salary, target_country)
    current_living_status = living_status(converted_salary, target_country)
    print_status(current_living_status, target_country, converted_salary)
