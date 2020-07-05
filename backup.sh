#!/usr/bin/env bash

TYPE=survival
PARENTDIR=/opt
GAMEDIR=$PARENTDIR/minecraft-$TYPE

DATE=`date "+%Y%m%d%H%M%S"`

tar czvf ${TYPE}-bak-${DATE}.tar.gz $GAMEDIR
