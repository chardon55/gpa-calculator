import numpy as np
import pandas as pd

from . import gpabase as b


class PekingGPA(b.GPACalcModule):
    '''
        GPA calculation method of Peking University since September 1, 2019

        For details: http://www.dean.pku.edu.cn/web/rules_info.php?id=12 (Chinese)
    '''

    def calculate(self, df: pd.DataFrame, score_col: str, grade_weight_col: str) -> np.float:
        df1 = df.copy()

        df1.drop(index=df1[df1[score_col] < 60].index, inplace=True)
        df1[score_col] = 4 - 3 * (100 - df1[score_col]) ** 2 / 1600

        return (df1[score_col] * df1[grade_weight_col]).sum() / df[grade_weight_col].sum()
