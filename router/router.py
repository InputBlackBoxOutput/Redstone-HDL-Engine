from itertools import permutations

class Router:
    ''' Channel router using the left edge algorithm '''

    def __init__(self, pins_A, pins_B, verbose=False):
        self.pins_A, self.pins_B = self.null_padding(pins_A, pins_B)
        self.verbose = verbose

        self.HCG = self.generate_horizontal_constraints_graph(self.pins_A, self.pins_B)
        self.VCG = self.generate_vertical_constraints_graph(self.pins_A, self.pins_B)
        self.left_edge_order = self.generate_left_edge_order(self.pins_A, self.pins_B)

        if self.verbose:
            print("Horizontal Constraints Graph:\n")
            for i in self.HCG:
                print(f"{i} : {self.HCG[i]}")

            print("\nVertical Constraints Graph:\n")
            for edge in self.VCG:
                print(f"{edge[0]} -> {edge[1]}")

            print("\nLeft edge order:\n")
            print(self.left_edge_order)

    def null_padding(self, pins_A, pins_B):
        len_A = len(pins_A)
        len_B = len(pins_B)

        if len_A != len_B:
            if len_A > len_B:
                pins_B += ['0' for _ in range(abs(len_A - len_B))]
            else:
                pins_A += ['0' for _ in range(abs(len_A - len_B))]

        return (pins_A, pins_B)

    def generate_horizontal_constraints_graph(self, pins_A, pins_B):
        
        HCG = {}
        passed_pins = []
        for i in range(len(pins_A)):
            HCG[i] = set(list(filter(lambda x:x!='0', [pins_A[i], pins_B[i]] + passed_pins)))

            if pins_A[i] not in passed_pins:
                passed_pins.append(pins_A[i])
            else:
                if pins_A[i] not in pins_A[i+1:] + pins_B[i+1:]:
                    passed_pins.remove(pins_A[i])

            if pins_B[i] not in passed_pins:
                passed_pins.append(pins_B[i])
            else:
                if pins_B[i] not in pins_A[i+1:] + pins_B[i+1:]:
                    passed_pins.remove(pins_B[i]) 

        # Restructure HCG
        HCG_restructured = {}
        for pin in set(pins_A + pins_B):
            HCG_restructured[pin] = set()

        for i in HCG:
            if len(HCG[i]) > 1:
                for each in HCG[i]:
                    HCG_restructured[each] = set.union(HCG_restructured[each], HCG[i])
                    HCG_restructured[each].discard(each)

        return HCG_restructured

    def generate_vertical_constraints_graph(self, pins_A, pins_B):

        VCG = []
        for i in range(len(pins_A)):
            if (pins_A[i], pins_B[i]) not in VCG:
                VCG.append((pins_A[i], pins_B[i]))

        # Remove self edges
        remove = []
        for edge in VCG:
            if edge[0] == edge[1]:
                remove.append(edge)
        
        for entity in remove:
            VCG.remove(entity)

        # Remove directed edges to null keeping solo nodes
        null_edges = []
        for edge in VCG:
            if '0' in edge:
                null_edges.append(edge)

        for null_edge in null_edges:
            VCG.remove(null_edge)

        for src, dst in null_edges:
            non_null_nodes = set([x for e in VCG for x in e])

            if src not in non_null_nodes and dst not in non_null_nodes:
                if src == '0':
                    VCG.append((dst, src))
                else:
                    VCG.append((src, dst))

        # Remove edges with transitivity
        trans_edge = []
        for src, dst in VCG:
            for edge_1, edge_2 in permutations(VCG, 2):
                if edge_1[1] == edge_2[0]:
                    if src == edge_1[0] and dst == edge_2[1]:
                        trans_edge.append((src, dst))

                # Cyclic conflict
                if edge_1[0] == edge_2[1] and edge_1[1] == edge_2[0]:
                    raise Exception("VCG - Cyclic conflict")

        for edge in trans_edge:
            VCG.remove(edge)

        return VCG

    def generate_left_edge_order(self, pins_A, pins_B):
        order = []
        for i in range(len(pins_A)):
            if pins_A[i] not in order and pins_A[i] != '0':
                order.append(pins_A[i])

            if pins_B[i] not in order and pins_B[i] != '0':
                order.append(pins_B[i])

        return order

    def route(self):
        n_pins = len(set(self.pins_A + self.pins_B))
        # n_nodes = len(set([x for e in self.VCG for x in e]))

        tracks = {}
        vertical = {}

        for i in range(n_pins):
            tracks[i] = []
            vertical[i] = []

        completed = []
        while(len(completed) < n_pins):

            # Find active nodes
            active = []
            for node in self.left_edge_order:
                if node not in [edge[1] for edge in self.VCG]:
                    if node not in completed:
                        active.append(node)

            # Process active nodes
            # print('-' * 50)
            # print(f"Active: {active}")
            if active == []:
                break

            current = active[0]           

            # Find track
            for track in range(len(tracks)):
                conflict = False
                for j in list(set(tracks[track] + vertical[track])):
                    if j in self.HCG[current]:
                        conflict = True

                vertical[track].append(current)

                if not conflict:
                    tracks[track].append(current)
                    vertical[track].remove(current)
                    break
            
            # Remove current from VCG
            updated_VCG = []
            for edge in self.VCG:
                if edge[0] != current:
                    updated_VCG.append(edge)                      
            
            self.VCG = updated_VCG
            completed.append(current)
            # print(f"Completed: {completed}\n")

        # Remove unassigned tracks
        remove = []
        for track in tracks:
            if tracks[track] == []:
                remove.append(track)
        
        for entity in remove:
            tracks.pop(entity)

        if self.verbose:
            print(f"\nRouter output:\n\n{tracks}")

        return (self.pins_A, self.pins_B, tracks)


if __name__ == "__main__":
    # A = ['0', 'B', 'D', 'E', 'B', 'F', 'G', '0', 'D']
    # B = ['A', 'C', 'E', 'C', 'E', 'A', 'F', 'H', '0', 'H', 'G']

    A = ['0', 'A', 'D', 'E', 'A', 'F', 'G', '0', 'D', 'I', 'J', 'J']
    B = ['B', 'C', 'E', 'C', 'E', 'B', 'F', 'H', 'I', 'H', 'G', 'I']

    # A = ['0', 'A', 'B', 'E', 'A', 'F', 'G', '0', 'D', 'I', 'J', 'J', 'K', 'L']
    # B = ['B', 'C', 'E', 'C', 'L', 'D', 'F', 'H', 'I', 'H', 'G', 'I', 'J', 'K']

    # Cyclic conflict
    # A = ['A', 'B']
    # B = ['B', 'A']

    # Direct connection + Cross connection with null
    # A = ['A', 'B', '0', 'C']
    # B = ['A', '0', 'B', 'C']

    # A = ['A', '0', 'B', 'C']
    # B = ['A', 'B', '0', 'C']

    # Different notation
    # A = ['N1', '0', 'N2', 'N3']
    # B = ['N3', 'N2', 'N1']

    r = Router(pins_A=A, pins_B=B, verbose=True)
    r.route()
