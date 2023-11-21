FROM jenkins/jenkins:lts

# Install Jenkins Configuration as Code using jenkins-plugin-cli
RUN jenkins-plugin-cli --plugins "configuration-as-code:1714.v09593e830cfa"

COPY jenkins.yaml $JENKINS_HOME/jenkins.yaml
ENV CASC_JENKINS_CONFIG=$JENKINS_HOME/jenkins.yaml

# Disable CSRF protection and setup wizard
ENV JAVA_OPTS "-Dhudson.security.csrf.GlobalCrumbIssuerConfiguration.DISABLE_CSRF_PROTECTION=true -Djenkins.install.runSetupWizard=false"

USER root

# Install required packages
RUN apt-get update && apt-get install -y unzip && apt-get clean

# Install SonarQube Scanner
RUN curl -L -o /tmp/sonarscanner.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip
RUN unzip /tmp/sonarscanner.zip -d /opt/ && mv /opt/sonar-scanner-5.0.1.3006-linux /opt/sonar-scanner
RUN rm /tmp/sonarscanner.zip

# Config a SonarQube job
COPY DummyProject/ $JENKINS_HOME/jobs/DummyProject/
RUN chown -R jenkins:jenkins $JENKINS_HOME

# Switch back to Jenkins user
USER jenkins

ENV SONAR_HOST_IP="192.168.1.68"
ENV SONAR_HOST_PORT="9000"

# Expose Jenkins ports
EXPOSE 8080
EXPOSE 50000

CMD ["/sbin/tini", "--", "/usr/local/bin/jenkins.sh"]