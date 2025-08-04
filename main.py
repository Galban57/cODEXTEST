import json
import requests
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class MyApp(MDApp):
    """KivyMD application showing top 100 cryptocurrencies from CoinGecko."""

    def build(self):
        screen = MDScreen()
        layout = MDBoxLayout(orientation="vertical")
        layout.add_widget(MDTopAppBar(title="Top 100 Cryptos"))

        data_table = MDDataTable(
            size_hint=(1, 0.9),
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("Name", dp(30)),
                ("Price", dp(30)),
                ("Market Cap", dp(30)),
                ("VWAP (24Hr)", dp(30)),
                ("Supply", dp(30)),
                ("Volume (24Hr)", dp(30)),
                ("Change (24Hr)", dp(30)),
            ],
            row_data=self.fetch_data(),
        )
        layout.add_widget(data_table)
        screen.add_widget(layout)
        return screen

    def fetch_data(self):
        """Retrieve top 100 cryptocurrency stats from CoinGecko API."""
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 100,
            "page": 1,
            "sparkline": "false",
        }
        headers = {"x-cg-demo-api-key": "ae8f74ab-e1b4-4483-86fe-9b59481e0962"}
        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
        except Exception:
            try:
                with open("sample_data.json", "r", encoding="utf-8") as fh:
                    data = json.load(fh).get("data", [])
            except Exception:
                return []

        rows = []
        for asset in data:
            if "current_price" in asset:
                price = float(asset.get("current_price", 0) or 0)
                market_cap = float(asset.get("market_cap", 0) or 0)
                volume = float(asset.get("total_volume", 0) or 0)
                supply = float(asset.get("circulating_supply", 0) or 0)
                change = float(asset.get("price_change_percentage_24h", 0) or 0)
                vwap = (
                    volume / supply if supply else 0
                )
            else:
                price = float(asset.get("priceUsd", 0) or 0)
                market_cap = float(asset.get("marketCapUsd", 0) or 0)
                vwap = float(asset.get("vwap24Hr", 0) or 0)
                supply = float(asset.get("supply", 0) or 0)
                volume = float(asset.get("volumeUsd24Hr", 0) or 0)
                change = float(asset.get("changePercent24Hr", 0) or 0)

            rows.append(
                (
                    asset.get("name", ""),
                    f"{price:,.2f}",
                    f"{market_cap:,.2f}",
                    f"{vwap:,.2f}",
                    f"{supply:,.0f}",
                    f"{volume:,.2f}",
                    f"{change:.2f}%",
                )
            )
        return rows


if __name__ == "__main__":
    MyApp().run()
