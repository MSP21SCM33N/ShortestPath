import pandas as pd


driv = pd.read_csv("../data/driving2.csv")
park = pd.read_csv("../data/parks.csv")
zone = pd.read_csv("../data/zones.csv")

class trip:
    def __init__(self,start_node,end_node):
        self.start_node = start_node
        self.end_node = end_node
        self.visited_states = []
        self.avoid_states = []
    
    def find