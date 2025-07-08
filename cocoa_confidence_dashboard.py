import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Make sure font works on Streamlit Cloud
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['axes.unicode_minus'] = False

# Generate time points from March 2025 to March 2026
dates = pd.date_range('2025-03-01', '2026-03-01', freq='MS')
t = np.arange(len(dates))

# Simulated median forecast and confidence interval width
mid = 160 + 2 * np.sin(t / 3)  # central estimate
ci_width = 20 * np.exp(-0.2 * t)  # uncertainty narrows over time
upper = mid + ci_width
lower = mid - ci_width

# Streamlit layout
st.title("📈 Cocoa 03 Contract: Forecast Confidence Dashboard")
st.markdown(
    "This tool visualizes how forecast confidence improves over time, "
    "as uncertainty narrows and market information increases."
)

# Slider to select a time point
idx = st.slider("Select forecast month", 0, len(dates) - 1, len(dates) - 1)
st.metric("Median forecast", f"{mid[idx]:.1f} 10k tons")
st.metric("95% Confidence Interval", f"{lower[idx]:.1f} – {upper[idx]:.1f} 10k tons")

# Plot the chart
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(dates, mid, color='blue', label='Median forecast')
ax.fill_between(dates, lower, upper, color='skyblue', alpha=0.3, label='95% Confidence Band')
ax.axvline(dates[idx], color='red', linestyle='--', alpha=0.6)
ax.set_title("Forecast Uncertainty Shrinks as Delivery Approaches")
ax.set_ylabel("Forecasted Output (10,000 tons)")
ax.grid(True)
ax.legend()
st.pyplot(fig)
