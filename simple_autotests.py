from functions import hello, salary

assert hello("Bob") == "Hello, Bob"
assert salary(12, 20) == 480, f"Ожидаемый результат {salary(12, 20)}"

print("OK")
