---
layout: post
title: "Siri, what's on TV?"
summary: A plugin for SiriProxy that gives Siri access to the Belgian television guide. You just ask "What's on TV?" and Siri will answer, even when there's nothing on!
thumbnail: /img/siriwhatsontv/siri.jpg
tags: siri, ruby, tv, belgium
---
###Introduction
Yes, yes, I sold a little piece of my soul and bank account and bought myself an iPhone 4S. Apart from the price tag, the only doubt I had was the due to the
closed nature of all Apple products. Seems its not all that closed though, with a little work, you can get Siri on the iPhone to just about anything you want except the dishes.
In this article, I will discuss the steps that were needed to add some custom functionality to Siri. With these steps, Siri will respond to the command "What's on TV?".
It will display a list of TV programmes and you can even ask for a summary for that program.


###The ingredients
Actually getting everything together is a bit of work but I managed to get it up and running in a few hours. Here are the main components you will need. <a href="https://gist.github.com/1428474" target="_blank">This script</a> by SiriProxy's author helped me a lot in setting up the environment so if you want more details, you should definitely check that out.


####A Linux (virtual) machine and custom DNS server
We basically want our iPhone to think its talking to an official Apple Siri server. For this, we will need a DNS server on our local network which will resolve the address _guzzoni.apple.com_ to the address
of our fake server which is running SiriProxy. For the sake of convenience, lets say this is the same one as the DNS server.

I added a new virtual machine in VMWare based on an Ubuntu 11.10 instance. Then I installed _dnsmasq_ using _apt-get_ and edited the _/etc/dnsmasq.conf_ file to redirect
_guzzoni.apple.com_ to the machine which will run SiriProxy; so in this case the same one. Here is the entry I had to add:

<script src="https://gist.github.com/1909620.js"> </script>


####SiriProxy
This opensource ruby project will fake Apple's official Siri servers protocol and allows user to create plugins that listen to commands. Writing these plugins
is extremely simple, as we will see later. I would say the installation is more difficult, though the process is described well <a href="https://github.com/plamoni/SiriProxy" target="_blank">on the website</a>.

Here is a screenshot of SiriProxy running in the VM.

<div style="text-align:center"><img src="../../../img/siriwhatsontv/vm.jpg" width="500" height="400" /></div>

####A configured iPhone
An important step here is to generate an SSL certificate using SiriProxy. You then need to install that certificate on your iPhone. You can do this easily by mailing it to yourself...

Open up the certificate file (siriproxy.pem) on your iPhone and install it by clicking the icon:

<div style="text-align:center"><img src="../../../img/siriwhatsontv/cert.jpg" width="200" height="300" /></div>

You will also need to point your iPhone's DNS server to the IP of our own DNS server. You can do this at Settings => WIFI => Press the arrow after your network => DNS. Enter the same IP address here, which is 192.168.0.133 in our case.

OK the iPhone is configured. To revert back, you can remove the certificate by going to General => Profile => Remove. Don't forget you'll also need to revert the DNS settings to point to your home gateway again.


####JXMLTV
JXMLTV is a Java XMLTV grabber; which means it can dump the TV schedule to an XML file, which is then readable by another application, such as my SiriProxy plugin.
To use it, go to <a href="http://users.skynet.be/jxmltv/index.html" target="_blank">the website</a> and download the latest version, preferably on the same machine that will run SiriProxy.
You can then start JXMLTV, which will dump the schedule to a file. Then we just need to copy that file to _/tmp/jxmltv/xmltv.xml_ so the SiriProxy plugin can read it.

<script src="https://gist.github.com/1909534.js?file=jxmltv.sh"> </script>

If you're installing something more permanent ,you may want to automate this process by creating a daily cron job for this.

Before running JXMLTV, you should first check if your system time is correct, because on my Virtual Machine that wasn't the case for some reason, which resulted in no data at all.


####Install DominiekTV
The SiriProxy plugin I created can be found on <a href="https://github.com/ddierickx/dominiektv" target="_blank">my github page</a>. It is also my first Ruby script ever and I have to say writing Ruby feels really natural.

To install DominiekTV, do the following:

<script src="https://gist.github.com/1909574.js"> </script>

Make sure you verified the directories in the above script above since they won't match your setup.

###The results
Okay, to recap, here's what you should have by now:

- A Linux VM running dnsmasq.
- SiriProxy installed on that machine.
- DominiekTV plugin for SiriProxy installed.
- The output of the JXMLTV tool in /tmp/jxmltv/xmltv.xml
- The certificate installed on your iPhone and the DNS server on your iPhone changed to the VM's IP.

If you have all these, you can fire up SiriProxy by going to the folder you installed it in and entering:

<script src="https://gist.github.com/1909660.js"> </script>

This should show a message saying SiriProxy has started on port 443.

Then you can ask Siri "What's on TV?", it will read the TV schedule for you, here's what you will see on the screen:

<div style="text-align:center">
	<img src="../../../img/siriwhatsontv/result.jpg" width="200" height="300" />
</div>

You can also ask Siri something like "What's 'My Wife and Kids' about?", it will give the synopsis of the show.

<div style="text-align:center">
	<img src="../../../img/siriwhatsontv/whatsabout.jpg" width="200" height="300" />
</div>

###Conclusion
That was pretty easy. There are some downsides though. Because we tampered with the iPhone configuration, Siri won't work out of your home network (unless you remove the certificate). Your iPhone's internet connection will also fail if the DNS server is not longer running.
That said, SiriProxy offered us a way to easily extend Siri with custom functionality. I can only imagine how difficult it must have been to get that working, so kudos!
