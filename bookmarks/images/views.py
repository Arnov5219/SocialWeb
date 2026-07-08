from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ImageCreateForm


@login_required
def image_create(request):
    if request.method == 'POST':
        # Form is submitted
        form = ImageCreateForm(data=request.POST)

        if form.is_valid():
            # Form data is valid
            cd = form.cleaned_data

            # Create image object but don't save it yet
            new_image = form.save(commit=False)

            # Assign current user to the image
            new_image.user = request.user

            # Save the image to the database
            new_image.save()

            messages.success(request, 'Image added successfully')

            # Redirect to the new image's detail page
            return redirect(new_image.get_absolute_url())

    else:
        # Build the form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)

    return render(
        request,
        'images/image/create.html',
        {
            'section': 'images',
            'form': form,
        }
    )