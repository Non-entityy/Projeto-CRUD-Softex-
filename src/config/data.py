# Configuração de Banco de Dados

# Um arquivo config/db.py pode conter informações sobre a conexão com o banco de dados:


# DATABASE = {
#     'HOST': 'localhost',
#     'PORT': 5432,
#     'USER': 'admin',
#     'PASSWORD': 'senha123',
#     'NAME': 'minhabase'
# }
# import config.db as db
# connection = connect_to_database(db.DATABASE)
#OR

# Configuração de API Key

# Em um arquivo config/api.py, você poderia armazenar informações de autenticação como chaves de API para interagir com serviços externos.

# api.py
# API_KEYS = {
#     'google_maps': 'AIzaSyD-xxxxxxxxxxxxxxxxxxxxxx',
#     'openweathermap': 'abcd1234efgh5678ijkl91011'
# }
# import config.api as api

# def get_weather(city):
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api.API_KEYS['openweathermap']}"
#     Faz a requisição com a chave da API

#OR
# Configuração de Parâmetros de Aplicação

# Um arquivo config/settings.py pode armazenar configurações gerais da aplicação, como parâmetros de segurança, configurações de cache, etc.
# # settings.py
# DEBUG = True
# SECRET_KEY = 'sua-chave-secreta-aqui'
# MAX_UPLOAD_SIZE = 10485760  # 10MB

# import config.settings as settings

# if settings.DEBUG:
    # print("Modo de depuração ativado!")


#OR

# Configuração de Cores e Estilos

# Um arquivo config/styles.py poderia armazenar definições relacionadas à aparência de uma interface gráfica:
# styles.py
# COLORS = {
#     'background': '#ffffff',
#     'primary_text': '#333333',
#     'button': '#4CAF50'
# }

# import config.styles as styles

# def apply_theme():
#     window.set_background_color(styles.COLORS['background'])
#     button.set_text_color(styles.COLORS['primary_text'])
