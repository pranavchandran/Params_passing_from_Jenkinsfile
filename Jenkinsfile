Pipeline {
    agent any

    parameters {
        choice(name: 'Environment', choices: ['Development', 'Production'], description: 'Choose the option')
    }

    Environment = "${params.Environment}"

    stage('Print Environment') {
        steps {
            echo "Environment: ${Environment}"
        }
    }
}