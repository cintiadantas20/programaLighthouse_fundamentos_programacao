## Desafio referente ao Módulo II - Fundamentos de programação do programa Lighthouse, trilha Data Science

A proposta do desafio é construir uma aplicação em Python que testará a conectividade de um site (se este site está online ou não).

A aplicação deverá permitir receber um ou mais URLs como argumento e retornar o status de cada website.

Além disso, o código deverá estar em um repositório público do Github ou do Bitbucket, contendo um README bem estruturado, um .gitignore e um arquivo requirements.txt, com todos os pacotes utilizados.

Para rodar a aplicação, após clonar o repositório, é necessário:
* Criar um ambiente virtual na pasta clonada, com o comando: python -m venv venv
* Ativar o ambiente virtual com o comando: venv\Scripts\activate
* Instalar as bibliotecas descritas no arquivo requirements.txt
* Abrir a linha de comando e executar o seguinte comando: python -m sitechecker -u "sites desejados"<br/>
    Ex: python -m sitechecker -u python.org google.com indicium.tech