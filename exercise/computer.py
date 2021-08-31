print("==========Computer Bazar =======")
print("1. Dell (Rs: 20000) 2.Toshiva(Rs: 30000) 3. Mac (Rs: 50000)")

dell_price = 20000
toshiva_price = 30000
mac_price = 50000

total_price = 0

option = int(input("Enter any options: "))

if option == 1:
    qt = int(input("Enter quantity: "))
    total_price += dell_price * qt

elif option == 2:
    qt = int(input("Enter quantity: "))
    total_price += toshiva_price * qt

elif option == 3:
    qt = int(input("Enter quantity: "))
    total_price += mac_price * qt
else:
    print("Bye")
    exit()

print("1. Home(Rs: 10000) 2. Pickup(free)")
pq = int(input("Enter any option: "))
home_price = 0
if pq == 1:
    home_price += 1000

print("1. Plastic bag(1000) 2. Bag (2000) 3. Git box(5000) 4. None")
plastic_price = 0
bag_price = 0
git_box_price = 0

packing_question = int(input("Enter any option: "))
if packing_question == 1:
    plastic_price += 1000
elif packing_question == 2:
    bag_price += 2000
elif packing_question == 3:
    git_box_price += 5000
else:
    exit()

print("1. Ktm(13% tax) 2. LTP(free) 3.(free)")
lq = int(input("Enter location option: "))
tax_amount = 0
if lq == 1:
    tax_amount += total_price * 0.13

gt_total = total_price + tax_amount + home_price + git_box_price + bag_price + plastic_price

print("============Result ============")
print(f"Total amount {total_price}")
print(f"Tax amount {tax_amount}")
print('-----------------------')
print(f"Grand total {gt_total}")
