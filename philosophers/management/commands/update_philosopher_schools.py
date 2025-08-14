from django.core.management.base import BaseCommand
from philosophers.models import Philosopher, PhilosophySchool

class Command(BaseCommand):
    help = 'Update philosophers with their correct schools'

    def handle(self, *args, **options):
        self.stdout.write('Updating philosopher schools...')
        
        # Get the schools
        political_philosophy = PhilosophySchool.objects.get(name='Political Philosophy')
        humanism = PhilosophySchool.objects.get(name='Humanism')
        african_philosophy = PhilosophySchool.objects.get(name='African Philosophy')
        virtue_ethics = PhilosophySchool.objects.get(name='Virtue Ethics')
        enlightenment = PhilosophySchool.objects.get(name='Enlightenment')
        social_contract = PhilosophySchool.objects.get(name='Social Contract Theory')
        
        # Update philosophers with their schools
        updates = [
            ('Mahatma Gandhi', [political_philosophy]),
            ('Rabindranath Tagore', [humanism]),
            ('Martha Nussbaum', [political_philosophy]),
            ('Kwame Nkrumah', [african_philosophy]),
            ('Léopold Sédar Senghor', [african_philosophy]),
            ('Alasdair MacIntyre', [virtue_ethics]),
            ('Amartya Sen', [political_philosophy]),
            ('Voltaire', [enlightenment]),
            ('Jean-Jacques Rousseau', [social_contract]),
        ]
        
        for philosopher_name, schools in updates:
            try:
                philosopher = Philosopher.objects.get(name=philosopher_name)
                for school in schools:
                    philosopher.schools.add(school)
                self.stdout.write(f'Updated {philosopher_name} with schools: {", ".join([s.name for s in schools])}')
            except Philosopher.DoesNotExist:
                self.stdout.write(f'Philosopher {philosopher_name} not found')
        
        self.stdout.write(self.style.SUCCESS('Successfully updated philosopher schools!'))