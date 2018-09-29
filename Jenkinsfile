pipeline {
    agent any
    stages {   
        stage('git pull') {
            git branch: 'staging', url: 'git@github.com:bunnydev26/development_docker.git'
        }

        stage('build') {
            sh 'sudo docker build -t amithapa/my_webapp:v_1.0 webapp/'
        }

        stage('test') {
            sh 'sudo docker build -t amithapa/my_frontend:v_1.0 render_php/'
        }
        
        stage('Deploy To Staging') {
            echo "Deploying to staging"    
        }
        
        
        stage('Confirm Deploy on Production') {
             input("Do you want to deploy on Production?")    
        }
        
        stage('Deploy To Production') {
            echo "Deployed on Production"
        }
        
        stage('Email') {
            emailext body: '''Git checkout docker_development.
            Building from Jenkinsfile
            Docker build for webapp.
            Docker build for render_php''', subject: 'Build Execution Completed', to: 'amithapa1994@gmail.com'
        }
    }
}
