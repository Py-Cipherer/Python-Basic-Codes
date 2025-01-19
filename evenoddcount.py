def odd_even_counter(a):
    tup=()
    tup+=(a,)
    s=str(a)
    e=0
    o=0
    for i in s:
        if (int(i))%2==0:
            e+=1
        else:
            o+=1
    print(tup)
    print("No. of Even digits= ",e,"\nNo. of Odd Digits= ",o)
odd_even_counter(62376)
