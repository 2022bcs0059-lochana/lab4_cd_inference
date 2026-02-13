pipeline {
    agent any

    environment {
        DOCKER_USERNAME = credentials('DOCKER_USERNAME')
        DOCKER_TOKEN = credentials('DOCKER_TOKEN')
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/2022bcs0059-lochana/lab4_cd_inference.git'
            }
        }

        stage('Setup Python venv & Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                . venv/bin/activate
                echo "Name: Lochana Balivada"
                echo "Roll No: 2022BCS0059"
                python scripts/train.py
                echo "Metrics Output:"
                cat metrics.json
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $DOCKER_USERNAME/lab5_wine:latest .
                '''
            }
        }

        stage('Docker Hub Login') {
            steps {
                sh '''
                echo
