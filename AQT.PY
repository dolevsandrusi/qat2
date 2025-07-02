import streamlit as st
import json
import matplotlib.pyplot as plt

# Streamlit app title
st.title("Sample Data Visualization App")

# File uploader for JSON file
uploaded_file = st.file_uploader("Upload a JSON file with sample data", type="json")

# Proceed only if a file is uploaded
if uploaded_file is not None:
    # Load JSON data
    data = json.load(uploaded_file)

    # Extract TIME and frequency values
    time_values = [sample["TIME"] for sample in data]
    frequencies = [sample["frequency"] for sample in data]

    # Compute ΔTIME between consecutive samples
    delta_time = [time_values[i+1] - time_values[i] for i in range(len(time_values) - 1)]
    y_values = time_values[1:]  # Corresponding TIME values for delta_time
    color_values = frequencies[1:]  # Frequency values for color mapping

    # UI: Select colormap
    colormap = st.selectbox("Choose a color map for frequency", ["viridis", "plasma", "inferno", "magma", "cividis"])

    # Plot the graph
    fig, ax = plt.subplots()
    scatter = ax.scatter(delta_time, y_values, c=color_values, cmap=colormap)
    ax.invert_yaxis()  # Invert Y-axis so that lower TIME values appear at the top
    ax.set_xlabel("ΔTIME between samples (usec)")
    ax.set_ylabel("TIME of sample (usec)")
    ax.set_title("TIME vs ΔTIME with Frequency-based Colorization")
    fig.colorbar(scatter, ax=ax, label="Frequency")

    # Display the plot in Streamlit
    st.pyplot(fig)
else:
    st.info("Please upload a JSON file to begin.")

