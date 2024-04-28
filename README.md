# Mini Project Metrics Monitoring Setup

## Assignment Overview
The goal of this assignment is to export metrics (e.g., request per second, memory usage, CPU usage, etc.) from an existing mini-project and set up Prometheus and Grafana to monitor these metrics.

## Prerequisites
- Docker installed on your system
- Minikube installed
- Helm installed

## Setup Instructions

### 1. Build and Push Docker Image
* Create DockerFile 
```bash
docker build -t imageName:version .
docker push dockerRepo_url
```
### 2. Start Minikube
```bash
minikube start
```
### 3. Create Helm Chart
```bash
helm create chart_name
```
### 4. Modify Helm Chart
Make necessary changes such as providing repository links and configuring value.yaml.
* Give docker repo link
* Change ports number for web aplication
* change service type-NodePort

### 5. Install Project using Helm
```bash
helm install release_name dir_path_of_chart

```
* Access application
```bash
minikube service servicename_of_App

```
### 6. Add Helm Repositories for Prometheus and Grafana
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
```
### 7. Update Helm Repositories
```bash
helm repo update
```
### 8. Install Prometheus and Grafana
```bash
helm install grafana grafana/grafana
helm install prometheus prometheus-community/prometheus
```
### 9.Configure Prometheus
* Edit the ConfigMap prometheus-server
* add the following lines under scrape_configs
* give target Ip address of aap and set alert manager
```bash
kubectl get cm
kubectl edit cm prometheus-server
```
* Confirm the changes:
```bash
kubectl get cm pprometheus-server -o yaml
```
### 10. Expose Prometheus ClusterIP at NodePort
```bash
kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-ext

```
### 11. Access Prometheus IP
```bash
minikube service prometheus-server-ext
```
* Note down the IP and port to access at the browser
* 
### 12. Configure Grafana to Fetch Metrics from Prometheus
* Update Grafana to fetch metrics from Prometheus using the IP obtained in the previous step.

#### Validation
* Check Prometheus UI to validate if the data is being scraped properly.
* Create dashboards in Grafana using Prometheus as a datasource to visualize the exported metric
