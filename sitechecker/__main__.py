import sys
import pathlib

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
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)

if __name__ == "__main__":
    main()

# python -m sitechecker -u python.org google.com indicium.tech