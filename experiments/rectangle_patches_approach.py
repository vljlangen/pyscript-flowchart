from pyscript import when
from js import document
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Rectangle

def draw_flowchart(event=None):
    # Get user input from textarea
    text = document.querySelector("#flow-input").value

    # Split nodes by empty lines (two consecutive newlines)
    raw_nodes = text.split("\n\n")
    nodes = [node.strip() for node in raw_nodes if node.strip()]

    if len(nodes) < 2:
        document.querySelector("#flow-output").innerText = "Need at least 2 steps!"
        return

    # Build graph sequentially
    G = nx.DiGraph()
    for i in range(len(nodes)-1):
        G.add_edge(nodes[i], nodes[i+1])

    # Calculate maximum text width for consistent node sizing
    fontsize = 10
    max_chars = 0
    for node in nodes:
        lines = node.split('\n')
        max_line_length = max(len(line) for line in lines) if lines else 0
        max_chars = max(max_chars, max_line_length)
    
    # Calculate consistent width based on max characters
    # Roughly 0.6 units per character + padding
    consistent_width = max_chars * 0.6 + 1.0
    node_height = 0.8  # Fixed height for all nodes

    # Fixed vertical spacing
    v_step = 1.5  # distance between node centers
    pos = {nodes[i]: (0, -i * v_step) for i in range(len(nodes))}

    # Create figure with height proportional to number of nodes
    fig_height = len(nodes) * v_step * 0.9
    fig, ax = plt.subplots(figsize=(6, fig_height))

    # Draw arrows manually to control positioning
    arrow_offset = 0.26  # smaller offset for better arrow positioning
    
    for i in range(len(nodes)-1):
        # Calculate start and end points for arrows
        start_y = -i * v_step - arrow_offset  # bottom of current node
        end_y = -(i+1) * v_step + arrow_offset  # top of next node
        
        # Draw arrow line
        ax.annotate('', xy=(0, end_y), xytext=(0, start_y),
                   arrowprops=dict(arrowstyle='-|>', 
                                 lw=1.5, 
                                 color='black',
                                 shrinkA=0,  # don't shrink at start
                                 shrinkB=0))  # don't shrink at end

    # Set axis limits to accommodate consistent node width
    x_margin = consistent_width / 2 + 0.5  # Half width + margin
    ax.set_xlim(-x_margin, x_margin)
    ax.set_ylim(-len(nodes)*v_step - 0.5, 0.5)

    # Draw nodes with consistent width using Rectangle patches
    for node, (x, y) in pos.items():
        # Keep internal line breaks inside a node
        lines_in_node = node.split("\n")
        node_text = "\n".join(lines_in_node)

        # Calculate rectangle position (centered on x, y)
        rect_x = x - consistent_width / 2
        rect_y = y - node_height / 2
        
        # Draw rectangle background
        rect = Rectangle(
            (rect_x, rect_y), 
            consistent_width, 
            node_height,
            linewidth=1.5,
            edgecolor='black',
            facecolor='white'
        )
        ax.add_patch(rect)
        
        # Draw text on top
        plt.text(
            x, y, node_text,
            ha="center",
            va="center",
            fontsize=fontsize,
            wrap=True
        )

    ax.axis("off")
    plt.show()

# Attach button event
@when("click", "#draw-btn")
def on_draw(event):
    draw_flowchart()
