from django.shortcuts import render


def SignInView(request):
    return render(request, 'sign_in.html')
