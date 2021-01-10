# Alfred
Your personal chef

### Build application
Build the Docker image manually by cloning the Git repo.
```
git clone https://github.com/kghumaan/Alfred.git
docker build -t Alfred:1.0 .
```

### Run the container
Create a container from the image.
```
ocker run --name my-container -d -p 8080:8080 Alfred:1.0
```

Now visit http://localhost:8080 - currently prints out hostname and IP for the client
```
 The hostname of the container is 6095273a4e9b and its IP is 172.17.0.2. 
```

### Verify the running container
Verify by checking the container ip and hostname (ID):
```
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-container
172.17.0.2
docker inspect -f '{{ .Config.Hostname }}' my-container
6095273a4e9b
```

### SET UP
Get Pycharm professional (~20 bucks a month or free through student account) :
https://www.jetbrains.com/pycharm/download/#section=mac


Set up requirements:
https://www.jetbrains.com/help/pycharm/managing-dependencies.html

Add following plugins within Pycharm:
* Requirements.txt
* env file support
* .ignore support
* Live Edit
* CSV pluggin

