#functions with output

def format_name(f_name, l_name):
    #convert the strings so every starting letter is capitol
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
   
    return f"{formated_f_name} {formated_l_name}"
    
    
formated_string = format_name("alex","sonsSSon")
print(formated_string)

print(len("alex"))


