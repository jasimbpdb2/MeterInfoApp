
def main():
    """Main interactive interface"""
    print("🚀 BPDB METER INFORMATION CHECKER")
    print("═" * 40)
    
    while True:
        print("\n🔧 Select Bill Type:")
        print("1. Prepaid (12-digit meter)")
        print("2. Postpaid (any digit meter)") 
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "3":
            print("👋 Goodbye!")
            break
            
        if choice not in ["1", "2"]:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")
            continue
        
        bill_type = "prepaid" if choice == "1" else "postpaid"
        
        # Conditional input prompt based on bill type
        if choice == "1":
            print(f"\n📝 Enter {bill_type.upper()} Meter Number:")
            meter_number = input("Meter Number: ").strip()
        elif choice == "2":
            print(f"\n📝 Enter {bill_type.upper()} Consumer Number:")
            meter_number = input("Consumer Number: ").strip()
        
        is_valid, message = validate_meter(meter_number, bill_type)
        if not is_valid:
            print(f"❌ {message}")
            continue
        
        print(f"\n🔄 Processing {bill_type.upper()} lookup...")
        
        try:
            if bill_type == "prepaid":
                result = fetch_prepaid_data(meter_number)
                display_prepaid_result(result)
            else:
                result = fetch_postpaid_data(meter_number)
                display_postpaid_result(result)
                
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        
        continue_test = input("\n🔄 Test another meter? (y/n): ").strip().lower()
        if continue_test != 'y':
            print("👋 Goodbye!")
            break

if __name__ == "__main__":
    main(
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

            # Parse weird JSON format keyed by "1"
            json_part = response.text.split('1:', 1)[1]
            data_all = json.loads(json_part)
            data = data_all.get("1")
            if not data:
                self.add_row("Error", 'No data under key "1"')
                return

            # Show Info Section: message, meterNo, customerNo
            attr = data.get("mOrderData", {}).get("result", {}).get("_attributes", {})
            self.add_row("Info", "--------------------")
            self.add_row("Message", attr.get("message", ""))
            self.add_row("Meter No", attr.get("meterNo", ""))
            self.add_row("Customer No", attr.get("customerNo", ""))

            # Show Customer Information
            self.add_row("", "")
            self.add_row("Customer Information", "--------------------")
            cust = data.get("mCustomerData", {}).get("result", {})
            for key, val in cust.items():
                if key.lower() == "_attributes":
                    continue
                self.add_row(format_key(key), get_text(val))

            # Show Orders table (last 3 recharges)
            self.add_row("", "")
            self.add_row("Last 3 Recharge Info", "--------------------")
            orders = data.get("mOrderData", {}).get("result", {}).get("orders", {}).get("order", [])
            if not isinstance(orders, list):
                orders = [orders]  # Make it a list if single order

            for idx, order in enumerate(orders[:3]):
                self.add_row(f"Recharge {idx + 1}", "")
                for key, val in order.items():
                    if key.lower() == "_attributes":
                        continue
                    if key == "tariffFees":
                        # Format tariff fees as joined string
                        fees = []
                        for fee in val.get("tariffFee", []):
                            name = get_text(fee.get('itemName'))
                            amount = get_text(fee.get('chargeAmount'))
                            fees.append(f"{name}: {amount}")
                        self.add_row(format_key(key), ", ".join(fees))
                    else:
                        self.add_row(format_key(key), get_text(val))

        except Exception as e:
            self.add_row("Error", str(e))

if __name__ == "__main__":
    MeterInfoApp().run()

