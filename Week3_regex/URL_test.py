import re


def check_web_address(text):
    pattern = '^(www\.)?[0-9a-zA-Z_-]*\.(com|org|US)$'
    result = re.search(pattern, text)
    return result is not None


print(check_web_address("gmail.com"))  # True
print(check_web_address("www@google"))  # False
print(check_web_address("www.Coursera.org"))  # True
print(check_web_address("web-address.com/homepage"))  # False
print(check_web_address("My_Favorite-Blog.US"))  # True

