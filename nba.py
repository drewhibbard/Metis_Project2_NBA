#!/usr/bin/env python
# coding: utf-8

'''
This module is for scraping NBA player statistics from basketball-reference.com
It will obtain the entire stats table for every player in the given year.
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
import pickle


def get_links():
    page = requests.get('https://www.basketball-reference.com/leagues/NBA_2019_per_game.html')
    soup = BeautifulSoup(page.content)
    table = soup.find('table')
    rows = [row for row in table.find_all('tr')]
    
    base_url = 'https://www.basketball-reference.com'
    log = '/gamelog/2019/'

    links = []
    
    for row in rows[1:]:
        try:
            part = row.find('td').findChild().get('href')
            short = part[:-5] # remove the .html because we need to go one 'click' further
            full = base_url + short + log
            links.append(full)
        except:
            continue
            
    return list(set(links))



def get_player_stats(url):
    headers = ['Player','Rank','Game','Date','Age','Team','Away','Opp','Result','Started','min_played','fgm','fga','fgp',
           '3pm','3pa','3pp','ftm','fta','ftp','orb','drb','trb','ast','stl','blk','tov','pf',
           'pts','GmSc','plus_minus']
    stats_list = []
    player_page = requests.get(url)
    player_table = player_soup.find('table',id='pgl_basic')
    player_rows = [row for row in player_table.find_all('tr')]
    
    for row in player_rows[1:]:
        try:
            stats = {}
            player = player_soup.find('title').text.split('2018-19')[0].strip()
            game = row.find('th').text
            items = row.find_all('td')
            stats = dict(zip(headers,([player] + [game] + [item.text for item in items])))
            stats_list.append(stats)
        except:
            continue
    return stats_list



def get_all_stats(links):
    total = []
    for link in links:
        try:
            player = get_player_stats(link)
            total += player
            time.sleep(1+2*np.random.uniform())
        except:
            continue
    return total


