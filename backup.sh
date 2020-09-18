#!/usr/bin/env bash

TYPE=survival
PARENTDIR=/opt
GAMEDIR=$PARENTDIR/minecraft-$TYPE

DATE=`date "+%Y%m%d%H%M%S"`
TAR=${TYPE}-bak-${DATE}.tar.gz
tar czvf $TAR $GAMEDIR
mv $TAR $PARENTDIR/bak/
