from adjectives import Adjectives
from adverbs import Adverbs
from conjunctions import Conjunctions
from nouns import Nouns
from prepositions import Prepositions
from pronouns import Pronouns
from verbs import Verbs

class SentenceBuilder:
    def __init__(self):
        self.adjectives = Adjectives()
        self.adverbs = Adverbs()
        self.conjunctions = Conjunctions()
        self.nouns = Nouns()
        self.prepositions = Prepositions()
        self.pronouns = Pronouns()
        self.verbs = Verbs()

    def get_adjectives(self):
        return self.adjectives.get_data()

    def get_adverbs(self):
        return self.adverbs.get_data()
    
    def get_conjunctions(self):
        return self.conjunctions.get_data()
    
    def get_nouns(self):
        return self.nouns.get_data()
    
    def get_prepositions(self):
        return self.prepositions.get_data()
    
    def get_pronouns(self):
        return self.pronouns.get_data()
    
    def get_verbs(self):
        return self.verbs.get_data()