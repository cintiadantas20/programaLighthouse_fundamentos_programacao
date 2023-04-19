import sys
import pathlib
import re

from sitechecker.cli import read_user_cli_args
from sitechecker.cli import display_check_result
from sitechecker.checker import site_is_online

def main():
    """Roda a aplicação"""
    user_args = read_user_cli_args()
    urls = user_args.urls
    if not urls:
        print("Erro: sem URLs para analisar.", file=sys.stderr)
        sys.exit(1)
    _site_check(urls)

def _site_check(urls):
    for url in urls:
        error = ""
        regex = re.compile("((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-=#])*")
        valid = regex.match(url)
        if valid:
            try:
                result = site_is_online(url)
            except Exception as e:
                result = False
                error = "Essa página está offline ou não existe"
            display_check_result(result, url, error)
        else:
            print(f'"{url}" não é uma URL válida')

if __name__ == "__main__":
    main()