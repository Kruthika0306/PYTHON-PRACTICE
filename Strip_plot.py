import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def main():
    data = pd.DataFrame({
        "Department": ["CSE"]*5 + ["ISE"]*5,
        "Marks": [80, 85, 78, 90, 88, 75, 82, 80, 79, 85]
    })

    sns.stripplot(x="Department", y="Marks", data=data)

    plt.title("Strip Plot")
    plt.show()


if __name__ == "__main__":
    main()
