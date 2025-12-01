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
                    withCredentials([string(credentialsId: 'dockerhubpwd', variable: 'dockerhubpwd')]) {
                        powershell '$env:dockerhubpwd | docker login -u jerrinthomast --password-stdin'
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