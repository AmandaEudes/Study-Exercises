# Study-Exercises

1. Run:
```shell
make run
```
2. Open [this](https://sonarqube.docker.localhost) site
3. Access using admin and admin as login and password, consecutively
4. Change password
5. Click on "Manually"
6. Fill in with what is in `SONARQUBE_PROJECT_NAME` (in the .env file)
7. Click on "Locally"
8. You can leave the default for the token
9. Copy the key
10. Paste in `SONARQUBE_PROJECT_KEY` (in the .env file)
11. Click the "continue" button
12. Run in a new terminal (without killing the initial terminal):
```shell
make sonar
```
13.  Open [this](https://sonarqube.docker.localhost) site
