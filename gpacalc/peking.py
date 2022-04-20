import numpy as np
import pandas as pd

from . import gpabase as b


class PekingGPA(b.GPACalcModule):
    '''
        GPA calculation method of Peking University since September 1, 2019

        For details: http://www.dean.pku.edu.cn/web/rules_info.php?id=12 (Chinese)
    '''

    def _calc_score(self, score_col: pd.Series):
        score_col.update(4 - 3 * (100 - score_col) ** 2 / 1600)
