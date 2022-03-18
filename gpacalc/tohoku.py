import numpy as np
import pandas as pd

from . import gpabase as b


class TohokuGPA(b.GPACalcModule):
    '''
        GPA calculation method (Cumulative) of Tohoku University since April 1, 2016
        (UNTESTED)

        For details: https://www.tohoku.ac.jp/en/academics/cn_gpa.html
    '''

    def calculate(self, df: pd.DataFrame, score_col: str, grade_weight_col: str) -> np.float:
        df1 = df.copy()

        df1.drop(index=df1[df1[score_col] < 60].index, inplace=True)
        df1[score_col] = df1[score_col] // 10 - 5
        df1.replace(5, 4, inplace=True)

        print(df1)

        return (df1[score_col] * df1[grade_weight_col]).sum() / df[grade_weight_col].sum()
