from absl import app
from absl import flags

FLAGS = flags.FLAGS

def main(argv):
    del argv  # Unused.
    print("Hello from quant-trading!")

if __name__ == '__main__':
    app.run(main)