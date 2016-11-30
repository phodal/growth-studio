git config user.email 'robot@phodal.com'
git config user.name 'phodal'
git tag -a 'v1.${env.BUILD_NUMBER}' -m 'Auto Tag: 1.${env.BUILD_NUMBER}'
git push origin 'v1.${env.BUILD_NUMBER}'
