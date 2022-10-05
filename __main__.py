from utils.configs import configData
from utils.loader import client

if __name__ == '__main__':

    client(configData['token'], configData['prefix']).__start__()