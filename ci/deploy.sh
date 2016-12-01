#!/usr/bin/env bash
. py35env/bin/activate
fab deploy:"1.${env.BUILD_NUMBER}"
