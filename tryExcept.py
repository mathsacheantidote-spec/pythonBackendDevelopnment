try:
    x = int(input("Input an Integer : "))
    print(x)
# except ValueError:
#      print("Value not an Integer" + x)
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("This will definitely be printed.")
