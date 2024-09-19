import pandas as pd
import country_converter as coco

df = pd.read_feather(r"./ids_stocks_raw.feather")


ib = "World Bank-IBRD"
df_ib = df[df["counterpart-area"] == ib]
df_ib["counterpart"] = "IBRD"
df_ib = df_ib.drop(["counterpart-area"], axis=1)
df_ib = df_ib.rename(columns={"country": "debtor", "counterpart": "creditor", "time": "year"})
df_ib["iso_code"] = coco.convert(df_ib["debtor"], to="ISO3")
df_ib = df_ib[df_ib["iso_code"] != "not found"]
df_ib = df_ib[["debtor", "iso_code", "creditor", "year", "value"]]
df_ib = df_ib.sort_values(["iso_code", "year"])
df_ib = df_ib.reset_index(drop=True)

df = pd.read_feather(r"./ids_stocks_raw.feather")

af = "African Dev. Bank"
df_af = df[df["counterpart-area"] == af]
df_af["counterpart"] = "AFDB"
df_af = df_af.drop(["counterpart-area"], axis=1)
df_af = df_af.rename(columns={"country": "debtor", "counterpart": "creditor", "time": "year"})
df_af["iso_code"] = coco.convert(df_af["debtor"], to="ISO3")
df_af = df_af[df_af["iso_code"] != "not found"]
df_af = df_af[["debtor", "iso_code", "creditor", "year", "value"]]
df_af = df_af.sort_values(["iso_code", "year"])
df_af = df_af.reset_index(drop=True)


df_final = df_ib.append(df_af, ignore_index=True)
df_final = df_final.reset_index(drop=True)
