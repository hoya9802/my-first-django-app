from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from blog.models import Post
from django.conf import settings
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render


# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html' # 지정 안하면 model명_list.html를 찾아 rendering 시도

    '''
    기존 context변수명인 object_list 이름을 posts로 변경이 가능!
    지정해주더라도 기존 object_list이름도 사용 가능!
    '''
    context_object_name = 'posts'
    paginate_by = 2 # 한 페이지에 보여줄 객체 리스트 개수를 제공

class PostDV(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    context_object_name = 'random_parameter'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'

class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self) -> QuerySet[Any]:
        # Django ORM에서 __name (더블 언더스코어)는 Post model과 연결된 Tag 모델의 이름을 나타낸다.
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))
    
    # To add context variable in templates file, override get_context_data()
    def get_context_data(self, **kwargs):
        # 상위 클래스에서 바뀌기 전 context variable를 가져옵니다.
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag'] # url에서 해시값으로 전달될 <str:'
        return context

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        print('method executed')
        context = super().get_context_data(**kwargs)
        # 폼을 my_form으로 설정
        context['my_form'] = context.get('form', self.get_form())
        print('++++++++++++', context)
        return context

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     print('method executed wrong')
    #     context = super().get_context_data(**kwargs)
    #     if 'myy_form' not in context:  # 만약 my_form이 없으면, 새로운 폼 객체 생성
    #         context['myy_form'] = self.get_form()
    #     context['myy_form'] = context.get('form')  # 기존 폼을 가져와서 my_form에 할당
    #     print('+++++++++++',context)
    #     return context
    
    def form_valid(self, form: Any) -> HttpResponse:
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(
            Q(title__icontains=searchWord) |
            Q(description__icontains=searchWord) |
            Q(content__icontains=searchWord)
        ).distinct()

        context = {
            'my_form': form,  # my_form으로 설정
            'search_term': searchWord,
            'object_list': post_list,
        }
        return render(self.request, self.template_name, context)
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tags']
    initial = {'slug': 'auto-filling-do-not-input'}
    # fields = ['title', 'description', 'content', 'tags']
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        # self.request.user : 현재 로그인한 유저
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blog/post_change_list.html'

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)

class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tags']
    success_url = reverse_lazy('blog:post_list')

class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')