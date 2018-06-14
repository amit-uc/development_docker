**Build the images**

```bash
docker build -t test_api /home/amit/workspace/development_docker/webapp

docker build -t test_php /home/amit/workspace/development_docker/render_php
```

**Runing Docker Image to run the Webapp**
```bash
docker run -it -p 9876:9876 -v /home/amit/workspace/development_docker/webapp:/app test_api /bin/sh
```

**Running Docker Image to run the website to render the PHP**
```bash
docker run -it -p 80:9000 -v /home/amit/workspace/development_docker/render_php/website:/var/www/html test_php /bin/bash
```
