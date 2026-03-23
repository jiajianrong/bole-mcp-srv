import sys
from create_episode import main

if __name__ == "__main__":
    text = sys.argv[1]
    result = main(text)
    print(result)