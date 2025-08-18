"""
URL configuration for api_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from django.contrib import admin
from django.urls import path, include
from api.urls import router
from rest_framework.authtoken import views as authtoken_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', authtoken_views.obtain_auth_token),
    # This line creates a new API endpoint at http://127.0.0.1:8000/api-token-auth/
]

'''
DRF's Built-in Views: Django REST Framework provides several generic, "plug-and-play" views that 
handle common tasks. obtain_auth_token is one of them. Its sole purpose is to receive a username 
and password in a POST request, validate them against the database, and return a unique token.

Minimal Configuration: By using this view, you avoid the need to write the logic for authentication
, validation, and token creation yourself. 
All you have to do is import it and include it in the urls.py file.
 DRF helps you build APIs faster by providing ready-to-use components.

The obtain_auth_token view only accepts POST requests. 
You can't just visit the URL in your browser and expect it to work.

To get a token, an application (or a tool like curl or Postman) must send a POST request to 
this new URL with the user's username and password in the request body.

If the username and password are correct, the API will respond with a 
JSON object containing the token.

This is the token that a client (like a mobile app or a front-end website) will then use in all 
subsequent requests to your protected API endpoints 
'''