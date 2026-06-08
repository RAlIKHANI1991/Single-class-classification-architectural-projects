# src/utils/seed.py

import random
import numpy as np
from config.constants import RANDOM_STATE


def set_seed():
    random.seed(RANDOM_STATE)
    np.random.seed(RANDOM_STATE)