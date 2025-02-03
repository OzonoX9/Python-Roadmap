# exception = Un evento que interrumpe el flujo normal de un programa
# Excepciones comunes: ImportError, IndexError, NameError, SyntaxError, TypeError, ValueError, ZeroDivisionError'
#  Se pueden usar: 1.try, 2.exept, 3.finally

try: 
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only numbers")
except Exception:
    print("Something went wrong")
finally:
    print("This will always execute")