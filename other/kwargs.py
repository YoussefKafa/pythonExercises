def sum(**kwargs):
    sum=0
    for k,v in kwargs.items():
        sum+=v
    return round(sum,1)

print(sum(coffee=1.22,tea=2.11)) #3.3