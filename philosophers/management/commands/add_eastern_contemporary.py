from django.core.management.base import BaseCommand
from philosophers.models import Philosopher, PhilosophySchool

class Command(BaseCommand):
    help = 'Add Eastern and contemporary philosophers to the database'

    def handle(self, *args, **options):
        self.stdout.write('Adding Eastern and contemporary philosophers...')
        
        # Eastern and Contemporary philosophers data
        philosophers_data = [
            # XI. Modern Eastern Philosophy
            {
                'name': 'Zhu Xi',
                'birth_year': 1130,
                'death_year': 1200,
                'country': 'China',
                'schools': ['Neo-Confucianism'],
                'bio': 'Chinese philosopher who synthesized Confucian thought with metaphysical elements, creating Neo-Confucianism that dominated Chinese thought for centuries.',
                'works': 'Commentaries on the Four Books, Reflections on Things at Hand',
                'key_ideas': 'Li (principle) and qi (material force), Investigation of things, Moral cultivation'
            },
            {
                'name': 'Wang Yangming',
                'birth_year': 1472,
                'death_year': 1529,
                'country': 'China',
                'schools': ['Neo-Confucianism'],
                'bio': 'Chinese philosopher who developed the idealist school of Neo-Confucianism, emphasizing the unity of knowledge and action.',
                'works': 'Instructions for Practical Living, Inquiry on the Great Learning',
                'key_ideas': 'Unity of knowledge and action, Innate knowledge, Mind as principle'
            },
            {
                'name': 'Nishida Kitaro',
                'birth_year': 1870,
                'death_year': 1945,
                'country': 'Japan',
                'schools': ['Kyoto School'],
                'bio': 'Japanese philosopher who founded the Kyoto School, combining Eastern and Western philosophical traditions.',
                'works': 'An Inquiry into the Good, Logic of Place, The Logic of Absolutely Nothing',
                'key_ideas': 'Pure experience, Logic of place (basho), Absolute nothingness'
            },
            {
                'name': 'D. T. Suzuki',
                'birth_year': 1870,
                'death_year': 1966,
                'country': 'Japan',
                'schools': ['Buddhism'],
                'bio': 'Japanese Buddhist scholar who introduced Zen Buddhism to the Western world through his writings and lectures.',
                'works': 'Essays in Zen Buddhism, Introduction to Zen Buddhism, The Zen Doctrine of No-Mind',
                'key_ideas': 'Zen enlightenment, Satori, Direct experience'
            },
            {
                'name': 'Mahatma Gandhi',
                'birth_year': 1869,
                'death_year': 1948,
                'country': 'India',
                'schools': ['Political Philosophy'],
                'bio': 'Indian philosopher and political leader who developed the philosophy of non-violent resistance (satyagraha) and applied it to social and political change.',
                'works': 'Hind Swaraj, The Story of My Experiments with Truth',
                'key_ideas': 'Ahimsa (non-violence), Satyagraha (truth-force), Self-rule (swaraj)'
            },
            {
                'name': 'Rabindranath Tagore',
                'birth_year': 1861,
                'death_year': 1941,
                'country': 'India',
                'schools': ['Humanism'],
                'bio': 'Indian philosopher, poet, and Nobel laureate who developed a humanistic philosophy emphasizing universal values and cultural synthesis.',
                'works': 'Gitanjali, The Religion of Man, Nationalism',
                'key_ideas': 'Universal humanism, Cultural synthesis, Creative freedom'
            },
            
            # XII. Important Female Philosophers and Activists
            {
                'name': 'Hypatia',
                'birth_year': 350,
                'death_year': 415,
                'country': 'Egypt',
                'schools': ['Neoplatonism'],
                'bio': 'Ancient Greek mathematician and philosopher in Alexandria, one of the earliest recorded female mathematicians and philosophers.',
                'works': 'Commentaries on Apollonius and Diophantus (lost)',
                'key_ideas': 'Mathematical philosophy, Neoplatonic metaphysics, Rational inquiry'
            },
            {
                'name': 'Mary Wollstonecraft',
                'birth_year': 1759,
                'death_year': 1797,
                'country': 'England',
                'schools': ['Feminism'],
                'bio': 'English writer and women\'s rights advocate who wrote one of the earliest works of feminist philosophy.',
                'works': 'A Vindication of the Rights of Woman, A Vindication of the Rights of Men',
                'key_ideas': 'Women\'s education, Gender equality, Rational feminism'
            },
            {
                'name': 'Judith Butler',
                'birth_year': 1956,
                'death_year': None,
                'country': 'USA',
                'schools': ['Feminism', 'Postmodernism'],
                'bio': 'American philosopher who developed influential theories of gender performativity and queer theory.',
                'works': 'Gender Trouble, Bodies That Matter, Undoing Gender',
                'key_ideas': 'Gender performativity, Queer theory, Subversion of identity'
            },
            {
                'name': 'Martha Nussbaum',
                'birth_year': 1947,
                'death_year': None,
                'country': 'USA',
                'schools': ['Political Philosophy'],
                'bio': 'American philosopher who applies ancient philosophy to contemporary issues, particularly in ethics and political philosophy.',
                'works': 'The Fragility of Goodness, Cultivating Humanity, Creating Capabilities',
                'key_ideas': 'Capabilities approach, Cosmopolitanism, Emotions in ethics'
            },
            {
                'name': 'Frantz Fanon',
                'birth_year': 1925,
                'death_year': 1961,
                'country': 'Martinique/Algeria',
                'schools': ['Postcolonialism'],
                'bio': 'Martinican psychiatrist and philosopher who analyzed the psychological effects of colonization and racism.',
                'works': 'Black Skin, White Masks, The Wretched of the Earth',
                'key_ideas': 'Psychology of oppression, Decolonization, Revolutionary violence'
            },
            {
                'name': 'Kwame Nkrumah',
                'birth_year': 1909,
                'death_year': 1972,
                'country': 'Ghana',
                'schools': ['African Philosophy'],
                'bio': 'Ghanaian political philosopher and first President of Ghana who developed theories of African socialism and pan-Africanism.',
                'works': 'Consciencism, Neo-Colonialism: The Last Stage of Imperialism',
                'key_ideas': 'African socialism, Pan-Africanism, Consciencism'
            },
            {
                'name': 'Léopold Sédar Senghor',
                'birth_year': 1906,
                'death_year': 2001,
                'country': 'Senegal',
                'schools': ['African Philosophy'],
                'bio': 'Senegalese poet and philosopher who developed the concept of Négritude and served as the first President of Senegal.',
                'works': 'Anthologie de la nouvelle poésie nègre et malgache, Liberté',
                'key_ideas': 'Négritude, African cultural identity, Universal civilization'
            },
            
            # XIII. Contemporary Philosophy
            {
                'name': 'Jürgen Habermas',
                'birth_year': 1929,
                'death_year': None,
                'country': 'Germany',
                'schools': ['Critical Theory'],
                'bio': 'German philosopher who developed the theory of communicative action and deliberative democracy.',
                'works': 'The Theory of Communicative Action, The Structural Transformation of the Public Sphere',
                'key_ideas': 'Communicative rationality, Public sphere, Discourse ethics'
            },
            {
                'name': 'Alasdair MacIntyre',
                'birth_year': 1929,
                'death_year': None,
                'country': 'Scotland/USA',
                'schools': ['Virtue Ethics'],
                'bio': 'Scottish-American philosopher who critiqued modern moral philosophy and advocated for a return to Aristotelian virtue ethics.',
                'works': 'After Virtue, Whose Justice? Which Rationality?, Three Rival Versions of Moral Enquiry',
                'key_ideas': 'Critique of modernity, Virtue ethics revival, Narrative unity'
            },
            {
                'name': 'Amartya Sen',
                'birth_year': 1933,
                'death_year': None,
                'country': 'India',
                'schools': ['Political Philosophy'],
                'bio': 'Indian economist and philosopher who developed the capabilities approach to human development and welfare.',
                'works': 'Development as Freedom, The Idea of Justice, Identity and Violence',
                'key_ideas': 'Capabilities approach, Development as freedom, Social choice theory'
            },
            {
                'name': 'Slavoj Žižek',
                'birth_year': 1949,
                'death_year': None,
                'country': 'Slovenia',
                'schools': ['Critical Theory'],
                'bio': 'Slovenian philosopher who combines Lacanian psychoanalysis, German idealism, and Marxist critique in his cultural and political analysis.',
                'works': 'The Sublime Object of Ideology, Violence, The Parallax View',
                'key_ideas': 'Ideology critique, Lacanian Marxism, Cultural analysis'
            },
            {
                'name': 'Cornel West',
                'birth_year': 1953,
                'death_year': None,
                'country': 'USA',
                'schools': ['Pragmatism'],
                'bio': 'American philosopher and political activist who combines pragmatism with social justice advocacy, particularly regarding race and class.',
                'works': 'Race Matters, The American Evasion of Philosophy, Democracy Matters',
                'key_ideas': 'Prophetic pragmatism, Democratic socialism, Racial justice'
            },
            
            # Additional Important Figures
            {
                'name': 'Friedrich Nietzsche',
                'birth_year': 1844,
                'death_year': 1900,
                'country': 'Germany',
                'schools': ['Existentialism'],
                'bio': 'German philosopher who proclaimed the "death of God" and developed ideas about the will to power and the Übermensch.',
                'works': 'Thus Spoke Zarathustra, Beyond Good and Evil, The Genealogy of Morals',
                'key_ideas': 'Will to power, Eternal recurrence, Master-slave morality'
            },
            {
                'name': 'Voltaire',
                'birth_year': 1694,
                'death_year': 1778,
                'country': 'France',
                'schools': ['Enlightenment'],
                'bio': 'French Enlightenment philosopher who advocated for freedom of speech, religion, and civil liberties.',
                'works': 'Candide, Letters on the English, Philosophical Dictionary',
                'key_ideas': 'Religious tolerance, Freedom of speech, Reason over superstition'
            },
            {
                'name': 'Jean-Jacques Rousseau',
                'birth_year': 1712,
                'death_year': 1778,
                'country': 'France',
                'schools': ['Social Contract Theory'],
                'bio': 'French philosopher who influenced the Enlightenment and developed theories of education and social contract.',
                'works': 'The Social Contract, Emile, Discourse on Inequality',
                'key_ideas': 'General will, Natural goodness, Social contract'
            },
        ]
        
        # Add philosophers
        for phil_data in philosophers_data:
            philosopher, created = Philosopher.objects.get_or_create(
                name=phil_data['name'],
                defaults={
                    'birth_year': phil_data.get('birth_year'),
                    'death_year': phil_data.get('death_year'),
                    'country': phil_data['country'],
                    'bio': phil_data['bio'],
                    'works': phil_data['works'],
                    'key_ideas': phil_data['key_ideas'],
                }
            )
            
            if created:
                self.stdout.write(f'Created philosopher: {phil_data["name"]}')
                
                # Add schools
                for school_name in phil_data['schools']:
                    try:
                        school = PhilosophySchool.objects.get(name=school_name)
                        philosopher.schools.add(school)
                    except PhilosophySchool.DoesNotExist:
                        self.stdout.write(f'Warning: School "{school_name}" not found for {phil_data["name"]}')
            else:
                self.stdout.write(f'Philosopher {phil_data["name"]} already exists')
        
        self.stdout.write(self.style.SUCCESS('Successfully added Eastern and contemporary philosophers!'))