import numpy as np
import pandas as pd

from . import gpabase as b


class QingdaoGPA(b.GPACalcModule):
    '''
        GPA calculation method of Qingdao University since 2019.
    '''

    def _calc_score(self, score_col: pd.Series):
        score_col.update(4 - 2.5 * (100 - score_col) ** 2 / 1600)


class QingdaoGPAUntil2018(b.GPACalcModule):
    '''
        GPA calculation method of Qingdao University during 2014-2018.
    '''

    def _calc_score(self, score_col: pd.Series):
        score_col.update(score_col / 10 - 5)
