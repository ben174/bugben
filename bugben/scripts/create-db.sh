#!/usr/bin/env bash
rm ../bugben.db
rm bugben.db
../manage.py syncdb
./provision-data.py
cp bugben.db ../
