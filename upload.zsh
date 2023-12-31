#!/bin/sh

git pull origin master
wait
echo 'pull completed'

git add --all
wait
echo ' add completed'

git commit -m "Upload"
wait
echo 'commit completed'

git push origin master
wait 
echo 'push completed'
