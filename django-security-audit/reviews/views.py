from django.shortcuts import render, redirect

from django.views.decorators.cache import cache_page

from .models import Review
from .forms import ReviewForm


# Cache this page for 15 minutes
# This reduces repeated database queries
# Risk: newly submitted reviews may not appear immediately
@cache_page(60 * 15)
def index(request):

    if request.method == 'POST':

        form = ReviewForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('index')

    else:

        form = ReviewForm()

    reviews = Review.objects.all().order_by('-created_at')

    return render(request, 'reviews/index.html', {
        'form': form,
        'reviews': reviews
    })