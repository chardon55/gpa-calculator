import pandas as pd

from gpacalc.peking import PekingGPA


def main():
    df = pd.read_csv('./score1.csv')

    print(df)

    p = PekingGPA()
    gpa = p.calculate(df, "score", "weight")

    print(f"{gpa} / 4.0")


if __name__ == '__main__':
    main()
