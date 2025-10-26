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
                bat '''
                    python --version
                    pip install --upgrade pip
                '''
            }
        }
        
        stage('Lint') {
            steps {
                echo 'Running code quality checks...'
                bat '''
                    pip install pylint
                    pylint app.py || exit 0
                '''
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running unit tests...'
                bat 'python -m unittest test_app.py -v'
            }
        }
        
        stage('Run Application') {
            steps {
                echo 'Running the application...'
                bat 'python app.py'
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