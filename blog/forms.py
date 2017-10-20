from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    # 장고가 폼을 만들 떄 어떤 데이터 모델을 참조해야 하는지 알기위한 class
    class Meta:
        model = Post
        fields = ('title', 'text')