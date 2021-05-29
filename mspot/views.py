from django.shortcuts import render, get_object_or_404, redirect

from .forms import RegisterForm, CommentForm
from .models import Category, Movie, Comment
from cart.forms import CartAddMovieForm


def movie_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    movies = Movie.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        movies = movies.filter(category=category)
    return render(request, 'movies/list.html', {'category': category, 'categories': categories, 'movies': movies})


def movie_detail(request, id, slug):
    movie = get_object_or_404(Movie, id=id, slug=slug, available=True)
    cart_movie_form = CartAddMovieForm()

    comments = movie.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = movie
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'movies/details.html', {'movie': movie, 'cart_movie_form': cart_movie_form, 'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form,})


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})