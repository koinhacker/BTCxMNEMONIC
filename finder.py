from colorama import Fore, Style
from hdwallet import HDWallet
from hdwallet.utils import generate_entropy
from hdwallet.symbols import BTC as SYMBOL
from typing import Optional
import json
import multiprocessing
from multiprocessing import Pool
import threading

koinhacker = '''

██╗░░██╗░█████╗░██╗███╗░░██╗██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██║░██╔╝██╔══██╗██║████╗░██║██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
█████═╝░██║░░██║██║██╔██╗██║███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔═██╗░██║░░██║██║██║╚████║██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░╚██╗╚█████╔╝██║██║░╚███║██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝░╚════╝░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
--------------------------------------------------------
[x] Software: BTCxMNEMONIC
[x] Author: KoinHacker
[x] Github: koinhacker
[x] Version: 1.0
--------------------------------------------------------
Donate me BTC: bc1qhzems2lsstx795ae8er698zp0vvcvg3p39e3yr
========================================================

▀▀█▀▀ ░█▀▀█ ▀█▀ ─█▀▀█ ░█─── 　 ░█──░█ ░█▀▀▀ ░█▀▀█ ░█▀▀▀█ ▀█▀ ░█▀▀▀█ ░█▄─░█ 
─░█── ░█▄▄▀ ░█─ ░█▄▄█ ░█─── 　 ─░█░█─ ░█▀▀▀ ░█▄▄▀ ─▀▀▀▄▄ ░█─ ░█──░█ ░█░█░█ 
─░█── ░█─░█ ▄█▄ ░█─░█ ░█▄▄█ 　 ──▀▄▀─ ░█▄▄▄ ░█─░█ ░█▄▄▄█ ▄█▄ ░█▄▄▄█ ░█──▀█
'''

PRINT = Fore.GREEN + koinhacker + Fore.RESET
print('\n\n', Fore.RED, str(PRINT), Style.RESET_ALL, '\n')

r = 1
cores = 8

def finder(r): 
    filename = "btc500.txt"
    with open (filename) as f: 
        add = f.read().split()
    add = set(add)
    
    z = 1
    w = 0
    while True:
        # Choose strength 128, 160, 192, 224 or 256
        STRENGTH: int = 256  # Default is 128
        # Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese or korean
        LANGUAGE: str = "english"
        ENTROPY: str = generate_entropy(strength=STRENGTH)
        PASSPHRASE: Optional[str] = None

        hdwallet: HDWallet = HDWallet(symbol=SYMBOL, use_default_path=False)

        hdwallet.from_entropy(
            entropy=ENTROPY, language=LANGUAGE, passphrase=PASSPHRASE
        )

        hdwallet.from_index(44, hardened=True)
        hdwallet.from_index(0, hardened=True)
        hdwallet.from_index(0, hardened=True)
        hdwallet.from_index(0)
        hdwallet.from_index(0)
        
        addr: str = hdwallet.p2pkh_address()
        p2sh_address: str = hdwallet.p2sh_address()
        p2wpkh_address: str = hdwallet.p2wpkh_address()
        p2wpkh_in_p2sh_address: str = hdwallet.p2wpkh_in_p2sh_address()
        p2wsh_address: str = hdwallet.p2wsh_address()
        p2wsh_in_p2sh_address: str = hdwallet.p2wsh_in_p2sh_address()
        mnemonic: str = hdwallet.mnemonic()
        private_key: str = hdwallet.private_key()
        #public_key: str = hdwallet.public_key()
        #xprivate_key: str = hdwallet.xprivate_key()
        #xpublic_key: str = hdwallet.xpublic_key()

        #print(f"COUNT: {counter}, P2KPH: {p2pkh_address}, P2SH: {p2sh_address}, P2WPKH: {p2wpkh_address}")
        print('Winner Wallet:',Fore.GREEN, str(w), Fore.YELLOW,'Total Scan:',Fore.WHITE, str(z), Fore.YELLOW, Fore.YELLOW, 'P2PKH:', Fore.WHITE, str(addr), Fore.YELLOW, 'P2SH:', Fore.WHITE, str(p2sh_address), Fore.YELLOW, 'P2WPKH:', Fore.WHITE, str(p2wpkh_address), Fore.YELLOW, 'P2WSH:', Fore.WHITE, str(p2wpkh_address), end='\r', flush=True)
        z += 1
        
        if addr in add or p2sh_address in add or p2wpkh_address in add or p2wpkh_in_p2sh_address in add or p2wsh_address in add or p2wsh_in_p2sh_address in add:
            print('Winning', Fore.GREEN, str(w), Fore.WHITE, str(z), Fore.YELLOW, 'Total Scan Checking ----- BTC Address =', Fore.GREEN, str(addr), end='\r')
            w += 1
            z += 1
            f = open("winner.txt", "a")
            f.write('\nAddress = ' + str(addr))
            f.write('\nP2SH Address = ' + str(p2sh_address))
            f.write('\nP2WPKH Address = ' + str(p2wpkh_address))
            f.write('\nP2WPKH in P2SH Address = ' + str(p2wpkh_in_p2sh_address))
            f.write('\nP2WSH Address = ' + str(p2wsh_address))
            f.write('\nP2WSH in P2SH Address = ' + str(p2wsh_in_p2sh_address))
            f.write('\nPrivate Key = ' + str(private_key))
            f.write('\nMnemonic Phrase = ' + str(mnemonic))
            f.write('\n=========================================================\n')
            f.close()
            print('Winner information Saved On text file = ADDRESS ', str(addr))
            continue

        
finder(r)

if __name__ == '__main__':
    jobs = []
    for r in range(cores):
        p = multiprocessing.Process(target=finder, args=(r,))
        jobs.append(p)
        p.start()