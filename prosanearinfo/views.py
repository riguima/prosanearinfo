from flask import render_template, request
from flask_cors import cross_origin
import re
from parsel import Selector

from httpx import Client


def init_app(app):
    @app.get('/')
    def index():
        with Client() as client:
            response = client.get('http://autoatendimento.prosanearinfo.com.br/v5.1/index.php?id=96AQ96X').text
            response = response.replace('js/', '/static/js/')
            response = response.replace('imagens/', '/static/imagens/')
            response = response.replace('css/', '/static/css/')
            response = response.replace('scripts/redirect.php', '/redirect')
            response = re.sub(r'data:image.+?">', '/static/imagens/logo.png\'>', response, re.DOTALL)
            return response
    
    @app.post('/redirect')
    def redirect():
        with Client() as client:
            response = client.post(
                'http://autoatendimento.prosanearinfo.com.br/v5.1/scripts/redirect.php',
                data=request.form,
                follow_redirects=True,
            )
            if 'bordaMensagemErro' in response.text:
                return render_template('redirect.php')
            else:
                response = client.get('http://autoatendimento.prosanearinfo.com.br/v5.1/debitos.php').text
                selector = Selector(response)
                debits = client.post(
                    'http://autoatendimento.prosanearinfo.com.br/v5.1/scripts/debitos_funcoes.php',
                    data={
                        'hCPF': selector.css('#txtCPF').attrib['value'],
                        'hTipo': 0,
                        'hDoc': 0,
                        'hCodLigacao': selector.css('#txtCodLigacao').attrib['value'],
                        'hTipoList': 0,
                    },
                ).text
                debits = debits.replace('imagens/', 'static/imagens/')
                header = re.findall(r'(<div class="bg_up"></div>.+?<div class="topo sistemaTopo">.+?)<div class="divCentralizado">', response, re.DOTALL)[0]
                header = header.replace('principal.php', '/')
                header = header.replace('logout.php', '/')
                return render_template('debitos.html', header=header, debits=debits)
