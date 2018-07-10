def find_my_gcd(a_list):
    def gcd (x,y):
        while y!=0:
            x,y=y,x%y
        return x
    acum = a_list[0]
    for e in a_list[1:]:
        acum = gcd(acum,e)
    return acum
