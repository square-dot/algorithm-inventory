using Test
using Combinatorics
using Plots
using Graphs
# using GraphPlot
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

function clusteringandsolving(locations::Vector{Location})
    lsts = clustering(locations, 4)
    solvedlsts = [bruteforce(l) for l in lsts]
    totalpath, labelslist = connectclusters(solvedlsts)
    return totalpath, labelslist
end

function connectclusters(lsts::Vector{Vector{Location}})
    avgs = map(average, lsts)
    ordering = bruteforce(avgs)
    totalpath = []
    labelslist = []
    labels=[:a, :b, :c, :d, :d, :f, :g, :h]
    for (index, el) in enumerate(ordering)
        referencelist = lsts[findfirst(x -> x == el, avgs)]
        append!(totalpath, referencelist)
        append!(labelslist, [labels[index] for p in referencelist])
    end
    return totalpath, labelslist
end


function plotpath(path, labelslist)
    g = SimpleGraph(length(path))
    for i in 1:(length(path)-1)
        add_edge!(g, i, i+1)
    end
    vec_xNode = [x.longitude for x in path]
    vec_yNode = [x.latitude for x in path]
    graphplot(g,
        x=vec_xNode,
        y=vec_yNode,
        nodeshape=:circle,
        markersize=12,
        names=labelslist,
        markercolor=[colorant"yellow"],
        )
end



locations = semirandomlocations(5, 20)


plotpath(clusteringandsolving(locations)...)