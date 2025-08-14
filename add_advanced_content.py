#!/usr/bin/env python
"""
Add advanced philosophical schools and contemporary philosophers
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'philosophy.settings')
django.setup()

from philosophers.models import Philosopher, PhilosophySchool
from chat.models import DiscussionCategory

def add_advanced_schools():
    """Add lesser-known but academically important philosophical schools"""
    
    advanced_schools = [
        # Byzantine Philosophy
        ("Byzantine Philosophy", "Medieval Greek philosophical tradition that preserved and developed ancient Greek philosophy within the Byzantine Empire."),
        
        # Ancient Indian Philosophy
        ("Nyaya", "Ancient Indian school of philosophy focused on logic, epistemology, and the means of acquiring knowledge."),
        ("Samkhya", "One of the oldest philosophical systems in India, emphasizing dualism between consciousness and matter."),
        ("Vedanta", "Hindu philosophical tradition focused on the interpretation of the Upanishads and the nature of ultimate reality."),
        ("Mimamsa", "Hindu philosophical school concerned with the interpretation of Vedic texts and ritual action."),
        ("Charvaka", "Ancient Indian materialist and atheistic school of philosophy, emphasizing empiricism and hedonism."),
        
        # Islamic Philosophy
        ("Islamic Peripatetic", "Islamic philosophical tradition following Aristotelian philosophy, developed by scholars like Al-Farabi and Averroes."),
        ("Illuminationist Philosophy", "Islamic philosophical school founded by Suhrawardi, emphasizing mystical illumination and light metaphysics."),
        ("Sufi Metaphysics", "Mystical dimension of Islamic philosophy focusing on spiritual realization and the nature of divine reality."),
        
        # Modern East Asian Philosophy
        ("Kyoto School", "Japanese philosophical movement that developed a unique synthesis of Eastern and Western philosophical traditions."),
        ("New Confucianism", "Modern Chinese philosophical movement that seeks to revitalize Confucian thought in dialogue with Western philosophy."),
        
        # Medieval Latin Philosophy
        ("Medieval Latin Philosophy", "Scholastic philosophical tradition of medieval Europe, synthesizing Aristotelian philosophy with Christian theology."),
        
        # Contemporary Critical Theories
        ("Postcolonialism", "Critical theory examining the cultural, political, and economic legacy of colonialism and imperialism."),
        ("Postmodern Feminism", "Feminist philosophical approach that challenges traditional gender categories and embraces plurality of identities."),
        
        # Modern Philosophy of Mind
        ("4E Cognition", "Contemporary approach to cognitive science emphasizing embodied, embedded, enacted, and extended cognition."),
        ("Extended Mind Theory", "Theory proposing that cognitive processes can extend beyond the boundaries of the individual brain."),
    ]
    
    added_count = 0
    for name, description in advanced_schools:
        school, created = PhilosophySchool.objects.get_or_create(
            name=name,
            defaults={'description': description}
        )
        if created:
            added_count += 1
            print(f"✅ Added school: {name}")
        else:
            print(f"⏭️ School already exists: {name}")
    
    print(f"\n📚 Added {added_count} new philosophical schools")
    return added_count

def add_contemporary_philosophers():
    """Add contemporary and influential philosophers"""
    
    # Get relevant schools
    postmodern_feminism = PhilosophySchool.objects.filter(name="Postmodern Feminism").first()
    philosophy_of_mind = PhilosophySchool.objects.filter(name="Philosophy of Mind").first()
    extended_mind = PhilosophySchool.objects.filter(name="Extended Mind Theory").first()
    postcolonialism = PhilosophySchool.objects.filter(name="Postcolonialism").first()
    utilitarianism = PhilosophySchool.objects.filter(name="Utilitarianism").first()
    kyoto_school = PhilosophySchool.objects.filter(name="Kyoto School").first()
    new_confucianism = PhilosophySchool.objects.filter(name="New Confucianism").first()
    
    contemporary_philosophers = [
        # Martha Nussbaum
        ("Martha Nussbaum", 1947, None, 
         "American philosopher known for her work in political philosophy, ethics, and ancient philosophy. Developer of the capabilities approach to human development.",
         []),
        
        # Judith Butler
        ("Judith Butler", 1956, None,
         "American philosopher and gender theorist whose work has influenced political philosophy, ethics, and feminist theory. Known for theory of gender performativity.",
         [postmodern_feminism] if postmodern_feminism else []),
        
        # Thomas Nagel
        ("Thomas Nagel", 1937, None,
         "American philosopher known for his work in moral and political philosophy, philosophy of mind, and epistemology. Famous for 'What Is It Like to Be a Bat?'",
         [philosophy_of_mind] if philosophy_of_mind else []),
        
        # David Chalmers
        ("David Chalmers", 1966, None,
         "Australian philosopher and cognitive scientist known for formulating the 'hard problem of consciousness' and his work on philosophy of mind.",
         [extended_mind] if extended_mind else []),
        
        # Amartya Sen
        ("Amartya Sen", 1933, None,
         "Indian economist and philosopher known for his work on welfare economics, social choice theory, and development economics. Nobel Prize winner.",
         []),
        
        # Slavoj Žižek
        ("Slavoj Žižek", 1949, None,
         "Slovenian philosopher and cultural critic known for his work in psychoanalysis, political theory, and cultural criticism.",
         []),
        
        # Peter Singer
        ("Peter Singer", 1946, None,
         "Australian moral philosopher known for his work in applied ethics, particularly animal rights and effective altruism.",
         [utilitarianism] if utilitarianism else []),
        
        # Cornel West
        ("Cornel West", 1953, None,
         "American philosopher, political activist, and social critic known for his work in political philosophy, race theory, and Christian philosophy.",
         [postcolonialism] if postcolonialism else []),
        
        # Additional important contemporary figures
        ("Gayatri Spivak", 1942, None,
         "Indian literary theorist and philosopher known for her work in postcolonial theory, feminism, and deconstruction.",
         [postcolonialism] if postcolonialism else []),
        
        ("Kwame Anthony Appiah", 1954, None,
         "Ghanaian-American philosopher known for his work in political and moral theory, philosophy of language, and African philosophy.",
         [postcolonialism] if postcolonialism else []),
        
        # Historical figures from underrepresented traditions
        ("Al-Ghazali", 1058, 1111,
         "Persian Islamic philosopher, theologian, and mystic. One of the most influential Muslim philosophers, known for 'The Revival of the Religious Sciences'.",
         []),
        
        ("Nagarjuna", 150, 250,
         "Indian Buddhist philosopher and founder of the Madhyamaka school of Mahayana Buddhism. Known for his philosophy of emptiness (śūnyatā).",
         []),
        
        ("Nishida Kitaro", 1870, 1945,
         "Japanese philosopher and founder of the Kyoto School. Known for his concept of 'absolute nothingness' and East-West philosophical synthesis.",
         [kyoto_school] if kyoto_school else []),
        
        ("Zhu Xi", 1130, 1200,
         "Chinese philosopher during the Song Dynasty, most influential Neo-Confucian philosopher. Synthesized Confucian ethics with metaphysical speculation.",
         [new_confucianism] if new_confucianism else []),
    ]
    
    added_count = 0
    for name, birth_year, death_year, bio, schools in contemporary_philosophers:
        philosopher, created = Philosopher.objects.get_or_create(
            name=name,
            defaults={
                'birth_year': birth_year,
                'death_year': death_year,
                'bio': bio,
            }
        )
        if created:
            # Add schools (ManyToMany relationship)
            for school in schools:
                if school:
                    philosopher.schools.add(school)
            added_count += 1
            print(f"✅ Added philosopher: {name}")
        else:
            print(f"⏭️ Philosopher already exists: {name}")
    
    print(f"\n👥 Added {added_count} new philosophers")
    return added_count

def add_advanced_discussion_categories():
    """Add discussion categories for advanced topics"""
    
    advanced_categories = [
        ("Byzantine Philosophy", "Discussions about medieval Greek philosophical traditions and their influence."),
        ("Indian Philosophy", "Discussions about ancient and modern Indian philosophical schools and thinkers."),
        ("Islamic Philosophy", "Discussions about Islamic philosophical traditions and their contributions to world philosophy."),
        ("East Asian Philosophy", "Discussions about Chinese, Japanese, and Korean philosophical traditions."),
        ("Postcolonial Philosophy", "Discussions about philosophy from postcolonial perspectives and decolonizing philosophy."),
        ("Contemporary Philosophy of Mind", "Discussions about modern theories of consciousness, cognition, and mental phenomena."),
        ("Feminist Philosophy", "Discussions about feminist philosophical theories and gender-related philosophical issues."),
        ("Applied Ethics", "Discussions about practical ethical issues in medicine, environment, technology, and society."),
    ]
    
    added_count = 0
    for name, description in advanced_categories:
        category, created = DiscussionCategory.objects.get_or_create(
            name=name,
            defaults={'description': description}
        )
        if created:
            added_count += 1
            print(f"✅ Added category: {name}")
        else:
            print(f"⏭️ Category already exists: {name}")
    
    print(f"\n💬 Added {added_count} new discussion categories")
    return added_count

def main():
    print("🔧 ADDING ADVANCED PHILOSOPHICAL CONTENT...")
    print("=" * 60)
    
    # Add advanced schools
    print("\n📚 Adding Advanced Philosophical Schools:")
    schools_added = add_advanced_schools()
    
    # Add contemporary philosophers
    print("\n👥 Adding Contemporary & Underrepresented Philosophers:")
    philosophers_added = add_contemporary_philosophers()
    
    # Add advanced discussion categories
    print("\n💬 Adding Advanced Discussion Categories:")
    categories_added = add_advanced_discussion_categories()
    
    print("\n" + "=" * 60)
    print("📊 SUMMARY:")
    print(f"✅ Schools added: {schools_added}")
    print(f"✅ Philosophers added: {philosophers_added}")
    print(f"✅ Categories added: {categories_added}")
    print(f"🎯 Total new content: {schools_added + philosophers_added + categories_added}")
    
    # Final database stats
    total_schools = PhilosophySchool.objects.count()
    total_philosophers = Philosopher.objects.count()
    total_categories = DiscussionCategory.objects.count()
    
    print(f"\n🌟 UPDATED DATABASE STATS:")
    print(f"📚 Total Schools: {total_schools}")
    print(f"👥 Total Philosophers: {total_philosophers}")
    print(f"💬 Total Categories: {total_categories}")
    print(f"🎊 Grand Total: {total_schools + total_philosophers + total_categories} records")
    
    print(f"\n🚀 Your database is now EXTREMELY comprehensive!")
    print("🌍 Includes underrepresented traditions from around the world")
    print("🔬 Features cutting-edge contemporary philosophy")
    print("🎓 Academic-level content that most websites lack")

if __name__ == "__main__":
    main()