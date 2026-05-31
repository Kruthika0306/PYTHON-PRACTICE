import pandas as pd
import matplotlib.pyplot as plt


def main():
    student_data = pd.DataFrame({
        "Marks": [80, 85, 90, 75, 95],
        "Attendance": [90, 95, 98, 85, 99],
        "StudyHours": [4, 5, 6, 3, 7]
    })

    correlation_matrix = student_data.corr()

    plt.figure(figsize=(8, 5))

    plt.imshow(correlation_matrix)

    plt.colorbar()

    plt.xticks(
        range(len(correlation_matrix.columns)),
        correlation_matrix.columns
    )

    plt.yticks(
        range(len(correlation_matrix.columns)),
        correlation_matrix.columns
    )

    plt.title("Correlation Heatmap")

    plt.show()


if __name__ == "__main__":
    main()
