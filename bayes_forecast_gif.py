import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.stats import norm
import streamlit as st
import os

# Set page title
st.set_page_config(page_title="Bayesian Forecast GIF Demo")

st.title("📊 Bayesian Forecast Animation")
st.markdown("This app shows the evolution of a forecast distribution as confidence increases over time.")

# Monthly steps
months = ['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
          'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar']
n = len(months)
x = np.linspace(140, 180, 400)

# Simulated evolving forecast
means = np.linspace(158, 160.5, n)
stds = np.linspace(10, 1.5, n)
pdfs = [norm.pdf(x, loc=means[i], scale=stds[i]) for i in range(n)]

# Output path
gif_path = "bayesian_forecast.gif"

# Only create gif if it doesn't already exist
if not os.path.exists(gif_path):
    fig, ax = plt.subplots(figsize=(8, 4))
    line, = ax.plot([], [], color='blue')
    title = ax.text(0.5, 1.05, '', transform=ax.transAxes, ha='center', fontsize=12)

    ax.set_xlim(140, 180)
    ax.set_ylim(0, 0.3)
    ax.set_xlabel("Predicted Output (10,000 tons)")
    ax.set_ylabel("Probability Density")
    ax.grid(True)

    def animate(i):
        line.set_data(x, pdfs[i])
        title.set_text(f"Forecast PDF – {months[i]}")
        return line, title

    ani = animation.FuncAnimation(fig, animate, frames=n, interval=800, blit=True)
    ani.save(gif_path, writer='pillow')

# Display the GIF
st.image(gif_path, caption="Bayesian Distribution Evolution")
