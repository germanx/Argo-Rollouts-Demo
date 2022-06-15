from os import environ, path
from dotenv import load_dotenv
from random import random
import time
from prometheus_client import start_http_server, Counter

METRICS_PORT = 8001


def main():
  basedir = path.dirname(path.abspath(__file__))
  load_dotenv(path.join(basedir, '.env'))
  OK_PERCENT = float(environ.get('OK_PERCENT'))
  DELAY_SEC = int(environ.get('DELAY_SEC'))

  app_all = Counter('app_all', 'app - all requests counter', ['app_name'])
  app_fail = Counter('app_fail', 'app - failed requests counter', ['app_name'])

  while True:
    app_all.labels(environ.get('POD_NAME')).inc() 
    if random() >= OK_PERCENT:
      app_fail.labels(environ.get('POD_NAME')).inc()
    time.sleep(DELAY_SEC)


if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    print('Prometeus Writer Started')
    main()