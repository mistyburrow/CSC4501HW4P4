import networkx as nx

class SDNController:
    def __init__(self):
        self.topology = nx.Graph()
        self.flow_table = {}  
        self.backup_paths = {} 

    def add_node(self, node_id):
        self.topology.add_node(node_id)

    def remove_node(self, node_id):
        self.topology.remove_node(node_id)

    def add_link(self, node1, node2, weight=1):
        self.topology.add_edge(node1, node2, weight=weight)

    def remove_link(self, node1, node2):
        self.topology.remove_edge(node1, node2)

    def compute_shortest_path(self, src, dest):
        return nx.shortest_path(self.topology, source=src, target=dest, weight='weight')

    def add_flow(self, flow_id, src, dest, bandwidth):
        path = self.compute_shortest_path(src, dest)
        self.flow_table[flow_id] = {'src': src, 'dest': dest, 'path': path, 'bandwidth': bandwidth}

    def handle_link_failure(self, failed_link):
        pass

    def visualize_network(self):
        import matplotlib.pyplot as plt
        import networkx as nx
        pos = nx.spring_layout(self.topology)
        nx.draw(self.topology, pos, with_labels=True, node_size=500, node_color="skyblue")
        plt.show()

    def cli(self):
        while True:
            cmd = input("SDN Controller CLI > ")
            pass

if __name__ == '__main__':
    controller = SDNController()
    controller.cli()

# import hashlib
# student_id = "898230981"
# secret = "NeoDDaBRgX5a9"
# hash_val = hashlib.sha256((student_id + secret).encode()).hexdigest()

