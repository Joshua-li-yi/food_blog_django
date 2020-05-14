from django.urls import path
from index.views import index

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', index)
]
