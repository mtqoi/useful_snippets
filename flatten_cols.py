def flatten_cols(df):
    cols = ['_'.join(map(str, vals))
            for vals in df.columns.to_flat_index()]
    df.columns = cols
    return df
