# Home Automation

## Introduction

Here is my home automation setup I'm working on. Everything is managed by a [Home Assistant](https://www.home-assistant.io/) instance running on a [Minikube](https://github.com/kubernetes/minikube). I'm planning on using [Sonoff Basic](http://sonoff.itead.cc/en/products/sonoff/sonoff-basic) switches flashed with a custom firmware I'll soon make available on Github.

This project will be hosted on a Raspberry Pi 3 made available through NAT/PAT rules and a dynamic DNS on my router.

## Prerequisites

What you'll need to successfuly install and run this project is :

* Git
* Minikube
* Python 3.x
* A registered domain name which points to your server running Minikube

## Services

The Minikube instance will host multiple home automation services :

* a Home Assistant instance to manage your system
* an Nginx instance to act as an entrypoint to your ecosystem, it will route traffic to the other services
* a Certbot / LetsEncrypt service that creates and renews SSL certificates when needed
* a Mosquitto MQTT bus to ensure the communication between services

## Installation

Start by cloning the project

```bash
git clone https://github.com/k2r79/home-automation.git
```

### Editing the templates

Then edit the Kubernetes template configuration file to suit your own setup.

```bash
vi kubernetes/config/template.properties
```

You must also copy and tune the _config/_ folder templates.

```bash
vi config/home-assistant/configuration.yaml
cp config/home-assistant/configuration.yaml /host/path/home-assistant

vi config/nginx/nginx.conf
cp config/nginx/nginx.conf /host/path/nginx
```

### Compiling the templates

Once that's done, you can compile the templates to fill the placeholders.

```bash
cd kubernetes
py compile-templates.py
```

Your Kubernetes configuration files are now ready in the _kubernetes/_ folder. You can install them in your Minikube.

```bash
cd ..
```

### Mounting the directories

The Nginx and Home Assistant configuration files must be mounted on the Minikube virtual machine to then mount them on the pods as the virtual machine is the host.

```bash
nohup minikube mount /host/path/nginx:/var/opt/nginx &
nohup minikube mount /host/path/home-assistant:/var/opt/home-assistant &
```

### Startup and setup Minikube

You can now start your Minikube instance and install the services on it.

```bash
minikube start --kubernetes-version v1.10.0

kubectl create -f nginx.yml
kubectl create -f letsencrypt.yml
kubectl create -f home-assistant.yml
kubectl create -f mqtt.yml
```

Home Assistant is now available at your domain's HTTPS address.