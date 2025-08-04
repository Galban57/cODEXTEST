import customtkinter as ctk
from tkinter import ttk
import json
import requests

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class CryptoDashboard(ctk.CTk):
    """Display top cryptocurrencies from CoinCap in a CustomTkinter window."""

    def __init__(self):
        super().__init__()

        self.title("Crypto Dashboard")
        self.geometry("1000x600")
        self.configure(bg="#F5F6FA")

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#FFFFFF")
        self.sidebar.pack(side="left", fill="y")

        ctk.CTkLabel(
            self.sidebar,
            text="CRYPTO",
            font=("Arial", 20, "bold"),
            text_color="#2D6CDF",
        ).pack(pady=(20, 10))
        for item in ["Top 100", "Portfolio", "Settings"]:
            ctk.CTkButton(
                self.sidebar,
                text=item,
                fg_color="transparent",
                text_color="#333",
                hover_color="#E5E5E5",
            ).pack(pady=5, fill="x", padx=20)

        # Main Content
        self.main = ctk.CTkFrame(self, fg_color="#F5F6FA")
        self.main.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(
            self.main,
            text="TOP 100 CRYPTOS",
            font=("Arial", 22, "bold"),
            text_color="#000000",
        ).pack(anchor="nw")

        table_frame = ctk.CTkFrame(self.main, fg_color="#FFFFFF", corner_radius=16)
        table_frame.pack(fill="both", expand=True, pady=10)

        columns = ("price", "market_cap", "vwap", "supply", "volume", "change")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=25)
        headings = [
            ("price", "Price (USD)"),
            ("market_cap", "Market Cap"),
            ("vwap", "VWAP 24Hr"),
            ("supply", "Supply"),
            ("volume", "Volume 24Hr"),
            ("change", "Change 24Hr"),
        ]
        for key, text in headings:
            self.tree.heading(key, text=text)
            self.tree.column(key, anchor="e")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        data = self.fetch_data()
        for asset in data:
            self.tree.insert(
                "",
                "end",
                values=(
                    f"{float(asset.get('priceUsd', 0)):,.2f}",
                    f"{float(asset.get('marketCapUsd', 0)):,.2f}",
                    f"{float(asset.get('vwap24Hr', 0)):,.2f}",
                    f"{float(asset.get('supply', 0)):,.2f}",
                    f"{float(asset.get('volumeUsd24Hr', 0)):,.2f}",
                    f"{float(asset.get('changePercent24Hr', 0)):,.2f}%",
                ),
            )

    def fetch_data(self):
        url = "https://api.coincap.io/v2/assets?limit=100"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()["data"]
        except Exception:
            with open("sample_data.json") as f:
                return json.load(f)["data"]


if __name__ == "__main__":
    app = CryptoDashboard()
    app.mainloop()
