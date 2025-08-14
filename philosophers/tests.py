from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import PhilosophySchool, Philosopher, UserProfile

class PhilosopherModelTest(TestCase):
    def setUp(self):
        # Create a test philosophy school
        self.school = PhilosophySchool.objects.create(
            name="Test School",
            description="A test philosophy school"
        )
        
        # Create a test philosopher
        self.philosopher = Philosopher.objects.create(
            name="Test Philosopher",
            bio="A test philosopher for unit tests",
            birth_year=1900,
            death_year=1980,
            works="Test Work 1, Test Work 2",
            key_ideas="Test Idea 1, Test Idea 2",
            country="Test Country"
        )
        self.philosopher.schools.add(self.school)
        
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create a user profile
        self.profile = UserProfile.objects.create(
            user=self.user,
            favorite_school=self.school
        )

    def test_philosopher_str(self):
        self.assertEqual(str(self.philosopher), "Test Philosopher")
    
    def test_philosopher_lifespan(self):
        self.assertEqual(self.philosopher.lifespan, "1900-1980")
    
    def test_philosophy_school_str(self):
        self.assertEqual(str(self.school), "Test School")
    
    def test_user_profile_str(self):
        self.assertEqual(str(self.profile), "testuser's profile")

class PhilosopherViewTest(TestCase):
    def setUp(self):
        # Create a test philosophy school
        self.school = PhilosophySchool.objects.create(
            name="Stoicism",
            description="Stoic philosophy"
        )
        
        # Create a test philosopher
        self.philosopher = Philosopher.objects.create(
            name="Marcus Aurelius",
            bio="Roman emperor and Stoic philosopher",
            birth_year=121,
            death_year=180
        )
        self.philosopher.schools.add(self.school)
        
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_home_page(self):
        response = self.client.get(reverse('philosophers:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Philosophy")
    
    def test_philosopher_list_page(self):
        response = self.client.get(reverse('philosophers:philosopher_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Philosophers")
    
    def test_philosopher_detail_page(self):
        response = self.client.get(reverse('philosophers:philosopher_detail', args=[self.philosopher.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Marcus Aurelius")
    
    def test_philosopher_api(self):
        response = self.client.get(reverse('philosophers:philosopher_api', args=[self.philosopher.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')
    
    def test_register_page(self):
        response = self.client.get(reverse('philosophers:register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Register")
    
    def test_profile_page_redirects_for_anonymous_user(self):
        response = self.client.get(reverse('philosophers:profile'))
        # Should redirect to login page
        self.assertEqual(response.status_code, 302)
    
    def test_profile_page_for_authenticated_user(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('philosophers:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your Profile")