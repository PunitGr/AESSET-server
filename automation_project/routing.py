from channels import route
from query_management.consumers import connect_query, disconnect_query, save_query


channel_routing = [
    route("websocket.connect", connect_query, path=r'^querylist/'),
    route("websocket.disconnct", disconnect_query, path=r'^querylist/'),
    route("websocket.recieve", save_query, path=r'^query/$')
]
