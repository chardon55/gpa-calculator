import pandas as pd

# from gpacalc.peking import PekingGPA
from gpacalc.tohoku import TohokuGPA


def main():
    df = pd.read_csv('./score.csv')

    print(df)

    p = TohokuGPA()
    gpa = p.calculate(df, "score", "weight")

    print(f"{gpa} / 4.0")


if __name__ == '__main__':
    main()
