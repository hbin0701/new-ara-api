import uuid

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_http_methods

from rest_framework_jwt.settings import api_settings

from ara.classes.sparcssso import Client

from apps.user.models import UserProfile, OldAraUser

import random

is_beta = [False, True][int(settings.SSO_IS_BETA)]
sso_client = Client(settings.SSO_CLIENT_ID, settings.SSO_SECRET_KEY, is_beta=is_beta)


@require_http_methods(['GET'])
def login_callback(request):
    next_path = request.session.pop('next', '/')
    state_before = request.session.get('sso_state')
    state = request.GET.get('state')

    # Possibility of Session Hijacked
    if state_before != state:
        return JsonResponse(status=403,
                            data={
                                'msg': 'TOKEN MISMATCH: session might be hijacked!'
                            })

    code = request.GET.get('code')
    user_data = sso_client.get_user_info(code)

    sid = user_data['sid']
    user_list = User.objects.filter(username=sid)
    if not user_list:
        user = User.objects.create_user(
            username=sid,
            email=user_data['email'],
            password=str(random.getrandbits(32)),
            first_name=user_data['first_name'],
            last_name=user_data['last_name']
        )
        user.save()

        profile, created = UserProfile.objects.get_or_create(
            sid=sid,
            user=user,
            defaults={'nickname': str(uuid.uuid4())},
        )

    else:
        user = authenticate(username=user_list[0].username)
        user = user_list[0]
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.save()
        user_profile = UserProfile.objects.get(user=user)
        user_profile.save()

    next_path = '{0}?jwt={1}'.format(next_path, api_settings.JWT_ENCODE_HANDLER(
        api_settings.JWT_PAYLOAD_HANDLER(
            user,
        )
    ))

    return redirect(next_path)


@login_required(login_url='/user/login/')
def unregister(request):
    if request.method != 'POST':
        return JsonResponse(status=405,
                            data={'msg': 'Should use POST'})

    user = request.user
    user_profile = UserProfile.objects.get(user=user)

    sid = user_profile.sid
    if sso_client.unregister(sid):
        user_profile.delete()
        user.delete()
        logout(request)
        return JsonResponse(status=200, data={})
    else:
        return JsonResponse(status=403,
                            data={'msg': 'Unregistered user'})


@csrf_exempt
@require_http_methods(['POST'])
def old_ara_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    old_ara_user = OldAraUser.objects.filter(username=username).first()

    if not old_ara_user or not old_ara_user.compare_password(password):
        return JsonResponse(status=401, data={'success': False})

    return JsonResponse(status=200, data={'success': True})
