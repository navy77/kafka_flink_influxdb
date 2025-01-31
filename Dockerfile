FROM openjdk:17-jdk-slim
WORKDIR /app
COPY target/kafka-streams-app.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
