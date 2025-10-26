pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '-u root'
        }
    }
    
    environment {
        PYTHONUNBUFFERED = '1'
    }
    
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
                    python --version
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    fi
                '''
            }
        }
        
        stage('Lint') {
            steps {
                echo 'Running code quality checks...'
                sh '''
                    pip install pylint
                    pylint app.py || true
                '''
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    python -m pytest test_app.py -v --junitxml=test-results.xml || \
                    python -m unittest test_app.py
                '''
            }
        }
        
        stage('Run Application') {
            steps {
                echo 'Running the application...'
                sh 'python app.py'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed!'
            // Archive test results if they exist
            junit '**/test-results.xml' allowEmptyResults: true
        }
        success {
            echo '✅ All tests passed successfully!'
        }
        failure {
            echo '❌ Pipeline failed! Check the logs.'
        }
        cleanup {
            cleanWs()
        }
    }
}