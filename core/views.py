from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, LoginForm
from django.db.models import Avg



from .models import District, Trek
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def trek_detail(request, trek_id):
    trek = get_object_or_404(Trek, id=trek_id)
    reviews = trek.reviews.all()
    form = ReviewForm()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')  # force login
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.trek = trek
            review.user = request.user
            review.save()
            return redirect('trek_detail', trek_id=trek.id)
    
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0

    return render(request, 'trek_detail.html', {
        'trek': trek,
        'reviews': reviews,
        'form': form,
        'average_rating': round(average_rating, 1),
    })

@login_required(login_url='login')
def home(request):
    districts = District.objects.all()
    return render(request, 'core/home.html', {'districts': districts})

@login_required(login_url='login')
def district_detail(request, district_id):
    district = get_object_or_404(District, id=district_id)
    treks = district.treks.all()
    return render(request, 'district_detail.html', {'district': district, 'treks': treks})
@login_required(login_url='login')
def trek_type_view(request, type):
    treks = Trek.objects.filter(description__icontains=type)
    return render(request, 'trek_type.html', {'treks': treks, 'type': type})





def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_user = True
            user.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # or 'home_alt'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # or 'home_alt'
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'core/login.html')



def logout_view(request):
    logout(request)
    return redirect('login')  # or use 'home_alt' if needed

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'core/dashboard.html')
 

def home_view(request):
    return render(request, 'core/home.html')