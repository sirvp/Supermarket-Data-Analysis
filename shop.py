import random
import csv

f =open("SM1.csv","wb")
writer = csv.writer(f,delimiter=",")
pair = ('Category','Item','ShopNo','No_of_Items_Purchased','No_of_Items_Sold','In_Price','Sold_Price')
writer.writerow(pair)
for i in range (10000):

    #Mobiles
    flag1=flag2=flag3=flag4=flag5=0
    s=random.randint(1,6)
    while s!=6:
        nop = random.randint(1,100)
        nos = random.randint(1,100)
        if nop<nos :
            nop,nos=nos,nop
            
        if s==1:
            if flag1==0:
                pair = ('Mobiles','Apple',i+1,nop,nos,800,random.randint(750,900))
                flag1 = 1
                writer.writerow(pair)
            
        elif (s==2 and flag2==0):
            pair = ('Mobiles','Samsung',i+1,nop,nos,700,random.randint(650,800))
            flag2=1
            writer.writerow(pair)
            
        elif (s==3 and flag3==0):
             pair = ('Mobiles','LG',i+1,nop,nos,650,random.randint(600,740))
             flag3 = 1
             writer.writerow(pair)

        elif (s==4 and flag4==0):
             pair = ('Mobiles','Lenovo',i+1,nop,nos,400,random.randint(350,430))
             flag4 = 1
             writer.writerow(pair)

        elif (s==5 and flag5==0):
             pair = ('Mobiles','HTC',i+1,nop,nos,700,random.randint(650,800))
             flag5 = 1
             writer.writerow(pair)
            
        s=random.randint(1,6)

    #Television
    flag1=flag2=flag3=flag4=flag5=0
    s=random.randint(1,5)
    while s!=5:
        nop = random.randint(1,100)
        nos = random.randint(1,100)
        if nop<nos :
            nop,nos=nos,nop
            
        if s==1 and flag1==0:
            pair = ('Televisions','Sony',i+1,nop,nos,4000,random.randint(3500,4500))
            flag1 = 1
            writer.writerow(pair)

            
        elif s==2 and flag2==0:
            pair = ('Televisions','Samsung',i+1,nop,nos,3500,random.randint(3000,4000))
            flag2=1
            writer.writerow(pair)

            
        elif s==3 and flag3==0:
             pair = ('Televisions','LG',i+1,nop,nos,3000,random.randint(2700,3300))
             flag3 = 1
             writer.writerow(pair)


        elif s==4 and flag4==0:
             pair = ('Televisions','Micromax',i+1,nop,nos,1000,random.randint(750,1300))
             flag4 = 1
             writer.writerow(pair)
             
        s=random.randint(1,5)

    

    #Smartwatches
    flag1=flag2=flag3=flag4=flag5=0
    s=random.randint(1,5)
    while s!=5:
        nop = random.randint(1,100)
        nos = random.randint(1,100)
        if nop<nos :
            nop,nos=nos,nop
            
        if s==1 and flag1==0:
            pair = ('Smartwatches','Fitbit',i+1,nop,nos,400,random.randint(380,450))
            flag1 = 1
            writer.writerow(pair)
            
        elif s==2 and flag2==0:
            pair = ('Smartwatches','Samsung',i+1,nop,nos,500,random.randint(470,530))
            flag2=1
            writer.writerow(pair)
            
        elif s==3 and flag3==0:
             pair = ('Smartwatches','Pebble',i+1,nop,nos,250,random.randint(220,270))
             flag3 = 1
             writer.writerow(pair)

        elif s==4 and flag4==0:
             pair = ('Smartwatches','Xiaomi',i+1,nop,nos,100,random.randint(80,120))
             flag4 = 1
             writer.writerow(pair)
             
        s=random.randint(1,5)
        
    #Tablets
    flag1=flag2=flag3=flag4=flag5=0
    s=random.randint(1,6)
    while s!=6:
        nop = random.randint(1,100)
        nos = random.randint(1,100)
        if nop<nos :
            nop,nos=nos,nop
            
        if s==1:
            if flag1==0:
                pair = ('Tablets','Apple',i+1,nop,nos,900,random.randint(750,1000))
                flag1 = 1
                writer.writerow(pair)
            
        elif (s==2 and flag2==0):
            pair = ('Tablets','Samsung',i+1,nop,nos,700,random.randint(650,800))
            flag2=1
            writer.writerow(pair)
            
        elif (s==3 and flag3==0):
             pair = ('Tablets','LG',i+1,nop,nos,650,random.randint(600,740))
             flag3 = 1
             writer.writerow(pair)

        elif (s==4 and flag4==0):
             pair = ('Tablets','Lenovo',i+1,nop,nos,300,random.randint(250,330))
             flag4 = 1
             writer.writerow(pair)

        elif (s==5 and flag5==0):
             pair = ('Tablets','HTC',i+1,nop,nos,700,random.randint(650,800))
             flag5 = 1
             writer.writerow(pair)
            
        s=random.randint(1,6)


f.close()

    
    
            
        
            
