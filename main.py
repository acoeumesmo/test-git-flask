from flask import Flask
import pyvibe as pv

app = Flask(__name__)

from rotas import *

# Eu so executo esse codigo se vc estiver rodando esse arquivo diretamente
if __name__ == '__main__':
    app.run()