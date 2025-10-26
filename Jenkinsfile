pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Setup') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                    python3 --version
                    python3 -m pip install --upgrade pip
                '''
            }
        }
        
        stage('Lint') {
            steps {
                echo 'Running code quality checks...'
                sh '''
                    python3 -m pip install pylint
                    python3 -m pylint app.py || true
                '''
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh 'python3 -m unittest test_app.py -v'
            }
        }
        
        stage('Run Application') {
            steps {
                echo 'Running the application...'
                sh 'python3 app.py'
            }
        }
    }
    
    post {
        success {
            echo '✅ All tests passed successfully!'
        }
        failure {
            echo '❌ Pipeline failed! Check the logs.'
        }
    }
}