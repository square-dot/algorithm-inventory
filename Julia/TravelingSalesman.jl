using Test
using Combinatorics
using Plots
using Graphs
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
    lsts = clustering(locations, 9)
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

function extendshortestpath!(path, newlocation)
    closestelement = closestelements([newlocation], path)[2]
    idx = findfirst(isequal(closestelement), path)
    if idx == 1
        if distance(path[end], newlocation) < distance(path[2], newlocation)
            insert!(path, 1, newlocation)
        else
            insert!(path, 2, newlocation)
        end
    elseif idx == length(path)
        if distance(path[end - 1], newlocation) < distance(path[1], newlocation)
            insert!(path, length(path), newlocation)
        else
            push!(path, newlocation)
        end
    else
        if distance(path[idx - 1], newlocation) < distance(path[idx + 1], newlocation)
            insert!(path, idx, newlocation)
        else
            insert!(path, idx + 1, newlocation)
        end
    end
end



global locations = semirandomlocations(5, 25)

global path = bruteforce(locations[1:4])

for l in locations[5:end]
    extendshortestpath!(path, l)
    plotpath(path, ["" for l in path])
    sleep(0.2)
end

plotpath(path, ["" for l in path])
