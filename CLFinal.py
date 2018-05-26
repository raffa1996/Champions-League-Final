import numpy as np
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import math
from __future__ import division
liv = pd.read_csv("C:/Users/win7/Downloads/liverpoolucl.csv")
rm = pd.read_csv("C:/Users/win7/Downloads/realmadriducl.csv")

def score(liv, rm):
    
    hf_attack_liv = liv.loc[(liv["HTEAM"]=="LIVERPOOL"), ["HTSCO"]]
    home_games_liv = len(hf_attack_liv.index)
    home_goals_scored_liv = sum(hf_attack_liv["HTSCO"])
    hf_defence_liv = liv.loc[(liv["HTEAM"]=="LIVERPOOL"), ["ATSCO"]]
    home_goals_conceded_liv = sum(hf_defence_liv["ATSCO"])
    af_attack_liv = liv.loc[(liv["ATEAM"]=="LIVERPOOL"), ["ATSCO"]]
    away_games_liv = len(af_attack_liv.index)
    away_goals_scored_liv = sum(af_attack_liv["ATSCO"])
    af_defence_liv = liv.loc[(liv["ATEAM"]=="LIVERPOOL"), ["HTSCO"]]
    away_goals_conceded_liv = sum(af_defence_liv["HTSCO"])
    hf_attack_rm = rm.loc[(rm["HTEAM"]=="REAL MADRID"), ["HTSCO"]]
    home_games_rm = len(hf_attack_rm.index)
    home_goals_scored_rm = sum(hf_attack_rm["HTSCO"])
    hf_defence_rm = rm.loc[(rm["HTEAM"]=="REAL MADRID"), ["ATSCO"]]
    home_goals_conceded_rm = sum(hf_defence_rm["ATSCO"])
    af_attack_rm = rm.loc[(rm["ATEAM"]=="REAL MADRID"), ["ATSCO"]]
    away_games_rm = len(af_attack_rm.index)
    away_goals_scored_rm = sum(af_attack_rm["ATSCO"])
    af_defence_rm = rm.loc[(rm["ATEAM"]=="REAL MADRID"), ["HTSCO"]]
    away_goals_conceded_rm = sum(af_defence_rm["HTSCO"])
    avg_goals_scored_home_liv = round(float(home_goals_scored_liv/home_games_liv), 4)
    avg_goals_conceded_home_liv = round(float(home_goals_conceded_liv/home_games_liv), 4)
    avg_goals_scored_away_liv = round(float(away_goals_scored_liv/away_games_liv), 4)
    avg_goals_conceded_away_liv = round(float(away_goals_conceded_liv/away_games_liv), 4) 
    avg_goals_scored_home_rm = round(float(home_goals_scored_rm/home_games_rm), 4)
    avg_goals_conceded_home_rm = round(float(home_goals_conceded_rm/home_games_rm), 4)
    avg_goals_scored_away_rm = round(float(away_goals_scored_rm/away_games_rm), 4)
    avg_goals_conceded_away_rm = round(float(away_goals_conceded_rm/away_games_rm), 4)  
    
    goals_scored_home_cl = 220
    goals_conceded_home_cl = 177 
    goals_scored_away_cl = 177 
    goals_conceded_away_cl = 220 
    total_games_cl = 124
    avg_goals_scored_home_cl = round(float(goals_scored_home_cl/total_games_cl), 4)
    avg_goals_conceded_home_cl = round(float(goals_conceded_home_cl/total_games_cl), 4)
    avg_goals_scored_away_cl = round(float(goals_scored_away_cl/total_games_cl), 4)
    avg_goals_conceded_away_cl = round(float(goals_conceded_away_cl/total_games_cl), 4)
    
    rm_attack_strength = round(float(avg_goals_scored_away_rm/avg_goals_scored_away_cl), 4)
    liv_defence_strength = round(float(avg_goals_conceded_away_liv/avg_goals_conceded_away_cl), 4) 
    liv_attack_strength = round(float(avg_goals_scored_away_liv/avg_goals_scored_away_cl), 4) 
    rm_defence_strength = round(float(avg_goals_conceded_away_rm/avg_goals_conceded_away_cl), 4)
    
    projected_goals_rm = round((rm_attack_strength*liv_defence_strength*avg_goals_scored_away_cl), 4) 
    projected_goals_liv = round((liv_attack_strength*rm_defence_strength*avg_goals_scored_away_cl), 4)
    
    i = 0
    print "Poisson % for the number of goals scored"
    print "----------------------------------------"
    print "    Goals", "Real Madrid", "Liverpool"
    for i in range(0,6):
        print "     ", (i), "     ", (round((((projected_goals_rm**i)*math.exp(-projected_goals_rm))/math.factorial(i)), 4)*100), "   ",(round((((projected_goals_liv**i)*math.exp(-projected_goals_liv))/math.factorial(i)), 4)*100)
    
    rmarr = [0] * 6
    livarr = [0] * 6
    i = 0
    for i in range(0,6): 
            rmarr[i] = round(((((projected_goals_rm**i)*math.exp(-projected_goals_rm))/math.factorial(i))*100), 2)
            livarr[i] = round(((((projected_goals_liv**i)*math.exp(-projected_goals_liv))/math.factorial(i))*100), 2)
    
    pos = np.ones((7,7))
    i = 1 
    for i in range(len(pos)):
         pos[:1,i] = rmarr[i-1]

    for i in range(len(pos)):
        pos[i,:1] = livarr[i-1]
        pos[:1,:1] = 0
    
   
    
    i = 1
    j = 1
    for i in range(1,7):
        for j in range(1,7):
            pos[i,j] = round(((pos[i,0]*pos[0,j])/100),2)
        
    
    
    i = 0
    j = 0 
    for i in range(0,7):
        pos[:1,i] = 0
        pos[i,:1] = 0
    
    
    
    draw_percentage = 0
    i = 0 
    j = 0
    for i in range(len(pos)):
        for j in range(len(pos)):
            if(i==j):
                draw_percentage += pos[i,j]
            
    
    
    rm_win_percentage = 0
    i = 0 
    j = 0
    for i in range(len(pos)):
        for j in range(len(pos)):
            if(i<j):
                rm_win_percentage += pos[i,j]

    
    
    liv_win_percentage = 0
    i = 0 
    j = 0
    for i in range(len(pos)):
        for j in range(len(pos)):
            if(i>j):
                liv_win_percentage += pos[i,j]
    
    
    
    pos = np.delete(pos, (0), axis=0)
    pos = np.delete(pos, (0), axis=1)
    
    
    max_num = pos.max()
    i = 0 
    j = 0 
    for i in range(len(pos)):
        for j in range(len(pos)):
            if(pos[i,j]==max_num):
                print "Final Result ----> Real Madrid ",j,"-",i, "Liverpool"
    
score(liv, rm)