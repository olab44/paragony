

def div(a, b):
    return a / b


# try:
#     result = div('fff', 0)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
def input_value(prompt=''):
    while True:
        try:
            text = input(prompt)
            return int(text)
        except ValueError:
            print('Incorrect Value')


at_end = False
while not at_end:
    a = input_value("Enter first number: ")
    b = input_value("Enter second number: ")
    try:
        result = div(a, b)
        print(f'{a}/{b} = {result}')
    except ZeroDivisionError:
        print('Division could not be completed- b == 0')
        at_end = True
