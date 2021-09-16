#!/bin/bash
pip3 install -r requirements.txt
sleep 5
python3 gensa.py --quick-setup $1
python3 createmail.py
zip -q accounts.zip accounts/
mv token_sa.pickle token.pickle
zip -q all.zip accounts.zip token.pickle email.txt
