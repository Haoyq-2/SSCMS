# -*- coding = utf-8 -*-
# @Time : 2022/5/28 19:10
# @Author : Haoyq
# @File : util.py
# @Software : PyCharm

from django.http.response import HttpResponse
from django.shortcuts import reverse, redirect

from constants import *
from user.models import Student, Teacher


def check_login(func):
    def _check(*args, **kwargs):
        request = args[1]
        cookie_kind = request.session.get('kind', '')
        if cookie_kind not in ["student", "teacher"]:
            to_url = reverse("login")
            return redirect(to_url)
        elif len(args) >= 2:
            kind = args[1]
            if kind == cookie_kind:
                return func(*args, **kwargs)
            else:
                return HttpResponse(ILLEGAL_KIND)
        return HttpResponse(INVALID_URL)

    return _check


def get_user(request, kind):
    if request.session.get('kind', '') != kind or kind not in ["student", "teacher"]:
        return None
    if len(request.session.get('user', '')) != 10:
        return None

    uid = request.session.get('user')
    if kind == "student":
        grade = uid[:4]
        number = uid[4:]
        student_set = Student.objects.filter(grade=grade, number=number)
        if student_set.count() == 0:
            return None
        return student_set[0]
    else:
        department_no = uid[:3]
        number = uid[3:]
        teacher_set = Teacher.objects.filter(department_no=department_no, number=number)
        if teacher_set.count() == 0:
            return None
        return teacher_set[0]


