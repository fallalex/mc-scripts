#!/usr/bin/env bash

# rewrite in python
# use mcstatus to check if the server is running

# get latest papermc jar
# should switch it to check if update is needed
curl --progress-bar https://papermc.io/api/v1/paper/1.16.1/latest/download -o server.jar

# get latest EssentialsX release jars
./update_plugins.py

# get Vault
git clone https://github.com/MilkBowl/Vault.git
cd Vault
git pull
mvn -q
cp ./target/Vault-*.jar ../plugins/Vault.jar
cd ..

# LuckPerms
git clone https://github.com/lucko/LuckPerms.git
cd LuckPerms
git pull
./gradlew -q build
cp ./bukkit/build/libs/LuckPerms-Bukkit-*.jar ../plugins/LuckPerms.jar
cd ..
