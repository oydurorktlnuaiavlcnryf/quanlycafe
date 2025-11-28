# quanlycafe
# Cafe Manager

A simple Python application for managing a coffee shop. This tool lets you manage the menu, place orders, handle invoices, and generate revenue reports.

## Features

- **Menu Management**
  - Add new menu items
  - Update item prices
  - Remove items from the menu
  - List all menu items

- **Order Handling**
  - Place orders with multiple menu items and quantities
  - Automatically calculates the total price of each order

- **Invoice & Revenue Reporting**
  - Stores all invoices
  - Generates overall revenue reports, including total sales and number of invoices

## Getting Started

### Requirements

- Python 3

### Usage

1. Clone this repository or download the source files.
2. Run the script from your terminal:

   ```bash
   python cafe_manager.py
   ```

3. The example in `cafe_manager.py` will:
   - Add items to the menu
   - Show all menu items
   - Create example orders
   - Print the revenue report

You can modify or extend the script to suit your specific needs.

## File Structure

- `cafe_manager.py` — Main application logic
- `README.md` — Documentation

## Example Output

```
=== MENU ===
Cà phê sữa: 25000 VND
Trà đào: 30000 VND
Bánh mì: 20000 VND

=== ORDER ===
2x Cà phê sữa - 50000 VND
1x Bánh mì - 20000 VND
Total: 70000 VND

=== ORDER ===
3x Trà đào - 90000 VND
Total: 90000 VND

=== REVENUE REPORT ===
Tổng doanh thu: 160000 VND
Số hóa đơn: 2
```

## License

This project is open source and available for modification and use.
