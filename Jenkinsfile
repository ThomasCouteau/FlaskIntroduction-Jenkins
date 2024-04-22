pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                script {
                    // Télécharger et installer Python 3 et pip
                    sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
                    sh 'python3 get-pip.py'

                    // Installer les dépendances Python depuis requirements.txt
                    sh 'pip install -r requirements.txt'
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
