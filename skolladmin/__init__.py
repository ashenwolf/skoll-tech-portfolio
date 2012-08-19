#
from webapp2 import Route

import views

routes = [
    Route(r'/', 					views.dashboard,		'admin-dashboard'),

    # authentication
    Route(r'/login', handler=views.login, name='user-login'),
    Route(r'/logout', handler=views.logout, name='user-logout'),
]
