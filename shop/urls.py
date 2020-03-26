from django.urls import path
from shop.views import (
    indexView,
    postFriend, 
)

urlpatterns = [
    # ... other urls
    path('', indexView),
    path('post/ajax/friend', postFriend, name = "post_friend"),
    # ...
]