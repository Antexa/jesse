from typing import Union

import numpy as np
import talib

from jesse.helpers import get_config


def medprice(candles: np.ndarray, sequential: bool = False) -> Union[float, np.ndarray]:
    """
    MEDPRICE - Median Price

    :param candles: np.ndarray
    :param sequential: bool - default=False

    :return: float | np.ndarray
    """
    warmup_candles_num = get_config('env.data.warmup_candles_num', 240)
    if not sequential and len(candles) > warmup_candles_num:
        candles = candles[-warmup_candles_num:]

    res = talib.MEDPRICE(candles[:, 3], candles[:, 4])

    if sequential:
        return res
    else:
        return None if np.isnan(res[-1]) else res[-1]
