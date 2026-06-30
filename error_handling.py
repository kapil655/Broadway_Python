

from datetime import datetime
#eror handling
def error(file_name,message):
    with open("eror_check.txt","a") as f:
        f.write(f'{datetime.now()} {message} \n')


try:
    a=10+"kapil"
except ZeroDivisionError as message:
    error("zero_div_err.txt",message)

except NameError as message:
    error("Name_error.txt",message)

except TypeError as message:
    error("Type_er.txt",message)

except Exception as e:
    error("Exception.txt",e)



    


        
