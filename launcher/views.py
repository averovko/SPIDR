from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
<<<<<<< HEAD
from django.conf import settings
from .models import Application
from .xmlconverter import XMLConverter
=======
from .models import Application
>>>>>>> origin/master

import os
try:
    import configparser
except:
    from six.moves import configparser


@login_required
def main(request):
<<<<<<< HEAD
    ext_apps_dir = getattr(settings, "EXTERNAL_APPS_DIR", None)
    apps = os.listdir(ext_apps_dir)
=======
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    apps_dir = os.path.join(base_dir, 'apps')
    apps = os.listdir(apps_dir)
>>>>>>> origin/master

    config = configparser.ConfigParser()
    applications = []
    for app in apps:
<<<<<<< HEAD
        app_home = os.path.join(ext_apps_dir, app)
=======
        app_home = os.path.join(apps_dir, app)
>>>>>>> origin/master
        config_file = os.path.join(app_home, 'config', 'app.conf')

        config.read(config_file)
        label = config.get('ui', 'label')
        application = Application(app, label, app_home)
        applications.append(application)

    return render(request, 'launcher/main.html', {'applications': applications})

<<<<<<< HEAD

@login_required
def launch_app(request, app_name):
    print(app_name)

    config_file = os.path.join(getattr(settings, "EXTERNAL_APPS_DIR", None), app_name, 'config', 'app.conf')

    config = configparser.ConfigParser()
    config.read(config_file)
    dashboard = config.get('ui', 'default_dashboard')

    return redirect('launch_app_dashboard', app_name=app_name, dashboard_name=dashboard) #render(request, 'launcher/main.html', {})


@login_required
def launch_app_dashboard(request, app_name, dashboard_name):
    print('Application:{}, Dashboard:{}'.format(app_name, dashboard_name))

    menu_html = XMLConverter.convert_navigation(xml_file=os.path.join(getattr(settings, "EXTERNAL_APPS_DIR", None), app_name, 'views', 'navigation', 'navigation.xml'))
    return render(request, 'launcher/main.html', {'menu_html': menu_html})
=======
@login_required
def launch_app(request, app_name):
    print(app_name)
    return render(request, 'launcher/main.html', {})
>>>>>>> origin/master
