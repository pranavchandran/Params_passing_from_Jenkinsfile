pipeline {
    agent any

    parameters {
        choice(
            name: 'Environment', 
            choices: ['Development', 'Production'], 
            description: 'Choose the option'
        )
    }

    environment {
        // set the environment variable
        Environment = "${params.Environment}"
    }

    stage('Print Environment') {
        steps {
            echo "Environment: ${Environment}"
        }
    }

    stage('Checkout') {
        steps {
            // checkout the code from the github url
            git url: 'https://github.com/pranavchandran/Params_passing_from_Jenkinsfile.git', branch: 'main'
        }
    }

    stage('Run Python Code') {
        steps {
            // run the python code
            sh 'python3 jenkins_choice_params.py'
        }
    }
}