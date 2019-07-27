from hypothesis import Hypothesis
from grammar import Grammar

class LearningSimulation:
    def __init__(self, syntactic_nodes, vocabulary, rules, data):
        """
        A simulation of an MDL learner.
        :param syntactic_nodes: a list of SyntacticNode instances representing the available syntactic nodes in the grammar
        :param data: a list of surface forms learned by the learner
        :param target_grammar: an instance of Grammar assumed to be the best grammar for the data
        """
        self.nodes_by_type = {}
        for node in syntactic_nodes:
            if node.type not in self.nodes_by_type:
                self.nodes_by_type[node.type] = []
            self.nodes_by_type[node.type].append(node)
        self.data = data
        self.target_grammar = Grammar(self.nodes_by_type, vocabulary, rules)

    def run(self):
        print("** Target grammar (score {}):".format(Hypothesis.get_mdl_score(self.target_grammar, self.data)))
        print(self.target_grammar)
        self.randomize_hypotheses()

    def randomize_hypotheses(self):
        # Start by just randomizing grammars and neighbors and seeing that their scores make sense
        # TODO move on to a search algorithm such as simulated annealing
        good_hypotheses = set()
        a = ord('a')
        possible_segments = [chr(i) for i in range(a, a+26)]
        for i in range(100000):
            hypothesis = Hypothesis.randomize_grammar(self.nodes_by_type, self.target_grammar.vocabulary, possible_segments)
            score = Hypothesis.get_mdl_score(hypothesis, self.data)
            if score < float('inf'):
                good_hypotheses.add(hypothesis)

        for hypothesis in sorted(good_hypotheses, key = lambda x : Hypothesis.get_mdl_score(x, self.data)):
            print("\n** Good hypothesis (score {}):".format(Hypothesis.get_mdl_score(hypothesis, self.data)))
            print(hypothesis)
            print()
