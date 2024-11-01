pipeline {
    agent any

    environment {
        // Define variáveis de ambiente necessárias
        DOCKER_IMAGE_FLASK = 'flask_app:latest'
        DOCKER_IMAGE_MARIADB = 'mariadb_container:latest'
    }

    stages {
        stage('Clonar Repositório') {
            steps {
                // Clonar o repositório do GitHub
                git 'https://github.com/PedroA-Santos/Devops-Docker.git'
            }
        }

        stage('Construir Imagens Docker') {
            steps {
                script {
                    // Construir as imagens Docker para Flask e MariaDB
                    sh 'docker-compose build'
                }
            }
        }

        stage('Executar Containers Docker') {
            steps {
                script {
                    // Subir os containers em segundo plano
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Verificar Containers') {
            steps {
                script {
                    // Listar containers em execução para verificar se estão ativos
                    sh 'docker ps'
                }
            }
        }

        stage('Rodar Testes (Opcional)') {
            steps {
                script {
                    // Aqui você pode adicionar comandos para rodar testes, se houver
                    // sh 'pytest'  // Exemplo de comando para rodar testes com pytest
                }
            }
        }
    }

    post {
        always {
            // Limpar os containers e imagens após a execução do pipeline
            sh 'docker-compose down'
        }
    }
}

