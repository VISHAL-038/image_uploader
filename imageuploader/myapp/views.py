from django.shortcuts import render
from .forms import ImageForm
from .models import Image

# Create your views here.
def home(request):
    form = ImageForm()  # Initialize the form first
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ImageForm()  # Reset the form after successful submission

    img = Image.objects.all()  # Fetch all images
    return render(request, 'myapp/home.html', {'img': img, 'form': form})
