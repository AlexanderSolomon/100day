
#docstrings multiline comments


def format_name(f_name, l_name):
    """take a fist and last name and format it 
to return the tilte case version of the name."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
   
    return f"{formated_f_name} {formated_l_name}"
    
    
formated_string = format_name("alex","sonsSSon")
print(formated_string)

print(len("alex"))
