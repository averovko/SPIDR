from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
from .models import Application
from .xmlconverter import XMLConverter

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
        config_file = os.path.join(app_home, 'local', 'app.conf')
        print(config_file)
        config.read(config_file)
        label = config.get('ui', 'label')
        application = Application(app, label, app_home)
        applications.append(application)

    return render(request, 'launcher/main.html', {'applications': applications})


@login_required
def launch_app(request, app_name):
    print(app_name)

    config_file = os.path.join(getattr(settings, "EXTERNAL_APPS_DIR", None), app_name, 'local', 'app.conf')

    config = configparser.ConfigParser()
    config.read(config_file)
    dashboard = config.get('ui', 'default_dashboard')

    return redirect('launch_app_dashboard', app_name=app_name, dashboard_name=dashboard)


@login_required
def launch_app_dashboard(request, app_name, dashboard_name):
#    print('Application:{}, Dashboard:{}'.format(app_name, dashboard_name))
    stylesheets = []
    menu_html, menu_stylesheet = XMLConverter.convert_navigation(xml_file=os.path.join(getattr(settings, "EXTERNAL_APPS_DIR", None), app_name, 'local', 'data', 'ui', 'nav', 'default.xml'))
    stylesheets.extend(menu_stylesheet)
    
    return render(request, 'launcher/app.html', {'app_name':app_name, 'stylesheets':stylesheets, 'menu_html':menu_html})

