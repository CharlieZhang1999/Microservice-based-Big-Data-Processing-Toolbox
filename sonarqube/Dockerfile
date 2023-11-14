FROM sonarqube

ENV SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true

USER root

RUN echo "sonar.forceAuthentication=false" >> $SONARQUBE_HOME/conf/sonar.properties

USER sonarqube

EXPOSE 9000

ENTRYPOINT ["/opt/sonarqube/docker/entrypoint.sh"]