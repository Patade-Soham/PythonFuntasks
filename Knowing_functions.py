
def format_name():
    fname = str(input('write your first name : ')).capitalize()
    lname = input('Write your last name : ').capitalize()

    output=f'{fname} {lname}'
    return output

name=format_name()

print(name)
