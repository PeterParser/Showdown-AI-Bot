# Showdown AI Bot
#### A bot player for Pokémon Showdown
The bot can play on the pokémon showdown platform in the following formats of battle:
<p>Gen 1, 2, 3, 4, 5, 6, 7 random battle
<p>It can play also in 3 different modes: Easy, Normal, Hard

##How to install
Install the repository:
```
git clone https://github.com/JJonahJson/Showdown-AI-Bot.git
cd /path/to/Showdown-AI-Bot
```
Install the requirements to launch the bot:
```
pip3 install -r requirements.txt
```
Install docker to use the database needed by the bot:
```
sudo apt update
sudo apt install docker
```
##Launch the bot
Start docker:
```
sudo docker pull errevas/showdown_db:latest
sudo docker run --name=showdown_db -d errevas/showdown_db:latest
```
Everytime you want to launch the bot be sure docker is running, you can check the
running container with `sudo docker ps -a`.

If it's not running you have to digit `sudo docker start showdown_db`

Possible arguments for launching the bot:

```
-u username     where username is your Pokémon Showdown username    [NEEDED]
-m mode         mode can be "searching" or "challenging", if you use "challenging" you must specify the opponent    [DEFAULT "searching"]
-o opponent     where opponent is the Pokémon Showdown username of the opponent
-d difficult    difficult can be "easy", "normal" or "hard", it can be changed by the opponent during the game      [DEFAULT "easy"]
-g gen          gen can be a number from 1 to 7, it represents the generation of random battle you want to play     [DEFAULT "7"]
-s sex          sex can be "m" for males of "f" for females, it changes the avatar of the bot                       [DEFAULT "m"]
```
Examples of launch:
```
cd /path/to/Showdown-AI-Bot/src
python3 main.py -u username
python3 main.py -u username -g 2
python3 main.py -u username -m challenging -o opponent -d normal
python3 main.py -u username -m challenging -o opponent -d normal -g 6 -s f
```


