from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from time import clock
import pandas as pd
start = clock()

G = BayesianModel()

G.add_edge('Burglary', 'Alarm')
G.add_edge('Earthquake', 'Alarm')
#G.add_edge('Alarm', 'JohnCalls')
#G.add_edge('Alarm', 'MaryCalls')
#print(len(G))

cpd_burglary = TabularCPD('Burglary', 2, [[0.999],[0.001]])
cpd_earthquake = TabularCPD('Earthquake', 2, [[0.998],[0.002]])
cpd_alarm = TabularCPD('Alarm', 2, [[0.999, 0.71, 0.06, 0.05],[0.001, 0.29, 0.94, 0.95]], evidence = ['Burglary','Earthquake'], evidence_card=[2,2])
cpd_JC = TabularCPD('JohnCalls', 2, [[0.95, 0.10],[0.05, 0.90]], evidence = ['Alarm'], evidence_card=[2])
cpd_MC = TabularCPD('MaryCalls', 2, [[0.99, 0.30],[0.01, 0.70]], evidence = ['Alarm'], evidence_card=[2])
#print(cpd_MC)
#print(G.check_model())
G.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_JC, cpd_MC)
#G.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm)
#print(G.check_model())

d = {'Burglary': [0], 'Alarm': [1, 1]}
df = pd.DataFrame(data = d)

#values = pd.DataFrame(columns = 'Burglary': [0, 1], 'Alarm': [1, 1])

#G.fit(d)

solution = G.predict(df)
print(solution)

#print(clock()-start)
