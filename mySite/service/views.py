from django.shortcuts import render
from .models import Contact

# Create your views here.

# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         textarea = request.POST.get('textarea')

#         data = Contact(name=name, email=email, phone=phone, textarea=textarea)

#         data.save()

#     return render(request, 'contact.html')