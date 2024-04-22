pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Installation de Python et pip
                    sh 'apt-get update'
                    sh 'apt-get install -y python3 python3-pip'

                    // Installation des dépendances Python depuis requirements.txt
                    sh 'pip3 install --user -r requirements.txt'
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
