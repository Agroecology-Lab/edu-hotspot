# Rosetta phone edu hotspot

Serve https://rosettaphone.org files 

Using a [Orange Pi Zero 1](https://s.click.aliexpress.com/e/_AkhAQ5)

1) Install Armbian
2) ssh root@your_ip
3) sudo apt-get install php-cgi iw perl lighttpd dnsmasq hostapd python zip avahi-daemon hostapd libcgi-pm-perl


<p>
Prevent the daemons from automatic loading.
</p>
<pre class="code">sudo systemctl stop lighttpd
sudo systemctl disable lighttpd
sudo systemctl stop dnsmasq
sudo systemctl disable dnsmasq
sudo systemctl stop hostapd
sudo systemctl disable hostapd</pre>

<p>
Get the piratebox code:
</p>
<pre class="code">wget  http://downloads.piratebox.de/piratebox-ws_current.tar.gz
tar xf piratebox-ws_current.tar.gz
cd piratebox
sudo cp -rv piratebox /opt
sudo ln -s /opt/piratebox/init.d/piratebox /etc/init.d/</pre>

<p>
All the files shared by this piratebox will be stored in <code>/opt/piratebox/share</code>.
</p>

<p>
It is a good idea to have a look and edit some configuration parameters (if you like) in the following files: <code>/opt/piratebox/conf/piratebox.conf</code> and <code>/opt/piratebox/conf/hostapd.conf</code>. (It is not strictly needed it works out-of-the-box).
</p>

<p>
Finalize the installation:
</p>
<pre class="code">sudo /opt/piratebox/bin/install_piratebox.sh /opt/piratebox/conf/piratebox.conf part2
sudo /etc/init.d/piratebox start
sudo /opt/piratebox/bin/install_piratebox.sh /opt/piratebox/conf/piratebox.conf imageboard</pre>

<p>
To activate the board, run the following command:
</p>
<pre class="code">sudo /opt/piratebox/bin/board-autoconf.sh</pre>

<p>
Everything is now ready. It is possible to start your PirateBox:
</p>
<pre class="code">sudo /etc/init.d/piratebox start</pre>

<p>
Obviously the PirateBox can be turned off in this way:
</p>
<pre class="code">sudo /etc/init.d/piratebox stop</pre>

<p>
Systemd can be instructed to start PirateBox at boot time:
</p>
<pre class="code">sudo systemctl enable piratebox</pre>

<p>
Use <code>disable</code> instead of <code>enable</code> to undo this operation.  
</p>

</div>



# PirateBox   

This was forked from the now discontinued [Piratebox_webserver](https://github.com/PierreMartin/PirateBoxScripts_Webserver)

Documentation above CC-By-4.0 from [Piratebox](https://piratebox.cc/raspberry_pi:diy:armbian)

© 2012-2019 [Matthias Strubel](mailto:matthias.strubel@aod-rpg.de) 

Licensed under the GNU GPLv3
