node('master') {
    stage('git pull') {
        git 'git@github.com:bunnydev26/development_docker.git'    
    }
    
    stage('build webapp') {
        sh 'sudo docker build -t amithapa/my_webapp:v_1.0 webapp/'
    }
    
    stage('build render_php') {
        sh 'sudo docker build -t amithapa/my_frontend:v_1.0 render_php/'
    }
    
    stage('Email') {
        emailext body: '''Git checkout docker_development.
        Building from Jenkinsfile
        Docker build for webapp.
        Docker build for render_php''', subject: 'Build Execution Completed', to: 'amithapa1994@gmail.com'
    }
    
}
