#!/usr/bin/env python3
# -*-coding : utf-8 -*-
# author magicdu
from botutils import getBotConfig,send_data,getIP

if __name__ == "__main__":
    config=getBotConfig()
    partyIds="@all"
    ip=getIP()
    print(ip)
    send_data(config,partyIds,ip)
    
