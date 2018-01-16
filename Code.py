purchase_amounts=[]
while True:
    s=input("enter the amount or 'done' to quit: ")
    if s=="done":
        break
    else:
        if s.isnumeric():
            purchase_amounts.append(int(s))
        else:
            print("Invalid !!")
print(purchase_amounts)
    
