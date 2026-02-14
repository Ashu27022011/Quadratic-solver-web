def Quadratic(eq):
    import re
    eq = eq.replace(" ", "")

    # Match ax^2, bx, c
    pattern = re.findall(r'[+-]?\d*\.?\d+', eq)

    coeffs = [float(x) for x in pattern]

    a,b,c = coeffs

    deter = ((a**2) - (4*a*c))

    x1 = (-b + (deter**0.5))/(2*a)
    x2 = (-b - (deter**0.5))/(2*a)
    x3 = f"({-b} + √{deter})/{(2*a)}"
    x4 = f"({-b} - √{deter})/{(2*a)}"
    return x1,x2,x3,x4,c,b,a

def loadlottie(url:str):
    import requests
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print("Lottie load failed:", e)
    return None

def timedtext(text):
    import time
    for i in text:
        yield i
        time.sleep(0.02)