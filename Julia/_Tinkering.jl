include("TravelingSalesman.jl")
include("Visualization.jl")
include("LocationsList.jl")

l = semirandomlocations(9)

path = bruteforce(l)

f, ax, p = plotpath(path)
p.edge_color = p.edge_color[] # trigger observable
ax.aspect = DataAspect()
f
