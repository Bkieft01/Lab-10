#Brenna Kieft
def my_get_method(dictionary,get,default):
    dictionary.get("get",default)

clothes={"shirt":blue, "pants":red, "coat":purple}

my_get_method(clothes,"shirt",pink)

my_get_method(clothes, "pants", yellow)

my_get_method(clothes, "coat", white)
