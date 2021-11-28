pipeline {
    environment {
        registry = "chuchodavids/chuchobot:latest"
        registryCredential = 'dockerhub'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Cloning git') {
            steps {
                git 'https://github.com/Chuchodavids/Chucho-Discord-Bot.git'
            }
         stage('Building image')
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
         stage('Deploy Image')
            steps {
                script {
                    docker.withRegistry( '', registryCredential ) {
                         dockerImage.push()
                    }
                }
            }
        stage('Remove unused docker image')
            steps {
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
    }
}