---
layout: post
title: Colruyt meets Foursquare
summary: Experiment on extracting visit statistics to points-of-interests using the Foursquare API and some Python scripts. Find out the best time & day to visit your local supermarket or other POIs by analyzing crowdsourced data. Results of a three-week data monitoring experiment is presented here as well as the created tools used to gather it.
thumbnail: /img/colruyt.png
tags: data-analysis, colruyt, foursquare, statistics
---
### Introduction

<img src="/img/colruyt.png" width="260" height="240" />

In this article, I will discuss the setup and results of an experiment I did with gathering data using the API offered by Foursquare. 
If you never heard of Foursquare, it is a (smartphone) application that allows users to share their whereabouts with the rest of the world, also know as checking-in. I can't really say why I would do this myself but apparently plenty of people love the idea and are checking in literally everywhere to conquer badges and street-cred...

While waiting in line at the local supermarket (<a href="http://www.colruyt.be" target="_blank">Colruyt</a>) I had the idea of using this publicly available crowd-sourced data to graph supermarket visits in time.
I was thinking where I could find the necessary data to make this graph and after digging into the <a href="https://developer.foursquare.com/docs/explore" target="_blank">Foursquare API</a>, I got an idea on how it could be done.

### The idea

Using the Foursquare API, we can search for venues that match given criteria, such as contain the word "Colruyt".
This search is limited to results within a 100 kilometer radius of the required "ll" (location) parameter, so in order to gather data for a larger dataset,
we would need just a couple of measure points (at least for Belgium). Keeping a list of unique venue ids we would like to monitor could also be an option but that would need too much requests since
the script would then have to send a request for each venue, while when using the search function, the number of checkins is also returned within the results.

Based on this idea, I wrote a script that takes as input a set of locations (lat/lon), a time interval n, a query (such as "Colruyt") and an <a href="https://developer.foursquare.com/overview/auth" target="_blank">OAuth2 token</a> (needed for Foursquare API authentication). Every n seconds, the script will send a search request to the
foursquare API and dump the results (venueID, number of checkins) to a file. This file is then after the monitoring is done aggregated and plotted.

### Tools

<div class="alert-box">Note: all code can be found in my <a href="https://github.com/ddierickx/scripts/tree/master/foursquarestats" target="_blank">github repository</a>.</div>

I created two tools to get the statistics:

- __fsquerystats.py__ : the generic monitoring script that will poll the Foursquare search results and store the number of checkins.
- __fsquerystats\_export.py__ : will aggreggate the results of the other script and create graphs using <a href="http://matplotlib.sourceforge.net/" target="_blank">mathplotlib</a>.

### Setup

The __fsquerystats__ script was run with the following arguments:

<script src="https://gist.github.com/1902530.js"> </script>

<p />
The script ran for __3 weeks__ and polled the search results for the term "Colruyt" in a large part of Belgium, storing the number of checkins to a file.
There were __118 establishment__ watched each __15 minutes__, this resulted in __14860724__ datapoints.

### Results & Chart

Now it gets interesting, here are some charts.

Here are the visit statistics for each day individually, Sunday not included for obvious reasons.

<a href="/img/colruyt/Mondays.png" title="Mondays" class="lbpopup"><img src="/img/colruyt/Mondays.png" width="325" height="325" /></a>
<a href="/img/colruyt/Tuesdays.png" title="Tuesdays" class="lbpopup"><img src="/img/colruyt/Tuesdays.png" width="325" height="325" /></a>
<a href="/img/colruyt/Wednesdays.png" title="Wednesdays" class="lbpopup"><img src="/img/colruyt/Wednesdays.png" width="325" height="325" /></a>
<a href="/img/colruyt/Thursdays.png" title="Thursdays" class="lbpopup"><img src="/img/colruyt/Thursdays.png" width="325" height="325" /></a>
<a href="/img/colruyt/Fridays.png" title="Fridays" class="lbpopup"><img src="/img/colruyt/Fridays.png" width="325" height="325" /></a>
<a href="/img/colruyt/Saturdays.png" title="Saturdays" class="lbpopup"><img src="/img/colruyt/Saturdays.png" width="325" height="325" /></a>

<p />
Here is a graph with visits per weekday:

<a href="/img/colruyt/all.png" title="Bar chart showing checkins per weekday." class="lbpopup"><img src="/img/colruyt/all.png" width="400" height="400" /></a>

Here is a combined graph for each day, you can clearly see some trends here.

<a href="/img/colruyt/AllInOne.png" title="Combined line chart of checkins per weekday." class="lbpopup"><img src="/img/colruyt/AllInOne.png" width="400" height="400" /></a>

### Conclusions

From these charts we can conclude some things:

- The calmest time to visit should be on Thursday, 09:00.
- Saturdays tend to be the most busy day, especially in the morning.
- Visitor count seems to decrease in the early afternoon after 13:00 until it rises again at 15:30.
- You can clearly see the store is open an extra hour on Friday (purple line).
- A lot of people seem to visit between 18:00 and 19:00, after work.

These numbers are of course not really representative, since Foursquare is only used by a really small (but sufficient) number of people and
its usage is probably restricted to technology enthousiasts, so that excludes most elderly people. The numbers are not that big but I had expected them to be
a lot lower than this. We could clearly see some trends here though I only had three weeks of data.

Don't hesitate to contact me with any questions or feedback, thanks for reading!
