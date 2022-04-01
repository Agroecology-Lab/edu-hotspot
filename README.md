# Rosetta phone edu hotspot

Serve https://rosettaphone.org files 

Using a [Orange Pi Zero 1](https://s.click.aliexpress.com/e/_9iQsGD) 

Install [Armbian for Orange Pi Zero](https://www.armbian.com/orange-pi-zero/)
<pre class="code">
ssh root@your_ip
</pre>
<pre class="code">
sudo apt-get install php-cgi iw perl lighttpd dnsmasq hostapd python zip avahi-daemon hostapd libcgi-pm-perl
</pre>

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
Get the server code:
</p>
<pre class="code">wget  https://github.com/Agroecology-Lab/edu-hotspot/archive/refs/heads/master.zip
unzip master.zip
cd edu-hotspot-master
cd piratebox
sudo cp -rv piratebox /opt
sudo ln -s /opt/piratebox/init.d/piratebox /etc/init.d/</pre>

<p>
All the files shared by this server will be stored in <code>/opt/piratebox/share</code>.
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
Everything is now ready. It is possible to start your server:
</p>
<pre class="code">sudo /etc/init.d/piratebox start</pre>

<p>
Obviously the server can be turned off in this way:
</p>
<pre class="code">sudo /etc/init.d/piratebox stop</pre>

<p>
Systemd can be instructed to start the server at boot time:
</p>
<pre class="code">sudo systemctl enable piratebox</pre>

<p>
Use <code>disable</code> instead of <code>enable</code> to undo this operation.  
</p>

</div>

<pre class="code">apt-get install kiwix-tools
wget some.zim
kiwix-serve -p 1024 ./Shared/*.zim
</pre>

# In progress
https://www.atechtown.com/install-nvm-debian-11/

Following this guide https://github.com/SSBC/ssb-server
```

root@orangepizero:~# npm config set user 0
root@orangepizero:~# npm config set unsafe-perm true
root@orangepizero:~# sh ~/run-server.sh
ssb-server 15.3.0 /root/.ssb logging.level:notice
my key ID: lY3Smp2YlOIC8gbtYnBFGLwYAJDn75q3BtsBbDLAhgk=.ed25519

/root/.nvm/versions/node/v10.24.1/lib/node_modules/ssb-server/node_modules/levelup/lib/levelup.js:119
      return callback(new OpenError(err))
                      ^
OpenError: IO error: lock /root/.ssb/blobs_push/LOCK: Resource temporarily unavailable
    at /root/.nvm/versions/node/v10.24.1/lib/node_modules/ssb-server/node_modules/levelup/lib/levelup.js:119:23
    at /root/.nvm/versions/node/v10.24.1/lib/node_modules/ssb-server/node_modules/deferred-leveldown/node_modules/abstract-leveldown/abstract-leveldown.js:38:14
    at /root/.nvm/versions/node/v10.24.1/lib/node_modules/ssb-server/node_modules/deferred-leveldown/deferred-leveldown.js:31:21
    at /root/.nvm/versions/node/v10.24.1/lib/node_modules/ssb-server/node_modules/encoding-down/node_modules/abstract-leveldown/abstract-leveldown.js:38:14
    at /root/.nvm/versions/node/v10.24.1/lib/node_modules/ssb-server/node_modules/leveldown/node_modules/abstract-leveldown/abstract-leveldown.js:38:14
Emitted 'error' event at:
    at /root/.nvm/versions/node/v10.24.1/lib/node_modules/ssb-server/node_modules/levelup/lib/levelup.js:60:19
    at /root/.nvm/versions/node/v10.24.1/lib/node_modules/ssb-server/node_modules/levelup/lib/levelup.js:119:14
    at /root/.nvm/versions/node/v10.24.1/lib/node_modules/ssb-server/node_modules/deferred-leveldown/node_modules/abstract-leveldown/abstract-leveldown.js:38:14
    [... lines matching original stack trace ...]
    at /root/.nvm/versions/node/v10.24.1/lib/node_modules/ssb-server/node_modules/leveldown/node_modules/abstract-leveldown/abstract-leveldown.js:38:14
ssb-server 15.3.0 /root/.ssb logging.level:notice
my key ID: lY3Smp2YlOIC8gbtYnBFGLwYAJDn75q3BtsBbDLAhgk=.ed25519
```
Trying https://github.com/nodejs/help/issues/3644#issuecomment-991971902

https://github.com/hackergrrl/git-ssb-intro

Install a [SSB-browser?](https://people.iola.dk/arj/2020/03/04/how-to-setup-a-pub-for-ssb-browser/)

[SSB-viewer](https://git.scuttlebot.io/%25MeCTQrz9uszf9EZoTnKCeFeIedhnKWuB3JHW2l1g9NA%3D.sha256)

Find/ design an open hardware LoRa shield

#Notes

u:rosetta

p:eduhotspot

# PirateBox   

This was forked from the now discontinued [Piratebox_webserver](https://github.com/PierreMartin/PirateBoxScripts_Webserver)

Documentation above CC-By-4.0 from [Piratebox](https://piratebox.cc/raspberry_pi:diy:armbian)

© 2012-2019 [Matthias Strubel](mailto:matthias.strubel@aod-rpg.de) 

Licensed under the GNU GPLv3
