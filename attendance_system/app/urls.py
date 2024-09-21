from django.urls import path
from django.urls import re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static 
from . import views
from .views import AttendanceListView,AttendanceCreateView, AttendanceReport

app_name ='app'

urlpatterns = [
    path('', views.index, name='index'),
    path('attendance',AttendanceListView.as_view(), name='attendance'),
    path('attendance/create/', AttendanceCreateView.as_view(), name='attendance_create'),
    path('charts', views.chart, name='charts'),
    path('api/attendance/report/', AttendanceReport.as_view(), name='attendance_report'),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),

]

