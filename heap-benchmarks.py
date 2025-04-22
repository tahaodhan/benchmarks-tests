import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("benchmark.csv")

# Convert heap used from bytes to kilobytes
df["heap_kb"] = df["heap_used"] / 1024

# Set Seaborn style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))

# Plot grouped bar chart
ax = sns.barplot(
    data=df,
    x="test_type",
    y="heap_kb",
    ci="sd",         # Show standard deviation as error bars
    palette="muted",
    width=0.6
)

# Styling
plt.title("Memory Usage Comparison: Native vs WASM", fontsize=14, weight='bold')
plt.xlabel("Test Type", fontsize=12)
plt.ylabel("Heap Usage (KB)", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()

# Save and show
plt.savefig("memory_usage_comparison.png", dpi=300)
plt.show()
