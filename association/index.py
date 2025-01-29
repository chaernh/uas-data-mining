from collections import Counter
from itertools import combinations
from itertools import permutations

def apriori(transactions, min_support, min_confidence):
  itemsets = {}
  frequent_itemsets = {}
  rules = []

  # Generate L1
  all_items = [item for transaction in transactions for item in transaction]
  item_counts = Counter(all_items)
  itemsets[1] = {k: v for k, v in item_counts.items() if v >= min_support}

  # Generate Lk (k > 1)
  k = 2
  while len(itemsets[k-1]) > 0:
    itemsets[k] = generate_itemsets(transactions, k)
    itemsets[k] = {k: v for k, v in itemsets[k].items() if v >= min_support}
    k += 1

  # Gabungkan semua frequent itemset
  for i in range(1, k-1):
    frequent_itemsets.update(itemsets[i])

  # Generate association rules
  for itemset, support in frequent_itemsets.items():
    if isinstance(itemset, tuple): # Pastikan itemset memiliki lebih dari 1 item
      for i in range(1, len(itemset)):
        for antecedent in permutations(itemset, i):
          antecedent = tuple(sorted(antecedent))
          consequent = tuple(sorted(set(itemset) - set(antecedent)))
          if antecedent in frequent_itemsets:
            confidence = support / frequent_itemsets[antecedent] * 100
            if confidence >= min_confidence:
              rules.append((antecedent, consequent, support, confidence))

  return rules

def generate_itemsets(transactions, itemset_size):
  """
  Menghasilkan itemset dengan ukuran tertentu dan menghitung support.

  Args:
      transactions: List transaksi.
      itemset_size: Ukuran itemset (misalnya, 2 untuk L2).

  Returns:
      Dictionary dengan itemset sebagai key dan support sebagai value.
  """
  itemsets = {}
  for transaction in transactions:
    for combination in combinations(transaction, itemset_size):
      if combination not in itemsets:
        itemsets[combination] = 0
      itemsets[combination] += 1
  return itemsets

transactions = [
    ['Roti', 'Susu'],
    ['Roti', 'Susu', 'Telur'],
    ['Blue_band', 'Coklat', 'Susu'],
    ['Blue_band', 'Roti', 'Susu'],
    ['Coklat', 'Roti', 'Susu', 'Telur']
]

# Gabungkan semua item dari transaksi
all_items = [item for transaction in transactions for item in transaction]

# Hitung kemunculan setiap item
item_counts = Counter(all_items)

# Tampilkan L1
print("L1 (Itemset dengan 1 item):")
for item, count in item_counts.items():
  print(f"{item}: {count}")
  
# Generate L2
L2 = generate_itemsets(transactions, 2)
print("\nL2 (Itemset dengan 2 item):")
for itemset, count in L2.items():
  print(f"{itemset}: {count}")

# Generate L3
L3 = generate_itemsets(transactions, 3)
print("\nL3 (Itemset dengan 3 item):")
for itemset, count in L3.items():
  print(f"{itemset}: {count}")
  
# Jalankan algoritma Apriori
rules = apriori(transactions, 2, 60)

# Tampilkan association rules
print("\nAssociation Rules:")
for antecedent, consequent, support, confidence in rules:
  print(f"{antecedent} -> {consequent}: support = {support}, confidence = {confidence:.2f}%")