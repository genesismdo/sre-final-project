from flask import Flask, Response
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST
import random, time, threading

app = Flask(__name__)

# Métricas
REQUESTS = Counter('example_app_http_requests_total', 'Total HTTP requests received')
RANDOM_VALUE = Gauge('example_random_metric', 'Random metric that changes over time')

def update_random():
    while True:
        RANDOM_VALUE.set(random.random() * 100)
        time.sleep(5)

thread = threading.Thread(target=update_random, daemon=True)
thread.start()

@app.route('/')
def index():
    REQUESTS.inc()
    return "Hola! Esta es la app con métricas para SRE proyecto final.\n"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
