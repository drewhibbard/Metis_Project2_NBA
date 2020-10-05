#!/usr/bin/env python
# coding: utf-8

'''
This module is for scraping NBA player statistics from basketball-reference.com
It will obtain the entire game logs table for every player in the given year.
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
import pickle


def get_links(year):
    '''
    Input: year of desired stats.

    Returns: a list of urls, one for each player's game log of the input year,
    to be fed to the get_all_stats function
    '''

    page = requests.get(f'https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html')
    soup = BeautifulSoup(page.content,features='lxml')

    table = soup.find('table')  # the stats are found in the html table
    rows = [row for row in table.find_all('tr')]  # parse the table into individual rows
    
    base_url = 'https://www.basketball-reference.com'
    log = f'/gamelog/{year}/'  # without this you will get the player's per-season stats, 
    # this will give you per-game

    links = []
    
    for row in rows[1:]:
        try:
            part = row.find('td').findChild().get('href')  # obtain the link extension
            short = part[:-5] # remove the .html because we need to go one 'click' further to the game log
            full = base_url + short + log
            links.append(full)
        except:
            continue
            
    return list(set(links))



def get_player_stats(url):
    '''
    Input: a url to a single player's game log stats for the year specified.

    Returns: a list of dictionaries, with each dictionary being a single game's statistics
    '''

    headers = ['Player','Rank','Game','Date','Age','Team','Away','Opp','Result','Started','min_played','fgm','fga','fgp',
           '3pm','3pa','3pp','ftm','fta','ftp','orb','drb','trb','ast','stl','blk','tov','pf',
           'pts','GmSc','plus_minus']

    stats_list = []

    user_agent = {'User-agent': 'Mozilla/81.0'}  # appear as a genuine browser to avoid the boot
    player_page = requests.get(url,headers=user_agent)
    player_soup = BeautifulSoup(player_page.content,features='lxml')
    player_table = player_soup.find('table',id='pgl_basic')
    player_rows = [row for row in player_table.find_all('tr')]
    
    for row in player_rows[1:]:
        try:
            stats = {}

            # player's name can be found in the html title, after stripping other text out
            player = player_soup.find('title').text.split('2')[0].strip()

            game = row.find('th').text
            items = row.find_all('td')
            stats = dict(zip(headers,([player] + [game] + [item.text for item in items])))
            stats_list.append(stats)
        except:
            continue
    return stats_list



def get_all_stats(links):
    '''
    Input: a list of links to players' game logs.  Generally obtained with the get_links function.

    Returns: the entire stats table for every input url in the form of a list of dictionaries, 
    with each dictionary being a single game log for a single player

    Function will also print to console each link for which stats were not scraped
    '''

    total = []
    for link in links:
        try:
            player = get_player_stats(link)
            total += player

            # wait a random number of seconds between 1 and 3 to pass as a human
            time.sleep(1+2*np.random.uniform()) 
        except:
            print(link)  # print out any link for which stats were not scraped
            continue
    return total


