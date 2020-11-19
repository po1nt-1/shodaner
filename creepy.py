import inspect
import os
import sys

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


class error(Exception):
    pass


def _get_script_dir(follow_symlinks=True) -> str:
    '''получить директорию со скриптом'''

    # https://clck.ru/P8NUA
    if getattr(sys, 'frozen', False):  # type: ignore
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(_get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


def write_token(plain_text):
    secret_folder = os.path.join(_get_script_dir(), 'secrets')
    if not os.path.exists(secret_folder):
        os.mkdir(secret_folder)

    key = RSA.generate(2048)
    private_key = key.export_key('DER')
    public_key = key.publickey()

    cipher = PKCS1_OAEP.new(public_key)
    cipher_text = cipher.encrypt(plain_text.encode("utf-8"))

    with open(os.path.join(secret_folder, 'private'), 'wb') as f:
        f.write(private_key)

    with open(os.path.join(secret_folder, 'token'), 'wb') as f:
        f.write(cipher_text)


def read_token():
    private_path = os.path.join(_get_script_dir(), 'secrets', 'token')
    token_path = os.path.join(_get_script_dir(), 'secrets', 'private')
    if not os.path.exists(private_path) or not os.path.exists(token_path):
        raise error('Secret files were not found.')

    with open(private_path, 'rb') as f:
        cipher_text = f.read()

    with open(token_path, 'rb') as f:
        private_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(private_key)

    return cipher.decrypt(cipher_text).decode("utf-8")
