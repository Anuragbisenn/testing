plugins {
    id 'java'
    id 'jacoco'
    id 'org.sonarqube' version '3.3'
}

jacocoTestReport {
    reports {
        xml.required = true
    }
    dependsOn test
}

sonarqube {
    properties {
        property 'sonar.host.url', 'http://localhost:9000'
    }
}

tasks.named('sonarqube').configure {
    dependsOn jacocoTestReport
}

// repositories, dependencies, etc.