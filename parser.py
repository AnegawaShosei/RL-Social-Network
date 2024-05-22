import pandas as pd


def parse_group_by_year_file(path):
    df = pd.read_csv(path)

    df = df.rename(columns={
        "year.of.birth": "yob",
        "behavioral.mother": "behavioral_mother",
        "group.at.birth": "group_at_birth",
        "ordinal.rank": "ordrank",
        "percofsex.dominated": "dominated",
        "hrs.focalfollowed": "focal_hours"
    })

    return df


def parse_prox_groups(path):

    df = pd.read_csv(path)

    df = df.rename(columns={
        "observation.name": "garbage!",
        "scan.number": "scan_num",
        "focal.monkey": "focal_monkey",
        "in.proximity": "in_prox",
        "focal.activity": "focal_activity",
        "partners.activity (sequential)": "partner_activity"
    })

    return df


def parse_groom_groups(path):

    df = pd.read_csv(path)

    df = df.rename(columns={
        "groom_giver": "giver",
        "groom_reciever": "reciever",
        "constrined_duration": "duration",
        "obervation_name": "name"
    })

    return df


def parse_2018_groups(path):

    df = pd.read_csv(path)

    df = df.rename(columns={
        "observer.initial": "initials",
        "scan.num": "scan_num",
        "start.time": "start",
        "stop.time": "stop",
        "cayo.map.code": "map_code",
        "subject.ID": "id",
        "subject.activity": "subject_activity",
        "partner.ID": "partner_id",
        "prox.adult.IDs": "prox_ids",
        "nearest.adult.neighbour.ID": "nearest_neighbor_id",
        "distance.nearest.neighbour": "nearest_neighbor_distance",
        "partner.activity": "partner_activity"
    })

    return df
