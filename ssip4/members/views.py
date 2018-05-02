from io import BytesIO

from django import forms
from django.http import HttpResponse
from django.template import Context, Template

from django.views.generic import DetailView, ListView
from django.views.decorators.http import require_http_methods

from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings

from environ import Env


from .models import Member
from .forms import PasswordForm
from .utils import make_pdf


@require_http_methods(['GET', 'POST'])
def member_list(request):
    if request.POST:
        pw_form = PasswordForm(request.POST)
        password_valid_and_correct = \
            pw_form.is_valid() \
            and pw_form.cleaned_data['password'] == settings.MEMBERS_PASSWORD
        if password_valid_and_correct:
            request.session['password'] = pw_form.cleaned_data['password']
        else:
            messages.error(request, "The password you entered was incorrect, please try again.")
        return redirect('members:member_list')
    
    password_in_session = request.session.get('password')
    password_correct = password_in_session\
        and request.session['password'] == settings.MEMBERS_PASSWORD
    if not password_correct:
        pw_form = PasswordForm()
        return render(request, 'members/members_password_form.html', {
            'pw_form': pw_form,
        })
    member_list = Member.objects.all()
    return render(request, 'members/member_list.html', {
        'member_list': member_list,
    })


def member_list_pdf(request):
    pdf = make_pdf()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="memberlist.pdf"'
    response.write(pdf)
    return response