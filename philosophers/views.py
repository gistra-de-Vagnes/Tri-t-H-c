from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from .models import Philosopher, PhilosophySchool
from .services import philosopher_api
import random

def home(request):
    # Get a random quote
    quotes = [
        "The unexamined life is not worth living. - Socrates",
        "I think therefore I am. - René Descartes",
        "The life of man is solitary, poor, nasty, brutish, and short. - Thomas Hobbes",
        "Man is condemned to be free. - Jean-Paul Sartre",
        "God is dead. - Friedrich Nietzsche",
        "The greatest happiness of the greatest number. - Jeremy Bentham",
        "It is undesirable to be restrained by a constitution. - Diogenes",
        "The mind is furnished with ideas by experience alone. - John Locke",
        "To be is to be perceived. - George Berkeley",
        "Hell is other people. - Jean-Paul Sartre"
    ]
    
    # Get all philosophy schools for the sidebar
    schools = PhilosophySchool.objects.all()
    
    # Get all philosophers for the main listing
    philosophers = Philosopher.objects.all()[:6]  # Limit to 6 for homepage
    
    context = {
        'quote': random.choice(quotes),
        'schools': schools,
        'philosophers': philosophers,
    }
    return render(request, 'philosophers/home.html', context)

def philosopher_list(request):
    # Try to get data from external API first
    search_query = request.GET.get('search', '')
    school_filter = request.GET.get('school', '')
    country_filter = request.GET.get('country', '')
    period_filter = request.GET.get('period', '')
    
    # For now, we'll use our database, but this is where you'd integrate the API
    philosophers = Philosopher.objects.all()
    schools = PhilosophySchool.objects.all()
    
    # Filtering
    if school_filter:
        philosophers = philosophers.filter(schools__id=school_filter)
    
    if country_filter:
        philosophers = philosophers.filter(country__icontains=country_filter)
    
    if period_filter:
        if period_filter == 'ancient':
            philosophers = philosophers.filter(birth_year__lt=500)
        elif period_filter == 'medieval':
            philosophers = philosophers.filter(birth_year__gte=500, birth_year__lt=1500)
        elif period_filter == 'modern':
            philosophers = philosophers.filter(birth_year__gte=1500, birth_year__lt=1800)
        elif period_filter == 'contemporary':
            philosophers = philosophers.filter(birth_year__gte=1800)
    
    # Search
    if search_query:
        philosophers = philosophers.filter(
            Q(name__icontains=search_query) | 
            Q(bio__icontains=search_query) |
            Q(works__icontains=search_query) |
            Q(key_ideas__icontains=search_query)
        )
    
    # Add pagination
    from django.core.paginator import Paginator
    # Order the queryset to avoid pagination warning
    philosophers = philosophers.order_by('name')
    paginator = Paginator(philosophers, 12)  # Show 12 philosophers per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'philosophers': page_obj,
        'schools': schools,
        'search_query': search_query,
        'school_filter': school_filter,
        'country_filter': country_filter,
        'period_filter': period_filter,
    }
    return render(request, 'philosophers/list.html', context)

def philosopher_detail(request, pk):
    # Try to get from external API first, then fall back to database
    philosopher = get_object_or_404(Philosopher, pk=pk)
    
    # Pre-process works and key_ideas to split them into lists and trim whitespace
    works_list = [work.strip() for work in philosopher.works.split(',')] if philosopher.works else []
    key_ideas_list = [idea.strip() for idea in philosopher.key_ideas.split(',')] if philosopher.key_ideas else []
    
    context = {
        'philosopher': philosopher,
        'works_list': works_list,
        'key_ideas_list': key_ideas_list,
    }
    return render(request, 'philosophers/detail.html', context)

def get_philosopher_data(request, pk):
    """API endpoint to get philosopher data"""
    # Try external API first
    api_data = philosopher_api.get_philosopher(pk)
    if api_data:
        return JsonResponse(api_data)
    
    # Fall back to database
    philosopher = get_object_or_404(Philosopher, pk=pk)
    data = {
        'id': philosopher.id,
        'name': philosopher.name,
        'bio': philosopher.bio,
        'lifespan': philosopher.lifespan,
        'schools': [school.name for school in philosopher.schools.all()],
        'works': philosopher.works.split(',') if philosopher.works else [],
        'key_ideas': philosopher.key_ideas.split(',') if philosopher.key_ideas else [],
        'country': philosopher.country,
        'image_url': philosopher.image_url,
    }
    return JsonResponse(data)

def search_philosophers_api(request):
    """API endpoint for searching philosophers"""
    query = request.GET.get('q', '')
    school = request.GET.get('school', '')
    country = request.GET.get('country', '')
    period = request.GET.get('period', '')
    
    # Try external API first
    api_results = philosopher_api.search_philosophers(
        query=query, 
        school=school, 
        country=country, 
        period=period
    )
    
    if api_results:
        return JsonResponse({'results': api_results})
    
    # Fall back to database
    philosophers = Philosopher.objects.all()
    
    if query:
        philosophers = philosophers.filter(
            Q(name__icontains=query) | 
            Q(bio__icontains=query) |
            Q(works__icontains=query) |
            Q(key_ideas__icontains=query)
        )
    
    if school:
        philosophers = philosophers.filter(schools__name__icontains=school)
    
    if country:
        philosophers = philosophers.filter(country__icontains=country)
    
    if period:
        if period == 'ancient':
            philosophers = philosophers.filter(birth_year__lt=500)
        elif period == 'medieval':
            philosophers = philosophers.filter(birth_year__gte=500, birth_year__lt=1500)
        elif period == 'modern':
            philosophers = philosophers.filter(birth_year__gte=1500, birth_year__lt=1800)
        elif period == 'contemporary':
            philosophers = philosophers.filter(birth_year__gte=1800)
    
    # Limit to 20 results
    philosophers = philosophers[:20]
    
    results = []
    for philosopher in philosophers:
        results.append({
            'id': philosopher.id,
            'name': philosopher.name,
            'bio': philosopher.bio[:200] + '...' if len(philosopher.bio) > 200 else philosopher.bio,
            'schools': [school.name for school in philosopher.schools.all()],
            'country': philosopher.country,
        })
    
    return JsonResponse({'results': results})

def school_list(request):
    """View to display all philosophy schools"""
    schools = PhilosophySchool.objects.all().order_by('name')
    
    # Add philosopher count for each school
    schools_with_counts = []
    for school in schools:
        philosopher_count = school.philosopher_set.count()
        schools_with_counts.append({
            'school': school,
            'philosopher_count': philosopher_count
        })
    
    context = {
        'schools_with_counts': schools_with_counts,
    }
    return render(request, 'philosophers/school_list.html', context)

def school_detail(request, pk):
    """View to display details of a specific philosophy school"""
    school = get_object_or_404(PhilosophySchool, pk=pk)
    philosophers = school.philosopher_set.all().order_by('name')
    
    # Add pagination for philosophers in this school
    from django.core.paginator import Paginator
    paginator = Paginator(philosophers, 12)  # Show 12 philosophers per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'school': school,
        'philosophers': page_obj,
        'page_obj': page_obj,
        'philosopher_count': philosophers.count(),
    }
    return render(request, 'philosophers/school_detail.html', context)