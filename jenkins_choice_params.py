import os

def main():
    environment = os.getenv('Environment')
    print("environment: {}".format(environment))

if __name__ == "__main__":
    main()
