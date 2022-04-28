from bokeh.plotting import figure, output_file, show
from bokeh.models import GraphRenderer, StaticLayoutProvider, GlyphRenderer, ColumnDataSource, CDSView, Ellipse
from bokeh.palettes import Spectral8

from Location import *
from TravelingSalesman import *

N = 5

locations = [Location(4651, 2995),
        Location(509, 136),
        Location(3704, 159),
        Location(4535, 4138),
        Location(9240, 9938),
        Location(8245, 8199),
        Location(3072, 5157),
        Location(9671, 2529),
        Location(6289, 2486),
        Location(7941, 2793),
        Location(8771, 729),
        Location(737, 1368),
        Location(9244, 4745),
        Location(2000, 8230),
        Location(2078, 689),
        Location(6404, 1473),
        Location(1328, 6985),
        Location(5975, 1056),
        Location(4227, 4882),
        Location(8908, 5486),
        Location(4870, 9874),
        Location(9796, 8575),
        Location(2631, 1801),
        Location(7874, 1275),
        Location(8645, 4815),
        Location(6881, 3631),
        Location(1154, 4880),
        Location(8401, 960),
        Location(6777, 223),
        Location(4198, 1024),
        Location(8791, 756),
        Location(1542, 9891),
        Location(5681, 4278),
        Location(5937, 784),
        Location(7914, 7373),
        Location(5015, 4892),
        Location(8724, 5728),
        Location(5763, 6189),
        Location(5369, 4768),
        Location(9491, 3942),
        Location(1826, 5641),
        Location(7803, 9888),
        Location(7139, 1582),
        Location(1128, 57),
        Location(7025, 4669),
        Location(4521, 9802),
        Location(24, 5944),
        Location(4147, 628),
        Location(5225, 2339),
        Location(376, 7549),
        Location(1854, 208),
        Location(8197, 9688),
        Location(3768, 7160),
        Location(3810, 6077),
        Location(5127, 5217),
        Location(4035, 4691),
        Location(9279, 8941),
        Location(6508, 9918),
        Location(7624, 1263),
        Location(7574, 1237),
        Location(1300, 7589),
        Location(8082, 993),
        Location(7567, 9721),
        Location(6792, 8905),
        Location(7638, 5894),
        Location(6427, 5290),
        Location(180, 1451),
        Location(8142, 8838),
        Location(8054, 7312),
        Location(8774, 859),
        Location(7150, 5487),
        Location(9158, 9068),
        Location(8979, 3612),
        Location(6211, 5590),
        Location(388, 4293),
        Location(1727, 6695),
        Location(8224, 1388),
        Location(4851, 3996),
        Location(6764, 9904),
        Location(6183, 6973),
        Location(5356, 924),
        Location(169, 5844),
        Location(1023, 8647),
        Location(9774, 8134),
        Location(350, 5636),
        Location(7111, 5900),
        Location(9974, 836),
        Location(4364, 7336),
        Location(397, 5445),
        Location(7480, 3248),
        Location(2222, 5781),
        Location(7257, 7523),
        Location(2345, 2813),
        Location(7875, 738),
        Location(4199, 1824),
        Location(5952, 7154),
        Location(6163, 5882),
        Location(5946, 9919),
        Location(5063, 5675),
        Location(2308, 4812),]


def brute_force_nw():
    return brute_force(locations[:5])


res = brute_force_nw()

node_indices = list(range(len(res)))

plot = figure(
    title="Traveling salesman brute force",
    x_range=(-1.1, 1.1),
    y_range=(-1.1, 1.1),
    tools="",
    toolbar_location=None,
)

graph = GraphRenderer()

graph_layout = dict(zip(node_indices, zip([x.longitude for x in res], [x.latitude for x in res])))

graph.node_renderer = GlyphRenderer(view=CDSView())

graph.edge_renderer = GlyphRenderer(view=CDSView())


graph.node_renderer.glyph = Ellipse(height=0.1, width=0.2,
                                    fill_color="fill_color")

graph.node_renderer.data_source = ColumnDataSource()
graph.edge_renderer.data_source = ColumnDataSource()

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