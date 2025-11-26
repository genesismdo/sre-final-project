Estructura del proyecto 

SRE Final Project/
├── app/
│   ├── app.py              # Código principal de la aplicación
│   ├── Dockerfile          # Imagen Docker para la app
│   ├── requirements.txt    # Dependencias Python
├── k8s/
│   ├── app/
│   │   ├── deployment.yaml # Despliegue de la app en Kubernetes
│   │   ├── service.yaml    # Servicio para exponer la app
│   ├── monitoring/
│   │   ├── prometheus.yaml       # Configuración de Prometheus
│   │   ├── prometheus-rules.yaml # Reglas de alertas
│   │   ├── alertmanager.yaml     # Configuración de Alertmanager
│   │   ├── grafana.yaml          # Configuración de Grafana
│   ├── ansible/
│       ├── inventory.ini         # Inventario Ansible
│       ├── playbook.yaml         # Playbook para desplegar el stack

Una aplicación web en Flask que expone métricas para Prometheus.
Despliegue en Kubernetes con manifiestos para la app y el stack de monitoreo.
Automatización con Ansible para aplicar los recursos.
Alertas configuradas para disponibilidad y tráfico.