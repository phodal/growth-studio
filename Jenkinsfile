node {

  stage 'Checkout'

  git 'https://github.com/phodal/growth-studio'

  stage 'Setup'
    stage 'Create Virtualenv'
      sh './ci/setup.sh'

    stage 'Install'
      sh './ci/install.sh'

  stage 'Test'
    stage 'Unit Test'
      sh './ci/unit_test.sh'

    stage 'E2E Test'
      sh './ci/e2e.sh'

  stage 'Deploy'
    echo 'Deploy In Design'
}