from django.core.management.base import BaseCommand
from chat.models import DiscussionCategory
from philosophers.models import PhilosophySchool

class Command(BaseCommand):
    help = 'Initialize discussion categories based on philosophy schools'

    def handle(self, *args, **options):
        self.stdout.write('Creating discussion categories...')
        
        # Create general categories
        categories_data = [
            {
                'name': 'General Philosophy',
                'description': 'General philosophical discussions and questions'
            },
            {
                'name': 'Ethics and Morality',
                'description': 'Discussions about right and wrong, moral philosophy'
            },
            {
                'name': 'Metaphysics',
                'description': 'Questions about reality, existence, and the nature of being'
            },
            {
                'name': 'Epistemology',
                'description': 'Discussions about knowledge, truth, and belief'
            },
            {
                'name': 'Philosophy of Mind',
                'description': 'Consciousness, free will, and the nature of mind'
            },
        ]
        
        for category_data in categories_data:
            category, created = DiscussionCategory.objects.get_or_create(
                name=category_data['name'],
                defaults={'description': category_data['description']}
            )
            if created:
                self.stdout.write(f'Created category: {category.name}')
        
        # Create categories for each philosophy school
        schools = PhilosophySchool.objects.all()
        for school in schools:
            if school:
                category, created = DiscussionCategory.objects.get_or_create(
                    name=f'{school.name} Discussions',
                    defaults={
                        'description': f'Discussions about {school.name} philosophy and related topics',
                        'school': school
                    }
                )
                if created:
                    self.stdout.write(f'Created school category: {category.name}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully initialized discussion categories!')
        )