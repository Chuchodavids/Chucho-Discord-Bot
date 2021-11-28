pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'touch $USERDIR/health'
            }
        }
    }
}