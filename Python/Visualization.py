from bokeh.plotting import figure, output_file, show
from bokeh.models import GraphRenderer, StaticLayoutProvider, GlyphRenderer
from bokeh.palettes import Spectral8

from Location import *
from TravelingSalesman import *

N = 8

locations = [
    Location(0, 0),
    Location(0, 1),
    Location(0, 10),
    Location(0, 83),
    Location(1, 12),
    Location(1, 98),
    Location(2, 45),
    Location(5, 17),
    Location(10, 64),
    Location(12, 40),
    Location(13, 2),
    Location(25, 99),
    Location(28, 32),
    Location(30, 5),
    Location(30, 78),
    Location(45, 12),
    Location(48, 57),
    Location(50, 34),
    Location(53, 111),
    Location(52, 32),
    Location(60, 0),
    Location(72, 32),
    Location(100, 10),
    Location(110, 39),
    Location(112, 80),
    Location(120, 1),
    Location(142, 95),
]


def brute_force_nw():
    random.shuffle(locations[:7])
    return brute_force(locations)


res = brute_force_nw()

node_indices = list(range(len(res)))

plot = figure(
    title="Travelins salesman brute force",
    x_range=(-1.1, 1.1),
    y_range=(-1.1, 1.1),
    tools="",
    toolbar_location=None,
)

graph = GraphRenderer()

graph_layout = dict(zip(node_indices, zip([x[0] for x in res], [x[1] for x in res])))

graph.node_renderer = GlyphRenderer()

graph.edge_renderer = GlyphRenderer()


# graph.node_renderer.glyph = Ellipse(height=0.1, width=0.2,
#                                     fill_color="fill_color")


# assign a palette to ``fill_color`` and add it to the data source
graph.node_renderer.data_source.data = dict(
    index=node_indices,
    fill_color=Spectral8)

# add the rest of the assigned values to the data source
graph.edge_renderer.data_source.data = dict(
    start=[0]*N,
    end=node_indices)

graph.layout_provider = StaticLayoutProvider(graph_layout = graph_layout)

# render the graph
plot.renderers.append(graph)

# specify the name of the output file
output_file('graph.html')

# display the plot
show(plot)