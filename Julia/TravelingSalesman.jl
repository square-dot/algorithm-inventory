using Test
using Combinatorics
include("Location.jl")
include("LocationsList.jl")
include("Visualization.jl")

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
    totalpath, labelslist = connectclustersandtag(solvedlsts)
    return totalpath, labelslist
end

function connectclustersandtag(lsts::Vector{Vector{Location}})
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
