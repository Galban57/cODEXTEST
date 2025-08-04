import json
import requests
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class MyApp(MDApp):
    """KivyMD application showing top 100 cryptocurrencies from CoinCap."""

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
        """Retrieve top 100 cryptocurrency stats from CoinCap API."""
        url = "https://api.coincap.io/v2/assets?limit=100"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json().get("data", [])
        except Exception:
            try:
                with open("sample_data.json", "r", encoding="utf-8") as fh:
                    data = json.load(fh).get("data", [])
            except Exception:
                return []

        rows = []
        for asset in data:
            rows.append(
                (
                    asset.get("name", ""),
                    f"{float(asset.get('priceUsd', 0) or 0):,.2f}",
                    f"{float(asset.get('marketCapUsd', 0) or 0):,.2f}",
                    f"{float(asset.get('vwap24Hr', 0) or 0):,.2f}",
                    f"{float(asset.get('supply', 0) or 0):,.0f}",
                    f"{float(asset.get('volumeUsd24Hr', 0) or 0):,.2f}",
                    f"{float(asset.get('changePercent24Hr', 0) or 0):.2f}%",
                )
            )
        return rows


if __name__ == "__main__":
    MyApp().run()
