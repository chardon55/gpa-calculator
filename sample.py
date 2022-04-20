import pandas as pd

# from gpacalc.peking import PekingGPA
# from gpacalc.tohoku import TohokuGPA
from gpacalc.kyoto import KyotoGPA


def main():
    df = pd.read_csv('./sample.csv')

    print(df)

    # p = TohokuGPA()
    # p = PekingGPA()
    p = KyotoGPA()

    gpa = p.calculate(df, "score", "weight")

    print(f"{gpa} / {p.full_gpa}")


if __name__ == '__main__':
    main()
