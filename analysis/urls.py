from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_network, name='upload_network'),
    path('hydraulic/<int:network_id>/', views.hydraulic_analysis, name='hydraulic_analysis'),
    path('valve-optimization/<int:network_id>/', views.valve_optimization, name='valve_optimization'),
    path('mpc/<int:network_id>/', views.mpc_control, name='mpc_control'),
    path('analysis-page/', views.analysis_view, name='analysis_page'),  # ← this is new
]
