class Datum:
    def __init__(self, root_node, feature_nodes, surface_form):
        self.root_node = root_node
        self.feature_nodes = feature_nodes
        self.surface_form = surface_form

    def __repr__(self):
        return "<Datum instance> {}\n\troot_node={}\n\tfeature_nodes={}".format(self.surface_form, self.root_node, self.feature_nodes)
