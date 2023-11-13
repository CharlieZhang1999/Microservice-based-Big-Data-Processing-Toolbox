FROM jenkins/jenkins:lts

# Install Jenkins plugins using jenkins-plugin-cli
RUN jenkins-plugin-cli --plugins "sonar:2.16.1" "github:latest" "configuration-as-code:1714.v09593e830cfa"

ENV CASC_JENKINS_CONFIG=/var/jenkins_home/jenkins.yaml
COPY jenkins.yaml /var/jenkins_home/jenkins.yaml

# Expose Jenkins ports
EXPOSE 8080
EXPOSE 50000

CMD ["/sbin/tini", "--", "/usr/local/bin/jenkins.sh"]