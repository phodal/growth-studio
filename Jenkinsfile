node {

  stage ('Checkout') {
    git 'https://github.com/phodal/growth-studio'
  }

  stage ('Create Virtualenv') {
    sh './ci/setup.sh'
  }

  stage ('Install') {
    sh './ci/install.sh'
  }

  stage ('Unit Test') {
    sh './ci/unit_test.sh'
  }

  stage ('E2E Test') {
    sh './ci/e2e.sh'
  }

  stage ('Release') {
    sh "git tag -a 'v1.${env.BUILD_NUMBER}' -m 'Auto Tag: 1.${env.BUILD_NUMBER}'"
    sh "git push origin 'v1.${env.BUILD_NUMBER}'"
  }
  
  stage ('Deploy') {
    sh '. py35env/bin/activate'
    sh "fab deploy:'1.${env.BUILD_NUMBER}'"
  }

  stage ('AC') {
    sh './ci/ac.sh'
  }
}