try:
    a = 10+"a"
   
except TypeError as e:
    print(e)

except ZeroDivisionError as e:
    print(e)

except NameError as e:
    print(e)

except Exception as e:
    print(e)
finally:
    print("done")