using Test
using Combinatorics
include("Location.jl")

function minimumby(f, itr)
    itr[argmin(map(f, itr))]
end

function bruteforce(locations::Array{Location, 1})::Array{Location, 1}
    c = collect(permutations(locations, length(locations)))
    return minimumby(pathlength, c)
end


println(bruteforce(semirandomlocations(10)))
