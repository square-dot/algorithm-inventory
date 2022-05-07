include("TravelingSalesman.jl")
include("LocationsList.jl")

locations = semirandomlocations(5, 20)


g = SimpleGraph(3)
add_edge!(g, 1, 2)
add_edge!(g, 2, 3)

d = Dict2 = Dict(1 => [0, 234], 2 => [284, 0], 3 => [25, 23])

cols = [colorant"yellow", colorant"red", colorant"blue", colorant"green"]
graphplot(g,
    x=[0, 284, 25],
    y=[234, 0, 23],
    nodeshape=:circle,
    markersize=7,
    markercolor=cols,
    names=1:3,
    linecolor=:darkgrey
)

# const n = 4
# const A = Float64[rand() < 0.5 ? 0 : rand() for i = 1:n, j = 1:n]
# for i = 1:n
#     A[i, 1:i-1] = A[1:i-1, i]
#     A[i, i] = 0
# end

# graphplot(g,
#     markersize=20,
#     markercolor=range(colorant"yellow", stop=colorant"red", length=n),
#     xy=[[0, 1] [284, 3] [25, 5]],
#     names=1:n,
#     linecolor=:darkgrey
# )