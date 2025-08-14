#!/usr/bin/env python
"""
Script to initialize the database with sample data for Philosophy Forum.
"""

import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'philosophy.settings')
django.setup()

from philosophers.models import PhilosophySchool, Philosopher, UserProfile
from django.contrib.auth.models import User

def create_sample_data():
    print("Creating sample philosophy schools...")
    
    # Create philosophy schools
    schools_data = [
        {"name": "Stoicism", "description": "A school of Hellenistic philosophy that teaches the development of self-control and fortitude as a means of overcoming destructive emotions."},
        {"name": "Existentialism", "description": "A philosophical movement that emphasizes individual existence, freedom, and choice."},
        {"name": "Rationalism", "description": "A philosophical view that regards reason as the chief source and test of knowledge."},
        {"name": "Empiricism", "description": "A theory that states that knowledge comes primarily from sensory experience."},
        {"name": "Ancient Greek Philosophy", "description": "The foundational period of Western philosophy, centered on ancient Greece."},
        {"name": "Analytic Philosophy", "description": "A philosophical movement that emphasizes clarity and argumentation, often using formal logic."},
    ]
    
    schools = []
    for school_data in schools_data:
        school, created = PhilosophySchool.objects.get_or_create(
            name=school_data["name"],
            defaults={"description": school_data["description"]}
        )
        schools.append(school)
        if created:
            print(f"Created school: {school.name}")
    
    print("\nCreating sample philosophers...")
    
    # Create philosophers
    philosophers_data = [
        {
            "name": "Marcus Aurelius",
            "bio": "Roman emperor and Stoic philosopher. Author of 'Meditations', a series of personal writings addressing how to maintain inner peace and virtue.",
            "birth_year": 121,
            "death_year": 180,
            "schools": [schools[0]],  # Stoicism
            "works": "Meditations, Apologies",
            "key_ideas": "Virtue, self-control, acceptance of fate, impermanence",
            "country": "Roman Empire",
            "image_url": ""
        },
        {
            "name": "Jean-Paul Sartre",
            "bio": "French philosopher and writer who was one of the key figures in the philosophy of existentialism. He argued that people are 'condemned to be free' and must create their own meaning.",
            "birth_year": 1905,
            "death_year": 1980,
            "schools": [schools[1]],  # Existentialism
            "works": "Being and Nothingness, Existentialism is a Humanism, Nausea",
            "key_ideas": "Existence precedes essence, radical freedom, bad faith",
            "country": "France",
            "image_url": ""
        },
        {
            "name": "René Descartes",
            "bio": "French philosopher, mathematician, and scientist who is often called the father of modern philosophy. He is known for the dictum 'Cogito ergo sum' (I think, therefore I am).",
            "birth_year": 1596,
            "death_year": 1650,
            "schools": [schools[2]],  # Rationalism
            "works": "Meditations on First Philosophy, Discourse on the Method",
            "key_ideas": "Methodological skepticism, mind-body dualism, foundationalism",
            "country": "France",
            "image_url": ""
        },
        {
            "name": "David Hume",
            "bio": "Scottish philosopher, historian, economist, and essayist who is known especially for his philosophical empiricism and skepticism. He argued that human knowledge is based on experience.",
            "birth_year": 1711,
            "death_year": 1776,
            "schools": [schools[3]],  # Empiricism
            "works": "A Treatise of Human Nature, An Enquiry Concerning Human Understanding",
            "key_ideas": "Empiricism, skepticism, problem of induction, is-ought problem",
            "country": "Scotland",
            "image_url": ""
        },
        {
            "name": "Socrates",
            "bio": "Classical Greek philosopher credited as one of the founders of Western philosophy. He is known for his contribution to the field of ethics and the Socratic method of questioning.",
            "birth_year": 470,
            "death_year": 399,
            "schools": [schools[4]],  # Ancient Greek Philosophy
            "works": "None (knowledge comes from students like Plato)",
            "key_ideas": "Socratic method, know thyself, the unexamined life is not worth living",
            "country": "Ancient Greece",
            "image_url": ""
        },
        {
            "name": "Ludwig Wittgenstein",
            "bio": "Austrian-British philosopher who worked primarily in logic, the philosophy of mathematics, the philosophy of mind, and the philosophy of language. He is considered one of the most influential philosophers of the 20th century.",
            "birth_year": 1889,
            "death_year": 1951,
            "schools": [schools[5]],  # Analytic Philosophy
            "works": "Tractatus Logico-Philosophicus, Philosophical Investigations",
            "key_ideas": "Language games, picture theory of language, ordinary language philosophy",
            "country": "Austria/UK",
            "image_url": ""
        },
    ]
    
    philosophers = []
    for philosopher_data in philosophers_data:
        # Remove schools from data for creation
        schools_list = philosopher_data.pop("schools", [])
        
        # Create or get philosopher
        philosopher, created = Philosopher.objects.get_or_create(
            name=philosopher_data["name"],
            defaults=philosopher_data
        )
        
        # Add schools
        if schools_list:
            philosopher.schools.set(schools_list)
            philosopher.save()
        
        philosophers.append(philosopher)
        if created:
            print(f"Created philosopher: {philosopher.name}")
    
    print("\nCreating sample users...")
    
    # Create a sample user
    try:
        user = User.objects.get(username="philosopher")
        print("Sample user 'philosopher' already exists")
    except User.DoesNotExist:
        user = User.objects.create_user(
            username="philosopher",
            password="philosopher123"
        )
        print("Created sample user: philosopher")
        
        # Create user profile
        profile, created = UserProfile.objects.get_or_create(
            user=user,
            defaults={"favorite_school": schools[0]}
        )
        if created:
            print("Created profile for sample user")
    
    print("\nSample data initialization complete!")

if __name__ == "__main__":
    create_sample_data()