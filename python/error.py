try:
    user_weight = float(input("Enter Your Weight in kg: "))
    user_height = float(input("Enter Your Height in m: "))
    user_BMI = user_weight / user_height ** 2
except ValueError:
    print("Enter a reasonable value")
except ZeroDivisionError:
    print("You cannot be 0m high")
except:
    print("Why you like playing dumb?")
else:
    print(f"Your BMI: {user_BMI}")
finally:
    print("Program Done!")