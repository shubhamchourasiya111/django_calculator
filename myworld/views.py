#create view in  project
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse



def ADD(request):
    c=""
    try:
        if request.method=="POST":
           
            n1 = eval(request.POST['num1'])
            n2 = eval(request.POST['num2'])
            opr=(request.POST['opr'])
            print(n1)
            if  opr=="+":
                c= n1+n2
                print("dsf")
                
            elif opr=="-":
                c=n1-n2
           
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
             

            

    except:
        c= "invaild Value"
        print(c)
       
       
    print(c)


    return render(request,"index.html",{"c":c})

    

     

 
