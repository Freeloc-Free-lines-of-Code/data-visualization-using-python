import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = [
    "USA",
    "Switzerland",
    "Germany",
    "United Kingdom",
    "France",
    "Australia",
    "India",
]
salary = [106816, 88773, 54705, 59072, 40558, 47147, 7105]
col = [31524, 45715, 26562, 33831, 29738, 27772, 3272]

x = np.arange(len(labels))
width = 0.40  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, salary, width, label="Software Developer Salary")
rects2 = ax.bar(x + width / 2, col, width, label="Cost of living")

ax.set_xlabel("Countries")
ax.set_ylabel("Money (in Dollars)")
ax.set_title("Countries Software Developer Salary VS Cost of living")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate(
            "{}".format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
        )


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()