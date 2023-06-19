#notify2

import feedparser
import notify2
import os
import time

def parseFeed():
    f = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
    ICON_PATH = os.getcwd() + "/icon.ico"
    notify2.init('News Notify')
    for newsitem in f['items']: 
        n = notify2.Notification(newsitem['title'], 
                                  newsitem['summary'], 
                                  icon=ICON_PATH 
                                  )
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.show()
        n.set_timeout(15000)
        time.sleep(1200)
        
if __name__ == '__main__':
    parseFeed()


# import dbus

# bus_name = "org.freedesktop.Notifications"
# object_path = "/org/freedesktop/Notifications"
# interface = bus_name

# notify = dbus.Interface(dbus.SessionBus().get_object(bus_name, object_path), interface)
# notify.Notify(ARGS)
