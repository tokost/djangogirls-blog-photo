from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.forms import UserCreationForm   pridane kvoli signup
from .forms import CustomUserCreationForm   # pridane kvoli registracii

from .models import Category, Photo     # pridane kvoli kombinacii

# creates the list of posts on the homepage
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

#what you see when you click on a post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

#creating a new post-- login required, I don't think I need this view anymore
#since I have the one below it now! 
# @login_required
# def post_new(request):
# 	form = PostForm()
# 	return render(request, 'blog/post_edit.html', {'form': form})

@login_required #decorator for securing the site, require login
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
# edit a post that has already been written
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form= PostForm()
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# list of posts that haven't been published yet (drafts)
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts':posts})

# manually publish a post
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

# delete a post
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


# najprv zacal tu vo views.py s def registerUser(request): a potom presiel do html napr. logi_register.html
def registerUser(request):      # urobil toto ako c.1
    page = 'register'
    form = CustomUserCreationForm() # potom toto ako c.2

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
                                            # tento riadok bol iba vo videu
            user=authenticate(request, username=user.username, password=request.POST['password1'])

            if user is not None:
                login(request, user)
                return redirect('post_list')

    context = {'form': form, 'page': page}   # nasledne toto ako c.3 bolo bez ,'page': page
    return render(request, 'blog/login_register.html', context)    # a nakoniec toto ako c.4
                                            # ostatne t.j. rozhodovanie if dal dodatocne
                                            # a potreboval k tomu page (page = 'register')

def render_to_response(CSRF_chyba, ctx):
    pass

class CSRF_chyba:
    pass

def csrf_failure(request, reason=""):
    ctx = {'message': 'some custom messages'}
    return render_to_response(CSRF_chyba, ctx)

#  pridane kvoli kombinacii blogov a foto

@login_required(login_url='login')
def gallery(request):
    user = request.user
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.filter(category__user=user)
    else:
        photos = Photo.objects.filter(
            category__name=category, category__user=user)

    categories = Category.objects.filter(user=user)
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)

@login_required(login_url='login')
def viewPhoto(request, pk):         # vlozi to do sablony na vykreslenie (rendering)
    photo = Photo.objects.get(id=pk)
#    return render(request, 'photos/photo.html', {'photo': photo})
    return render(request, 'photos/photo.html', {'photo': photo})

@login_required(login_url='login')
def addPhoto(request):
    user = request.user

    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)

# delete a photo
#  @login_required
#  def post_remove(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    post.delete()
#    return redirect('post_list')


