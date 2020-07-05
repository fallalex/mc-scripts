#!/usr/bin/env bash

# use mcstatus to check if the server is running

# get latest papermc jar
./update_papermc.py

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
