from colorama import Fore, Back, Style

# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

def validate_max():
    try:
        max = float(input("\nMax. possible score: "))
        if max <= 0:
            print("Invalid entry. Try again")
            return validate_max()
        else:
            validate_score(max)
            return max
    except ValueError:
        print("Invalid entry. Please try again.")
        return validate_max()

def validate_score(max):
    try:
        score = float(input("\nYour score: "))
        if score < 0 or score > max:
            print("Score must be between 0 and the maximum score.")
            return validate_score(max)
        else:
            calc_percent(max, score)
            return score
    except ValueError:
        print("Invalid entry. Please try again.")
        return validate_score(max)

def calc_percent(max, score):
    percent = round((score / max) * 100)
    get_grade(percent)
    return percent

def get_grade(percent):
    if percent > 98:
        grade = "A+"
        message(name, percent, grade)
        return grade
    elif percent < 98 and percent > 92:
        grade = "A"
        message(name, percent, grade)
        return grade
    elif percent < 93 and percent > 89:
        grade = "A-"
        message(name, percent, grade)
        return grade

    elif percent > 87 and percent < 90:
        grade = "B+"
        message(name, percent, grade)
        return grade
    elif percent < 88 and percent > 82:
        grade = "B"
        message(name, percent, grade)
        return grade
    elif percent < 83 and percent > 79:
        grade = "B-"
        message(name, percent, grade)
        return grade

    elif percent > 77 and percent < 80:
        grade = "C+"
        message(name, percent, grade)
        return grade
    elif percent < 78 and percent > 72:
        grade = "C"
        message(name, percent, grade)
        return grade
    elif percent < 73 and percent > 69:
        grade = "C-"
        message(name, percent, grade)
        return grade

    elif percent > 68 and percent < 70:
        grade = "D+"
        message(name, percent, grade)
        return grade
    elif percent < 68 and percent > 62:
        grade = "D"
        message(name, percent, grade)
        return grade
    elif percent < 63 and percent > 59:
        grade = "D-"
        message(name, percent, grade)
        return grade
    else:
        grade = "F"
        message(name, percent, grade)
        return grade
    return grade

def message(name, percent, grade):
    if percent >= 90:
        print(f"\nThe grade for the {name.capitalize()} Exam " + Fore.YELLOW + f"is {percent}% " + Style.RESET_ALL + "which is a " + Fore.GREEN + f"{grade}.\n")
    elif percent <= 69:
        print(f"\nThe grade for the {name.capitalize()} Exam " + Fore.YELLOW + f"is {percent}% " + Style.RESET_ALL + "which is a " + Fore.RED + f"{grade}.\n")
    else:
        print(f"\nThe grade for the {name.capitalize()} Exam " + Fore.YELLOW + f"is {percent}% " + Style.RESET_ALL + "which is a " + Fore.YELLOW + f"{grade}.\n")

print(Back.BLUE + Fore.BLACK + "*********************")
print(Back.BLUE + Fore.BLACK + "Exam Grade Calculator")
print(Back.BLUE + Fore.BLACK + "*********************")
print(Style.RESET_ALL)
name = input("Name of exam: ").capitalize()
validate_max()
