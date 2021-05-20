## Objetivo do projeto
Orientação base para quem deseja aprender um pouco do Framework Django/Python


## Configuração do ambiente Virtual

1. #### criação da venv
    ```python -m venv [NOME DA VENV, por ex: "venv"]```

2. #### ativando a venv
    - Windows
    ```source venv\Script\activate```
    - Linux ou Mac
    ```source venv\bin\activate```

3. #### Instalação dos pacotes necessários
    - pacotes no arquivo ```requirements.txt```

        ```pip install -r requirements.txt```
4. #### copiar o arquivo de configuração dentro da pasta core

    ```copiar local_settings.example.py``` para ```local_settings.py```
    - Configurar este arquivo conforme a necessidade, por padrão, já temos o necessário

5. #### Criar um super usuário
    ```python manage.py createsuperuser --username=[usuário] --email=[email do usuário]```

    - Após o último comando, será solicitado a criação da senha e confirmação 

6. #### Executar o servidor
     ```python manage.py runserver```
