from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import GumiPost
from django.db.models import Q 
from django.contrib import messages
from accounts.models import CustomUser,Connection
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from accounts.helpers import get_current_user
from django.views.generic import FormView
from .forms import ContactForm

class IndexView(ListView):
    template_name='index.html'
    queryset=GumiPost.objects.order_by('-posted_at')
    paginate_by=9
    def get_queryset(self):
        q_word = self.request.GET.get('query')
 
        if q_word:
            object_list = GumiPost.objects.filter(
                Q(title__icontains=q_word) | Q(maker__makername__icontains=q_word))
            
        else:
            object_list = GumiPost.objects.all()
        
        return object_list
    
class GumiListView(ListView):
    template_name='search.html'
    def get_queryset(self):
        q_word = self.request.GET.get('query')
 
        if q_word:
            object_list = GumiPost.objects.filter(
                Q(title__icontains=q_word) | Q(maker__makername__icontains=q_word))
            
        else:
            object_list = GumiPost.objects.all()
        
        return object_list
            
            

class DetailView(DetailView):
    template_name='detail.html'
    model=GumiPost
    def get_context_data(self,*args,**kwargs):
       context = super(DetailView,self).get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
       guminame = self.kwargs['pk']
       context['guminame']=guminame
       context['user'] = get_current_user(self.request)
       if guminame is not context['user'].username:
           result = Connection.objects.filter(like__username=context['user'].username).filter(liked__id=guminame)
           context['connected'] = True if result else False

       return context
    
class MypageView(ListView):
    template_name='mypage.html'
    paginate_by=9
    
    def get_queryset(self):
        user=get_current_user(self.request)
        pk_list=Connection.objects.filter(like__username=user).values_list('liked__id', flat=True)
        object_list=[]
        if pk_list:
            for x in pk_list:    
               object_list+=GumiPost.objects.filter(pk=x)
        return object_list          
 
class MakerView(ListView):
    template_name='index.html'
    paginate_by=9
    
    def get_queryset(self):
        maker_id=self.kwargs['maker']
        maker_id=maker_id
        makers=GumiPost.objects.filter(maker=maker_id).order_by('-posted_at')
        return makers     

class CategoryView(ListView):
    template_name='index.html'
    paginate_by=9
    
    def get_queryset(self):
        category_id=self.kwargs['category']
        categories=GumiPost.objects.filter(category=category_id).order_by('-posted_at')
        return categories        
    
              
            
class HardView(ListView):
    template_name='index.html'
    paginate_by=9
    
    def get_queryset(self):
        hard_id=self.kwargs['hard']
        hards=GumiPost.objects.filter(hard=hard_id).order_by('-posted_at')
            
        return hards  

class PowderView(ListView):
    template_name='index.html'
    paginate_by=9
    
    def get_queryset(self):
        pow_id=self.kwargs['maker']
       
        powders=GumiPost.objects.filter(powder=pow_id).order_by('-posted_at')
        return powders 
    
    
  
            

def follow(request,*args, **kwargs):
    like = CustomUser.objects.get(username=request.user.username)
    liked = GumiPost.objects.get(id=kwargs['pk'])
    re, created = Connection.objects.get_or_create(like=like, liked=liked)
    if created==False:
        re.delete()
    return HttpResponseRedirect(reverse_lazy('gumi:gumi_detail', kwargs={'pk': liked.id}))
  
    



class ContactView(FormView):
    template_name='contact.html'
    form_class=ContactForm
    success_url=reverse_lazy('gumi:contact')
    
    def form_valid(self,form):
        form.send_email()
        messages.success(self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)
    
    