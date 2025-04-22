import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("combinedtests.csv")

if "latency_us" in df.columns:
    df["exec_time_us"] = df["latency_us"]

df["exec_time_ms"] = df["exec_time_us"] / 1000

sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=False)

loop_df = df[df["test_type"] == "loop_test"]
sensor_df = df[df["test_type"] == "sensor_test"]

sns.barplot(
    data=loop_df,
    x="test_type",
    y="exec_time_ms",
    hue="version",
    ci="sd",
    palette="muted",
    ax=axes[0]
)

axes[0].set_title("Loop Test Execution Time", fontsize=14, weight="bold")
axes[0].set_xlabel("Test Type")
axes[0].set_ylabel("Execution Time (ms)")

sns.barplot(
    data=sensor_df,
    x="test_type",
    y="exec_time_ms",
    hue="version",
    ci="sd",
    palette="muted",
    ax=axes[1]
)

axes[1].set_title("Sensor Test Execution Time", fontsize=14, weight="bold")
axes[1].set_xlabel("Test Type")
axes[1].set_ylabel("Execution Time (ms)")

plt.tight_layout()
plt.savefig("execution_time_split.png", dpi=300)
plt.show()
