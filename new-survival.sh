#!/usr/bin/env bash

TYPE=survival
PARENTDIR=/opt
GAMEDIR=$PARENTDIR/minecraft-$TYPE

# BACKUP
cd $PARENTDIR
$PARENTDIR/backup.sh

#rm -rf $GAMEDIR
mkdir $GAMEDIR
#cp $PARENTDIR/template/server-${TYPE}.properties $GAMEDIR/server.properties
ln -s $PARENTDIR/server.jar $GAMEDIR/server.jar
ln -s $PARENTDIR/template/whitelist.json $GAMEDIR/whitelist.json
# need to add plugin config links
echo "eula=true" > $GAMEDIR/eula.txt
