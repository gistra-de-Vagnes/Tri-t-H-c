from django.core.management.base import BaseCommand
from philosophers.models import PhilosophySchool

class Command(BaseCommand):
    help = 'Add missing philosophy schools'

    def handle(self, *args, **options):
        self.stdout.write('Adding missing philosophy schools...')
        
        schools = [
            {
                'name': 'Political Philosophy',
                'description': 'The study of government, politics, liberty, justice, property, rights, law, and the enforcement of laws by authority. Key concepts include Justice, Liberty, Authority, Rights, Social Contract, and Democracy. Time period: Ancient to Contemporary.'
            },
            {
                'name': 'Humanism',
                'description': 'A philosophical stance that emphasizes the value and agency of human beings, individually and collectively. Key concepts include Human Dignity, Reason, Ethics, Individual Worth, and Secular Values. Time period: Renaissance to Contemporary.'
            },
            {
                'name': 'African Philosophy',
                'description': 'Philosophy produced by African people, philosophy that presents African worldviews, or philosophy that uses distinct African philosophical methods. Key concepts include Ubuntu, Communalism, Oral Tradition, Decolonization, and Pan-Africanism. Time period: Ancient to Contemporary.'
            },
            {
                'name': 'Virtue Ethics',
                'description': 'An approach to ethics that emphasizes the character of the moral agent rather than rules or consequences. Key concepts include Character, Virtue, Flourishing, Practical Wisdom, and Moral Excellence. Time period: Ancient to Contemporary.'
            },
            {
                'name': 'Enlightenment',
                'description': 'An intellectual and philosophical movement that dominated Europe in the 17th and 18th centuries. Key concepts include Reason, Science, Progress, Individual Liberty, and Religious Tolerance. Time period: 17th-18th Century.'
            },
            {
                'name': 'Social Contract Theory',
                'description': 'The theory that persons moral and political obligations are dependent upon a contract or agreement among them. Key concepts include Natural Rights, Consent, Legitimacy, State of Nature, and Civil Society. Time period: 17th-18th Century.'
            },
            {
                'name': 'Philosophy of Science',
                'description': 'A branch of philosophy concerned with the foundations, methods, and implications of science. Key concepts include Scientific Method, Falsifiability, Paradigms, Reductionism, and Empiricism. Time period: 19th Century to Contemporary.'
            },
            {
                'name': 'Feminist Philosophy',
                'description': 'Philosophy that seeks to both critique and re-envision philosophy from within a feminist framework. Key concepts include Gender Equality, Patriarchy, Intersectionality, Care Ethics, and Embodiment. Time period: 18th Century to Contemporary.'
            },
            {
                'name': 'Postcolonial Philosophy',
                'description': 'Philosophy that examines the legacy of colonialism and seeks to understand postcolonial conditions. Key concepts include Decolonization, Cultural Identity, Hybridity, Subaltern, and Orientalism. Time period: 20th Century to Contemporary.'
            },
            {
                'name': 'Critical Theory',
                'description': 'A social theory oriented toward critiquing and changing society as a whole. Key concepts include Ideology Critique, Emancipation, Dialectical Thinking, and Social Justice. Time period: 20th Century to Contemporary.'
            }
        ]
        
        for school_data in schools:
            school, created = PhilosophySchool.objects.get_or_create(
                name=school_data['name'],
                defaults=school_data
            )
            if created:
                self.stdout.write(f'Created school: {school.name}')
            else:
                self.stdout.write(f'School {school.name} already exists')
        
        self.stdout.write(self.style.SUCCESS('Successfully added missing philosophy schools!'))