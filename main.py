import pandas as pd

from gpacalc.gpa import gpa_calc_pku


def main():
    df = pd.read_csv('./score1.csv')

    print(df)

    gpa = gpa_calc_pku(df, "score", "weight")

    print(f"{gpa} / 4.0")


if __name__ == '__main__':
    main()
