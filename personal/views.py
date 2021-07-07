from django.shortcuts import render


def home_screen(request, *args, **kwargs):
    template = 'personal/home.html'
    context = {

    }
    return render(request, template_name=template, context=context)
