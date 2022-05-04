using Test
using Random

struct Location
    longitude::Int
    latitude::Int
end

function distance(location::Location, otherlocation::Location)
    return sqrt((location.longitude - otherlocation.longitude)^2 + (location.latitude - otherlocation.latitude)^2)
end

function distance(location::Location, otherlocations::Vector{Location})
    return min(map(x -> distance(location, x), otherlocations)...)
end

function distance(otherlocations::Vector{Location}, location::Location)
    return distance(location, otherlocations)
end

function distance(locations::Vector{Location}, otherlocations::Vector{Location})
    return min(map(x -> distance(locations, x), otherlocations)...)
end

function closestelements(locations, otherlocations)::Vector{Location}
    closestelements = [locations[1], otherlocations[1]]
    dst = distance(closestelements...)
    for loc in locations
        for otherloc in otherlocations
            if dst > distance(loc, otherloc)
                closestelements = [loc, otherloc]
                dst = distance(loc, otherloc)
            end
        end
    end
    return closestelements
end

function pathlength(locations::Vector{Location})::Float64
    tot = 0
    for i = 1:(length(locations)-1)
        tot += distance(locations[i], locations[i+1])
    end
    return tot
end

function clusteringdistances(locations)
    otherlocations = copy(locations)
    cluster = [pop!(otherlocations)]
    distances = []
    while !isempty(otherlocations)
        pair = closestelements(cluster, otherlocations)
        push!(cluster, pair[2])
        deleteat!(otherlocations, findall(x->x==pair[2], otherlocations))
        push!(distances, distance(pair[1], pair[2]))
    end
    sort!(distances)
    return distances        
end

function clustering(locations::Vector{Location}, n)
    stair = clusteringdistances(locations)
    dist = stair[end-n + 1]
    lsts::Vector{Vector{Location}} = [[locations[1]]]
    for location in locations
        if location == locations[1]
            continue
        end
        idxs = findall(x->distance(location, x) <= dist, lsts)
        mergedcollections = mergecollections(lsts, idxs)
        push!(mergedcollections, location)
        deleteat!(lsts, idxs)
        push!(lsts, mergedcollections)
    end
    return lsts
end

function mergecollections(collection::Vector{Vector{Location}}, indexes)::Vector{Location}
    mergedcollections = []
    for i in indexes
        append!(mergedcollections, collection[i])
    end
    return mergedcollections
end

function randomlocations(n::Int)::Vector{Location}
    v = Vector{Location}(undef, n)
    r = rand(1:1000, 2 * n, 1)
    for i = 1:n
        longi = r[i]
        lati = r[i+n]
        v[i] = Location(longi, lati)
    end
    return v
end


@testset "Distance" begin
    @test distance(Location(0, 0), Location(3, 4)) == 5
    @test distance(Location(0, 0), [Location(3, 4), Location(100, 100)]) == 5
    @test distance([Location(3, 4), Location(100, 100)], Location(0, 0)) == 5
    @test distance([Location(0, 100), Location(0, 0)], [Location(3, 4), Location(100, 100)]) == 5
end

@testset "Clustering" begin
    @test length(clustering([Location(0, 0), Location(1,1), Location(1, 10), Location(1, 11)], 2)) == 2
end

@test pathlength([Location(0, 0), Location(3, 4), Location(0, 0)]) == 10



@test length(randomlocations(5)) == 5