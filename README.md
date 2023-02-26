# Automated RUB-Network Login 
In order to gain access to network in dorms connected to RUB-Network you have to constantly login over at
[login dot rz](https://login.ruhr-uni-bochum.de/cgi-bin/start). Not only is it really annoying, but you are
constantly being logged out due to inactivity. Apart from that, you will lose connection every day at 7:00 AM.
<br>
<br>
In order to fix this madness, you could use something like a Raspberry PI (any model will be fine, even old and
cheap one like Raspberry PI Zero W or 2) with an automated script, that constantly checks for connection and logs
you back in, as soon as you are logged out. An always-on PC or old Android smartphone could also do the trick.
<br>
<br>
## Prerequisites on a system
 - Docker

In order to install docker on your PI, follow [these](https://www.simplilearn.com/tutorials/docker-tutorial/raspberry-pi-docker)
instructions. After installation don't forget to update Docker, see [here](https://stackoverflow.com/a/72719088), in 
order to give sufficient permissions to docker, **OTHERWISE SCRIPT WON'T RUN**.

## Installation process
 - Make sure that Docker is up and running
 - Clone this project with `git clone git@github.com:l0rem/AutoRUBLogin.git`
 - Open project folder with `cd AutoRUBLogin/`
 - Open and insert your login credentials into `.env-example` with something like `nano .env-example`, save changes
 - Rename file to `.env` with `mv .env-example .env`
 - Run `docker compose up -d` to start the script

## Debugging
In order to access logs of the script do `docker ps`, then find container named `autorublogin-login` and note its
CONTAINER ID on the left of the line. Use that CONTAINER ID in `docker logs <CONTAINER_ID>` in order to get logs from 
container.