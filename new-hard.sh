#!/usr/bin/env bash

TYPE=hardcore
PARENTDIR=/opt
GAMEDIR=$PARENTDIR/minecraft-$TYPE

rm -rf $GAMEDIR
mkdir $GAMEDIR
cp $PARENTDIR/template/server-${TYPE}.properties $GAMEDIR/server.properties
ln -s $PARENTDIR/server.jar $GAMEDIR/server.jar
ln -s $PARENTDIR/template/whitelist.json $GAMEDIR/whitelist.json
echo "eula=true" > $GAMEDIR/eula.txt
