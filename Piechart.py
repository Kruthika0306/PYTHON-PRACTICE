import matplotlib.pyplot as plt


def main():
    departments = ["CSE", "ISE", "ECE", "ME"]
    students = [120, 90, 80, 60]

    plt.figure(figsize=(8, 5))

    plt.pie(
        students,
        labels=departments,
        autopct="%1.1f%%"
    )

    plt.title("Student Distribution by Department")

    plt.show()


if __name__ == "__main__":
    main()
