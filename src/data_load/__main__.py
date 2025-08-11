from absl import app
from absl import flags

from src.data_load import test_function

FLAGS = flags.FLAGS

def main(argv):
    del argv  # Unused.
    print("Hello from data loader!")
    print(test_function())

if __name__ == '__main__':
    app.run(main)