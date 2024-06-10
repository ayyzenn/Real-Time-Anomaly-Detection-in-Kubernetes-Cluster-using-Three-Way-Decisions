sudo apt install docker.io -y
sudo snap install curl
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
sudo snap install kubectl --classic
alias kubectl="minikube kubectl --"

sudo minikube start --force

# Installing helm
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
sudo apt-get install apt-transport-https --yes
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm -y

# # Installing Prometheus
# sudo helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
# sudo helm repo update
# sudo helm install prometheus prometheus-community/prometheus
# # Configuring Prometheus
# sudo kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-ext
# sudo minikube service prometheus-server-ext

# # Installing Grafana
# sudo helm repo add grafana https://grafana.github.io/helm-charts
# sudo helm repo update
# sudo helm install grafana grafana/grafana
# sudo kubectl expose service grafana --type=NodePort --target-port=3000 --name=grafana-ext
# sudo minikube service grafana-ext

# #Getting the password for grafana admin
# sudo kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo

# #the above command will return the password for the username "admin" which will be used in grafana.
