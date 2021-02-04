import pubnub#pubnub==4.0.2
import time
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

pnconf = PNConfiguration()
pnconf.subscribe_key = "demo"
pnconf.publish_key = "demo"
pnconf.origin = "ps1.pndsn.com"
pubnub = PubNub(pnconf)

def show(msg, stat):
    if msg and stat: print( msg.timetoken, stat.status_code )
    else           : print( "Error", stat and stat.status_code )

while True:
    print("publishing")
    pubnub.publish().channel("change_log").message("hello").sync()
    time.sleep(10)
