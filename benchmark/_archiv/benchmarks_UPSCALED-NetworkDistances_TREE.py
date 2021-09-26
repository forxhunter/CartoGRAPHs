

######################
#
# CAYLEY TREE
# Benchmarking - U P S C A L I N G 
# save network distances to files 
#
#####################

from benchmark_main import *

# 100
#branch=3
#i=121

# 500 
#branch=2
#i=511

# 1k
#branch=3
#i=1093

# 5k
#branch=4
#i=5461

# 10 k
#branch=3
#i=9841

# 20 k
branch=5
i=19531

G = nx.full_rary_tree(branch,i)
print(len(G.nodes()))

print('calculate network distance')
dist_network = pairwise_network_distance(G)
print('distances network done')

a_file = open('netdist_precalc/dist_network_'+str(i)+'_tree.pkl', "wb")
pickle.dump(dist_network, a_file)
a_file.close()

#b_file = open('dist_network_'+str(i)+'_tree.pkl', "rb")
#dist_network = pickle.load(b_file)
#print(len(dist_network))
