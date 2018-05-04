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

## Installation

Start by clonin the project

```bash
git clone https://github.com/k2r79/home-automation.git
```

Then edit the Kubernetes template configuration file to suit your own setup.

```bash
vi kubernetes/config/template.properties
```

Once that's done, you can compile the templates to fill the placeholders.

```bash
cd kubernetes
py compile-templates.py
```

Your Kubernetes configuration files are now ready in the _kubernetes/_ folder. You can install them in your Minikube.

```bash
cd ..

kubectl create -f letsencrypt.yml
kubectl create -f home-assistant.yml
kubectl create -f mqtt.yml
```

Home Assistant is now available at your domain's HTTPS address.