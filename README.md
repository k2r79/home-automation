# Home Automation

## Introduction

Here is my future home automation setup I'm working on. Everything is managed by a [Home Assistant](https://www.home-assistant.io/). I'm planning on using [Sonoff Basic](http://sonoff.itead.cc/en/products/sonoff/sonoff-basic) switches flashed with a custom firmware I'll soon make available on Github.

This project will be hosted on a Raspberry Pi made available through NAT/PAT rules and a dynamic DNS on my router.

## Prerequisites

What you'll need to successfuly install and run this project is :

* Git
* Ansible
* Python 3.x
* A registered domain name which points to your server running Home Assistant

## Installation

Start by cloning the project

```bash
git clone https://github.com/k2r79/home-automation.git
```

### Tweak the configuration files

Before launching the main playbook, start by tweaking the configuration files in the `ansible/config/` folder.  
Sample files are given to guide you, they must be copied without the `.sample` extension to be used as a configuration baseline.

### Setup your Ansible hosts

Edit the `/etc/ansible/hosts`file to add your Home Assistant server as so :

```
[home-assistant]
<server_ip> ansible_user=root home_assistant_password=<frontend_password> domain_name=<your_domain_name> letsencrypt_email=<your_letsencrypt_email>
```

### Setup a dynamic DNS and NAT/PAT rules

Before launching the Ansible playbooks you must setup a dynamic DNS and some NAT/PAT rules on your router.

You'll need to map the following ports to your server :
- 8123 -> 443 for HTTPS
- 1883 -> 1883 for the MQTT Broker

### Launch the Ansible playbook

By running the following command `ansible-playbook ansible/playbooks/main.yml` from the project's root directory.

