using Test
using Combinatorics
using Plots
using Graphs
using GraphPlot
using Cairo
using GraphRecipes
include("Location.jl")

function minimumby(f, itr)
    itr[argmin(map(f, itr))]
end

function bruteforce(locations::Array{Location,1})::Array{Location,1}
    c = collect(permutations(locations, length(locations)))
    return minimumby(pathlength, c)
end

locations = semirandomlocations(5, 14)

res = bruteforce(locations)

println("solution:")
println(res)
println(pathlength(res))



# Load the adjacency matrix and graph attributes
adjmatrix = [i - j == 1 for i in 1:length(locations), j in 1:length(locations)]

vec_xNode = [x.longitude for x in res]
vec_yNode = [x.latitude for x in res]

# Plot the graph
graphplot(adjmatrix, x=vec_xNode, y=vec_yNode, nodeshape=:circle, nodesize=4, nodecolor = colorant"#389826")