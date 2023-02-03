import time

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from auth_helper import get_sign_in_flow, get_token_from_code, store_user, remove_user_and_token, get_token
from graph_helper import *
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    #context = initialize_context(request)
    return render(request, 'app/index.html')


def initialize_context(request):
    context = {}
    error = request.session.pop('flash_error', None)

    if error is not None:
        context['errors'] = []
        context['errors'].append(error)

    # Check for user in the session
    context['user'] = request.session.get('user', {'is_authenticated': False})
    print(context['user'])
    print('aqui')

    return context


def sign_in(request):
    # Get the sign-in flow
    flow = get_sign_in_flow()
    # Save the expected flow so we can use it in the callback
    try:
        request.session['auth_flow'] = flow
    except Exception as e:
        print(e)
    # Redirect to the Azure sign-in page

    print(request.session)
    print("aqui2")
    return HttpResponseRedirect(flow['auth_uri'])


def sign_out(request):
    # Clear out the user and token
    remove_user_and_token(request)
    return HttpResponseRedirect(reverse('index'))


def callback(request):
    # Make the token request
    result = get_token_from_code(request)
    # Get the user's profile from graph_helper.py script
    user = get_user(result['access_token'])
    # Store user from auth_helper.py script
    store_user(request, user)
    return HttpResponseRedirect(reverse('index'))

