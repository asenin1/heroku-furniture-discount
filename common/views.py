from django.shortcuts import render


def landing_page(request):
    return render(request, 'common/landing_page.html', {})
