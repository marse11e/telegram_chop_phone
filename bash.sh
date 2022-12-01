#!/bin/zsh

echo "Start"

git init
git remote add origin git@github.com:marse11e/telegram_chop_phone.git
git add .
git commit -m 'all'
git push -u origin master

echo "Finish"
