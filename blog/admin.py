from django.contrib import admin
from blog.models import Post

# admin에 Post라는 모델을 등록해서 관리할 수 있도록 한다.
admin.site.register(Post)