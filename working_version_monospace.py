from pyscript import when
from js import document
import matplotlib.pyplot as plt
import networkx as nx

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

    # Set axis limits for spacing
    ax.set_xlim(-3, 3)
    ax.set_ylim(-len(nodes)*v_step - 0.5, 0.5)

    # Find the longest line across all nodes for consistent width
    max_chars = 0
    for node in nodes:
        lines = node.split('\n')
        max_line_length = max(len(line) for line in lines) if lines else 0
        max_chars = max(max_chars, max_line_length)
    
    # Draw nodes with character padding for consistent width
    for node, (x, y) in pos.items():
        # Keep internal line breaks inside a node
        lines_in_node = node.split("\n")
        
        # Pad each line to the same length with even distribution
        padded_lines = []
        for line in lines_in_node:
            # Add spaces to pad the line to max_chars length
            padding_needed = max_chars - len(line)
            # Distribute padding evenly on both sides
            left_padding = padding_needed // 2
            right_padding = padding_needed - left_padding
            padded_line = " " * left_padding + line + " " * right_padding
            padded_lines.append(padded_line)
        
        node_text = "\n".join(padded_lines)

        plt.text(
            x, y, node_text,
            ha="center",
            va="center",
            fontsize=10,
            fontfamily="monospace",  # Use monospace font for consistent character widths
            wrap=True,
            bbox=dict(
                boxstyle="square,pad=0.6",  # square box with more padding
                facecolor="white",
                edgecolor="black",
                linewidth=1.5
            )
        )
    
    # Show the target width in title
    plt.title(f"All lines padded to {max_chars} characters", fontsize=8, pad=10)

    ax.axis("off")
    plt.show()

# Attach button event
@when("click", "#draw-btn")
def on_draw(event):
    draw_flowchart()