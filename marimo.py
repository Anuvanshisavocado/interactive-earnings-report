# 23f3002037@ds.study.iitm.ac.in
import marimo as mo
import numpy as np
import matplotlib.pyplot as plt

# Cell 1: Define the interactive slider widget.
# The state of this widget ('threshold.value') is used by other cells.
threshold = mo.ui.slider(
    start=0, stop=10, step=0.5, value=5, label="X-axis Threshold:"
)

# Cell 2: Generate the base dataset.
# This cell is independent and provides the raw 'x' and 'y' data for analysis.
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = 2.5 * x + np.random.normal(0, 2, 100)

# Cell 3: Create dynamic markdown output.
# This cell's output depends on the slider from Cell 1.
# The text updates reactively as the user moves the slider.
md_output = mo.md(f"""
    ## Interactive Data Exploration
    This notebook analyzes the relationship between two variables.
    Currently displaying data points where the x-value is less than **{threshold.value}**.
""")

# Cell 4: Filter data and generate a plot.
# This cell's output (the plot) depends on the dataset from Cell 2
# and the interactive 'threshold' widget from Cell 1.
def create_plot(x_data, y_data, limit):
    """Filters data and returns a matplotlib figure."""
    mask = x_data < limit
    fig, ax = plt.subplots()
    
    # Plot the full dataset in the background
    ax.scatter(x_data, y_data, alpha=0.2, color='gray', label="Full Dataset")
    
    # Plot the filtered data on top
    ax.scatter(x_data[mask], y_data[mask], color='crimson', label="Selected Data")
    
    # Add a line to show the current threshold
    ax.axvline(limit, color='black', linestyle='--', label=f"Threshold")
    
    ax.set_title("Variable Relationship")
    ax.set_xlabel("Independent Variable (X)")
    ax.set_ylabel("Dependent Variable (Y)")
    ax.legend()
    ax.grid(True)
    return fig

plot = create_plot(x, y, threshold.value)


# Cell 5: Display the final composed UI.
# This cell aggregates the outputs from other cells into a final view.
mo.vstack([
    md_output,
    threshold, # Display the slider widget itself
    plot
])
