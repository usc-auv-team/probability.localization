from pgmpy.models import BayesianModel
G = BayesianModel()

G.add_node('Burglary')
G.add_node('Alarm')
G.add_node('Earthquake')
G.add_node('JohnCalls')
G.add_node('MaryCalls')

G.add_edge('Burglary', 'Alarm')
G.add_edge('Earthquake', 'Alarm')
G.add_edge('Alarm', 'JohnCalls')
G.add_edge('Alarm', 'MaryCalls')

cpd_a = TabularCPD('Burglary', 2, [[]])
