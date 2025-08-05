from django.urls import path
from . import views
#from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.chart_view)),
    path('dashboard/chart/', views.chart_view, name='chart'),
    path('dashboard/chart_excel/', views.excel_chart_view, name='chart_excel'),


]
