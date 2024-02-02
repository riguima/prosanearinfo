import re

import toml
from flask import redirect, render_template, request, url_for
from flask_login import login_required, login_user
from httpx import Client
from parsel import Selector
from pixqrcodegen import Payload
from sqlalchemy import select

from prosanearinfo.config import config
from prosanearinfo.database import Session
from prosanearinfo.forms import ConfigForm, LoginForm
from prosanearinfo.models import User


def init_app(app):
    @app.get('/')
    def index():
        with Client(timeout=10000) as client:
            response = client.get(
                'http://autoatendimento.prosanearinfo.com.br/v5.1/index.php?id=96AQ96X'
            ).text
            response = response.replace('js/', '/static/js/')
            response = response.replace('imagens/', '/static/imagens/')
            response = response.replace('css/', '/static/css/')
            response = response.replace('scripts/redirect.php', '/redirect')
            response = re.sub(
                r'data:image.+?">',
                "/static/imagens/logo.png'>",
                response,
                re.DOTALL,
            )
            return response

    @app.post('/redirect')
    def redirect_view():
        with Client(timeout=10000) as client:
            response = client.post(
                'http://autoatendimento.prosanearinfo.com.br/v5.1/scripts/redirect.php',
                data=request.form,
                follow_redirects=True,
            )
            if 'bordaMensagemErro' in response.text:
                return render_template('redirect.php')
            else:
                response = client.get(
                    'http://autoatendimento.prosanearinfo.com.br/v5.1/debitos.php'
                ).text
                selector = Selector(response)
                response = selector.css('html').get()
                for table in selector.css('#enviarDebitos table'):
                    try:
                        input = re.sub(
                            r'value=".+?"',
                            f'value="{table.css("td::text")[2].get()}"',
                            table.css('#debitos').get(),
                            re.DOTALL,
                        )
                        response = response.replace(
                            table.css('#debitos').get(), input
                        )
                    except (TypeError, IndexError):
                        continue
                response = re.sub(
                    r'<form id="enviarDebitos".+?action=""',
                    '<form id="enviarDebitos" name="enviarDebitos" method="post" action="/qrcode"',
                    response,
                )
                response = response.replace(
                    selector.css('.textoTituloCampo tr')[-3].get(), ''
                )
                response = response.replace(
                    selector.css('.textoTituloCampo tr')[-2].get(), ''
                )
                response = response.replace(
                    selector.css('.textoTituloCampo tr')[-1].get(), ''
                )
                response = response.replace(
                    selector.css('.btConta').get(),
                    '<input type="submit" class="btConta" value="">',
                )
                response = response.replace('js/', '/static/js/')
                response = response.replace('imagens/', '/static/imagens/')
                response = response.replace('css/', '/static/css/')
                response = response.replace(
                    'scripts/redirect.php', '/redirect'
                )
                response = response.replace(
                    'javascript:imprimirConta(0)', '/qrcode'
                )
                response = response.replace(
                    'javascript:imprimirListagem();',
                    'http://autoatendimento.prosanearinfo.com.br/v5.1/impressoes/debitos_imprimir.php?formato=0&selDoc=0',
                )
                response = response.replace('principal.php', '/')
                response = response.replace('scripts/', '/static/scripts/')
                return response

    @app.post('/qrcode')
    def qrcode():
        if request.form.get('debitos'):
            payload = Payload(
                config['name'],
                config['pix'],
                request.form['debitos'],
                config['city'],
                config['txt_id'],
            )
            payload.gerarPayload()
            payload.gerarQrCode(payload.payload_completa, 'static/imagens')
            return render_template(
                'qrcode.html',
                payload=payload.payload_completa,
                price=request.form['debitos'],
            )
        return redirect(url_for('redirect_view'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            with Session() as session:
                query = select(User).where(User.login == request.form['login'])
                user = session.scalars(query).first()
                if user and user.password == request.form['password']:
                    user.authenticated = True
                    session.commit()
                    session.flush()
                    login_user(user)
                    return redirect(url_for('config_view'))
                else:
                    return render_template(
                        'login.html', form=form, error_message='Login Inválido'
                    )
        return render_template('login.html', form=form)

    @app.route('/config', methods=['GET', 'POST'])
    @login_required
    def config_view():
        form = ConfigForm()
        if form.validate_on_submit():
            config['name'] = request.form['name']
            config['pix'] = request.form['pix']
            config['txt_id'] = request.form['txt_id']
            config['city'] = request.form['city']
            toml.dump(config, open('.config.toml', 'w'))
            return redirect(url_for('index'))
        return render_template('config.html', form=form)
