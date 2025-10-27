#Program 1 - INVOICE GENERATION

prods = int(input("Enter the number of products purchased: "))
pids, names, qtys, prices, discounts = [], [], [], [], []
bill=0

for i in range(prods):
    print(f"\n--- Product {i + 1} Details ---")
    name = input("Enter product name: ")
    pid = "PDT-" + name[0].upper() + str(i + 1)
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    if price>=200 and price<500:
        print("This product has a discount of 2 %")
        disc=price*2/100
    elif price>=500 and price<1000:
        print("This product has a discount of 5 %")
        disc=price*5/100
    elif price>=1000 and price<5000:
        print("This product has a discount of 8 %")
        disc=price*8/100
    elif price>=5000:
        print("This product has a discount of 10 %")
        disc=price*10/100
    else:
        disc=0
        print("No discount")

    pids.append(pid)
    names.append(name)
    qtys.append(qty)
    prices.append(price)
    discounts.append(disc)

print(f"{'FINAL INVOICE':^65}")
print("=" * 65)

print(f"{'Prod_ID':<10}{'Prod_Name':<15}{'Qty':<8}{'Price':<10}{'Discount':<10}{'Total':<10}")
print("-" * 65)

for i in range(prods):
    total = prices[i] * qtys[i] - discounts[i]
    name_disp = names[i][:15]
    print(f"{pids[i]:<10}{name_disp:<15}{qtys[i]:<8}{prices[i]:<10.2f}{discounts[i]:<10.2f}{total:<10.2f}")
    bill += total

print("-" * 65)
print(f"{'TOTAL BILL AMOUNT':>50}: {bill:.2f}")
print("=" * 65)