from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from service.models import service
from News.models import News


def Home(request):
    Newsdata=News.objects.all()
    servicedata=service.objects.all().order_by('-service_title')[1:4]
    # for n in servicedata:
    #     print(n.service_icon)
    # print(service)
    data={
        'servicedata':servicedata,
        'Newsdata':Newsdata
    }
    return render(request,"index.html",data)
def newsdetail(request,newid):
    newsdetail=News.objects.get(id=newid)
    print(newsdetail)
    return render(request,"news.html",{'newsdetail':newsdetail})

def index(request):
    return render(request,"inner-page.html")

def porfolio(request):
    return render(request,"portfolio-details.html")

def contant(request):
    answer=0
    sub=0
    try:
        if request.method=="GET":
            n1=int(request.GET.get("num1"))
            n2=int(request.GET.get("num2"))
            answer=n1+n2
            sub=n1-n2
            return HttpResponseRedirect(redirect_to)
    except:
        pass
    return render(request,"contant.html",{'a':answer,'b':sub})

def post(request):
    answer=0
    sub=0
    try:
        if request.method=="POST":
            n1=int(request.POST.get("num1"))
            n2=int(request.POST.get("num2"))
            answer=n1+n2
            sub=n1-n2
        
    except:
        pass
    return render(request,"post.html",{'a':answer,'b':sub})

def submit(request):
    answer=0
    sub=0
    try:
        if request.method=="POST":
            n1=int(request.POST.get("num1"))
            n2=int(request.POST.get("num2"))
            answer=n1+n2
            sub=n1-n2
            data={
                'n1':n1,
                'n2':n2,
                'output':answer
            }
            url='/index/?output={}'.format(answer)
            return redirect(url)

    except:
        pass
    
def security(request):
    fn=UserForm()
    answer=0
    try:
        data={
                'form':fn,
            }
        if request.method=="POST":
            n1=int(request.POST.get("num1"))
            n2=int(request.POST.get("num2"))
            answer=n1+n2
            data={
                'sum':answer,
                'form':fn
            }
            
    except:
        pass
    return render(request,'security.html',data)


def calcu(request):
    ans=0
    c=""
    d=""
    try:
        if request.method=="POST":
            n1=eval(request.POST.get("num1"))
            n2=eval(request.POST.get("num2"))
            opr=request.POST.get("opr")
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
    except:
        c="invalid value-------"
    print(c)
    return render(request,'cal.html',{"c":c})


def marksheet(request):
    total=0
    per=0
    ob_Total=0
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get("num1"))
            m1=eval(request.POST.get("mun1"))
            n2=eval(request.POST.get("num2"))
            m2=eval(request.POST.get("mun2"))
            n3=eval(request.POST.get("num3"))
            m3=eval(request.POST.get("mun3"))
            n4=eval(request.POST.get("num4"))
            m4=eval(request.POST.get("mun4"))
            n5=eval(request.POST.get("num5"))
            m5=eval(request.POST.get("mun5"))
            total=n1+n2+n3+n4+n5
            ob_Total=m1+m2+m3+m4+m5
            per=(total*100)/ob_Total
            if per>80:
                c=" Grade :A"
            elif per>59:
                c=" Grade :B"
            elif per>32:
                c="Grade:C"
            else:
                c="Fall"
            
            data={
                't':total,
                'p':per,
                'ot':ob_Total,
                'c':c
            }
            return render(request,"marksheet.html",data)
    except:
        pass
    return render(request,"marksheet.html")

def ev_od(request):
    n=""
    
    try:
        if request.method=="POST":
            if request.POST.get("num1")=="":
                 return render(request,"ev_od.html",{'error':True})

            n1=int(request.POST.get("num1"))
            if n1%2==0:
                n="even no"
            elif n1%2!=0:
                n="odd no"
            print(n)
    except:
        pass

    return render(request,"ev_od.html",{'c':n})

    