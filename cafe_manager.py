class CafeManager:
    def __init__(self):
        # Danh sách món (menu)
        self.menu = []
        # Danh sách các hóa đơn đã thanh toán
        self.invoices = []

    def add_menu_item(self, name, price):
        self.menu.append({'name': name, 'price': price})

    def remove_menu_item(self, name):
        self.menu = [item for item in self.menu if item['name'] != name]

    def update_menu_item(self, name, new_price):
        for item in self.menu:
            if item['name'] == name:
                item['price'] = new_price

    def list_menu(self):
        print("=== MENU ===")
        for item in self.menu:
            print(f"{item['name']}: {item['price']} VND")

    def order(self, items):
        total = 0
        print("=== ORDER ===")
        for order_item in items:
            for menu_item in self.menu:
                if menu_item['name'] == order_item['name']:
                    subtotal = menu_item['price'] * order_item['quantity']
                    total += subtotal
                    print(f"{order_item['quantity']}x {menu_item['name']} - {subtotal} VND")
        print(f"Total: {total} VND")
        self.invoices.append({'items': items, 'total': total})

    def revenue_report(self):
        print("=== REVENUE REPORT ===")
        total_revenue = sum(invoice['total'] for invoice in self.invoices)
        print(f"Tổng doanh thu: {total_revenue} VND")
        print(f"Số hóa đơn: {len(self.invoices)}")


# Ví dụ sử dụng:
if __name__ == "__main__":
    manager = CafeManager()
    manager.add_menu_item("Cà phê sữa", 25000)
    manager.add_menu_item("Trà đào", 30000)
    manager.add_menu_item("Bánh mì", 20000)

    manager.list_menu()
    manager.order([{'name': 'Cà phê sữa', 'quantity': 2}, {'name': 'Bánh mì', 'quantity': 1}])
    manager.order([{'name': 'Trà đào', 'quantity': 3}])
    
    manager.revenue_report()
