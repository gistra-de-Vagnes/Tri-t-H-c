from django.core.management.base import BaseCommand
from philosophers.models import PhilosophySchool, Philosopher

class Command(BaseCommand):
    help = 'Add comprehensive philosophy data with detailed information and images'

    def handle(self, *args, **options):
        self.stdout.write('Adding comprehensive philosophy schools...')
        
        # Comprehensive philosophy schools data
        schools_data = [
            {
                "name": "Stoicism",
                "description": "Stoicism is a school of Hellenistic philosophy founded at Athens by Zeno of Citium in the early 3rd century BC. It teaches the development of self-control and fortitude as a means of overcoming destructive emotions. The philosophy asserts that virtue, the highest good, is based on knowledge; the wise live in harmony with the divine Reason that governs nature, and are indifferent to the vicissitudes of fortune and to pleasure and pain. Key principles include living according to nature, accepting what cannot be changed, focusing on what is within our control, and maintaining inner tranquility through rational thinking."
            },
            {
                "name": "Existentialism", 
                "description": "Existentialism is a philosophical movement that emerged in the 20th century, emphasizing individual existence, freedom, and choice. It is the view that humans define their own meaning in life, and try to make rational decisions despite existing in an irrational universe. Key themes include anxiety, despair, freedom, responsibility, and authenticity. Existentialists believe that existence precedes essence - that individuals exist first and then create meaning through their choices and actions. The movement was particularly influential in post-war Europe, addressing themes of alienation, absurdity, and the human condition."
            },
            {
                "name": "Rationalism",
                "description": "Rationalism is the philosophical view that regards reason as the chief source and test of knowledge. Rationalists believe that reality has a logical structure that can be discovered through reason, independent of sensory experience. This school of thought emphasizes the power of the mind to understand the world through thinking rather than sensory experience. Key figures developed methods of systematic doubt, mathematical reasoning, and logical deduction to arrive at certain knowledge. Rationalists argue that some ideas are innate and that mathematical truths provide a model for all knowledge."
            },
            {
                "name": "Empiricism",
                "description": "Empiricism is a theory that states that knowledge comes primarily from sensory experience. It emphasizes evidence, especially as discovered in experiments, over theoretical reasoning. Empiricists argue that the mind is initially a 'blank slate' (tabula rasa) and that all knowledge is derived from experience through the senses. This philosophical approach emphasizes observation, experimentation, and inductive reasoning as the primary methods for acquiring knowledge about the world. Empiricism forms the philosophical foundation of the scientific method and modern experimental science."
            },
            {
                "name": "Ancient Greek Philosophy",
                "description": "Ancient Greek philosophy arose in the 6th century BC and continued throughout the Hellenistic period. It dealt with a wide variety of subjects, including political philosophy, ethics, metaphysics, ontology, logic, biology, rhetoric, and aesthetics. Greek philosophy is known for its rational approach to understanding the world, moving away from mythological explanations toward logical reasoning. The period saw the development of major philosophical schools and methods that continue to influence Western thought today, including the Socratic method, Platonic idealism, and Aristotelian logic and ethics."
            },
            {
                "name": "Analytic Philosophy",
                "description": "Analytic philosophy is a branch of philosophy that emphasizes clarity and argumentation, often using formal logic and analysis of language. It became dominant in the English-speaking world during the 20th century. Analytic philosophers seek to clarify concepts and examine the logical structure of thoughts and arguments. The movement emphasizes precision, logical rigor, and often focuses on the philosophy of language, mind, and science. Key methods include conceptual analysis, formal logic, and careful attention to the meanings of words and concepts."
            },
            {
                "name": "Phenomenology",
                "description": "Phenomenology is the philosophical study of the structures of experience and consciousness. It seeks to identify the essential features of experiences and the objects of experience, focusing on how things appear to consciousness rather than their objective existence. Founded by Edmund Husserl, phenomenology emphasizes the first-person perspective and the intentional structure of consciousness - the fact that consciousness is always consciousness of something. This approach has been influential in psychology, sociology, and literary theory."
            },
            {
                "name": "Utilitarianism",
                "description": "Utilitarianism is a family of normative ethical theories that prescribe actions that maximize happiness and well-being for all affected individuals. The principle of utility judges the rightness of actions based on their consequences - specifically, their tendency to promote happiness or pleasure and prevent pain or suffering. Classical utilitarians like Jeremy Bentham and John Stuart Mill argued that the moral worth of an action is determined solely by its outcome, making it a form of consequentialism. The theory has been influential in ethics, political philosophy, and public policy."
            },
            {
                "name": "German Idealism",
                "description": "German Idealism is a philosophical movement that emerged in Germany in the late 18th and early 19th centuries. It developed out of the work of Immanuel Kant and was characterized by the belief that reality is fundamentally mental or spiritual in nature. Key figures include Fichte, Schelling, and Hegel, who each developed systematic philosophies attempting to overcome the limitations they saw in Kant's critical philosophy. German Idealists emphasized the active role of the mind in constituting reality and sought to develop comprehensive systems explaining the relationship between thought and being."
            },
            {
                "name": "Pragmatism",
                "description": "Pragmatism is a philosophical tradition that began in the United States around 1870. It emphasizes the practical application of ideas by acting on them to test them in human experiences. Pragmatists argue that the truth or meaning of an idea or a proposition lies in its observable practical consequences. The philosophy emphasizes the connection between thought and action, viewing ideas as tools for action rather than representations of reality. Key figures include Charles Sanders Peirce, William James, and John Dewey, who applied pragmatic principles to psychology, education, and social reform."
            }
        ]
        
        schools = {}
        for school_data in schools_data:
            school, created = PhilosophySchool.objects.get_or_create(
                name=school_data["name"],
                defaults={"description": school_data["description"]}
            )
            schools[school_data["name"]] = school
            if created:
                self.stdout.write(f'Created school: {school.name}')
            else:
                # Update description if school exists
                school.description = school_data["description"]
                school.save()
                self.stdout.write(f'Updated school: {school.name}')

        self.stdout.write('\nAdding comprehensive philosophers...')
        
        # Comprehensive philosophers data with images
        philosophers_data = [
            {
                "name": "Marcus Aurelius",
                "bio": "Marcus Aurelius Antoninus (121-180 AD) was Roman Emperor from 161 to 180 and a Stoic philosopher. He is considered the last of the Five Good Emperors and the last emperor of the Pax Romana. His personal philosophical writings, known as 'Meditations', were written as a source for his own guidance and self-improvement. These reflections, written in Greek while on military campaigns, offer insights into Stoic philosophy and have been praised for their moral guidance and practical wisdom. As emperor, he faced numerous military conflicts, including wars with the Parthian Empire and Germanic tribes, while also dealing with the Antonine Plague that devastated the Roman Empire.",
                "birth_year": 121,
                "death_year": 180,
                "schools": ["Stoicism"],
                "works": "Meditations (Τὰ εἰς ἑαυτόν), Letters to Fronto, Legal and Administrative Documents",
                "key_ideas": "Virtue as the highest good, acceptance of fate (amor fati), impermanence of all things, duty to the common good, rational self-examination, emotional resilience, cosmic perspective",
                "country": "Roman Empire",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Marcus_Aurelius_-_Palazzo_Altemps_-_Rome.jpg/256px-Marcus_Aurelius_-_Palazzo_Altemps_-_Rome.jpg"
            },
            {
                "name": "Jean-Paul Sartre",
                "bio": "Jean-Paul Charles Aymard Sartre (1905-1980) was a French philosopher, playwright, novelist, screenwriter, political activist, biographer, and literary critic. He was one of the key figures in the philosophy of existentialism and phenomenology, and one of the leading figures in 20th-century French philosophy and Marxism. Sartre was awarded the 1964 Nobel Prize in Literature but refused it, saying that he always declined official honors and that 'a writer should not allow himself to be turned into an institution.' His work influenced sociology, critical theory, post-colonial theory, and literary studies, and continues to influence these fields.",
                "birth_year": 1905,
                "death_year": 1980,
                "schools": ["Existentialism", "Phenomenology"],
                "works": "Being and Nothingness (L'Être et le néant), Existentialism is a Humanism, Nausea (La Nausée), No Exit (Huis clos), The Roads to Freedom trilogy, Critique of Dialectical Reason",
                "key_ideas": "Existence precedes essence, radical freedom and responsibility, bad faith (mauvaise foi), the look of the other, authenticity, anguish and abandonment, commitment and engagement",
                "country": "France",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Sartre_1967_crop.jpg/256px-Sartre_1967_crop.jpg"
            },
            {
                "name": "René Descartes",
                "bio": "René Descartes (1596-1650) was a French philosopher, mathematician, and scientist who is widely considered the father of modern philosophy and analytical geometry. His philosophical and mathematical work had a profound impact on the development of Western thought. Descartes sought to establish a secure foundation for knowledge through methodological skepticism, doubting everything that could possibly be false until he arrived at something that could not be doubted. His famous cogito ergo sum ('I think, therefore I am') became a fundamental element of Western philosophy. He also made significant contributions to mathematics, developing Cartesian coordinates and analytical geometry.",
                "birth_year": 1596,
                "death_year": 1650,
                "schools": ["Rationalism"],
                "works": "Discourse on the Method (Discours de la méthode), Meditations on First Philosophy (Meditationes de prima philosophia), Principles of Philosophy (Principia philosophiae), Rules for the Direction of the Mind, The Passions of the Soul",
                "key_ideas": "Methodological skepticism, cogito ergo sum, mind-body dualism, clear and distinct ideas, foundationalism, mechanical philosophy, mathematical method in philosophy",
                "country": "France",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Frans_Hals_-_Portret_van_René_Descartes.jpg/256px-Frans_Hals_-_Portret_van_René_Descartes.jpg"
            },
            {
                "name": "David Hume",
                "bio": "David Hume (1711-1776) was a Scottish Enlightenment philosopher, historian, economist, and essayist who is best known today for his highly influential system of philosophical empiricism, skepticism, and naturalism. Beginning with A Treatise of Human Nature, Hume strove to create a naturalistic science of man that examined the psychological basis of human nature. Hume argued against the existence of innate ideas, positing that all human knowledge derives solely from experience. He also argued that inductive reasoning and belief in causality cannot be justified rationally; instead, they result from custom and mental habit.",
                "birth_year": 1711,
                "death_year": 1776,
                "schools": ["Empiricism"],
                "works": "A Treatise of Human Nature, An Enquiry Concerning Human Understanding, An Enquiry Concerning the Principles of Morals, Dialogues Concerning Natural Religion, The History of England, Essays Moral and Political",
                "key_ideas": "Empiricism and skepticism, problem of induction, is-ought problem, bundle theory of the self, critique of causation, moral sentimentalism, critique of the design argument",
                "country": "Scotland",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Painting_of_David_Hume.jpg/256px-Painting_of_David_Hume.jpg"
            },
            {
                "name": "Socrates",
                "bio": "Socrates (470-399 BC) was a classical Greek philosopher credited as one of the founders of Western philosophy and the first moral philosopher of the Western ethical tradition of thought. An enigmatic figure, he made no writings and is known chiefly through the accounts of classical writers composing after his lifetime, particularly his students Plato and Xenophon. Through his portrayal in Plato's dialogues, Socrates has become renowned for his contributions to the fields of ethics and epistemology, and his ideas and approach have been influential in Western philosophy. Socrates exerted a strong influence on philosophers in later antiquity and has continued to do so in the modern era.",
                "birth_year": -470,
                "death_year": -399,
                "schools": ["Ancient Greek Philosophy"],
                "works": "None directly (known through Plato's Dialogues: Apology, Crito, Phaedo, Meno, Republic, and others)",
                "key_ideas": "Socratic method (elenchus), 'Know thyself' (gnothi seauton), 'The unexamined life is not worth living', virtue is knowledge, no one does wrong willingly, Socratic irony, care of the soul",
                "country": "Ancient Greece (Athens)",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Socrates_Louvre.jpg/256px-Socrates_Louvre.jpg"
            },
            {
                "name": "Ludwig Wittgenstein",
                "bio": "Ludwig Josef Johann Wittgenstein (1889-1951) was an Austrian-British philosopher who worked primarily in logic, the philosophy of mathematics, the philosophy of mind, and the philosophy of language. He is considered by many to be the greatest philosopher of the 20th century. From 1929 to 1947, Wittgenstein taught at the University of Cambridge. During his lifetime he published just one book review, one article, a children's dictionary, and the 75-page Tractatus Logico-Philosophicus (1921). In 1999, his posthumously published Philosophical Investigations (1953) was ranked as the most important book of 20th-century philosophy.",
                "birth_year": 1889,
                "death_year": 1951,
                "schools": ["Analytic Philosophy"],
                "works": "Tractus Logico-Philosophicus, Philosophical Investigations (Philosophische Untersuchungen), On Certainty (Über Gewißheit), Remarks on the Foundations of Mathematics, The Blue and Brown Books",
                "key_ideas": "Language games, picture theory of language, ordinary language philosophy, private language argument, rule-following paradox, forms of life, showing vs. saying",
                "country": "Austria/United Kingdom",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Ludwig_Wittgenstein.jpg/256px-Ludwig_Wittgenstein.jpg"
            },
            {
                "name": "Plato",
                "bio": "Plato (428/427 or 424/423 – 348/347 BC) was an ancient Greek philosopher born in Athens during the Classical period in Ancient Greece. He founded the Platonist school of thought and the Academy, the first institution of higher learning in the Western world. He is widely considered the pivotal figure in the history of Ancient Greek and Western philosophy, along with his teacher, Socrates, and his most famous student, Aristotle. Plato has also often been cited as one of the founders of Western religion and spirituality. The so-called Neoplatonism of philosophers like Plotinus and Porphyry influenced Saint Augustine and thus Christianity.",
                "birth_year": -428,
                "death_year": -348,
                "schools": ["Ancient Greek Philosophy"],
                "works": "The Republic, Phaedo, Symposium, Phaedrus, Meno, Apology, Crito, Laws, Timaeus, Parmenides, Theaetetus, Sophist, Statesman",
                "key_ideas": "Theory of Forms (Ideas), philosopher-king, tripartite soul, allegory of the cave, dialectical method, theory of recollection, critique of democracy, ideal state",
                "country": "Ancient Greece (Athens)",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Plato-raphael.jpg/256px-Plato-raphael.jpg"
            },
            {
                "name": "Aristotle",
                "bio": "Aristotle (384-322 BC) was a Greek philosopher and polymath during the Classical period in Ancient Greece. Taught by Plato, he was the founder of the Lyceum, the Peripatetic school of philosophy, and the Aristotelian tradition. His writings cover many subjects including physics, biology, zoology, metaphysics, logic, ethics, aesthetics, poetry, theatre, music, rhetoric, psychology, linguistics, economics, politics, and government. Aristotle provided a complex synthesis of the various philosophies existing prior to him. It was above all from his teachings that the West inherited its intellectual lexicon, as well as problems and methods of inquiry.",
                "birth_year": -384,
                "death_year": -322,
                "schools": ["Ancient Greek Philosophy"],
                "works": "Nicomachean Ethics, Politics, Metaphysics, Physics, Poetics, Rhetoric, Categories, Prior Analytics, Posterior Analytics, Topics, On the Soul (De Anima)",
                "key_ideas": "Virtue ethics, golden mean, four causes, substance and accident, potentiality and actuality, syllogistic logic, classification of knowledge, theory of tragedy",
                "country": "Ancient Greece (Macedonia/Athens)",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Aristotle_Altemps_Inv8575.jpg/256px-Aristotle_Altemps_Inv8575.jpg"
            },
            {
                "name": "Immanuel Kant",
                "bio": "Immanuel Kant (1724-1804) was a German philosopher and one of the central Enlightenment thinkers. Born in Königsberg, Kant's comprehensive and systematic works in epistemology, metaphysics, ethics, and aesthetics have made him one of the most influential figures in modern Western philosophy. In his doctrine of transcendental idealism, Kant argued that space and time are mere 'forms of intuition' which structure all experience, and therefore that while the appearance of things is real, their nature independent of our experience remains unknowable. His ethical theory, based on the concept of duty and the categorical imperative, has been highly influential.",
                "birth_year": 1724,
                "death_year": 1804,
                "schools": ["German Idealism"],
                "works": "Critique of Pure Reason (Kritik der reinen Vernunft), Critique of Practical Reason, Critique of Judgment, Groundwork for the Metaphysics of Morals, What is Enlightenment?, Perpetual Peace",
                "key_ideas": "Transcendental idealism, categorical imperative, synthetic a priori knowledge, phenomena vs. noumena, autonomy of reason, duty-based ethics, enlightenment as maturity",
                "country": "Prussia (Germany)",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Kant_gemaelde_3.jpg/256px-Kant_gemaelde_3.jpg"
            },
            {
                "name": "Friedrich Nietzsche",
                "bio": "Friedrich Wilhelm Nietzsche (1844-1900) was a German philosopher, cultural critic, composer, poet, and philologist whose work has exerted a profound influence on modern intellectual history. He began his career as a classical philologist before turning to philosophy. His writing spans philosophical polemics, poetry, cultural criticism, and fiction while displaying a fondness for aphorism and irony. Nietzsche's key ideas include the death of God, the Übermensch, eternal recurrence, and the will to power. His radical questioning of truth and morality, his concern with the individual's creative self-realization, and his critique of traditional values have been influential across philosophy, literature, and the arts.",
                "birth_year": 1844,
                "death_year": 1900,
                "schools": ["Existentialism"],
                "works": "Thus Spoke Zarathustra (Also sprach Zarathustra), Beyond Good and Evil, On the Genealogy of Morality, The Birth of Tragedy, The Gay Science, Twilight of the Idols, The Antichrist",
                "key_ideas": "Death of God, Übermensch (overman), will to power, eternal recurrence, master-slave morality, perspectivism, amor fati, critique of Christianity and traditional morality",
                "country": "Germany",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Nietzsche187a.jpg/256px-Nietzsche187a.jpg"
            },
            {
                "name": "John Stuart Mill",
                "bio": "John Stuart Mill (1806-1873) was an English philosopher, political economist, and civil servant. One of the most influential thinkers in the history of classical liberalism, he contributed widely to social theory, political theory, and political economy. Dubbed 'the most influential English-speaking philosopher of the nineteenth century', Mill's conception of liberty justified the freedom of the individual in opposition to unlimited state and social control. Mill was a proponent of utilitarianism, an ethical theory developed by his predecessor Jeremy Bentham. He contributed to the investigation of scientific methodology, though his knowledge of the topic was based on the work of others, notably William Whewell.",
                "birth_year": 1806,
                "death_year": 1873,
                "schools": ["Utilitarianism", "Empiricism"],
                "works": "On Liberty, Utilitarianism, The Subjection of Women, A System of Logic, Principles of Political Economy, On the Subjection of Women, Considerations on Representative Government",
                "key_ideas": "Harm principle, higher and lower pleasures, qualified hedonism, individual liberty, women's rights, representative government, inductive logic, tyranny of the majority",
                "country": "England",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/John_Stuart_Mill_by_London_Stereoscopic_Company%2C_c1870.jpg/256px-John_Stuart_Mill_by_London_Stereoscopic_Company%2C_c1870.jpg"
            },
            {
                "name": "Edmund Husserl",
                "bio": "Edmund Gustav Albrecht Husserl (1859-1938) was a German philosopher who established the school of phenomenology. In his early work, he elaborated critiques of historicism and of psychologism in logic based on analyses of intentionality. In his mature work, he sought to develop a systematic foundational science based on the so-called phenomenological reduction. Arguing that transcendental consciousness sets the limits of all possible knowledge, Husserl redefined phenomenology as a transcendental-idealist philosophy. Husserl's thought profoundly influenced 20th-century philosophy, and he has been called the father of phenomenology.",
                "birth_year": 1859,
                "death_year": 1938,
                "schools": ["Phenomenology"],
                "works": "Logical Investigations (Logische Untersuchungen), Ideas: General Introduction to Pure Phenomenology, Cartesian Meditations, The Crisis of European Sciences and Transcendental Phenomenology",
                "key_ideas": "Intentionality of consciousness, phenomenological reduction (epoché), transcendental ego, lifeworld (Lebenswelt), eidetic reduction, natural attitude vs. phenomenological attitude",
                "country": "Germany/Austria",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Edmund_Husserl_1900.jpg/256px-Edmund_Husserl_1900.jpg"
            }
        ]
        
        for philosopher_data in philosophers_data:
            # Get schools
            school_names = philosopher_data.pop("schools", [])
            school_objects = [schools[name] for name in school_names if name in schools]
            
            # Create or update philosopher
            philosopher, created = Philosopher.objects.get_or_create(
                name=philosopher_data["name"],
                defaults=philosopher_data
            )
            
            if not created:
                # Update existing philosopher with new data
                for key, value in philosopher_data.items():
                    setattr(philosopher, key, value)
                philosopher.save()
                self.stdout.write(f'Updated philosopher: {philosopher.name}')
            else:
                self.stdout.write(f'Created philosopher: {philosopher.name}')
            
            # Set schools
            if school_objects:
                philosopher.schools.set(school_objects)
                philosopher.save()

        self.stdout.write(
            self.style.SUCCESS('\nComprehensive philosophy data added successfully!')
        )