FROM jenkins/jenkins:lts

USER root

# Install required packages
RUN apt-get update && apt-get install -y unzip && apt-get clean

# Install SonarQube Scanner
RUN curl -L -o /tmp/sonarscanner.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip
RUN unzip /tmp/sonarscanner.zip -d /opt/ && mv /opt/sonar-scanner-5.0.1.3006-linux /opt/sonar-scanner
RUN rm /tmp/sonarscanner.zip

# Switch back to Jenkins user
USER jenkins

# Install Jenkins plugins using jenkins-plugin-cli
RUN jenkins-plugin-cli --plugins "sonar:2.16.1" "github:latest" "configuration-as-code:1714.v09593e830cfa"

ENV CASC_JENKINS_CONFIG=/var/jenkins_home/jenkins.yaml

# Disable CSRF protection and setup wizard
ENV JAVA_OPTS "-Dhudson.security.csrf.GlobalCrumbIssuerConfiguration.DISABLE_CSRF_PROTECTION=true -Djenkins.install.runSetupWizard=false"
COPY jenkins.yaml /var/jenkins_home/jenkins.yaml

# Expose Jenkins ports
EXPOSE 8080
EXPOSE 50000

CMD ["/sbin/tini", "--", "/usr/local/bin/jenkins.sh"]