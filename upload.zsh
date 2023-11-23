#!/bin/sh

git add --all
wait
echo ' add completed'

git commit -m "Upload"
wait
ehco 'commit completed'

git push origin main
wait 
echo 'push completed'
