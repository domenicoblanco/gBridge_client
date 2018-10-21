# gBridge_client

This is an **unofficial** client to connect Raspberry Pi's GPIO to Google Assistant using [Kappelt gBridge](https://about.gbridge.kappelt.net/) 

# Installation
- [Debian](#Debian)
- Windows   [*TODO*]
- macOS   [*TODO*]

# Debian
   First of all, create a new [gBridge account](https://gbridge.kappelt.net/register).
   Install the dependencies and devDependencies and start the server.
   ```sh
     $ sudo apt install python3 mosquitto
     $ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
     $ python3 get-pip.py
     $ pip3 install paho-mqtt
   ```
   **Let's setup Mosquitto**
    Open with a text editor with admin privileges the following path `/etc/mosquitto/mosquitto.conf`, we will use nano:
   ```sh
    $ sudo nano /etc/mosquitto/mosquitto.conf
   ```
   and copy the following configuration making sure to edit text inside the brackets `{}`
   ```yaml
    connection kappelt-gbridge
    address mqtt.gbridge.kappelt.net:8883
    bridge_attempt_unsubscribe true
    cleansession true
    remote_username {gbridge-mqtt-username}
    remote_password {gbridge-mqtt-password}
    topic gBridge/u{gbridge-userid}/d{device-id}/{onoff} both 0 "" ""
    topic gBridge/u{gbridge-userid}/d{device-id}/{onoff}/set both 0 "" ""
    #you might need to change the path of the CA files
    bridge_capath /etc/ssl/certs/
    bridge_tls_version tlsv1.2
   ```
   ❗gBridge credentials are available [here]()ttps://gbridge.kappelt.net/profile). Remember to set your password  in that page.
   **Restart Mosquitto**
   ```sh
    $ sudo service mosquitto restart
   ```
   Now we're ready to setup our client, let's set it up. Open the [client](https://github.com/domenicoblanco/gBridge_client/blob/master/client.py) and edit `MQTT_TOPIC` and `PIN` according to your needs and your gBridge topic's name.
   **Start the client**
    Your client is complete, it's time to execute it with `python3 client.py`
    
# TODO
   [ ] Improve English
   [ ] Write Windows setup guide
   [ ] Write macOS setup guide
    

     
