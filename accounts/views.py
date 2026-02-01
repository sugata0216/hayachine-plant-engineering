from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pw = request.POST.get('pw')
        user = authenticate(request, username = username, password = pw)
        if user is not None:
            login(request, user)
            return redirect('main:news')
        else:
            context = {'error' : 'ユーザー名またはパスワードが違います'}
            return render(request, 'root/admin_login.html', context)
    return render(request, 'root/admin_login.html')