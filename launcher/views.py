from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Application

import os
try:
    import configparser
except:
    from six.moves import configparser


@login_required
def main(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    apps_dir = os.path.join(base_dir, 'apps')
    apps = os.listdir(apps_dir)

    config = configparser.ConfigParser()
    applications = []
    for app in apps:
        app_home = os.path.join(apps_dir, app)
        config_file = os.path.join(app_home, 'config', 'app.conf')

        config.read(config_file)
        label = config.get('ui', 'label')
        application = Application(app, label, app_home)
        applications.append(application)

    return render(request, 'launcher/main.html', {'applications': applications})

@login_required
def launch_app(request, app_name):
    print(app_name)
    return render(request, 'launcher/main.html', {})