amount = 92
is_member = True
is_coupon = False

if amount >= 100:
    if is_member:
        print("member")
        if is_coupon:
            print("20% discount")
        else:
            print("10% discount")
    else:
        if is_coupon:
            print("5% discount")
        else:
            print("0% discount")
else:
    print("No discount")


print("-------------------")
amount =   92
is_member = "yes"
is_coupon = "no"

if amount >= 100:
    if is_member == "yes":
        print("member")
        if is_coupon == "yes":
            print("20% discount")
        else:
            print("10% discount")
    else:
        if is_coupon == "yes":
            print("5% discount")
        else:
            print("0% discount")
else:
    print("No discount")


#single line if-else
gender="male"
data = "male" if gender =="male" else "female"
print(data)
name="kapil joshi"
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())


num="123"
print(num.isdigit())
print(num.isnumeric())
print(num.isalnum())
print(num.isnumeric())
