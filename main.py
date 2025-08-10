import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
import requests
import json
import urllib3
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
Window.clearcolor = (1, 1, 1, 1)

def get_text(field):
    if isinstance(field, dict) and "_text" in field:
        return field["_text"].strip()
    return str(field).strip() if field else "N/A"

def format_key(key):
    key = re.sub(r'([a-z])([A-Z])', r'\1 \2', key)
    return key.replace('_', ' ').title()

class SelectableTextInput(TextInput):
    def __init__(self, **kwargs):
        super(SelectableTextInput, self).__init__(**kwargs)
        self.background_color = (1, 1, 1, 1)
        self.selected = False
        self.multiline = False
        self.readonly = True

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.toggle_selection()
            return True
        return super(SelectableTextInput, self).on_touch_down(touch)

    def toggle_selection(self):
        self.selected = not self.selected
        if self.selected:
            self.background_color = (0.7, 0.7, 1, 1)  # Light blue when selected
        else:
            self.background_color = (1, 1, 1, 1)  # White when not selected

class MeterInfoApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        center_box = BoxLayout(orientation='vertical',
                               size_hint=(None, None),
                               height=dp(110),
                               width=dp(300),
                               pos_hint={'center_x': 0.5})

        self.input = TextInput(
            hint_text="Enter 12-digit Meter Number",
            multiline=False,
            size_hint=(None, None),
            height=dp(50),
            width=dp(280),
            font_size=dp(22),
            background_color=(1, 1, 1, 1),
            halign='center')

        btn = Button(
            text="Check",
            size_hint=(None, None),
            height=dp(50),
            width=dp(280),
            font_size=dp(18),
            background_color=get_color_from_hex('#4CAF50'),
            background_normal='',
            color=(1, 1, 1, 1))
        btn.bind(on_press=self.check_meter)

        center_box.add_widget(self.input)
        center_box.add_widget(btn)

        layout.add_widget(center_box)

        # Add a clear selection button
        self.clear_btn = Button(
            text="Clear Selection",
            size_hint=(None, None),
            height=dp(40),
            width=dp(150),
            font_size=dp(14),
            background_color=get_color_from_hex('#FF9800'),
            background_normal='',
            color=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5})
        self.clear_btn.bind(on_press=self.clear_selection)
        layout.add_widget(self.clear_btn)

        # Scrollable table area
        outer_scroll = ScrollView(do_scroll_x=1, do_scroll_y=1, size_hint=(1, 1))
        self.table = GridLayout(cols=2,
                                size_hint=(None, None),
                                width=Window.width,
                                size_hint_y=None,
                                spacing=dp(2),
                                padding=dp(4))
        self.table.bind(minimum_height=self.table.setter('height'),
                        minimum_width=self.table.setter('width'))

        outer_scroll.add_widget(self.table)
        layout.add_widget(outer_scroll)

        return layout

    def add_row(self, key, value):
        key_widget = SelectableTextInput(text=key,
                               size_hint_y=None,
                               height=dp(40),
                               size_hint_x=None,
                               width=Window.width / 2,
                               background_color=(0.95, 0.95, 0.95, 1),
                               foreground_color=(0, 0, 0, 1))

        value_widget = SelectableTextInput(text=value,
                                 size_hint_y=None,
                                 height=dp(40),
                                 size_hint_x=None,
                                 width=Window.width / 2,
                                 background_color=(1, 1, 1, 1),
                                 foreground_color=(0, 0, 0, 1))

        self.table.add_widget(key_widget)
        self.table.add_widget(value_widget)

    def clear_selection(self, instance):
        for child in self.table.children:
            if isinstance(child, SelectableTextInput):
                child.selected = False
                child.background_color = (1, 1, 1, 1) if child.text.strip() != "--------------------" else (0.95, 0.95, 0.95, 1)

    def check_meter(self, instance):
        meter_no = self.input.text.strip()
        self.table.clear_widgets()

        if not meter_no:
            self.add_row("Error", "Please enter a meter number")
            return
        if len(meter_no) != 12:
            self.add_row("Error", "Meter number must be 12 digits")
            return

        url = "https://web.bpdbprepaid.gov.bd/en/token-check"
        headers = {
            "accept": "text/x-component",
            "content-type": "text/plain;charset=UTF-8",
            "next-action": "29e85b2c55c9142822fe8da82a577612d9e58bb2",
            "origin": "https://web.bpdbprepaid.gov.bd",
            "referer": "https://web.bpdbprepaid.gov.bd/en/token-check",
            "user-agent": "Mozilla/5.0"
        }

        try:
            response = requests.post(url, headers=headers, data=f'[{{"meterNo":"{meter_no}"}}]', verify=False)
            if '1:' not in response.text:
                self.add_row("Error", "Invalid response or meter not found")
                return

            json_part = response.text.split('1:', 1)[1]
            data = json.loads(json_part)

            self.add_row("Customer Info", "--------------------")
            cust = data.get("mCustomerData", {}).get("result", {})
            for key, val in cust.items():
                if key.lower() == "_attributes":
                    continue
                self.add_row(format_key(key), get_text(val))

            self.add_row("", "")
            self.add_row("Last 3 Recharge Info", "--------------------")
            orders = data.get("mOrderData", {}).get("result", {}).get("orders", {}).get("order", [])
            for idx, order in enumerate(orders[:3]):
                self.add_row(f"Recharge {idx + 1}", "")
                for key, val in order.items():
                    if key.lower() == "_attributes":
                        continue
                    if key == "tariffFees":
                        for fee in val.get("tariffFee", []):
                            name = get_text(fee.get('itemName'))
                            desc = get_text(fee.get('chargeDes'))
                            amount = get_text(fee.get('chargeAmount'))
                            self.add_row(f"  {name}", f"{desc} = {amount}")
                    else:
                        self.add_row(format_key(key), get_text(val))

        except Exception as e:
            self.add_row("Error", str(e))

if __name__ == "__main__":
    MeterInfoApp().run()