from absl import app
from absl import flags

from src.config import PROJECT_DIR
from src.utility import add_diagnostics

FLAGS = flags.FLAGS

@add_diagnostics()
def test_function():
    return None

def main(argv):
    del argv  # Unused.
    print("Hello from Utility Module!")
    test_function()

if __name__ == '__main__':
    app.run(main)