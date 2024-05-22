import pandas as pd

def split_years_bysex(groupbyyear, prox_df, groom_df):
    '''
    Splits dataframes by sex, ONLY USE ON NON-2018
    takes: GroupByYear df, proximity groups df, grooming events df
    returns: Proximity male, proximity female, groom male, groom female, groupbyyear male, groupbyyear female
    '''
    
    gby_m = groupbyyear[groupbyyear.sex == "M"]
    gby_f = groupbyyear[groupbyyear.sex == "F"]
    
    prox_df_male = prox_df[prox_df.focal_monkey.isin(gby_m.id)]
    prox_df_female = prox_df[prox_df.focal_monkey.isin(gby_f.id)]
    
    #Filtering grooming events by giver, not reciever
    groom_df_male = groom_df[groom_df.giver.isin(gby_m.id)]
    groom_df_female = groom_df[groom_df.giver.isin(gby_f.id)]
    
    return prox_df_male, prox_df_female, groom_df_male, groom_df_female, gby_m, gby_f

def split_years_byage(groupbyyear, prox_df, groom_df, age = 20):
    '''
    Splits dataframes by age, ONLY USE ON NON-2018
    takes: GroupByYear df, proximity groups df, grooming events df, and age to split on
    returns: Proximity old, proximity young, groom old, groom young, groupbyyear old, groupbyyear young
    '''
    gby_old = groupbyyear[groupbyyear.age >= age]
    gby_young = groupbyyear[groupbyyear.age < age]
    
    prox_df_old = prox_df[prox_df.focal_monkey.isin(gby_old.id)]
    prox_df_young = prox_df[prox_df.focal_monkey.isin(gby_young.id)]
    
    #Filtering grooming events by giver, not reciever
    groom_df_old = groom_df[groom_df.giver.isin(gby_old.id)]
    groom_df_young = groom_df[groom_df.giver.isin(gby_young.id)]
    
    return prox_df_old, prox_df_young, groom_df_old, groom_df_young, gby_old, gby_young


def split_2018_bysex(scans, gby_dfs):
    '''
    scans: 2018 funny file
    gby_dfs: List of all groupbyyear dataframes
    returns: Male df, female df
    '''
    
    gby = gby_dfs[0]
    
    for i in range(1, len(gby_dfs)): 
        gby = pd.concat([gby, gby_dfs[i]], axis = 0)
        
    gby_m = gby[gby.sex == "M"]
    gby_f = gby[gby.sex == "F"]
    
    scans_m = scans[scans.id.isin(gby_m.id)]
    scans_f = scans[scans.id.isin(gby_f.id)]
    
    return scans_m, scans_f


def split_2018_byage(scans, gby_dfs, age = 25):
    '''
    scans: 2018 funny file
    gby_dfs: List of all groupbyyear dataframes
    returns: Old_df, Young_df
    '''
    
    gby = gby_dfs[0]
    
    for i in range(1, len(gby_dfs)): 
        gby = pd.concat([gby, gby_dfs[i]], axis = 0)
        
    gby_old = gby[gby.age >= age]
    gby_young = gby[gby.age < age]
    
    scans_old = scans[scans.id.isin(gby_old.id)]
    scans_young = scans[scans.id.isin(gby_young.id)]
    
    return scans_old, scans_young