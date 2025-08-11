from absl import app
from absl import flags

from src.config import PROJECT_DIR

FLAGS = flags.FLAGS

def main(argv):
    del argv  # Unused.
    print("Hello from data loader!")
    print(PROJECT_DIR)

if __name__ == '__main__':
    app.run(main)