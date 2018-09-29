pipeline {
    agent any
    parameters {
        string(name: 'webapp', defaultValue: 'v_1.1', description: 'Webapp Docker Version')
        string(name: 'render_php', defaultValue: 'v_1.12', description: 'render_php Docker Version')
    }
    
    stages {   
        stage('git pull') {
            steps {
                git branch: 'staging', url: 'git@github.com:bunnydev26/development_docker.git'
                
            }
        }
        
        stage('Build and Test') {
            steps {
                sh 'sudo docker build -t amithapa/my_webapp:${params.webapp} webapp/'
                sh 'sudo docker build -t amithapa/my_frontend:${params.render_php} render_php/'
            }
        }
        
        stage('Deploy To Staging') {
            steps {
                echo "Deploying to staging"
            }
        }
        
        stage('Deploy To Production') {
            steps {               
                input("Do you want to deploy on Production?")  
                echo "Deployed on Production"
            }
        }
        
        stage('Email') {
            steps {               
                emailext body: '''Git checkout docker_development.
                Building from Jenkinsfile
                Docker build for webapp.
                Docker build for render_php''', subject: 'Build Execution Completed', to: 'amithapa1994@gmail.com'
            }
        }
    }
    post {
        success {
            echo "Merge Code to master"

            emailext body: '''Deployment is successfully completed''', 
                subject: 'Deploy Completed', to: 'amithapa1994@gmail.com'
        }
        failure {
            
            emailext body: '''Deployment has failed kindly check Jenkins''', 
                subject: 'Deploy Failed', to: 'amithapa1994@gmail.com'
        
        }
    }
}
