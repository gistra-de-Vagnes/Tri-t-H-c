#!/usr/bin/env python
"""
Check database content for Philosophy Chat
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'philosophy.settings')
django.setup()

from philosophers.models import Philosopher, PhilosophySchool
from chat.models import DiscussionTopic, DiscussionCategory, DiscussionReply
from django.contrib.auth.models import User

def check_database():
    print("🔍 CHECKING DATABASE CONTENT...")
    print("=" * 50)
    
    # Check Philosophers
    philosophers_count = Philosopher.objects.count()
    print(f"👥 Philosophers: {philosophers_count}")
    
    if philosophers_count > 0:
        print("   Sample philosophers:")
        for p in Philosopher.objects.all()[:5]:
            print(f"   - {p.name} ({p.birth_year}-{p.death_year or 'present'})")
    
    # Check Philosophy Schools
    schools_count = PhilosophySchool.objects.count()
    print(f"\n🏛️ Philosophy Schools: {schools_count}")
    
    if schools_count > 0:
        print("   Sample schools:")
        for s in PhilosophySchool.objects.all()[:5]:
            print(f"   - {s.name}")
    
    # Check Discussion Categories
    categories_count = DiscussionCategory.objects.count()
    print(f"\n💬 Discussion Categories: {categories_count}")
    
    if categories_count > 0:
        print("   Categories:")
        for c in DiscussionCategory.objects.all():
            print(f"   - {c.name}")
    
    # Check Discussion Topics
    topics_count = DiscussionTopic.objects.count()
    print(f"\n📝 Discussion Topics: {topics_count}")
    
    # Check Discussion Replies
    replies_count = DiscussionReply.objects.count()
    print(f"\n💭 Discussion Replies: {replies_count}")
    
    # Check Users
    users_count = User.objects.count()
    print(f"\n👤 Users: {users_count}")
    
    print("\n" + "=" * 50)
    
    # Database readiness assessment
    print("📊 DATABASE READINESS ASSESSMENT:")
    
    if philosophers_count == 0:
        print("❌ No philosophers data - Need to populate")
    elif philosophers_count < 10:
        print("⚠️ Few philosophers - Consider adding more")
    else:
        print("✅ Good philosophers data")
    
    if schools_count == 0:
        print("❌ No philosophy schools - Need to populate")
    elif schools_count < 5:
        print("⚠️ Few schools - Consider adding more")
    else:
        print("✅ Good schools data")
    
    if categories_count == 0:
        print("❌ No discussion categories - Need to create")
    else:
        print("✅ Discussion categories ready")
    
    # Overall assessment
    total_content = philosophers_count + schools_count + categories_count
    
    print(f"\n🎯 OVERALL ASSESSMENT:")
    if total_content == 0:
        print("❌ EMPTY DATABASE - Need to populate all data")
        return False
    elif total_content < 20:
        print("⚠️ MINIMAL DATA - Functional but could use more content")
        return True
    else:
        print("✅ GOOD DATABASE - Ready for deployment")
        return True

def suggest_improvements():
    print("\n💡 SUGGESTIONS FOR IMPROVEMENT:")
    
    philosophers_count = Philosopher.objects.count()
    schools_count = PhilosophySchool.objects.count()
    categories_count = DiscussionCategory.objects.count()
    
    if philosophers_count < 50:
        print(f"📚 Add more philosophers (current: {philosophers_count}, recommended: 50+)")
        print("   - Ancient philosophers (Socrates, Plato, Aristotle)")
        print("   - Modern philosophers (Descartes, Kant, Nietzsche)")
        print("   - Contemporary philosophers")
    
    if schools_count < 10:
        print(f"🏛️ Add more philosophy schools (current: {schools_count}, recommended: 10+)")
        print("   - Stoicism, Existentialism, Utilitarianism")
        print("   - Phenomenology, Pragmatism, Analytic Philosophy")
    
    if categories_count < 5:
        print(f"💬 Add more discussion categories (current: {categories_count}, recommended: 5+)")
        print("   - Ethics, Metaphysics, Epistemology")
        print("   - Political Philosophy, Philosophy of Mind")

def create_sample_data():
    print("\n🔧 CREATING SAMPLE DATA...")
    
    # Create sample philosophy schools if none exist
    if PhilosophySchool.objects.count() == 0:
        schools_data = [
            ("Stoicism", "Ancient Greek school emphasizing virtue, logic, and living in accordance with nature."),
            ("Existentialism", "Philosophy emphasizing individual existence, freedom and choice."),
            ("Utilitarianism", "Ethical theory that determines right from wrong by focusing on outcomes."),
            ("Phenomenology", "Study of structures of experience and consciousness."),
            ("Analytic Philosophy", "Style of philosophy that emphasizes clarity and logical rigor."),
        ]
        
        for name, description in schools_data:
            PhilosophySchool.objects.create(name=name, description=description)
        print(f"✅ Created {len(schools_data)} philosophy schools")
    
    # Create sample philosophers if none exist
    if Philosopher.objects.count() == 0:
        philosophers_data = [
            ("Socrates", -470, -399, "Ancient Greek philosopher known for the Socratic method."),
            ("Plato", -428, -348, "Student of Socrates, founded the Academy in Athens."),
            ("Aristotle", -384, -322, "Student of Plato, tutor to Alexander the Great."),
            ("Marcus Aurelius", 121, 180, "Roman Emperor and Stoic philosopher."),
            ("Immanuel Kant", 1724, 1804, "German philosopher of the Enlightenment."),
            ("Friedrich Nietzsche", 1844, 1900, "German philosopher and cultural critic."),
            ("Jean-Paul Sartre", 1905, 1980, "French existentialist philosopher."),
            ("Simone de Beauvoir", 1908, 1986, "French existentialist philosopher and feminist."),
        ]
        
        stoicism = PhilosophySchool.objects.filter(name="Stoicism").first()
        existentialism = PhilosophySchool.objects.filter(name="Existentialism").first()
        
        for name, birth, death, bio in philosophers_data:
            school = None
            if name in ["Marcus Aurelius"]:
                school = stoicism
            elif name in ["Jean-Paul Sartre", "Simone de Beauvoir"]:
                school = existentialism
                
            Philosopher.objects.create(
                name=name,
                birth_year=birth,
                death_year=death if death > 0 else None,
                biography=bio,
                school=school
            )
        print(f"✅ Created {len(philosophers_data)} philosophers")
    
    # Create sample discussion categories if none exist
    if DiscussionCategory.objects.count() == 0:
        categories_data = [
            ("Ethics", "Discussions about moral philosophy and ethical dilemmas."),
            ("Metaphysics", "Discussions about the nature of reality and existence."),
            ("Epistemology", "Discussions about knowledge, truth, and belief."),
            ("Political Philosophy", "Discussions about government, justice, and society."),
            ("Philosophy of Mind", "Discussions about consciousness, mental states, and cognition."),
        ]
        
        for name, description in categories_data:
            DiscussionCategory.objects.create(name=name, description=description)
        print(f"✅ Created {len(categories_data)} discussion categories")

if __name__ == "__main__":
    is_ready = check_database()
    
    if not is_ready:
        print("\n🔧 Would you like to create sample data? (This will populate your database)")
        create_sample_data()
        print("\n" + "=" * 50)
        print("🔄 RECHECKING DATABASE AFTER ADDING SAMPLE DATA...")
        is_ready = check_database()
    
    suggest_improvements()
    
    print(f"\n🚀 DEPLOYMENT READY: {'YES' if is_ready else 'NO'}")
    
    if is_ready:
        print("\n✅ Your database has sufficient content for deployment!")
        print("🌐 You can now deploy your website to production.")
    else:
        print("\n❌ Your database needs more content before deployment.")
        print("🔧 Run this script again to add sample data.")