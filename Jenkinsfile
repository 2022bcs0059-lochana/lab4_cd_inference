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

        stage('Install Dependencies') {
            steps {
                sh '''
                pip3 install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                echo "Name: Lochana Balivada"
                echo "Roll No: 2022BCS0059"
                python3 scripts/train.py
                echo "Metrics:"
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
                echo $DOCKER_TOKEN | docker login -u $DOCKER_USERNAME --password-stdin
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                docker push $DOCKER_USERNAME/lab5_wine:latest
                '''
            }
        }
    }
}
