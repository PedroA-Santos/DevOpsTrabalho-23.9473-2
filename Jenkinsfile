pipeline {
    agent any

    stages {
        stage('Build Containers') {
            steps {
                script {
                    // Step 1: Destrói os containers existentes e constrói novos
                    sh 'docker-compose down -v'
                    sh 'docker-compose build'
                }
            }
        }

        stage('Start Application') {
            steps {
                script {
                    // Step 2: Inicia os containers
                    sh 'docker-compose up -d'
                }
            }
        }
    }

    post {
        always {
            // Limpando os containers após o término da execução
            sh 'docker-compose down'
        }
    }
}
