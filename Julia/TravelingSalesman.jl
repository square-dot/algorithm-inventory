using Test
using Combinatorics
using Plots
using Graphs
using GraphPlot
using Cairo
using GraphRecipes
include("Location.jl")
include("LocationsList.jl")

function minimumby(f, itr)
    itr[argmin(map(f, itr))]
end

function bruteforce(locations::Vector{Location})::Vector{Location}
    c = collect(permutations(locations, length(locations)))
    return minimumby(pathlength, c)
end

locations = semirandomlocations(5, 14)

println("solution:")
println(res)
println(pathlength(res))

function clusteringandsolving(locations::Vector{Location})::Vector{Location}
    lsts = clustering(locations, 4)
    totalpath = []
    for lst in lsts
        append!(totalpath, bruteforce(lst))
    end
    return totalpath
end

function plotpath(path)
    # Load the adjacency matrix and graph attributes
    adjmatrix = [i - j == 1 for i in 1:length(path), j in 1:length(path)]
    vec_xNode = [x.longitude for x in path]
    vec_yNode = [x.latitude for x in path]
    colors = [colorant"blue", colorant"red", colorant"yellow", colorant"green", colorant"violet"]
    mmb = [i%3 + 1 for i in 1:length(path)]
    nodefill = [colors[m] for m in mmb]
    print(length(vec_xNode) == length(nodefill))
    graphplot(adjmatrix, x=vec_xNode, y=vec_yNode, nodeshape=:circle, nodesize=4, nodefillc = nodefill)
end


plotpath(clusteringandsolving(locations))