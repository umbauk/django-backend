from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
# ]
