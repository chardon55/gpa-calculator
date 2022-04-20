import numpy as np
import pandas as pd

from . import gpabase as b


class TohokuGPA(b.GPACalcModule):
    '''
        GPA calculation method (Cumulative) of Tohoku University since March 3, 2020.

        For details: https://www.tohoku.ac.jp/japanese/studentinfo/education/01/education0110/015_2.pdf (Japanese)
    '''

    def calculate(self, df: pd.DataFrame, score_col, grade_weight_col) -> np.float:
        df1 = df.copy()

        df1.drop(index=df1[df1[score_col] < 60].index, inplace=True)
        df1[score_col] = df1[score_col] // 10 - 5
        df1[score_col].replace(5, 4, inplace=True)

        return (df1[score_col] * df1[grade_weight_col]).sum() / df[grade_weight_col].sum()
