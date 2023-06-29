from django.shortcuts import render
from . import func
from django.http import HttpResponse
def resetpassword(request):
    return render(request, 'login.html')


def submit(request):

    username = request.POST.get('username')
    email = request.POST.get('email')

    func.get_change_user(username, func.gerar_senha())

    return HttpResponse(status=204)