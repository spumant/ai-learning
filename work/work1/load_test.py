import pandas as pd
import numpy as np
from sklearn.datasets._base import Bunch


def _get_target_names():
    tnames=['是否购买']
    return tnames


def _get_feature_names():
    fnames=['年龄','年级','月生活费']
    return fnames


def _get_quedescr(data):
    pass


def _get_quetarget(data):
    data_b=data.iloc[:,7:8]
    data_np=np.array(data_b)
    return data_np


def load_que():
    data_csv=pd.read_excel(io="D:\python\code\homework\que.xlsx")
    que=Bunch()
    que.data = _get_quedata(data_csv)
    que.target = _get_quetarget(data_csv)
    que.DESCR = _get_quedescr(data_csv)
    que.feature_names = _get_feature_names()
    que.target_names = _get_target_names()

    return que

def _get_quedata(data):
    data_r=data.loc[:,["年龄","地区","月生活费"]]
    data_np=np.array(data_r)
    return data_np

