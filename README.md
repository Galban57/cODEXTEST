# cODEXTEST

This repository now provides a small cryptocurrency dashboard built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter).
It displays the top 100 assets from the CoinCap API with columns for price, market cap, VWAP (24Hr), supply, volume (24Hr) and daily change.
If the API request fails, the app falls back to the bundled `sample_data.json`.

## Getting started

Install the dependencies and run the application:

```bash
pip install -r requirements.txt
python main.py
```

Running the script opens a window titled **Crypto Dashboard** using a light theme with blue accents.
