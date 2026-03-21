def generate_pandas_schema(l: list) -> dict:
    return {k: v.lower() for d in l for k, v in d.items()}