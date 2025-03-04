import logging

import pandas as pd
from .config import CHAR_GROUPS, CHAR_LEVELS


def get_stats3(df: pd.DataFrame) -> dict:
    stats = {key: df[df[key].fillna("") != ""].shape[0] for key in ["code", "units"]}
    stats["segments"] = len(df[df["segments"].fillna("").apply(lambda x: len(x) > 0)])
    stats["total"] = len(df)
    return stats


def get_stats2(df: pd.DataFrame) -> dict:
    stats = get_stats3(df)
    result = {
        "count": stats,
        "groups": CHAR_GROUPS,
        "levels": CHAR_LEVELS,
    }
    return result


def get_top_chars(df, start=0, count=1500):
    df["freq2"] = df["freq"].fillna(0).rank(ascending=False)
    df["basic"] = df["basic"].fillna(0).astype(int)
    levels = ["一级", "二级"]
    df1 = df[(df["level"].isin(levels)) | (df["basic"] == 1) | (df["group"] == "B1")]

    # rest = count - len(df1)
    # df2 = df[~df["char"].isin(df1["char"])].sort_values("freq2").head(rest)

    df_top = df1.sort_values("freq2")
    chars = df_top["char"].iloc[start : start + count].tolist()

    logging.info(f"top chars = {len(chars)}")
    return "".join(chars)


def get_level_chars(df, level):
    # levels = {1: "一级", 2: "二级", 3: "三级"}
    # df_lv = df[(df["level"] == levels[level])]
    levels2 = {0: "A1a", 1: "A1b", 2: "A2", 3: "A3", 4: "A4", 5: "B1"}
    df_lv = df[(df["group"] == levels2[level])]
    chars = df_lv["char"].tolist() if df_lv is not None else []
    logging.info(f"level={level} / chars = {len(chars)}")
    return "".join(chars)


def get_special_chars(df, unit):
    cols = ["key_unit", "stroke_unit", "char_unit"]
    df2 = df[(df[cols].sum(axis=1) >= 1) & (df["group"] <= "B2")]
    if unit == 0:
        df2 = df2[df2[cols[:2]].sum(axis=1) >= 1]
    else:
        df2 = df2[df2[cols[:2]].sum(axis=1) == 0]

    chars = df2["char"].tolist() if df2 is not None else []
    logging.info(f"chars = {len(chars)}")
    return "".join(chars)
