import os

def main():
    environment = os.getenv('Env')
    print("environment: {}".format(environment))

if __name__ == "__main__":
    main()
