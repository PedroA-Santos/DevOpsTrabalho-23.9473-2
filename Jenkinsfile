pipeline {
    agent any

    environment {
        REGISTRY = "dockerhub/your-repository"
        IMAGE_NAME = "flask_app"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repository.git'
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run tests
                    sh 'pytest'
                }
            }
        }
        stage('Build & Push Docker Image') {
            steps {
                script {
                    // Build Docker Image
                    sh 'docker build -t ${REGISTRY}/${IMAGE_NAME}:${GIT_COMMIT} .'
                    // Push Docker Image to DockerHub
                    sh 'docker push ${REGISTRY}/${IMAGE_NAME}:${GIT_COMMIT}'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Deploy using Docker Compose
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}
