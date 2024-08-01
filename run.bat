@echo off

:: {{ url_for('static', filename='')}}
:: Navegue até o diretório do seu projeto (substitua "C:\caminho\do\seu\projeto" pelo caminho real)
cd C:\Users\Julio Rafael\Desktop\Julio\Codes\site\

:: Ative o ambiente virtual, se estiver usando um
:: call caminho\do\seu\ambiente\virtual\Scripts\activate.bat

:: Execute o comando Flask
flask --app main run --reload
