pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = "laxminavalagi/flask-hello-world"
        CONTAINER_NAME = "flask-hello-world"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']],
                          extensions: [], 
                          userRemoteConfigs: [[url: 'https://github.com/laxminavalagi/flask-hello-world-devops-project.gits']]])
            }
        }

        stage('Build') {
            steps {
                echo 'Building..'
                bat 'docker build -t %DOCKER_HUB_REPO%:latest .'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing..'
                bat 'docker stop %CONTAINER_NAME% || exit 0'
                bat 'docker rm %CONTAINER_NAME% || exit 0'
                bat 'docker run --name %CONTAINER_NAME% %DOCKER_HUB_REPO% cmd /c "pytest test.py && flake8"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying....'
                bat 'docker stop %CONTAINER_NAME% || exit 0'
                bat 'docker rm %CONTAINER_NAME% || exit 0'
                bat 'docker run -d -p 5000:5000 --name %CONTAINER_NAME% %DOCKER_HUB_REPO%'
            }
        }
    }
}
