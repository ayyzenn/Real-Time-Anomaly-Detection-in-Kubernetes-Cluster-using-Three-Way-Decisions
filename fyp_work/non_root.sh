#! /bin/bash

confirm_agreement() {
    read -p "Make sure that you have fast internet so that things can run smoothly. If you don't have fast internet, then remember not to run this file. (yes/no): " answer
    case $answer in
        [Yy]|[Yy][Ee][Ss]) return 0 ;;
        *) return 1 ;;
    esac
}

remove()
{
    echo "Removing Docker and Minikube..."
    sudo apt purge docker.io -y
    sudo apt purge docker-compose -y
    sudo minikube delete
    sudo rm /tmp/* -rf
    sudo rm /usr/local/bin/minikube
    sudo snap remove kubectl
    echo "Removal completed."
}

install()
{
    echo "Installing Docker..."
    sudo apt install docker.io -y
    sudo usermod -aG docker $USER
    newgrp docker
    sudo apt install docker-compose -y
    echo "Docker installation completed."
    echo "#####################################"
    sleep 2

    echo "Installing kubectl..."
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
    kubectl version --client
    echo "kubectl installation completed."
    echo "#####################################"
    sleep 2

    echo "Installing Minikube..."
    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
    sudo install minikube-linux-amd64 /usr/local/bin/minikube
    minikube start
    echo "Minikube installation completed."
    echo "#####################################"
    sleep 2
}

if confirm_agreement; then
    remove
    install
    echo "You are good to go... install groundcover know."
else
    echo "You did not agree the terms. Exiting... :)"
    exit 1
fi
