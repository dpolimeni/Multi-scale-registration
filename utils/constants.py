import os
import time
from datetime import datetime
from pathlib import Path

# TIMESTAMP (COMPUTED ONCE FOR LOGGERS INITIALIZATION)
__TIME_NOW__ = time.time()

# TIMESTAMP EXPRESSED IN HUMAN READABLE FORMAT
__DATETIME_NOW__ = formatted_time = datetime.fromtimestamp(__TIME_NOW__).strftime(
    "%Y_%m_%d_%H_%M_%S"
)

# PROJECT ROOT
__ROOT__ = str(Path(os.getcwd()).parent)

# LOG DEFAULT FOLDER
__LOG_FOLDER__ = os.path.join(__ROOT__, "logs", __DATETIME_NOW__)

# LOG DEFAULT FORMAT
__DEFAULT_LOG_FORMAT__ = "%(asctime)s | %(name)s | %(levelname)s : %(message)s"


# DOWN SAMPLERS
# VOXEL DOWN SAMPLER
__BASE_VOXEL_SIZE__ = 0.1
__MIN_VOXEL_SIZE__ = 0.005
__DELTA__ = 0.05
__EPS__ = 0.001

# DOWNSAMPLER DEFAULT SAMPLE SIZE
__SAMPLE_SIZE__ = 4096

# FAST GLOBAL OPTIMIZER
__DIVISION_FACTOR__ = 1.4
__TUPLE_SCALE__ = 0.95
__MAXIMUM_CORRESPONDENCE_DISTANCE__ = 0.05
__ITERATION_NUMBER__ = 100
__DECREASE_MU__ = True
__NORMAL_ESTIMATE_RADIUS__ = 0.05
__NORMAL_ESTIMATE_KNN__ = 20
__FPFH_RADIUS__ = 0.05
__FPFH_KNN__ = 20

# GENERALIZED ICP
__MAX_CORRESPONDENCE_DISTANCE__ = 0.05
__MAX_ITERATIONS__ = 100
