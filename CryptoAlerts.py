import configuration as conf
import requests, json, time
from datetime import datetime

def get_coin_price(COIN):
    if COIN == 'BTC':
         URL = conf.BITCOIN_URL
    elif COIN == 'ETH':
        URL = conf.ETHEREUM_URL
    elif COIN == 'DOGE':
        URL = conf.DOGE_URL
    elif COIN == 'BAT' :
        URL = conf.BAT_URL
    elif COIN == 'TNC':
        URL = conf.TNC_URL

    response = requests.request('GET',URL)
    response = json.loads(response.text)
    current_price = response['INR']
    return current_price


def send_telegram_message(COIN,COIN_VALUE):
    telegram_url = "https://api.telegram.org/" + conf.TELEGRAM_BOT_API_KEY + "/sendMessage"

    if COIN == 'BTC':
        BUY_COIN = conf.BUY_BTC
        SELL_COIN = conf.SELL_BTC 
    elif COIN == 'ETH':
        BUY_COIN = conf.BUY_ETH
        SELL_COIN = conf.SELL_ETH
    elif COIN == 'DOGE':
        BUY_COIN = conf.BUY_DOGE
        SELL_COIN = conf.SELL_DOGE
    elif COIN == 'BAT' :
        BUY_COIN = conf.BUY_BAT
        SELL_COIN = conf.SELL_BAT
    elif COIN == 'TNC':
        SELL_COIN = conf.SELL_TNC
        BUY_COIN = conf.BUY_TNC
    

    if COIN_VALUE <= BUY_COIN:
        print(str(COIN) + " price has went Down To " + str(COIN_VALUE) + "\n You Can Buy now...")
        data = {
                    "chat_id": conf.TELEGRAM_CHAT_ID,
                    "text": str(COIN) + " price has went Down To " + str(COIN_VALUE) + "\n You Can Buy now... \n Happy CryptoTrading \n -CryptoAlerts"
        }
        try:
            response = requests.request("POST",telegram_url,params=data)
            print("\nThis is the Telegram URL")
            print(telegram_url)
            print("\nThis is the Telegram response")
            print(response.text)
        except Exception as e:
            print("\nAn error occurred in sending the alert message via Telegram")
            print(e)
    
    if COIN_VALUE >= SELL_COIN :
        print(str(COIN) + " price has went Up To " + str(COIN_VALUE) + "\n You Can Sell now...")
        #Sending Telegram Messaage
        data = {
                    "chat_id": conf.TELEGRAM_CHAT_ID,
                    "text": str(COIN) + " price has went Up To " + str(COIN_VALUE) + "\n You Can Sell now... \n Happy CryptoTrading \n -CryptoAlerts"
        }
        try:
            response = requests.request("POST",telegram_url,params=data)
            print("\nThis is the Telegram URL")
            print(telegram_url)
            print("\nThis is the Telegram response")
            print(response.text)
        except Exception as e:
            print("\nAn error occurred in sending the alert message via Telegram")
            print(e)

while True:
    now = datetime.now()
    print("\n\n" + now.strftime("%d/%m/%Y %H:%M:%S"))
    print("Current Crypto Value(INR)....\n")
    #BITCOIN
    COIN = 'BTC'
    COIN_VALUE = get_coin_price(COIN)
    print("BTC : " + str(COIN_VALUE))
    send_telegram_message(COIN,COIN_VALUE)

    #ETHEREUM
    COIN = 'ETH'
    COIN_VALUE = get_coin_price(COIN)
    print("ETH : " + str(COIN_VALUE))
    send_telegram_message(COIN,COIN_VALUE)

    #DOGE
    COIN = 'DOGE'
    COIN_VALUE = get_coin_price(COIN)
    print("DOGE : " + str(COIN_VALUE))
    send_telegram_message(COIN,COIN_VALUE)

    #BAT
    COIN = 'BAT'
    COIN_VALUE = get_coin_price(COIN)
    print("BAT : " + str(COIN_VALUE))
    send_telegram_message(COIN,COIN_VALUE)

    #TNC
    COIN = 'TNC'
    COIN_VALUE = get_coin_price(COIN)
    print("TNC : " + str(COIN_VALUE))
    send_telegram_message(COIN,COIN_VALUE)

    time.sleep(280)
