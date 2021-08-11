import numpy as np
import pandas as pd


def gpa_calc_pku(df: pd.DataFrame, score_col: str, grade_weight_col: str, max_score_col=None) -> np.float:
    """ GPA calculator using Peking University's calculation method """

    grade_weight_sum = df[grade_weight_col].sum()

    df1 = df.copy()
    if max_score_col is not None:
        df1[score_col] /= df[max_score_col]
        df1[score_col] *= 100

    df1.drop(index=df1[df1[score_col] < 60].index, inplace=True)
    df1[score_col] = 4 - 3 * (100 - df1[score_col]) ** 2 / 1600

    point_scores = df1[score_col] * df1[grade_weight_col]
    return point_scores.sum() / grade_weight_sum
