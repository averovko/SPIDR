from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def main(request):
    return render(request, 'launcher/main.html', {})
