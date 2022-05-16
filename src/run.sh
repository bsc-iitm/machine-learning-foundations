#!/bin/sh
ifile=$1
ofile=$2
while inotifywait -qqre modify "$ifile"; do
    pandoc -t slidy -s "$ifile" -o "$ofile" --mathjax
    sed -i 's/<head>/<head>\n  <script type="text\/javascript" src="https:\/\/livejs.com\/live.js"><\/script>/g' "$ofile"
done
