pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'sudo apt update'
                    sh 'sudo apt install -y python3 python3-pip'

                    sh 'pip3 install -r requirements.txt'
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
