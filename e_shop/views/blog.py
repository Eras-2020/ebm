from django.views import View
from django.shortcuts import render, redirect
from e_shop.models.blog import Blog, Comment, CommentForm


class BlogView(View):
    def get(self, request):
        blogs = Blog.get_all_blogs()

        return render(request, 'e_shop/blog.html', {"blogs": blogs})


class BlogDetails(View):
    def get(self, request, id):
        blog = Blog.objects.get(id=id)
        return render(request, "e_shop/blog_details.html", {"blog": blog})


def comment(request, id):
    topic = Blog.objects.get(id=id)
    comments = Comment.objects.filter(topic=topic).order_by('-created_on')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comm = Comment(
                name=request.user,
                comment=form.cleaned_data["comment"],
                topic=topic,
            )
            comm.save()
            return redirect('e_shop:comment', id=id)
    context = {
        'topic': topic,
        'comments': comments,
        'form': form,
    }
    return render(request, "e_shop/comment.html", context)
