import random

hero_hp = 100
monster_hp = 100

print("⚔️ Починається бій Героя і Монстра!\n")

round_num = 1

while hero_hp > 0 and monster_hp > 0:
    print(f"----- Раунд {round_num} -----")

    # Герой б'є першим
    hero_damage = random.randint(5, 20)
    monster_hp -= hero_damage
    if monster_hp < 0:
        monster_hp = 0
    print(f"Герой ударив на {hero_damage} урону. У Монстра лишилось {monster_hp} HP.")

    if monster_hp == 0:
        break

    # Монстр відповідає
    monster_damage = random.randint(5, 20)
    hero_hp -= monster_damage
    if hero_hp < 0:
        hero_hp = 0
    print(f"Монстр ударив на {monster_damage} урону. У Героя лишилось {hero_hp} HP.")

    print()
    round_num += 1

print("\n🏆 Бій завершено!")

if hero_hp > 0:
    print("Герой переміг! 🎉")
else:
    print("Монстр переміг! 💀")
