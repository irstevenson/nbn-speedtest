# Introduction

After experiencing download speed degredation at my home, I decided to monitor
my download speeds with the use of <http://speedtest.net>. Specifically
though, I wanted to capture the data automatically so that I could graph it and
look for any patterns.

The result was this project which consists of:

* The `speedtest-cli` script by Matt Martz -
  <https://github.com/sivel/speedtest-cli>
* A crond schedule to call `speedtest-cli` at 15 minute intervals and append to
  a CSV
* The `process.py` script I hacked together to transform from CSV to a JSON
  file suitable for a [plotly.js](https://plot.ly/javascript/) heatmap.
* And `speedtest.html` to tie it all together.

# Usage

After cloning the project, have a crond schedule such as:

    */15 * * * * /home/<username>/<clone_loc>/speedtest-cli --csv >> /home/<username>/<clone_loc>/speedtest.csv

Once you've accumulated some data, then use the `process.py` script to create the JSON:

    $ cat speedtest.json

Lastly, place the speedtest.json and speedtest.html on your web server.

(And if you wanted more live data, you'd actually schedule in those last two steps.)

# ToDo

There's plenty more fun to be had with this data if time permitted:

* Do some other graphs
* Graph some of the other data - upload speeds and/or latency
* Change the heatmap colours to be linear on a single colour
* Change the numbers to Mbps rather than just bps

But, not sure I'll do anything more... not for now. It's shown me what I wanted to see.
