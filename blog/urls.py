from django.urls import path
from .views import HomePage, PostDetailView, SignUpView

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('blog/<slug>/', PostDetailView.as_view(), name='detail-view'),
    path('signup/', SignUpView.as_view(), name='signup')
]


