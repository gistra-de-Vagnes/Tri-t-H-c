from django.core.management.base import BaseCommand
from philosophers.models import Philosopher, PhilosophySchool

class Command(BaseCommand):
    help = 'Add comprehensive list of philosophers to the database'

    def handle(self, *args, **options):
        self.stdout.write('Adding comprehensive list of philosophers...')
        
        # First, create all the philosophy schools
        schools_data = [
            # Ancient Greek Schools
            ('Pre-Socratic', 'Early Greek philosophers before Socrates'),
            ('Classical Greek', 'Classical period of Greek philosophy'),
            ('Hellenistic', 'Post-Aristotelian Greek philosophy'),
            ('Neoplatonism', 'Revival and development of Platonic philosophy'),
            
            # Eastern Schools
            ('Confucianism', 'Chinese ethical and philosophical system'),
            ('Taoism', 'Chinese philosophical tradition emphasizing harmony with the Tao'),
            ('Buddhism', 'Indian religion and philosophy founded by Buddha'),
            ('Jainism', 'Indian religion emphasizing non-violence'),
            ('Vedanta', 'Hindu philosophical tradition'),
            ('Madhyamaka', 'Buddhist philosophical school'),
            ('Neo-Confucianism', 'Revival of Confucian philosophy'),
            ('Kyoto School', 'Japanese philosophical movement'),
            
            # Medieval Schools
            ('Christian Philosophy', 'Medieval Christian philosophical tradition'),
            ('Islamic Philosophy', 'Medieval Islamic philosophical tradition'),
            ('Jewish Philosophy', 'Medieval Jewish philosophical tradition'),
            ('Scholasticism', 'Medieval method of philosophical inquiry'),
            
            # Modern Schools
            ('Renaissance Humanism', 'Renaissance philosophical movement'),
            ('Rationalism', 'Philosophical method emphasizing reason'),
            ('Empiricism', 'Philosophical method emphasizing experience'),
            ('German Idealism', 'German philosophical movement'),
            ('Utilitarianism', 'Ethical theory of greatest happiness'),
            ('Existentialism', 'Philosophy emphasizing individual existence'),
            ('Phenomenology', 'Study of consciousness and experience'),
            ('Analytic Philosophy', 'Philosophical tradition emphasizing logical analysis'),
            ('Pragmatism', 'American philosophical tradition'),
            ('Positivism', 'Philosophical theory of scientific knowledge'),
            ('Postmodernism', 'Late 20th century philosophical movement'),
            ('Feminism', 'Philosophy advocating for women\'s rights'),
            ('Critical Theory', 'Social theory and philosophy'),
            ('Postcolonialism', 'Critical analysis of colonialism'),
        ]
        
        # Create schools
        for name, description in schools_data:
            school, created = PhilosophySchool.objects.get_or_create(
                name=name,
                defaults={'description': description}
            )
            if created:
                self.stdout.write(f'Created school: {name}')
        
        # Now add all philosophers
        philosophers_data = [
            # I. Ancient (Before CE - around 6th century CE)
            {
                'name': 'Thales',
                'birth_year': -624,
                'death_year': -546,
                'country': 'Greece',
                'schools': ['Pre-Socratic'],
                'bio': 'Often considered the first philosopher in the Greek tradition. Thales sought natural explanations for phenomena and laid the foundation for natural philosophy. He believed water was the fundamental principle of all things.',
                'works': 'No written works survive, known through later testimonies',
                'key_ideas': 'Water as fundamental principle, Natural explanations for phenomena, Mathematical theorems'
            },
            {
                'name': 'Pythagoras',
                'birth_year': -570,
                'death_year': -495,
                'country': 'Greece',
                'schools': ['Pre-Socratic'],
                'bio': 'Greek philosopher and mathematician who founded the Pythagorean school. He emphasized the importance of numbers and mathematical relationships in understanding the universe.',
                'works': 'No authentic writings survive',
                'key_ideas': 'Mathematics and cosmic structure, Transmigration of souls, Harmony of the spheres'
            },
            {
                'name': 'Heraclitus',
                'birth_year': -535,
                'death_year': -475,
                'country': 'Greece',
                'schools': ['Pre-Socratic'],
                'bio': 'Known as the "Obscure" philosopher, Heraclitus emphasized the constant flux of all things. His famous saying "panta rhei" (everything flows) captures his view of reality as perpetual change.',
                'works': 'On Nature (fragments survive)',
                'key_ideas': 'Constant change (panta rhei), Unity of opposites, Logos as cosmic principle'
            },
            {
                'name': 'Parmenides',
                'birth_year': -515,
                'death_year': -450,
                'country': 'Greece',
                'schools': ['Pre-Socratic'],
                'bio': 'Founder of the Eleatic school, Parmenides argued for the unity and unchanging nature of being, directly opposing Heraclitus. His work laid important groundwork for later metaphysics.',
                'works': 'On Nature (poem, fragments survive)',
                'key_ideas': 'Being is one and unchanging, Distinction between appearance and reality, Logic of being'
            },
            {
                'name': 'Democritus',
                'birth_year': -460,
                'death_year': -370,
                'country': 'Greece',
                'schools': ['Pre-Socratic'],
                'bio': 'Known as the "laughing philosopher," Democritus developed the atomic theory of matter, proposing that everything is composed of indivisible atoms moving in void.',
                'works': 'Over 70 works attributed (fragments survive)',
                'key_ideas': 'Atomic theory of matter, Materialism, Determinism'
            },
            {
                'name': 'Epicurus',
                'birth_year': -341,
                'death_year': -270,
                'country': 'Greece',
                'schools': ['Hellenistic'],
                'bio': 'Founder of Epicureanism, he taught that the highest good is pleasure, but advocated for a refined hedonism based on wisdom and moderation.',
                'works': 'Letter to Menoeceus, Principal Doctrines',
                'key_ideas': 'Refined hedonism, Ataraxia (tranquility), Atomic materialism'
            },
            {
                'name': 'Zeno of Citium',
                'birth_year': -334,
                'death_year': -262,
                'country': 'Cyprus/Greece',
                'schools': ['Hellenistic'],
                'bio': 'Founder of Stoicism, Zeno taught that virtue is the only true good and that we should accept fate while focusing on what is within our control.',
                'works': 'Republic, On Nature (lost)',
                'key_ideas': 'Virtue through reason, Acceptance of fate, Living according to nature'
            },
            {
                'name': 'Pyrrho',
                'birth_year': -360,
                'death_year': -270,
                'country': 'Greece',
                'schools': ['Hellenistic'],
                'bio': 'Founder of Pyrrhonian skepticism, he advocated for suspension of judgment (epoché) on all matters to achieve tranquility.',
                'works': 'No writings (taught orally)',
                'key_ideas': 'Skepticism, Suspension of judgment, Ataraxia through doubt'
            },
            {
                'name': 'Plotinus',
                'birth_year': 204,
                'death_year': 270,
                'country': 'Egypt',
                'schools': ['Neoplatonism'],
                'bio': 'Founder of Neoplatonism, Plotinus developed a complex metaphysical system based on Plato\'s philosophy, emphasizing the One as the source of all reality.',
                'works': 'The Enneads',
                'key_ideas': 'The One as ultimate reality, Emanation theory, Mystical union'
            },
            {
                'name': 'Cicero',
                'birth_year': -106,
                'death_year': -43,
                'country': 'Rome',
                'schools': ['Hellenistic'],
                'bio': 'Roman statesman and philosopher who transmitted Greek philosophy to the Roman world. He was particularly influenced by Stoicism and Academic skepticism.',
                'works': 'De Officiis, De Re Publica, Tusculan Disputations',
                'key_ideas': 'Natural law, Political philosophy, Rhetorical theory'
            },
            {
                'name': 'Seneca',
                'birth_year': -4,
                'death_year': 65,
                'country': 'Rome',
                'schools': ['Hellenistic'],
                'bio': 'Roman Stoic philosopher and advisor to Emperor Nero. His letters and essays provide practical guidance on Stoic living.',
                'works': 'Letters to Lucilius, Essays, Tragedies',
                'key_ideas': 'Practical Stoicism, Virtue and wisdom, Acceptance of mortality'
            },
            {
                'name': 'Marcus Aurelius',
                'birth_year': 121,
                'death_year': 180,
                'country': 'Rome',
                'schools': ['Hellenistic'],
                'bio': 'Roman Emperor and Stoic philosopher, known for his personal reflections on Stoic philosophy and leadership.',
                'works': 'Meditations',
                'key_ideas': 'Stoic leadership, Self-discipline, Cosmic perspective'
            },
            
            # III. Eastern Classical Philosophy
            {
                'name': 'Confucius',
                'birth_year': -551,
                'death_year': -479,
                'country': 'China',
                'schools': ['Confucianism'],
                'bio': 'Chinese philosopher whose teachings on ethics, morality, and social relationships became the foundation of Confucianism and deeply influenced Chinese culture.',
                'works': 'The Analects (compiled by disciples)',
                'key_ideas': 'Ren (benevolence), Li (ritual propriety), Junzi (exemplary person)'
            },
            {
                'name': 'Mencius',
                'birth_year': -372,
                'death_year': -289,
                'country': 'China',
                'schools': ['Confucianism'],
                'bio': 'Confucian philosopher who developed Confucian thought, particularly emphasizing the innate goodness of human nature.',
                'works': 'Mencius',
                'key_ideas': 'Innate human goodness, Righteous government, Moral cultivation'
            },
            {
                'name': 'Sun Tzu',
                'birth_year': -544,
                'death_year': -496,
                'country': 'China',
                'schools': ['Chinese Military Philosophy'],
                'bio': 'Chinese military strategist and philosopher whose work on warfare strategy has influenced both military and business thinking.',
                'works': 'The Art of War',
                'key_ideas': 'Strategic thinking, Winning without fighting, Know yourself and your enemy'
            },
            {
                'name': 'Laozi',
                'birth_year': -601,
                'death_year': -531,
                'country': 'China',
                'schools': ['Taoism'],
                'bio': 'Legendary founder of Taoism, emphasizing the Tao (Way) as the source of all things and advocating for wu wei (non-action).',
                'works': 'Tao Te Ching',
                'key_ideas': 'The Tao (Way), Wu wei (non-action), Harmony with nature'
            },
            {
                'name': 'Zhuangzi',
                'birth_year': -369,
                'death_year': -286,
                'country': 'China',
                'schools': ['Taoism'],
                'bio': 'Taoist philosopher known for his wit and paradoxes, who developed Taoist thought with emphasis on relativism and spontaneity.',
                'works': 'Zhuangzi',
                'key_ideas': 'Relativism, Spontaneity, Skepticism of conventional values'
            },
            {
                'name': 'Mozi',
                'birth_year': -470,
                'death_year': -391,
                'country': 'China',
                'schools': ['Mohism'],
                'bio': 'Chinese philosopher who advocated for universal love and opposed Confucian emphasis on family loyalty.',
                'works': 'Mozi',
                'key_ideas': 'Universal love, Meritocracy, Utilitarianism'
            },
            {
                'name': 'Buddha',
                'birth_year': -563,
                'death_year': -483,
                'country': 'India',
                'schools': ['Buddhism'],
                'bio': 'Founder of Buddhism, Siddhartha Gautama achieved enlightenment and taught the Four Noble Truths and the Eightfold Path.',
                'works': 'Teachings compiled in various sutras',
                'key_ideas': 'Four Noble Truths, Eightfold Path, Impermanence and suffering'
            },
            {
                'name': 'Mahavira',
                'birth_year': -599,
                'death_year': -527,
                'country': 'India',
                'schools': ['Jainism'],
                'bio': 'The 24th Tirthankara of Jainism, he emphasized non-violence (ahimsa) and liberation from the cycle of rebirth.',
                'works': 'Teachings preserved in Jain Agamas',
                'key_ideas': 'Ahimsa (non-violence), Karma and rebirth, Liberation (moksha)'
            },
            
            # IV. Ancient-Medieval India
            {
                'name': 'Shankara',
                'birth_year': 788,
                'death_year': 820,
                'country': 'India',
                'schools': ['Vedanta'],
                'bio': 'Founder of Advaita Vedanta, he taught the non-dualistic philosophy that Brahman is the only ultimate reality.',
                'works': 'Commentaries on Upanishads, Brahma Sutras, Bhagavad Gita',
                'key_ideas': 'Advaita (non-dualism), Brahman as ultimate reality, Maya (illusion)'
            },
            {
                'name': 'Nagarjuna',
                'birth_year': 150,
                'death_year': 250,
                'country': 'India',
                'schools': ['Madhyamaka'],
                'bio': 'Founder of the Madhyamaka school of Buddhist philosophy, he developed the concept of emptiness (śūnyatā).',
                'works': 'Mūlamadhyamakakārikā, Vigrahavyāvartanī',
                'key_ideas': 'Emptiness (śūnyatā), Middle Way, Dependent origination'
            },
            {
                'name': 'Kautilya',
                'birth_year': -350,
                'death_year': -275,
                'country': 'India',
                'schools': ['Political Philosophy'],
                'bio': 'Ancient Indian political philosopher and economist, author of the Arthashastra on statecraft and economics.',
                'works': 'Arthashastra',
                'key_ideas': 'Political realism, Economic policy, Statecraft'
            },
            
            # V. Medieval - Islamic, Jewish, Christian World
            {
                'name': 'Augustine of Hippo',
                'birth_year': 354,
                'death_year': 430,
                'country': 'North Africa',
                'schools': ['Christian Philosophy'],
                'bio': 'Early Christian philosopher who synthesized Christian doctrine with Platonic philosophy, profoundly influencing Western Christianity.',
                'works': 'Confessions, City of God, On the Trinity',
                'key_ideas': 'Divine grace, Original sin, Just war theory'
            },
            {
                'name': 'Boethius',
                'birth_year': 480,
                'death_year': 524,
                'country': 'Rome',
                'schools': ['Christian Philosophy'],
                'bio': 'Roman philosopher who transmitted Greek philosophical knowledge to the medieval world through his translations and commentaries.',
                'works': 'The Consolation of Philosophy, translations of Aristotle',
                'key_ideas': 'Divine providence, Fortune and happiness, Logic'
            },
            {
                'name': 'Al-Farabi',
                'birth_year': 872,
                'death_year': 950,
                'country': 'Kazakhstan/Iraq',
                'schools': ['Islamic Philosophy'],
                'bio': 'Known as the "Second Teacher" after Aristotle, he synthesized Aristotelian philosophy with Islamic thought.',
                'works': 'The Perfect State, The Attainment of Happiness',
                'key_ideas': 'Perfect state, Emanation theory, Harmony of philosophy and religion'
            },
            {
                'name': 'Avicenna',
                'birth_year': 980,
                'death_year': 1037,
                'country': 'Persia',
                'schools': ['Islamic Philosophy'],
                'bio': 'Persian polymath who made significant contributions to philosophy, medicine, and science, bridging Aristotelian thought with Islamic theology.',
                'works': 'The Book of Healing, The Canon of Medicine',
                'key_ideas': 'Distinction between essence and existence, Floating man argument, Medical philosophy'
            },
            {
                'name': 'Averroes',
                'birth_year': 1126,
                'death_year': 1198,
                'country': 'Spain',
                'schools': ['Islamic Philosophy'],
                'bio': 'Andalusian philosopher who wrote extensive commentaries on Aristotle and defended philosophy against theological criticism.',
                'works': 'Commentaries on Aristotle, The Incoherence of the Incoherence',
                'key_ideas': 'Double truth theory, Aristotelian rationalism, Unity of intellect'
            },
            {
                'name': 'Al-Ghazali',
                'birth_year': 1058,
                'death_year': 1111,
                'country': 'Persia',
                'schools': ['Islamic Philosophy'],
                'bio': 'Islamic theologian and philosopher who critiqued pure rationalism and emphasized mystical experience in religious knowledge.',
                'works': 'The Incoherence of the Philosophers, The Revival of the Religious Sciences',
                'key_ideas': 'Critique of rationalism, Mystical knowledge, Occasionalism'
            },
            {
                'name': 'Maimonides',
                'birth_year': 1135,
                'death_year': 1204,
                'country': 'Spain/Egypt',
                'schools': ['Jewish Philosophy'],
                'bio': 'Medieval Jewish philosopher who harmonized Aristotelian philosophy with Jewish theology, profoundly influencing Jewish thought.',
                'works': 'Guide for the Perplexed, Mishneh Torah',
                'key_ideas': 'Negative theology, Prophecy, Harmony of reason and faith'
            },
            {
                'name': 'Thomas Aquinas',
                'birth_year': 1225,
                'death_year': 1274,
                'country': 'Italy',
                'schools': ['Scholasticism'],
                'bio': 'Dominican friar who synthesized Aristotelian philosophy with Christian theology, creating a comprehensive philosophical system.',
                'works': 'Summa Theologica, Summa Contra Gentiles',
                'key_ideas': 'Five Ways (proofs for God), Natural law, Virtue ethics'
            },
            {
                'name': 'Duns Scotus',
                'birth_year': 1266,
                'death_year': 1308,
                'country': 'Scotland',
                'schools': ['Scholasticism'],
                'bio': 'Franciscan philosopher who emphasized the primacy of will over intellect and developed subtle theological distinctions.',
                'works': 'Ordinatio, Reportatio',
                'key_ideas': 'Voluntarism, Haecceitas (thisness), Univocity of being'
            },
            {
                'name': 'William of Ockham',
                'birth_year': 1287,
                'death_year': 1347,
                'country': 'England',
                'schools': ['Scholasticism'],
                'bio': 'Franciscan philosopher famous for Ockham\'s Razor, the principle that the simplest explanation is usually the best.',
                'works': 'Summa Logicae, Commentary on the Sentences',
                'key_ideas': 'Ockham\'s Razor, Nominalism, Divine command theory'
            },
        ]
        
        # Add first batch of philosophers
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
        
        self.stdout.write(self.style.SUCCESS('Successfully added first batch of philosophers!'))