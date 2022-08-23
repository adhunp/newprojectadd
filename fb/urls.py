from django.urls import path
from .import views

urlpatterns=[
    path('',views.fb),
    path('validation',views.domvalidation),
    path('val',views.val),
    path('calculater',views.calculater),
    path('array',views.array),
    path('firstpush',views.firstpush),
    path('thirdpush',views.thirdpush),
    path('grid',views.css_grid),
    path('grid2',views.css_grid2),
    path('grid3',views.css_grid3),
    path('bootstrap1',views.bootstrap1),
    path('grid4',views.css_grid4),

]