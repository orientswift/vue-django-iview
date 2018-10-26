# -*- coding: UTF-8 -*-
import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.views.generic import View
from Utils.django_utils import  JsonError, JsonSuccess, get_token, redis_get, redis_db
from Web.models import XYUser

class Login(View):

    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        # next_url = request.GET.get('next') or resolve_url("admin")
        # if user.is_active is false then can't use authenticate() to validate
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            ret = {'username': username}
            token = redis_get(username)
            if not token:
                token = get_token()
                redis_db.setex(username, token, 300)
            session_id = request.session.session_key
            ret['token'] = token
            ret['session_id'] = session_id
            return JsonSuccess('登录成功', **ret)
        user = XYUser.objects.filter(username=username).first()
        if not user:
            return JsonError('用户名未注册')
        if user.is_active is False:
            return JsonError('账号未激活')
        return JsonError('账号密码不正确')