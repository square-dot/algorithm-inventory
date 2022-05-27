using GLMakie
using GraphMakie
using Graphs
using GraphMakie.NetworkLayout


function plotpath(path)
    g = SimpleGraph(length(path))
    for i in 1:(length(path)-1)
        add_edge!(g, i, i+1)
    end
    edgecolors = [:black for i in 1:ne(g)]
    f, ax, p = graphplot(g, layout=Shell(),
                node_color=[:black, :red, :red, :red, :black],
                edge_color=edgecolors)
    hidedecorations!(ax); hidespines!(ax)
    ax.aspect = DataAspect()
    positions(_) = [(x.longitude, x.latitude) for x in path]
    # set new layout
    p.layout = positions; autolimits!(ax)
    # change edge width & color
    p.edge_width = 5.0
    p.edge_color[][3] = :green;
    p.edge_color = p.edge_color[] # trigger observable
    f, ax, p
end