def calculator(x,y,op):
    if op == "+":
        return x+y
    elif op == "-":
        return x-y
    elif op == "*":
        return x*y
    elif op == "/":
        return float(x)/float(y)
    else:
        print("Unknown operator")
        return