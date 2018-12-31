from app import nav
from flask_login import current_user
from flask_nav.elements import Navbar, View, Text
import os


@nav.navigation()
def topbar():
    if current_user.is_authenticated:
        return Navbar(
            os.environ.get('BLOGGING_SITENAME'),
            Text(str(os.environ.get('BLOGGING_SITENAME'))),
            View('Home', 'main.index'),
            View('Updates', 'blogging.index'),
            View('Account', 'auth.account'),
            View('Logout', 'auth.logout')
        )
    else:
        return Navbar(
            os.environ.get('BLOGGING_SITENAME'),
            Text(str(os.environ.get('BLOGGING_SITENAME'))),
            View('Home', 'main.index'),
            View('Updates', 'blogging.index'),
            View('Login', 'auth.login')
        )
