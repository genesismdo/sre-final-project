## Estructura del proyecto 
--

## Proyecto Final — SRE Monitoring Stack
Este proyecto implementa un stack completo de observabilidad y despliegue SRE utilizando:
Python + Flask (aplicación demo)
Kubernetes
Prometheus (métricas)
Grafana (dashboards y visualización)
Alertmanager (alertas)
Ansible (automatización de despliegue)


## Arquitectura

App publica métricas vía /metrics
Prometheus scrapea métricas y evalúa alertas
Grafana visualiza métricas y dashboards
Alertmanager maneja notificaciones de alertas
Ansible automatiza despliegue de Prometheus y Grafana

## Estructura del repositorio
SRE Final Project
│
├── app
│   ├── app.py               # Flask + Prometheus metrics
│   ├── requirements.txt
│   └── Dockerfile
│
├── k8s
│   ├── app
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   │
│   ├── monitoring
│   │   ├── grafana.yaml
│   │   ├── prometheus.yaml
│   │   ├── prometheus-rules.yaml
│   │   └── alertmanager/
│   │       ├── alertmanager.yaml
│   │       └── alertmanagerdeploy.yaml
│   │
│   └── ansible
│       ├── inventory.ini
│       └── playbook.yaml
│
└── README.md

## Deploy
Requisitos
Docker
Minikube
Kubernetes kubectl
Python 3.9+

## Ansible
Crear imagen de la app
```bash
cd app
docker build -t sre-app .
```

## Iniciar minikube
```bash

minikube start
```

## Crear namespace monitoring
```bash
kubectl create namespace monitoring
```

## Deploy de la aplicación
```bash
kubectl apply -f k8s/app/
```
## Deploy del stack de monitoreo
```bash
kubectl apply -f k8s/monitoring/
```
## O con Ansible
```bash
cd k8s/ansible
ansible-playbook -i inventory.ini playbook.yaml
```
## 📊 Dashboards
📌 Acceder a Grafana:
```bash
minikube service grafana-service -n monitoring
User / Pass por defecto:
admin / admin
```

## 🚨 Alertas
Se incluyen reglas de Prometheus vía prometheus-rules.yaml:
Detecta caída de la app (AppDown)
Detecta bajo tráfico HTTP (LowRequestTraffic)
Y Alertmanager envía notificaciones por email.
🧪 Endpoints
```bash
GET / → página básica
GET /metrics → exporta métricas Prometheus
```
## Autor
Génesis Montes de Oca
Proyecto final SRE — IBM