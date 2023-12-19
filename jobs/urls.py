from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/add/', views.addjob, name='addjob'),
    path('jobs/', views.jobs, name='jobs'),
    path('job/details/<int:id>/', views.jobdetails, name='jobdetails')
]





# 1. OS Command Injection
# import os

# input_data = input("Enter command: ")
# os.system(input_data)

# 2. Cross-site Scripting (XSS)
# Assuming this is part of a Django template
# user_input = '<script>alert("XSS attack!")</script>'
# html_output = f'<p>{user_input}</p>'
# print(html_output)

# 3. Session Hijacking
# No code snippet provided, but typically involves stealing or manipulating session cookies.

# 4. Cross-Site Request Forgery (CSRF)
# Django provides built-in protection, but an example might involve tricking a user into clicking a malicious link.

# 5. SQL Injection
# Using raw SQL queries without parameterization
# user_input = input("Enter username: ")
# query = f"SELECT * FROM users WHERE username = '{user_input}'"
# Instead, use Django's ORM or parameterized queries.






# 1. OS Command Injection
# import subprocess

# input_data = input("Enter command: ")
# Use subprocess module and provide arguments separately
# subprocess.run(['ls', input_data])

# 2. Cross-site Scripting (XSS)
# Use Django's template system to automatically escape user input
# from django.utils.html import escape

# user_input = '<script>alert("XSS attack!")</script>'
# html_output = f'<p>{escape(user_input)}</p>'
# print(html_output)

# 3. Session Hijacking
# Use secure session mechanisms (e.g., HTTPS, secure cookies, session timeouts).

# 4. Cross-Site Request Forgery (CSRF)
# Django provides built-in protection using a CSRF token.
# Ensure {% csrf_token %} is included in forms.

# 5. SQL Injection
# Use Django's ORM and parameterized queries
# from django.db import models

# user_input = input("Enter username: ")
# user = models.User.objects.raw('SELECT * FROM users WHERE username = %s', [user_input])
# Or use ORM: user = models.User.objects.get(username=user_input)


