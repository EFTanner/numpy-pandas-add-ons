#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 22:10:48 2017

@author: eftanner
"""
import pandas as pd
import numpy as np


def strjoin(dataframe, series=None, sep=None, raise_on_na=False,
            ignore_index=True, return_series=True):
    """
    join strings in dataframe with series or separator
    """
    if raise_on_na:
        to_join = dataframe.values
        if not sep:
            join_strings = series.values
    else:
        to_join = np.where(dataframe.isnull(), '', dataframe.values)
        if not sep:
            join_strings = np.where(series.isnull(), '', series.values)
    join_array = np.empty((to_join.shape[0], to_join.shape[1]*2-1),
                          dtype=np.object)
    indices = 2*np.arange(to_join.shape[1])
    join_array[:, indices] = to_join
    if sep:
        join_array[:, indices[:-1]+1] = sep
    else:
        join_array[:, indices[:-1]+1] = np.expand_dims(join_strings, axis=1)
    if return_series:
        return pd.Series(join_array.sum(axis=1))
    else:
        return join_array.sum(axis=1)
