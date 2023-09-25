# variable length argument
def mult(*m):
    result=1
    for i in m:
        result=result*i
    print("The product is:",result)
mult(3)
mult(6,9,12)
mult(11,22,33,44,55)
# keyword variable length argument
def key(*name, **details):
    print(name)
    print(details)
    for j in name:
        print(j)
        for k,v in details.items():
            print(k,v)
key("Dharshan",city="salem",mobile="oppo",age=20)
key("Karthi",city="namakkal",Mobile="oppo",age=20)
key("Jana",city="rasipuram",mobile="vivo",age=21)