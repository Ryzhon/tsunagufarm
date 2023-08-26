from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404, redirect
from ..models import Recipe
from ..form import CommentForm
# @login_required
def recipe_all(request):
    recipes = Recipe.objects.all()
    context = {
        'page_title': 'レシピ',
        "recipes": recipes,
    }
    return render(request, 'recipe.html', context)

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    comments = recipe.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.user = request.user
            comment.save()
            return redirect('recipe_detail', id=id)
    else:
        form = CommentForm()

    context = {
        'page_title': "レシピ",
        'recipe': recipe,
        'comments': comments,
        'form': form,
    }

    return render(request, 'recipe_detail.html', context)
