a=str(input(""))
card_num=[]
counter=0
sumt=0
tamp=0
sumc=0
for i in a:
    
    card_num.append(int(i))

for j in  card_num:
    if counter%2!=0:
        sumt=sumt+j
    else:
        tamp=j*2
        if tamp>=10:
            tamp=str(tamp)
            for l in tamp:
                sumc=sumc+int(l)
        else:
            sumc=sumc+tamp
    counter+=1
last_sum=sumc+sumt
if last_sum%10==0:
    print("Luhn algoritmasına uyuyor.")
else:
    print("Luhn algoritmasına uymuyor.")

        
