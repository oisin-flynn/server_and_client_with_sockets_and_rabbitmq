# create an empty dictionary to store employee information
employees = {'E00123': {'name': 'Aadya Khan', 'salary': 38566, 'annual_leave': 25},
             'E01033': {'name': 'John Smith', 'salary': 29400, 'annual_leave': 25}}


def get_employees():
    return employees


def get_id(key):
    if key in employees:
        return employees[key]
    return None


def get_name(key):
    if key in employees:
        return employees[key]['name']
    return None


def get_salary(key):
    if key in employees:
        return employees[key]['salary']
    return None


def get_annual_leave(key):
    if key in employees:
        return employees[key]['annual_leave']
    return None


def get_total_salary(key, year):
    if key in employees:
        if year == 2018 or 2016:
            # assume basic pay is the employee's salary
            basic_pay = employees[key]['salary']
            # assume overtime pay is 5% of the basic pay
            overtime_pay = basic_pay * 0.05
            return basic_pay + overtime_pay
    return None


def get_leave_taken(key, year):
    if key in employees:
        if year == 2016 or 2018:
            # assume employees took half of their annual leave entitlement
            return employees[key]['annual_leave'] / 2
    return None
