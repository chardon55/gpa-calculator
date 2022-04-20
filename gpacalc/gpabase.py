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
    def calculate(self, df: pd.DataFrame, score_col, grade_weight_col) -> np.float:
        pass
