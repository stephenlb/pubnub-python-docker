import pubnub

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub          import PubNub, SubscribeListener

class DatabaseSync(SubscribeListener):
    def message( self, pubnub, data ):
        print( "Saving to Database: ", data.message )

pnconfig               = PNConfiguration()
pnconfig.subscribe_key = 'demo'
pnconfig.publish_key   = 'demo'
pubnub                 = PubNub(pnconfig)

pubnub.add_listener(DatabaseSync())
pubnub.subscribe().channels("change_log").execute()