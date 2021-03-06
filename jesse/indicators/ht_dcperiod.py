from typing import Union

import numpy as np
import talib

from jesse.helpers import get_candle_source
from jesse.helpers import get_config


def ht_dcperiod(candles: np.ndarray, source_type: str = "close", sequential: bool = False) -> Union[float, np.ndarray]:
    """
    HT_DCPERIOD - Hilbert Transform - Dominant Cycle Period

    :param candles: np.ndarray
    :param source_type: str - default: "close"
    :param sequential: bool - default=False

    :return: float | np.ndarray
    """
    warmup_candles_num = get_config('env.data.warmup_candles_num', 240)
    if not sequential and len(candles) > warmup_candles_num:
        candles = candles[-warmup_candles_num:]

    source = get_candle_source(candles, source_type=source_type)
    res = talib.HT_DCPERIOD(source)

    return res if sequential else res[-1]
