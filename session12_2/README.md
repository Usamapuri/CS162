## Software Containers

Today work is a guided exercise through docker.  You are encouraged to poke
things along the way to better understand what the different commands do (e.g
what happens if I edit this command?).  All of these commands are typed into a
shell which has changed to the `session12_1/web` directory.

### 1. Install docker
Start installing docker by following the instructions at:
https://www.docker.com/community-edition

Docker is reasonably lightweight in terms of how much memory and CPU it will use
on your laptop, but you are still encouraged to exit docker before coming to
class!

**On Windows**

Docker Desktop for Windows requires Hyper-V, which is only supported for 64-bit Windows 10 Pro, Enterprise or Education. Windows 10 Home users, as well as users of 32-bit versions and older versions of Windows have to resort to a legacy solution, and use the outdated "Docker Toolbox". See [this link](https://docs.docker.com/toolbox/toolbox_install_windows/).

### 2. Do the tutorial
First work through the 6 part tutorial on docker.  For this session focus on
sessions one and two.

### 3. Build the dockerfile:
```bash
docker build -t simple-cs162-flask:latest .
```
If anything fails here, then please ask for some technical assistance from
fellow students, and if they don't know ask your instructor.

### 4. Run an instance:
```bash
docker run --name=simple-cs162-instance -d --expose 5000 -p 5000:5000/tcp simple-cs162-flask
```
This command will run the container in detached mode, and will connect port 5000
on your local machine to port 5000 of the container.  You can verify this by
visiting `http://localhost:5000/` and you should see the interface to the
computation server.

**On Windows Running Docker Toolbox**

Find the app on the Docker Machine IP. By default, this is `http://192.168.99.100:5000/` where the port is specified after the colon). The IP can be found with the command `docker-machine ip`.

After the instance has started, then you can get a list of all running docker
instances with the command:
```bash
docker ps
```
You can also watch the logs of a docker instance by using the command:
```bask
docker logs -f simple-cs162-instance
```
Stopping or starting the container is a matter of:
```bash
docker container stop simple-cs162-instance
docker container start simple-cs162-instance
```

### 5. Tear it all down
Don't forget to clean up after yourself with the command:
```bash
docker rm -f simple-cs162-instance
```

## Questions
Bring to class a copy of the output from `docker ps` when your container is
successfully running. This needs to be in plain text, so a screenshot is
not appropriate.  Be prepared to explain your answers for the questions below.
```
Taha@DESKTOP-CH358ND MINGW64 ~/desktop/Spring 2020/cs162/session12_1/web (master)
$ docker ps  
CONTAINER ID        IMAGE                COMMAND             CREATED              STATUS              PORTS                    NAMES
cd1091c153e2        simple-cs162-flask   "python app.py"     About a minute ago   Up About a minute   0.0.0.0:5000->5000/tcp   simple-cs162-instance
```

### Q1. Bigger picture
Sketch out the bigger picture.  What parts are running on your computer, and
how do they interact with each other?  If there is terminology or acronyms that
you don't understand, search for an explanation on the internet, and bring these
explanation(s) to class to help your fellow students.

Sketch this out as a picture, in a format suitable for pasting into a group
document, and bring it to class.

```
$ docker logs -f simple-cs162-instance  
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)  
/usr/local/lib/python3.6/site-packages/sqlalchemy/sql/sqltypes.py:603: SAWarning: Dialect  
sqlite+pysqlite does *not* support Decimal objects natively,  
and SQLAlchemy must convert from floating point - rounding errors and other issues may occur.  
Please consider storing Decimal numbers   as strings or integers on this platform for lossless storage.  
'storage.' % (dialect.name, dialect.driver))  
192.168.99.1 - - [01/Apr/2020 04:25:31] "GET / HTTP/1.1" 200 -  
192.168.99.1 - - [01/Apr/2020 04:25:36] "POST /add HTTP/1.1" 302 -  
192.168.99.1 - - [01/Apr/2020 04:25:36] "GET / HTTP/1.1" 200 -  
[2021-03-30 04:25:39,799] ERROR in app: Exception on /add [POST]  
```

### Q2. Data persistence
Does the computation server persist data if it is stopped?  How can you tell?
```
It doesn't keep data when stopped becasue upon restarting the app, the table that is supposed to hold the previously entered data is empty.
```

### Q3. Environment variables
Read up on environment variables, and how Python accesses these variables.

Change the code such that the configuration information for the
SQLALCHEMY_DATABASE_URI is given by an environment variable.  What sort of
benefit might this entail?
