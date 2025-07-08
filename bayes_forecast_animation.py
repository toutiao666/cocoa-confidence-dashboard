import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.stats import norm

# Generate time axis (monthly steps)
months = ['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
          'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar']
n = len(months)
x = np.linspace(140, 180, 400)  # x-axis: production output in 10k tons

# Simulate forecast evolution: mean shifts slightly, stddev narrows
means = np.linspace(158, 160.5, n)         # gradual forecast drift
stds = np.linspace(10, 1.5, n)             # confidence improves over time

# Build list of monthly PDFs (normal distributions)
pdfs = [norm.pdf(x, loc=means[i], scale=stds[i]) for i in range(n)]

# Set up animation figure
fig, ax = plt.subplots(figsize=(10, 5))
line, = ax.plot([], [], color='blue', lw=2)
title = ax.text(0.5, 1.05, '', transform=ax.transAxes,
                ha='center', fontsize=14)

ax.set_xlim(140, 180)
ax.set_ylim(0, 0.3)
ax.set_xlabel("Predicted Output (10,000 tons)")
ax.set_ylabel("Probability Density")
ax.set_title("Bayesian Forecast Distribution")
ax.grid(True)

# Animation function
def animate(i):
    line.set_data(x, pdfs[i])
    title.set_text(f"Forecast PDF – {months[i]}")
    return line, title

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=n,
                              interval=800, blit=True)

plt.tight_layout()
plt.show()
