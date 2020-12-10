
# data
TRAINING_DATA_FILE = "raw.csv"
PIPELINE_NAME = 'model'

TARGET = 'RUL'

# input variables 
FEATURES = ['engine_id', 'time_cycle','op_set_1', 'op_set_2', 'op_set_3', 'sensor_1',
           'sensor_2', 'sensor_3', 'sensor_4', 'sensor_5', 'sensor_6', 'sensor_7',
           'sensor_8', 'sensor_9', 'sensor_10', 'sensor_11', 'sensor_12',
           'sensor_13', 'sensor_14', 'sensor_15', 'sensor_16', 'sensor_17',
           'sensor_18', 'sensor_19', 'sensor_20', 'sensor_21']


# must be dropped afterwards
labels = ['engine_id', 'time_cycle', 'max_cycle'] # id/label cols
cst_features = ['op_set_3', 'sensor_18', 'sensor_19'] # constant features
quasi_cst_features = ['sensor_1', 'sensor_5', 'sensor_6', 'sensor_10', 'sensor_16'] # quasi-constant features
high_corr_to_drop = ['sensor_9', 'sensor_14'] # fan speed & corrected fan speed
discreet_features = ['op_set_2', 'sensor_17'] 

DROP_FEATURES = labels + cst_features + quasi_cst_features + high_corr_to_drop['sensor_14']

TEMPORAL_VARS = 'YearRemodAdd'

# variables to log transform
NUMERICALS_LOG_VARS = ['LotFrontage', '1stFlrSF', 'GrLivArea']

