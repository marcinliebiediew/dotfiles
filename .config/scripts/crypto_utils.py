import os
from cryptography.fernet import Fernet


def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    keypath = '/home/marcin/.ssh/pycrypt.key'
    return open(keypath, "rb").read()


def get_from_env(envvar, key):
    entry = [e for e in os.getenv(envvar).split(';')
             if key in e]
    value = entry[0]
    value = value.split(f'{key}=')
    value = value[-1]
    return value


def get_credentials(encrypted_credentials):
    key = load_key()
    f = Fernet(key)
    byte_repr = encrypted_credentials.encode()
    decrypted = f.decrypt(byte_repr).decode()
    return decrypted
