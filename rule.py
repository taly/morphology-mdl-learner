class Rule:

    EMPTY_SET = 'emptyset'
    RULE_COMPONENT_DELIMITER = '#rc'
    SYNTACTIC_NODE_DELIMITER = '#sn'
    ENVIRONMENT_ROOT_DELIMITER = '#er'

    COMPONENT_ENCODINGS = {
        EMPTY_SET: '0000',
        RULE_COMPONENT_DELIMITER: '0001',
        SYNTACTIC_NODE_DELIMITER: '0010',
        ENVIRONMENT_ROOT_DELIMITER: '0011'
    }

    def __init__(self, input_nodes, output_affix, environment_roots):
        """
        Represents a morphological vocabulary insertion rule.
        :param input_nodes: a list of SyntacticNode instances
        :param output_affix: a string representing the affix instructed by the rule
        :param environment_roots: a list of SyntacticNode instances representing roots where rule applies
        """
        self.input_nodes = input_nodes
        self.output_affix = output_affix
        self.environment_roots = sorted(environment_roots, key = lambda x: x.repr) if environment_roots else environment_roots

    def get_encoding_length(self):
        # See _repr_ to understand how a rule is encoded.
        # Here we assume that delimiters have fixed lengths specified in this class.

        # First add the constant number of rule component delimiters, and the output affix
        length = 3 * self._get_component_length(Rule.RULE_COMPONENT_DELIMITER) + len(self.output_affix)

        # Then add input nodes if necessary
        for i in range(len(self.input_nodes)):
            length += self.input_nodes[i].get_encoding_length()
            if i < len(self.input_nodes) - 1: # No need to add delimiter after last node
                length += self._get_component_length(Rule.SYNTACTIC_NODE_DELIMITER)

        # Then add environment roots if necessary (with delimiters between them)
        if self.environment_roots:
            length += (len(self.environment_roots) - 1) * self._get_component_length(Rule.ENVIRONMENT_ROOT_DELIMITER)
            for root in self.environment_roots:
                length += root.get_encoding_length()

        return length

    def _get_component_length(self, delimiter):
        return len(Rule.COMPONENT_ENCODINGS[delimiter])

    def __repr__(self):
        """
        General format:
        [INPUT NODES] -> -AFFIX / [ENVIRONMENT ROOTS]

        Examples:
        [+PL] -> -z
        [+PL] -> -emptyset / [DEER]
        """
        # Assuming that affix is singular and is a suffix for now. TODO sophisticate.
        affix_str = self.output_affix if self.output_affix else 'Ø'
        ret = "[{}] -> -{}".format(','.join(repr(x) for x in self.input_nodes), affix_str)

        if self.environment_roots:
            ret += " / [{}]".format(','.join(repr(x) for x in self.environment_roots))

        return ret
