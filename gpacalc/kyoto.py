import numpy as np
import pandas as pd

from . import gpabase as b


class KyotoGPA(b.GPACalcModule):
    '''
        GPA calculation method (Cumulative) of Kyoto University since 2015.

        Details: https://www.kyoto-u.ac.jp/ja/education-campus/curriculum/grading-gpa (Japanese)
    '''

    def _calc_score(self, score_col: pd.Series):
        score_col.replace(95, 94, inplace=True)
        score_col.update((score_col + 5) // 10 - 5)
        score_col.replace(5.0, 4.3, inplace=True)
