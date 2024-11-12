# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import os
import getpass
import subprocess

def htop_view(request):
    # Information for the webpage
    name = "Chinni Yandapalli"  # Replace with your name
    username = getpass.getuser()

    server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
    
    # Get system top command output
    top_output = subprocess.check_output(['top', '-bn', '1']).decode('utf-8')

    # HTML structure
    html_content = f"""
    <html>
        <head><title>System Info</title></head>
        <body>
            <h1>System Information</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    return HttpResponse(html_content)