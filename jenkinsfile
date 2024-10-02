pipeline {
    agent any

    environment {
        GIT_COMMIT_SHORT = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
        VERSION = "${GIT_COMMIT_SHORT}-${BUILD_NUMBER}"
        NEXUS_URL = 'http://nexus.example.com/repository/maven-releases/'
        SONARQUBE_URL = 'http://sonarqube.example.com'
        EC2_IP = 'your-ec2-ip-address'
        DEPLOY_USER = 'ec2-user'
        DEPLOY_DIR = '/home/ec2-user/opskart-project-healthcare'
    }

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/your-repo/opskart-project-healthcare.git'
            }
        }

        stage('Build App') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '. venv/bin/activate && python3 manage.py test'
            }
        }

        stage('Code Scan') {
            steps {
                script {
                    withSonarQubeEnv('SonarQube') {
                        sh '. venv/bin/activate && sonar-scanner -Dsonar.projectKey=myhealthapp -Dsonar.sources=. -Dsonar.host.url=${SONARQUBE_URL}'
                    }
                }
            }
        }

        stage('Publish to Cobertura') {
            steps {
                sh '. venv/bin/activate && coverage run --source=. manage.py test && coverage xml'
                cobertura coberturaReportFile: 'coverage.xml'
            }
        }

        stage('Upload Artifacts to Nexus') {
            steps {
                sh """
                . venv/bin/activate
                tar -czf myhealthapp-${VERSION}.tar.gz *
                curl -u user:password --upload-file myhealthapp-${VERSION}.tar.gz ${NEXUS_URL}
                """
            }
        }

        stage('Send Email for Approval') {
            steps {
                emailext subject: "Approval Required for Deployment",
                         body: "Please approve the deployment of build ${BUILD_NUMBER}.\n\nBuild Status: ${currentBuild.currentResult}\nBuild Number: ${BUILD_NUMBER}\nTriggered By: ${currentBuild.getBuildCauses()[0].userId}",
                         to: 'approver@example.com'
            }
        }

        stage('Approval') {
            steps {
                input message: 'Approve Deployment?', ok: 'Deploy'
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['your-credentials-id']) {
                    sh """
                    ssh ${DEPLOY_USER}@${EC2_IP} 'curl -u user:password -O ${NEXUS_URL}/myhealthapp-${VERSION}.tar.gz -o ${DEPLOY_DIR}/myhealthapp-${VERSION}.tar.gz'
                    ssh ${DEPLOY_USER}@${EC2_IP} 'cd ${DEPLOY_DIR} && tar -xzf myhealthapp-${VERSION}.tar.gz && . venv/bin/activate && python3 manage.py migrate && sudo systemctl restart gunicorn'
                    """
                }
            }
        }
    }

    post {
        always {
            emailext subject: "Build ${BUILD_NUMBER} - ${currentBuild.currentResult}",
                     body: "Build Status: ${currentBuild.currentResult}\nBuild Number: ${BUILD_NUMBER}\nTriggered By: ${currentBuild.getBuildCauses()[0].userId}",
                     to: 'your-email@gmail.com'
        }
    }
}
