pipeline {
    agent any
    stages {
        stage('Jerrin - Build Docker Image') {
            steps {
                echo 'This is from stage: Build Docker Image'
                script {
                    powershell 'docker build -t jerrinthomast/jenkins-project:v1 .'
                }
            }
        }

        stage('Jerrin - Login to Dockerhub') {
            steps {
                echo 'This is from stage: Login to Dockerhub'
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhubpwd1', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                        bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASS%'
                    }
                }
                
            }
        }

        stage('Jerrin - Push image to Dockerhub') {
            steps {
                echo 'This is from stage: Push image to Dockerhub'
                script {
                    powershell 'docker push jerrinthomast/jenkins-project:v1'
                }
            }
        }
    }
}