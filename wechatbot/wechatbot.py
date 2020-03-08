#!/usr/bin/env python3
# -*-coding : utf-8 -*-
# author magicdu
from botutils import getBotConfig,send_data

if __name__ == "__main__":
    config=getBotConfig()
    partyIds="@all"
    send_data(config,partyIds,"hello,hello")
