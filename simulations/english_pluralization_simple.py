from simulations.learning_simulation import LearningSimulation
from grammar import Grammar
from syntactic_node import SyntacticNode
from rule import Rule
from datum import Datum

class EnglishPluralizationSimple(LearningSimulation):

    # Lexical
    DOG_NODE = SyntacticNode(SyntacticNode.TYPE_ROOT, 'DOG', 1000, 'dog')
    TABLE_NODE = SyntacticNode(SyntacticNode.TYPE_ROOT, 'TABLE', 1001, 'teibl')
    TREE_NODE = SyntacticNode(SyntacticNode.TYPE_ROOT, 'TREE', 1010, 'tri')
    CAR_NODE = SyntacticNode(SyntacticNode.TYPE_ROOT, 'CAR', 1011, 'car')
    DEER_NODE = SyntacticNode(SyntacticNode.TYPE_ROOT, 'DEER', 1100, 'dir')
    FISH_NODE = SyntacticNode(SyntacticNode.TYPE_ROOT, 'FISH', 1101, 'fish')

    # Functional
    PLURAL_NODE = SyntacticNode(SyntacticNode.TYPE_FEATURE, '+PL', 1100)

    NODES = [DOG_NODE, TABLE_NODE, TREE_NODE, CAR_NODE, DEER_NODE, FISH_NODE, PLURAL_NODE]
    VOCABULARY = ['z']
    RULES = [
        Rule([PLURAL_NODE], 'z', []),
        Rule([PLURAL_NODE], '', [DEER_NODE, FISH_NODE])
             ]

    TARGET_GRAMMAR = Grammar(NODES, VOCABULARY, RULES)

    DATA = [
        Datum(DOG_NODE, [], 'dog'),
        Datum(DOG_NODE, [PLURAL_NODE], 'dogz'),
        Datum(TABLE_NODE, [], 'teibl'),
        Datum(TABLE_NODE, [PLURAL_NODE], 'teiblz'),
        Datum(TREE_NODE, [], 'tri'),
        Datum(TREE_NODE, [PLURAL_NODE], 'triz'),
        Datum(CAR_NODE, [], 'car'),
        Datum(CAR_NODE, [PLURAL_NODE], 'carz'),
        Datum(DEER_NODE, [], 'dir'),
        Datum(DEER_NODE, [PLURAL_NODE], 'dir'),
        Datum(FISH_NODE, [], 'fish'),
        Datum(FISH_NODE, [PLURAL_NODE], 'fish'),
    ]

    def __init__(self):
        super().__init__(self.NODES, self.VOCABULARY, self.RULES, self.DATA)
