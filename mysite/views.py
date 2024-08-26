from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin

"""
reverse() : FBV에서 해당 함수가 실행되면 즉시, URL를 계산한다.
reverse_lazy() : CBV에서 상위 클래스를 overriding하는 과정에서 상위 클래스의 url관련 메서드가 자동으로
실행되어 메모리를 잡아먹는 문제가 발생하기 때문에 이를 해결하기 위한 함수로 해당 함수는 url이 정말 필요한 순간
이 오면 그때 url를 계산
"""

class HomeView(TemplateView):
    template_name = 'home.html'

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)