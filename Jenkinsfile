pipeline{
    agent any
    stages{
        stage('Checkout'){
            steps{

                checkout scm
            }
        }
        stage('Dependency Check') {
            steps {
                sh('mkdir -p build/reports')
                dependencycheck additionalArguments: '--project PythonStig --scan ./ --out build/reports/dependency-check-report.xml --format XML', odcInstallation: 'OWASP-Dependency-Check'
            }
        }

    }
    post {
        always {
            dependencyCheckPublisher pattern: 'build/reports/dependency-check-report.xml'
        }
    }
}
