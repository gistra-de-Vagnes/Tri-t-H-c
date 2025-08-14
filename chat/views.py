from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import DiscussionCategory, DiscussionTopic, DiscussionReply
from philosophers.models import PhilosophySchool

def discussions_home(request):
    """Display all discussion categories"""
    categories = DiscussionCategory.objects.all()
    recent_topics = DiscussionTopic.objects.order_by('-updated_at')[:5]
    
    context = {
        'categories': categories,
        'recent_topics': recent_topics,
    }
    return render(request, 'discussions/home.html', context)

def category_detail(request, pk):
    """Display topics in a specific category"""
    category = get_object_or_404(DiscussionCategory, pk=pk)
    topics_list = category.topics.all()
    
    # Pagination
    paginator = Paginator(topics_list, 10)
    page_number = request.GET.get('page')
    topics = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'topics': topics,
    }
    return render(request, 'discussions/category_detail.html', context)

def topic_detail(request, pk):
    """Display a topic and its replies"""
    topic = get_object_or_404(DiscussionTopic, pk=pk)
    
    # Increment view count
    topic.views += 1
    topic.save()
    
    replies = topic.replies.all()
    
    context = {
        'topic': topic,
        'replies': replies,
    }
    return render(request, 'discussions/topic_detail.html', context)

@login_required
def create_topic(request, category_pk):
    """Create a new discussion topic"""
    category = get_object_or_404(DiscussionCategory, pk=category_pk)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if title and content:
            topic = DiscussionTopic.objects.create(
                title=title,
                content=content,
                author=request.user,
                category=category
            )
            messages.success(request, 'Topic created successfully!')
            return redirect('discussions:topic_detail', pk=topic.pk)
        else:
            messages.error(request, 'Please fill in all fields.')
    
    context = {
        'category': category,
    }
    return render(request, 'discussions/create_topic.html', context)

@login_required
def create_reply(request, topic_pk):
    """Create a reply to a topic"""
    if request.method == 'POST':
        content = request.POST.get('content')
        
        if content:
            topic = get_object_or_404(DiscussionTopic, pk=topic_pk)
            
            DiscussionReply.objects.create(
                topic=topic,
                author=request.user,
                content=content
            )
            
            # Update topic's updated_at field
            topic.save()
            
            messages.success(request, 'Reply posted successfully!')
        else:
            messages.error(request, 'Please enter your reply.')
    
    return redirect('discussions:topic_detail', pk=topic_pk)