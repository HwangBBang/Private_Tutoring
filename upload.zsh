#!/bin/sh

git add --all
wait
echo ' add completed'

git commit -m "Upload"
wait
echo 'commit completed'

git push origin main
wait 
echo 'push completed'
