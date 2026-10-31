"""Create a formatted grocery receipt with a discount and GST."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


GST_RATE = Decimal("5")
DISCOUNT_RATE = Decimal("10")
CENT = Decimal("0.01")


def get_positive_decimal(prompt):
    while True:
        value = input(prompt).strip()
        try:
            number = Decimal(value)
        except InvalidOperation:
            print("Please enter a valid number.")
            continue

        if not number.is_finite() or number <= 0:
            print("Please enter a number greater than zero.")
            continue
        return number


def format_money(amount):
    return f"Rs. {amount:,.2f}"


def main():
    item_name = ""
    while not item_name:
        item_name = input("Grocery item name: ").strip()
        if not item_name:
            print("Item name cannot be empty.")

    quantity = get_positive_decimal("Quantity (e.g. 1 or 1.5): ")
    unit_price = get_positive_decimal("Price per unit (Rs.): ")
    unit_price = unit_price.quantize(CENT, rounding=ROUND_HALF_UP)

    subtotal = (quantity * unit_price).quantize(CENT, rounding=ROUND_HALF_UP)
    discount = (subtotal * DISCOUNT_RATE / 100).quantize(
        CENT, rounding=ROUND_HALF_UP
    )
    taxable_amount = subtotal - discount
    gst = (taxable_amount * GST_RATE / 100).quantize(
        CENT, rounding=ROUND_HALF_UP
    )
    total = taxable_amount + gst

    quantity_text = format(quantity.normalize(), "f")
    receipt = [
        "INDIAN GROCERY STORE",
        "GROCERY BILL",
        "",
        f"Item: {item_name}",
        f"Quantity: {quantity_text}",
        f"Price per unit: {format_money(unit_price)}",
        f"Subtotal: {format_money(subtotal)}",
        f"Discount ({DISCOUNT_RATE}%): -{format_money(discount)}",
        f"Taxable amount: {format_money(taxable_amount)}",
        f"GST ({GST_RATE}%): {format_money(gst)}",
        f"TOTAL: {format_money(total)}",
        "",
        "Thank you for shopping with us!",
    ]
    width = max(len(line) for line in receipt)

    print()
    print("+" + "-" * (width + 2) + "+")
    for line in receipt:
        print("| " + line.ljust(width) + " |")
    print("+" + "-" * (width + 2) + "+")


if __name__ == "__main__":
    main()
