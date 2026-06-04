import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def main():
    data = pd.DataFrame({
        "Marks": [80, 85, 90, 75, 95, 88],
        "StudyHours": [4, 5, 6, 3, 7, 5],
        "Attendance": [90, 95, 98, 85, 99, 92]
    })

    sns.pairplot(data)

    plt.show()


if __name__ == "__main__":
    main()
