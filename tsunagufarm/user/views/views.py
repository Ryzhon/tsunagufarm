from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('/map')  # ログインページにリダイレクト。'login' はログインページのURL nameです。
    else:
        form = UserCreationForm()
    context ={
        "page_title": "ユーザー登録画面",
        'form':form
    }
    return render(request, 'register.html', context=context)


class SignInView(LoginView):
    template_name = 'signin.html'  # サインイン用のテンプレート名
    redirect_authenticated_user = True  # 既に認証されているユーザーはリダイレクト

    def get_success_url(self):
        return reverse_lazy('home') 
