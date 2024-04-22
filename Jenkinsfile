pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                script {
                    sh 'python3 --version || sudo apt install -y python3'
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate'
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Run Unit Tests') {
            steps {
                script {
                    def testsExist = fileExists('tests/')
                    if (testsExist) {
                        sh 'pytest'
                    } else {
                        echo 'No unit tests found for this project.'
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t myflaskapp .'
                }
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: '**/*', onlyIfSuccessful: true
        }
        failure {
            echo 'Build failed, no artifacts to archive.'
        }
    }
}
