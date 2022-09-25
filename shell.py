import Yopthon

while True:
    text = input("yopthon> ")
    result, error = Yopthon.run('<stdin>', text)
    if error: print(error.as_string())
    else: print(result)