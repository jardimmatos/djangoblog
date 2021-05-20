from blog.forms import EmailForm
from django.views import generic
from .models import Post
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail


class PostList(generic.ListView):
    model = Post
    queryset = model.publicados.all().order_by('-publicado_em')
    template_name = "blog/list.html"
    context_object_name = 'posts'
    paginate_by = 2
    allow_empty = True


class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog/detail.html"
    #context_object_name = 'posts'
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


def post_share(request, pk):
    post = get_object_or_404(Post, pk=pk, status='publicado')
    sent = False
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{data['nome']}"
            message = f"Leia o post {post.titulo} em {post_url}\n\n"\
                f"Seu comentário:{data['comentario']}"
            send_mail(subject, message, 'admin@admin.com', [data['email']])
            sent = True

    else:
        form = EmailForm()
    
    return render(request, 'blog/share.html', {'post':post, 'form':form, 'sent':sent})

    

