from django.conf.urls import url

from . import views

app_name = 'members'

urlpatterns = [
    url(
        regex=r'^$',
        view=views.member_list,
        name='member_list'
    ),
    # url(
    #     regex=r'^pdf/',
    #     view=views.member_list_pdf,
    #     name='member_list_pdf'
    # ),
]
