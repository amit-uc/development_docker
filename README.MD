
**Building the API Image**
```bash
docker build --tag test_api /home/mis/workspace/development_docker/webapp
docker run -it -p 8876:9876 -v /home/mis/workspace/development_docker/webapp:/app test_api /bin/sh
```

**Building the Website Image**
```bash
docker build --tag test_php /home/mis/workspace/development_docker/render_php
docker run -d -p 9001:80 -v /home/mis/workspace/development_docker/render_php/website:/var/www/html test_php
```

**Curl Request**
```bash
curl http://localhost:8876/product
```
