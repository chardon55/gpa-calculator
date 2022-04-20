from abc import abstractmethod
import numpy as np
import pandas as pd


class GPACalcModule(object):

    def __init__(self):
        self.__full_gpa = None

    def __get_full_gpa(self) -> np.float:
        return self.calculate(pd.DataFrame([[100, 1]]), 0, 1)

    @property
    def full_gpa(self) -> np.float:
        if not self.__full_gpa:
            self.__full_gpa = self.__get_full_gpa()

        return self.__full_gpa

    @abstractmethod
    def _calc_score(self, score_col: pd.Series):
        pass

    def calculate(self, df: pd.DataFrame, score_col, grade_weight_col) -> np.float:
        df1 = df.copy()
        sc = df1[score_col]

        df1.drop(index=df1[sc < 60].index, inplace=True)
        self._calc_score(sc)

        return (sc * df1[grade_weight_col]).sum() / df[grade_weight_col].sum()
