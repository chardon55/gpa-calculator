import numpy as np
import pandas as pd

from . import gpabase as b


class TohokuGPA(b.GPACalcModule):
    '''
        GPA calculation method (Cumulative) of Tohoku University since March 3, 2020.

        For details: https://www.tohoku.ac.jp/japanese/studentinfo/education/01/education0110/015_2.pdf (Japanese)
    '''

    def _calc_score(self, score_col: pd.Series):
        score_col.update(score_col // 10 - 5)
        score_col.replace(5, 4, inplace=True)
