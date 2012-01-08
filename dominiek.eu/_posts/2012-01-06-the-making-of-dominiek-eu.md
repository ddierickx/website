---
layout: post
title: The making of dominiek.eu
summary: Some words on how this website was created using third party tools such as Jekyll and Foundation.
thumbnail: /img/makingof/jekyll.png
tags: meta, jekyll, foundation, static-site-generators, github
---
#### The makeover
A while ago I decided it was time for a makeover of my old website, which was actually a blog.
The entries that were a bit outdated, nor in line with the ideas and interests I have now.
I also wanted to get rid of the whole "blog" stuff, my new site will offer some articles but I don't intend to be adding stuff daily or
even weekly, so the term "Article" should be a better fit for that purpose.

I decided it was time for action.

The first thing I would normally do in that situation would be:

- Download the latest Wordpress install.
- Create a new MySQL database.
- Install and configure Wordpress.

This all seemed a bit heavy for the purpose at hand, so I went out looking for something a bit more lightweight, something that didn't require any backend database or server-side scripting language.
I started Google'ing for "static web site generator" and quickly came across <a href="https://github.com/mojombo/jekyll" target="_blank">Jekyll</a>.

#### Jekyll
Jekyll is an awesome ruby gem that can will generate a website (html/js/css), given a template and content. One of the main advantages for me here
is that I can version control the entire website, so I can store it on github! This also makes it a lot easier to backup the entire thing, since all the
content is kept in the files and nothing needs to be in a database. 

Because of this, I could host my site anywhere I'd like and I'm not attached to MySQL or PHP...
A final reason to this for me was speed. Since all pages are generated beforehand, the webserver just needs to pass the html/css/js/images to the browser, no server clock cycles needed!

Jekyll also contains a very nice preview server that will auto-regenerate the site when a file has changed.

Starting the server is easy as:

<script type="text/javascript" src="http://snipt.net/embed/5b5c39bf9d9d488f7f004f5dc1d88e75">
</script>
<p />
OK, so I decided to do my website using Jekyll. I still needed to do some webdesign, enter Foundation.

#### Foundation

I am __not__ a webdesigner. I don't know much about aesthetics or about building a web design that is portable across both devices and browser versions. That's just no my cup of tea.

Enter <a href="http://foundation.zurb.com" target="_blank">Foundation</a>.

Foundation is a framework that consists of javascript and css files. The idea that everything is in there to quickly create a website from scratch, without all the boilerplate code.
The framework <a href="http://foundation.zurb.com/docs" target="_blank">contains a bunch of stuff</a> but the thing I used most extensively on this site is the grid system.

<style>
	.row.display { background: #f4f4f4; margin-bottom: 10px; border-radius: 3px; -webkit-border-radius: 3px; -moz-border-radius: 3px; }
	.row.display .column, .row.display .columns { background: #e7e7e7; font-size: 11px; text-indent: 3px; padding-top: 6px; padding-bottom: 6px; border-radius: 3px; -webkit-border-radius: 3px; -moz-border-radius: 3px; }
</style>

<div class="row display">
	<div class="twelve columns">
		twelve columns
	</div>
</div>

<div class="row display">
					<div class="three columns">
						.three.columns				
					</div>
					<div class="six columns">
						.six.columns				
					</div>
					<div class="three columns">
						.three.columns				
					</div>
</div>

Grid systems are pretty hot nowadays (<a href="http://www.960.gs" target="_blank">960.gs</a>, <a href="http://code.google.com/p/the-golden-grid/" target="_blank">Golden grid</a>, <a href="http://blueprintcss.org/" target="_blank">Blueprint</a>, ...).
They help out in creating websites that scale properly across different screen sizes. The grid system in Foundation has been created from the ground up and seems really good and was very intuitive to use.

Foundation comes with a bunch of javascript and css files which need to be included along with all the other stuff you may already use. Looking for a way to optimize this, I came across Juicer.

#### Juicer
Juicer is a javascript and css bundler and minifier. It will take a set of js or css files, compress them and add merge them into a single file. This will reduce the number of files and the total filesize, which will make it alot faster to download.
On your webpage, you only need to refer to one js and css file which contains all the merged scripts.

I "integrated"  this with Jekyll using a <a href="http://rake.rubyforge.org/" target="_blank">rake</a> task which calls:

<script type="text/javascript" src="http://snipt.net/embed/e2a1630a85d2e433609c8da85c42e981">
</script>
<p />
This will create a single min.js file which contains all javascript for the website.

#### The result
Your looking at it! This was the first time I did this but I would really recommended it to anyone
that just wants to create a small website and doesn't want the overhead of PHP/MySQL. In the spirit of Jekyll, Foundation and Juicer, you can also find the source of this website in <a href="http://github.com/ddierickx" target="_blank">my github repository</a>.