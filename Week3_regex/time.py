import re


def check_time(text):
    pattern = '^[0-9]+\:[1-5][0-9]\s*(am|AM|pm|PM)'
    result = re.search(pattern, text)
    return result != None


print(check_time("12:45pm"))  # True
print(check_time("9:59 AM"))  # True
print(check_time("6:60am"))  # False
print(check_time("five o'clock"))  # False
