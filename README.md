build and push to registry

```
docker build -t nmap-json .
docker login
docker tag nmap-json reisinge/nmap-json
docker push reisinge/nmap-json
```

run

```
docker run reisinge/nmap-json scanme.nmap.org
```
