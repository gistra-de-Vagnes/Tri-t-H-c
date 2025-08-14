from django.core.management.base import BaseCommand
from philosophers.models import Philosopher, PhilosophySchool

class Command(BaseCommand):
    help = 'Add modern and contemporary philosophers to the database'

    def handle(self, *args, **options):
        self.stdout.write('Adding modern and contemporary philosophers...')
        
        # Modern and Contemporary philosophers data
        philosophers_data = [
            # VI. Renaissance - Early Modern (around 1500-1700)
            {
                'name': 'Niccolò Machiavelli',
                'birth_year': 1469,
                'death_year': 1527,
                'country': 'Italy',
                'schools': ['Renaissance Humanism'],
                'bio': 'Italian political philosopher known for his pragmatic approach to politics. His work "The Prince" became a foundational text in political realism.',
                'works': 'The Prince, Discourses on Livy, The Art of War',
                'key_ideas': 'Political realism, The ends justify the means, Separation of politics and morality'
            },
            {
                'name': 'Michel de Montaigne',
                'birth_year': 1533,
                'death_year': 1592,
                'country': 'France',
                'schools': ['Renaissance Humanism'],
                'bio': 'French philosopher who popularized the essay as a literary genre and developed a skeptical approach to knowledge and human nature.',
                'works': 'Essays',
                'key_ideas': 'Skepticism, Self-examination, "What do I know?" (Que sais-je?)'
            },
            {
                'name': 'Francis Bacon',
                'birth_year': 1561,
                'death_year': 1626,
                'country': 'England',
                'schools': ['Empiricism'],
                'bio': 'English philosopher and scientist who developed the scientific method based on empirical observation and inductive reasoning.',
                'works': 'Novum Organum, The Advancement of Learning, New Atlantis',
                'key_ideas': 'Scientific method, Inductive reasoning, Knowledge is power'
            },
            {
                'name': 'Thomas Hobbes',
                'birth_year': 1588,
                'death_year': 1679,
                'country': 'England',
                'schools': ['Social Contract Theory'],
                'bio': 'English philosopher who developed social contract theory and argued for strong sovereign authority to prevent the "war of all against all."',
                'works': 'Leviathan, De Cive, Elements of Law',
                'key_ideas': 'Social contract, State of nature, Absolute sovereignty'
            },
            {
                'name': 'Baruch Spinoza',
                'birth_year': 1632,
                'death_year': 1677,
                'country': 'Netherlands',
                'schools': ['Rationalism'],
                'bio': 'Dutch philosopher who developed a pantheistic philosophy, identifying God with nature and emphasizing the power of reason.',
                'works': 'Ethics, Theological-Political Treatise, Political Treatise',
                'key_ideas': 'Pantheism, Determinism, Conatus (striving)'
            },
            {
                'name': 'John Locke',
                'birth_year': 1632,
                'death_year': 1704,
                'country': 'England',
                'schools': ['Empiricism'],
                'bio': 'English philosopher who developed empiricist epistemology and liberal political theory, influencing the Enlightenment and modern democracy.',
                'works': 'Essay Concerning Human Understanding, Two Treatises of Government',
                'key_ideas': 'Tabula rasa, Natural rights, Government by consent'
            },
            {
                'name': 'Gottfried Leibniz',
                'birth_year': 1646,
                'death_year': 1716,
                'country': 'Germany',
                'schools': ['Rationalism'],
                'bio': 'German philosopher and mathematician who developed a systematic philosophy based on the concept of monads and the principle of sufficient reason.',
                'works': 'Monadology, Theodicy, New Essays on Human Understanding',
                'key_ideas': 'Monads, Best of all possible worlds, Principle of sufficient reason'
            },
            
            # VII. Enlightenment & Modern (18th century - Kant)
            {
                'name': 'George Berkeley',
                'birth_year': 1685,
                'death_year': 1753,
                'country': 'Ireland',
                'schools': ['Empiricism'],
                'bio': 'Irish philosopher who developed immaterialism, arguing that material objects exist only as ideas perceived by minds.',
                'works': 'A Treatise Concerning the Principles of Human Knowledge, Three Dialogues',
                'key_ideas': 'Immaterialism, "To be is to be perceived", Idealism'
            },
            {
                'name': 'David Hume',
                'birth_year': 1711,
                'death_year': 1776,
                'country': 'Scotland',
                'schools': ['Empiricism'],
                'bio': 'Scottish philosopher who developed radical empiricism and skepticism, questioning causation, induction, and the self.',
                'works': 'A Treatise of Human Nature, An Enquiry Concerning Human Understanding',
                'key_ideas': 'Problem of induction, Skepticism about causation, Is-ought problem'
            },
            {
                'name': 'Immanuel Kant',
                'birth_year': 1724,
                'death_year': 1804,
                'country': 'Germany',
                'schools': ['German Idealism'],
                'bio': 'German philosopher who revolutionized philosophy by combining rationalism and empiricism, and developed influential moral and political theories.',
                'works': 'Critique of Pure Reason, Critique of Practical Reason, Critique of Judgment',
                'key_ideas': 'Categorical imperative, Transcendental idealism, Synthetic a priori knowledge'
            },
            
            # VIII. 19th Century (Near-Modern)
            {
                'name': 'Georg Wilhelm Friedrich Hegel',
                'birth_year': 1770,
                'death_year': 1831,
                'country': 'Germany',
                'schools': ['German Idealism'],
                'bio': 'German philosopher who developed a comprehensive philosophical system based on dialectical reasoning and absolute idealism.',
                'works': 'Phenomenology of Spirit, Science of Logic, Philosophy of Right',
                'key_ideas': 'Dialectical method, Absolute Spirit, Master-slave dialectic'
            },
            {
                'name': 'Karl Marx',
                'birth_year': 1818,
                'death_year': 1883,
                'country': 'Germany',
                'schools': ['Critical Theory'],
                'bio': 'German philosopher and economist who developed historical materialism and critiqued capitalism, profoundly influencing political thought.',
                'works': 'Das Kapital, The Communist Manifesto, The German Ideology',
                'key_ideas': 'Historical materialism, Class struggle, Alienation'
            },
            {
                'name': 'Arthur Schopenhauer',
                'birth_year': 1788,
                'death_year': 1860,
                'country': 'Germany',
                'schools': ['German Idealism'],
                'bio': 'German philosopher who developed a pessimistic philosophy based on the primacy of will and the inevitability of suffering.',
                'works': 'The World as Will and Representation, On the Fourfold Root of the Principle of Sufficient Reason',
                'key_ideas': 'Will as thing-in-itself, Pessimism, Aesthetic contemplation'
            },
            {
                'name': 'Søren Kierkegaard',
                'birth_year': 1813,
                'death_year': 1855,
                'country': 'Denmark',
                'schools': ['Existentialism'],
                'bio': 'Danish philosopher considered the father of existentialism, emphasizing individual existence, freedom, and choice.',
                'works': 'Either/Or, Fear and Trembling, The Sickness Unto Death',
                'key_ideas': 'Leap of faith, Anxiety, Three stages of existence'
            },
            {
                'name': 'John Stuart Mill',
                'birth_year': 1806,
                'death_year': 1873,
                'country': 'England',
                'schools': ['Utilitarianism'],
                'bio': 'English philosopher who developed utilitarian ethics and liberal political theory, advocating for individual liberty and women\'s rights.',
                'works': 'On Liberty, Utilitarianism, The Subjection of Women',
                'key_ideas': 'Harm principle, Greatest happiness principle, Individual liberty'
            },
            {
                'name': 'Jeremy Bentham',
                'birth_year': 1748,
                'death_year': 1832,
                'country': 'England',
                'schools': ['Utilitarianism'],
                'bio': 'English philosopher who founded modern utilitarianism, advocating for the greatest happiness for the greatest number.',
                'works': 'Introduction to the Principles of Morals and Legislation, Panopticon',
                'key_ideas': 'Principle of utility, Hedonistic calculus, Legal reform'
            },
            {
                'name': 'Auguste Comte',
                'birth_year': 1798,
                'death_year': 1857,
                'country': 'France',
                'schools': ['Positivism'],
                'bio': 'French philosopher who founded positivism and sociology, emphasizing scientific method in understanding society.',
                'works': 'Course in Positive Philosophy, System of Positive Polity',
                'key_ideas': 'Positivism, Law of three stages, Sociology'
            },
            
            # IX. 20th Century - Analytical and Continental Philosophy
            {
                'name': 'Bertrand Russell',
                'birth_year': 1872,
                'death_year': 1970,
                'country': 'England',
                'schools': ['Analytic Philosophy'],
                'bio': 'British philosopher and mathematician who made significant contributions to logic, mathematics, and analytic philosophy.',
                'works': 'Principia Mathematica, The Problems of Philosophy, A History of Western Philosophy',
                'key_ideas': 'Logical atomism, Theory of descriptions, Russell\'s paradox'
            },
            {
                'name': 'G. E. Moore',
                'birth_year': 1873,
                'death_year': 1958,
                'country': 'England',
                'schools': ['Analytic Philosophy'],
                'bio': 'English philosopher who developed common sense philosophy and made important contributions to ethics and epistemology.',
                'works': 'Principia Ethica, Some Main Problems of Philosophy',
                'key_ideas': 'Naturalistic fallacy, Common sense philosophy, Open question argument'
            },
            {
                'name': 'Ludwig Wittgenstein',
                'birth_year': 1889,
                'death_year': 1951,
                'country': 'Austria',
                'schools': ['Analytic Philosophy'],
                'bio': 'Austrian-British philosopher who revolutionized philosophy of language and logic in two distinct periods of his career.',
                'works': 'Tractus Logico-Philosophicus, Philosophical Investigations',
                'key_ideas': 'Language games, Picture theory of meaning, Private language argument'
            },
            {
                'name': 'Edmund Husserl',
                'birth_year': 1859,
                'death_year': 1938,
                'country': 'Germany',
                'schools': ['Phenomenology'],
                'bio': 'German philosopher who founded phenomenology, the study of consciousness and the structures of experience.',
                'works': 'Logical Investigations, Ideas, Crisis of European Sciences',
                'key_ideas': 'Phenomenological reduction, Intentionality, Epoché'
            },
            {
                'name': 'Martin Heidegger',
                'birth_year': 1889,
                'death_year': 1976,
                'country': 'Germany',
                'schools': ['Phenomenology', 'Existentialism'],
                'bio': 'German philosopher who developed fundamental ontology and profoundly influenced 20th-century continental philosophy.',
                'works': 'Being and Time, What is Metaphysics?, The Origin of the Work of Art',
                'key_ideas': 'Being-in-the-world, Dasein, Authenticity'
            },
            {
                'name': 'Jean-Paul Sartre',
                'birth_year': 1905,
                'death_year': 1980,
                'country': 'France',
                'schools': ['Existentialism'],
                'bio': 'French philosopher who developed atheistic existentialism, emphasizing human freedom and responsibility.',
                'works': 'Being and Nothingness, Existentialism is a Humanism, No Exit',
                'key_ideas': 'Existence precedes essence, Bad faith, Radical freedom'
            },
            {
                'name': 'Simone de Beauvoir',
                'birth_year': 1908,
                'death_year': 1986,
                'country': 'France',
                'schools': ['Existentialism', 'Feminism'],
                'bio': 'French philosopher and feminist who applied existentialist philosophy to women\'s condition and founded modern feminism.',
                'works': 'The Second Sex, The Ethics of Ambiguity, The Mandarins',
                'key_ideas': 'Women as "Other", Situated ethics, Feminist existentialism'
            },
            {
                'name': 'Hannah Arendt',
                'birth_year': 1906,
                'death_year': 1975,
                'country': 'Germany/USA',
                'schools': ['Political Philosophy'],
                'bio': 'German-American political theorist who analyzed totalitarianism, power, and the human condition in modern politics.',
                'works': 'The Origins of Totalitarianism, The Human Condition, Eichmann in Jerusalem',
                'key_ideas': 'Banality of evil, Vita activa, Public and private spheres'
            },
            {
                'name': 'Karl Popper',
                'birth_year': 1902,
                'death_year': 1994,
                'country': 'Austria/England',
                'schools': ['Philosophy of Science'],
                'bio': 'Austrian-British philosopher who developed critical rationalism and the principle of falsifiability in science.',
                'works': 'The Logic of Scientific Discovery, The Open Society and Its Enemies',
                'key_ideas': 'Falsifiability, Critical rationalism, Open society'
            },
            {
                'name': 'Thomas Kuhn',
                'birth_year': 1922,
                'death_year': 1996,
                'country': 'USA',
                'schools': ['Philosophy of Science'],
                'bio': 'American philosopher who revolutionized understanding of scientific progress through his concept of paradigm shifts.',
                'works': 'The Structure of Scientific Revolutions, The Copernican Revolution',
                'key_ideas': 'Paradigm shifts, Normal science, Incommensurability'
            },
            {
                'name': 'Michel Foucault',
                'birth_year': 1926,
                'death_year': 1984,
                'country': 'France',
                'schools': ['Postmodernism'],
                'bio': 'French philosopher who analyzed the relationship between power and knowledge, and the history of social institutions.',
                'works': 'Discipline and Punish, The History of Sexuality, Madness and Civilization',
                'key_ideas': 'Power/knowledge, Discourse analysis, Genealogy'
            },
            {
                'name': 'Jacques Derrida',
                'birth_year': 1930,
                'death_year': 2004,
                'country': 'France',
                'schools': ['Postmodernism'],
                'bio': 'French philosopher who developed deconstruction, a method of critical analysis that questions the stability of meaning.',
                'works': 'Of Grammatology, Writing and Difference, Margins of Philosophy',
                'key_ideas': 'Deconstruction, Différance, Logocentrism'
            },
            {
                'name': 'John Rawls',
                'birth_year': 1921,
                'death_year': 2002,
                'country': 'USA',
                'schools': ['Political Philosophy'],
                'bio': 'American philosopher who revitalized political philosophy with his theory of justice based on fairness and equality.',
                'works': 'A Theory of Justice, Political Liberalism, The Law of Peoples',
                'key_ideas': 'Original position, Veil of ignorance, Justice as fairness'
            },
            {
                'name': 'Richard Rorty',
                'birth_year': 1931,
                'death_year': 2007,
                'country': 'USA',
                'schools': ['Pragmatism'],
                'bio': 'American philosopher who developed neopragmatism and critiqued traditional epistemology and metaphysics.',
                'works': 'Philosophy and the Mirror of Nature, Contingency, Irony, and Solidarity',
                'key_ideas': 'Anti-foundationalism, Neopragmatism, Conversation over truth'
            },
            {
                'name': 'Hilary Putnam',
                'birth_year': 1926,
                'death_year': 2016,
                'country': 'USA',
                'schools': ['Analytic Philosophy'],
                'bio': 'American philosopher who made significant contributions to philosophy of mind, language, and science.',
                'works': 'Reason, Truth and History, The Many Faces of Realism, Mind, Language and Reality',
                'key_ideas': 'Twin Earth argument, Internal realism, Multiple realizability'
            },
            {
                'name': 'Simone Weil',
                'birth_year': 1909,
                'death_year': 1943,
                'country': 'France',
                'schools': ['Religious Philosophy'],
                'bio': 'French philosopher and mystic who combined social activism with spiritual philosophy, emphasizing attention and affliction.',
                'works': 'Gravity and Grace, The Need for Roots, Waiting for God',
                'key_ideas': 'Attention, Affliction, Spiritual gravity'
            },
            {
                'name': 'Ludwig Feuerbach',
                'birth_year': 1804,
                'death_year': 1872,
                'country': 'Germany',
                'schools': ['German Idealism'],
                'bio': 'German philosopher who critiqued religion and influenced Marx with his materialist approach to human nature.',
                'works': 'The Essence of Christianity, Principles of the Philosophy of the Future',
                'key_ideas': 'Critique of religion, Anthropological materialism, Species-being'
            },
            
            # X. American Pragmatism
            {
                'name': 'Charles Sanders Peirce',
                'birth_year': 1839,
                'death_year': 1914,
                'country': 'USA',
                'schools': ['Pragmatism'],
                'bio': 'American philosopher who founded pragmatism and made significant contributions to logic and semiotics.',
                'works': 'How to Make Our Ideas Clear, The Fixation of Belief',
                'key_ideas': 'Pragmatic maxim, Fallibilism, Semiotics'
            },
            {
                'name': 'William James',
                'birth_year': 1842,
                'death_year': 1910,
                'country': 'USA',
                'schools': ['Pragmatism'],
                'bio': 'American philosopher and psychologist who developed pragmatism and radical empiricism, emphasizing the practical consequences of ideas.',
                'works': 'The Principles of Psychology, Pragmatism, The Varieties of Religious Experience',
                'key_ideas': 'Stream of consciousness, Will to believe, Radical empiricism'
            },
            {
                'name': 'John Dewey',
                'birth_year': 1859,
                'death_year': 1952,
                'country': 'USA',
                'schools': ['Pragmatism'],
                'bio': 'American philosopher who applied pragmatism to education, democracy, and social reform, emphasizing learning through experience.',
                'works': 'Democracy and Education, Experience and Nature, Art as Experience',
                'key_ideas': 'Learning by doing, Democratic education, Instrumentalism'
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
        
        self.stdout.write(self.style.SUCCESS('Successfully added modern and contemporary philosophers!'))