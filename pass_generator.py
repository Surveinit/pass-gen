import random


# 8 digit password
def pass_gen_e():
    list = ['a','b','c','d','e','f']
    la = str(random.choice(list))

    lista = ["A","B","C","D","E","F"]
    b = random.choice(lista)

    c = str(random.randint(0,9))
 

    listb = ['!','@','#','$','%','&','*']
    lb = str(random.choice(listb))


    all = str(c+la+c+"="+lb+b+lb+".")
    return all

# 10 digit password
def pass_gen():
    list = ['a','b','c','d','e','f']
    la = str(random.choice(list))

    lista = ["A","B","C","D","E","F"]
    b = random.choice(lista)

    c = str(random.randint(10,99))
 

    listb = ['!','@','#','$','%','&','*']
    lb = str(random.choice(listb))


    all = str(c+la+c+"="+lb+b+lb+".")
    return all




# 12 digit password

def pass_gen_e():
    list = ['a','b','c','d','e','f']
    la = str(random.choice(list))

    lista = ["A","B","C","D","E","F"]
    b = random.choice(lista)

    c = str(random.randint(0,9))
 

    listb = ['!','@','#','$','%','&','*']
    lb = str(random.choice(listb))


    all = str(c+la+c+"="+lb+b+lb+".")
    return all




# 10 digit password
def pass_gen_t():
    list = ['a','b','c','d','e','f']
    la = str(random.choice(list))

    lista = ["A","B","C","D","E","F"]
    b = random.choice(lista)

    c = str(random.randint(10,99))
 

    listb = ['!','@','#','$','%','&','*']
    lb = str(random.choice(listb))


    all = str(c+la+c+"="+lb+b+lb+".")
    return all

