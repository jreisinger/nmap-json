```
docker login
docker build -t nmap-json .
docker tag nmap-json reisinge/nmap-json
docker push reisinge/nmap-json
docker run reisinge/nmap-json scanme.nmap.org
```
