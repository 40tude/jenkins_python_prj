pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
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