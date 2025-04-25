import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, ScalarFormatter

df = pd.read_csv("execution-time-combined.csv")

if "latency_us" in df.columns:
    df["exec_time_us"] = df["latency_us"]

df["exec_time_ms"] = df["exec_time_us"] / 1000

df["test_type"] = df["test_type"].replace({
    "sensor_test": "Sensor Test",
    "loop_test": "Loop Test"
})

sns.set_theme(style="whitegrid")
plt.figure(figsize=(9, 6))

ax = sns.barplot(
    data=df,
    x="test_type",
    y="exec_time_ms",
    hue="version",
    ci="sd",
    palette="muted"
)

ax.set_yscale("log")
ax.yaxis.set_major_locator(LogLocator(base=10.0))
ax.yaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_minor_formatter(plt.NullFormatter())

plt.title("Execution Time Comparison: Native vs WASM", fontsize=16, weight="bold")
plt.xlabel("Test Type", fontsize=12)
plt.ylabel("Execution Time (ms, log scale)", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.savefig("execution_time_logscale.png", dpi=300)
plt.show()
