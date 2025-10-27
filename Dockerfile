# créer un utilisateur non privilégié jenkins
# exécuter Jenkins sous cet utilisateur (et non sous root)
FROM jenkins/jenkins:lts-jdk17           

# on passe ROOT
USER root 
RUN apt-get update && apt-get install -y docker.io && \
    usermod -aG docker jenkins && \
    apt-get clean

# on redevient user jenkins
USER jenkins 