import random
import math
from rule import Rule
from grammar import Grammar
from syntactic_node import SyntacticNode

INF = float('inf')


class Hypothesis:

    @classmethod
    def get_mdl_score(cls, grammar, data):
        if not cls.validate_rules(grammar.rules):
            return INF
        data_given_grammar_length = cls.get_data_given_grammar_encoding_length(grammar, data)
        if data_given_grammar_length == INF:
            return INF
        return grammar.get_encoding_length() + data_given_grammar_length

    @classmethod
    def validate_rules(cls, rules):
        # TODO do we need this step? (e.g. there can only be 1 'elsewhere' rule per set of input nodes etc.)
        return True

    @classmethod
    def get_data_given_grammar_encoding_length(cls, grammar, data):
        length = 0
        for datum in data:
            current_length = grammar.get_encoding_length_of_datum_given_grammar(datum)
            if current_length == INF:
                return INF
            length += current_length
        return length

    @classmethod
    def randomize_grammar(cls, nodes_by_type, vocabulary, possible_segments):
        # Randomize rules
        min_rules_num = 1
        max_rules_num = 2
        rules_num = random.randint(min_rules_num, max_rules_num)
        max_num_feature_nodes_per_rule = 1
        max_num_affix_segments_per_rule = 1
        max_num_environment_roots = len(nodes_by_type[SyntacticNode.TYPE_ROOT])

        rules = []
        for i in range(rules_num):
            num_feature_nodes = random.randint(1, max_num_feature_nodes_per_rule)
            feature_nodes = random.choices(nodes_by_type[SyntacticNode.TYPE_FEATURE], k=num_feature_nodes)

            num_affix_segments = random.randint(0, max_num_affix_segments_per_rule)
            output_affix = ''
            for _ in range(num_affix_segments): # We don't use choices because segments in affix can repeat
                output_affix += random.choice(possible_segments)

            num_environment_roots = random.randint(0, max_num_environment_roots)
            environment_roots = random.sample(nodes_by_type[SyntacticNode.TYPE_ROOT], k=num_environment_roots)
            rules.append(Rule(feature_nodes, output_affix, environment_roots))

        return Grammar(nodes_by_type, vocabulary, rules)

    @classmethod
    def randomize_neighbor(cls, grammar, possible_roots, possible_segments):
        pass # TODO
