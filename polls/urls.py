from django.urls import path

from . import views

#  Using angle brackets “captures” part of the URL and sends it as a keyword argument to the view function.
# The colon (:) separates the converter and pattern name.


# Need to do below as to differentiate if other apps have the same names 
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]