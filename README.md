# hubitat-upload
a small repo to automate hubitat development of device drivers into sublime text with abuild process 

This is a total hack job to automate uploading of device drivers to hubitat from sublime text to make device driver development easier.

USE AT YOUR OWN RISK and keep backups of your hub before you start using.  There are lots of things that I can imagine that would make this safer but as of this moment it's kind of sensitive to using it correctly **MAKE A BACKUP OF YOUR HUB** before yous start!

1.  Move the hubitat.sublime-build to your packages->User folder.  You can go to the packages dir within sublime (on a mac it's sublime text->preferences->Browse Packages).  Once you have installed it there you should see 'hubitat' as a build option (tools->build options).  Note that this build system usese 'python3' --make sure you have python3
2.  make a folder and put upload.py into it.  This does the heavy lifting.  I've hard coded my hubitat IP address into it so go change it for yours (note to self:  Fix this)
3. This assumes you already have the device driver in hubitat -- if not go create one.
4. Copy and paste the device driver from hubitat to the same folder you put the 'upload.py' script.  It can be named anything you want (doesn't matter) but give it a name that makes sense. You also ned to put the ID number in the filename.  For instance if the device driver is ID 910 (you can see that from the URL when editing it in hubitat) then call it something like driver-910.groovy -- Again it the thing that matters is the -910 as that is how it knows what the ID is. **IF YOU GET THIS WRONG IT WILL OVERWRITE WHATEVER ID 910 IS -- IT"S DIFFERENT FOR EACH DEVICE** 
5. Again, backup your hub
6. From within sublime open the groovy device handler, select the hubitat build system.  Make a small change and then hit cmd-b to build.  You should see it upload (and if there is an error it should be reported.'

There is a ton of cleanup and work that should happen.  For instance it should be modified to deal with applications also.  Also some attempt for safety should be done, etc.  I'm totally open to anyone who can improve it (or do something much better)

