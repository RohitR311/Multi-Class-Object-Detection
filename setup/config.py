import os

BASE_PATH = "dataset"

IMAGES_PATH = os.path.join(BASE_PATH, 'images')
ANNOTS_PATH = os.path.join(BASE_PATH, 'annotations')


BASE_OUTPUT = "output"

MODEL_PATH = os.path.join(BASE_OUTPUT, 'detector.h5')
LB_PATH = os.path.join(BASE_OUTPUT, 'lb.pickle')
PLOTS_PATH = os.path.join(BASE_OUTPUT, 'plots')
TEST_PATHS = os.path.join(BASE_OUTPUT, 'test_path.txt')


INIT_LR = 1e-4
NUM_EPOCHS = 20
BATCH_SIZE = 32

