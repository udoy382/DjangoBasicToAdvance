from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls.conf import path
from .forms import usersForm
from service.models import Service
from news.models import News
from django.core.paginator import Paginator
from service.models import Contact


# -------------------------
# Username = admin
# Password = admin
# ---------------------------

# def homePage(request):
    
#     data={
#         'title':'Home Page',
#         'bdata':'hey there im udoy rahmn',
#         'clist':['PHP', 'Django', 'C++', 'Python'],
#         'numbers':[10, 20, 30, 40, 50],
#         'student_details':[
#             {'name':'udoy', 'phone':'01782299436'},
#             {'name':'testing','phone':'11122233565'}
#         ]
#     }

#     return render(request, 'index.html', data)


# ------------ New WebPage --------------

def homePage(request):
    #( use minus (-) after title for reverse)
    serviceData = Service.objects.all().order_by('title')[2:5] # set limite with using slicing method
    newsData = News.objects.all()
    paginator = Paginator(serviceData, 1)
    page_number = request.GET.get('page')
    serviceDataFinal = paginator.get_page(page_number)

    data = {
        # 'serviceData':serviceData,
        'serviceData':serviceDataFinal,
        'newsData':newsData
    }

    return render(request, 'index.html', data)

# newsid -> for take a unique id in url like slug
def newsDeatils(request, slug):
    # newsDeatils = News.objects.get(id=newsid)
    newsDeatils = News.objects.get(new_slug=slug)
    data = {
        'newsDeatils':newsDeatils
    }
    return render(request, 'blogPost.html', data)

# Not Work For Some Resion
def services(request):
    serviceD = Service.objects.all()
    if request.method == 'GET':
        st = request.GET.get('query')
        if st != None:
            # __icontains
            serviceD = Service.objects.filter(title=st)

    data = {
        'serviceD':serviceD
    }
    
    return render(request, 'base.html', data)

# def contact(request):
#     try:
#         name = request.GET.get('name')
#         email = request.GET.get('email')
#         Phone = request.GET.get('Phone')
#         # print(name, email, Phone)
#         finalans = [name, email, Phone]
#     except:
#         pass
        
#     # return HttpResponse('Welcome to about us page')

#     return render(request, 'contact.html', {'output':finalans})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        textarea = request.POST.get('textarea')

        mydata = Contact(name=name, email=email, phone_number=phone_number, textarea=textarea)

        mydata.save()

    return render(request, 'contact.html')

def Course(request):
    return HttpResponse('Welcome to Course page')


def courseDetails(request, courseid):
    return HttpResponse(courseid)

def about(request):
    final_output = []
    fn = usersForm()

    data = {'form':fn}
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')

            final_output = str([name, email, phone])

            data = {
                'form':fn,
                'output':final_output
            }

            url = '/contact/?output={}'.format(final_output)

            # return HttpResponseRedirect(url)
            return redirect(url)
    except:
        pass

    return render(request, 'about.html', data)


def submitform(request):
    final_output = []
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')

            final_output = str([name, email, phone])

            url = '/contact/?output={}'.format(final_output)

            return HttpResponse(final_output)
    except:
        pass


def calculator(request):
    c = ''
    try:
        if request.method == 'POST':
            num1 = eval(request.POST.get('num1'))
            num2 =eval(request.POST.get('num2'))
            opr = request.POST.get('opr')

            if opr == '+':
                c = num1 + num2
            elif opr == '-':
                c = num1 - num2
            elif opr == '*':
                c = num1 * num2
            elif opr == '/':
                c = num1 / num2

    except:
        c = 'Invalid Opr...'
    print(c)
    return render(request, 'calculator.html', {'c':c})


def evenodd(request):
    c = ''
    if request.method == 'POST':
        if request.POST.get('num1') == '':
            return render(request, 'evenodd.html', {'error':True})

        n = int(request.POST.get('num1'))
        if n%2==0:
            c = 'Even Number'
        else:
            c = 'Odd Number'

    return render(request, 'evenodd.html', {'c':c})


def marksheet(request):
    if request.method == 'POST':
        s1 = int(request.POST.get('subject1'))
        s2 = int(request.POST.get('subject2'))
        s3 = int(request.POST.get('subject3'))
        s4 = int(request.POST.get('subject4'))
        s5 = int(request.POST.get('subject4'))

        t = s1 + s2 + s3 + s4 + s5
        p = t*100/500

        if p >= 60:
            d = 'First Div'
        elif p >= 48:
            d = 'Second Div'
        elif p >= 35:
            d = 'Third Div'

        else:
            d = 'Fail'
        
        data = {
            'total':t,
            'pers':p,
            'div':d
        }
        return render(request, 'marksheet.html', data)

    return render(request, 'marksheet.html')