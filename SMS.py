import nexmo

client = nexmo.Clinet(key= 'ed320a43', secret ='OlUMCY1dswQYQ9FD',

client.send_message({
        "from": "HEY",
        "to": "989926834697",
        "text": "Hi Ali", 
})