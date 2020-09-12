#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 10:38:27 2020

@author: yashmadhwal
"""

from web3 import Web3
import os
import json


def main():
    ganache_url = "HTTP://127.0.0.1:7545"
    web3 = Web3(Web3.HTTPProvider(ganache_url))
    print("Ganache Connection: ", web3.isConnected())
    
    print('\n\n')
    
    
    with open('build/contracts/helloWorld.json', 'r') as jsonfile:
        variable = json.load(jsonfile)
           
    
    
    contract = web3.eth.contract(address = web3.toChecksumAddress(variable['networks']['5777']['address']), abi = variable['abi'])
    
    while True: 
        clear = lambda: os.system('clear')
        clear()    
        print('Current Block Number:' , web3.eth.blockNumber)
        print('\nCurrent Contract String: ',contract.functions.Greet().call({'from': web3.eth.accounts[0]}))
        print('''\n
              
        1. Print Hello World (Calling Hello World Contract)
        2. Call Function to Update status on the Contract
        3. Call New/Updated Status
        4. Exit
              ''')
        user_input = int(input("Enter: "))
        
        if user_input == 1:
            print(contract.functions.getGreeting().call({'from': web3.eth.accounts[0]}))
            input("Press Any Key to continue: ")
    
        elif user_input == 2:
            updated_value = input("New Value to Update: ")
            contract.functions.setGreeting(updated_value).transact({'from': web3.eth.accounts[0]})
            input("Value Updated\nPress Any Key to continue: ")
            
        elif user_input == 3:
            print("Called Current Value")
            print(contract.functions.Greet().call({'from': web3.eth.accounts[0]}))
            input("Press Any Key to continue: ")
        
        elif user_input == 4:
            break
            
        else:
            print("Invalid Input!!\nTry Again")

    
    
if __name__ == '__main__':
    main()    
