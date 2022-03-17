from abc import abstractmethod
import numpy as np
import pandas as pd


class GPACalcModule(object):

    @abstractmethod
    def calculate(df: pd.DataFrame, score_col: str, grade_weight_col: str) -> np.float:
        pass
