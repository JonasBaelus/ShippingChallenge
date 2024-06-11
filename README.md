# Shipping Challenge Project


# Context
In the first semester of the second year, we had to complete a shipping challenge for the course Linux Webservices. The goal of this project was to create a Kubernetes cluster and run a web stack on it. The web stack consists of three containers: a web frontend container, an API service, and a backend database. Additionally, I used Adminer, a database management tool.

# Implementation
For Kubernetes, I used a Minikube cluster to run my application. The following technologies were used:

Web Frontend Container: nginx
API Service: FastAPI
Backend Database: MariaDB
Database Management Tool: Adminer

# Learnings
During this project, I acquired the following skills:

Working with Kubernetes.
Getting familiar with Docker, which was completely new to me before this project.
Setting up a working web application stack with three containers.
Deepening my knowledge of virtual machines and expanding my existing understanding.

# Installation
Follow the steps below to install and run the application:

1. Clone the repository:
git clone https://github.com/your-username/shipping-challenge.git
cd shipping-challenge

2. Install Minikube:
Follow the instructions on the official Minikube website to install Minikube.

3. Start Minikube:
minikube start

4. Deploy the application:
kubectl apply -f k8s

5. Access the application:
Get the IP address of Minikube:
minikube ip
Navigate to http://<minikube-ip>:<node-port> in your web browser.

# Usage
The web application stack includes the following components:

nginx: For the web frontend.
FastAPI: For the API service.
MariaDB: As the backend database.
Adminer: For database management.
