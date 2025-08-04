# cODEXTEST

This repository provides a simple interface built with [KivyMD](https://kivymd.readthedocs.io/) that fetches data from the [CoinCap API](https://api.coincap.io/).

## Getting started

Install the dependencies and run the app:

```bash
pip install -r requirements.txt
python main.py
```

The application displays a toolbar and a paginated table showing the top 100 cryptocurrencies with their Price, Market Cap, VWAP (24Hr), Supply, Volume (24Hr), and Change (24Hr).

If the CoinCap API cannot be reached (for example, when offline or behind a restrictive proxy), the app falls back to the local `sample_data.json` file bundled with the project.
