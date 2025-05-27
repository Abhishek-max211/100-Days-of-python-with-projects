# Day 12
# Scope in Python
enemies=1
def increase_enemies():
   enemies=2
   print(f"enemies inside function:{enemies}")
increase_enemies()
print(f"enemies outside function:{enemies}")

# Local Scope in Python
def drink_potion():
   potion_strenth=2
   print(potion_strenth)
drink_potion()

# Global Scope in Python
player_health=10
def drink_potion():
   print(player_health)
drink_potion()
print(player_health)

# Modifying Global Scope
enemies=1
def increase_enemies():
   global enemies
   enemies+=1
   print(f"enemies inside function:{enemies}")
increase_enemies()
print(f"enemies outside the functon:{enemies}")