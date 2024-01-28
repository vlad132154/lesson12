from functions import hello, salary

hello("Alex")
if hello("Alex") != "Hello, Alex":
    print("Error")

if salary(20, 20) != 800:
    print("Error")
if salary(1, 1) != 2:
    print("Error")
if salary(100, 100) != 20000:
    print("Error")
