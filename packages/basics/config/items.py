# -*-coding:utf-8 -*
from packages.basics.config.shop_menus import *
from packages.basics.item import Item

# Defining items

# Useful variables we'll use to shorten the code

SR = ["Summoner's Rift"]
TT =["Twisted Treeline"]
CS = ["Crystal Scar"]
HA = ["Howling Abyss"]
COMMON = SR + TT + CS + HA

# Consumables

crystalline_flask = Item("Crystalline Flask", SR + TT + HA, "Consumable",
                         cost=345, menu=[shop["Defense"]["Health_Regen"],
                         shop["Magic"]["Mana_Regen"], shop["Consumables"]],
                         capacities=dict(Active=["Consumes a charge to restore "
                         "120 health and 60 mana over 12 seconds."],
                         Passive=["Unique: Starts with 3 charges and "
                                   "refills each time you stop by your shop."])
                         )
elixir_of_brilliance = Item("Elixir of Brilliance", SR, "Consumable", cost=250,
                            menu=[shop["Consumables"]],
                            capacities=dict(Consume=["On use, grants 25-40 "
                            "ability power, based on champion level, and 10% "
                            "cooldown reduction for 3 minutes."]))
elixir_of_fortitude = Item("Elixir of Fortitude", SR,
                           "Consumable", cost=350, menu=[shop["Consumables"]],
                           capacities=dict(Consume=["On use, grants 120-235 "
                           "health, based on champion level and 15 attack "
                           "damage for 3 minutes."]))
explorer_s_ward = Item("Explorer's Ward", SR, "Consumable",
                       capacities=dict(Consume=["Places an invisible ward that "
                       "reveals the surrounding area for 60 seconds."]))
health_potion = Item("Health Potion", COMMON, "Consumable", cost=35,
                     menu=[shop["Consumables"]],
                     capacities=dict(Consume=["Restores 150 health over 15 "
                     "seconds."]))
mana_potion = Item("Mana Potion", COMMON, "Consumable", cost=35,
                   menu=[shop["Consumables"]],
                   capacities=dict(Consume=["Restores 100 mana over 15 "
                   "seconds."]))
ichor_of_illumination = Item("Ichor of Illumination", TT, "Consumable",
                             cost=500, menu=[shop["Consumables"]],
                             capacities=dict(Consume=["On use, grants 30-64 "
                             "ability power based on champion level, 15% "
                             "cooldown reduction and a huge boost to mana and "
                             "energy regeneration for 4 minutes."]))
ichor_of_rage = Item("Ichor of Rage", TT, "Consumable", cost=500,
                     menu=[shop["Consumables"]], capacities=dict(Consume=["On "
                     "use, grants 20-42 attack damage, based on champion "
                     "level, 20-42 attack speed (based on champion level) and "
                     "15% increased damage to turrets for 4 minutes."]))
oracle_s_elixir = Item("Oracle's Elixir", SR, "Consumable", cost=400,
                       menu=[shop["Consumables"]],
                       capacities=dict(Consume=["Grants your champion stealth "
                       "detection for 4 minutes."]))
oracle_s_extract = Item("Oracle's Extract", TT + CS + HA, "Consumable",
                        cost=250, menu=[shop["Consumables"]],
                        capacities=dict(Consume=["Grants your champion stealth"
                        " detection for 5 minutes or until they die."]))
poro_snax = Item("Poro-Snax", HA, "Consumable", menu=[shop["Consumables"]],
                 capacities=dict(Consume=["Serves a scrumptious scoop to a "
                 "nearby Poro."]))
sight_ward = Item("Sight Ward", SR, "Consumable", cost=75,
                  menu=[shop["Consumables"]], capacities=dict(Consume=["Places"
                  " an invisible ward with 1100 range. Lasts 3 minutes."]))
vision_ward = Item("Vision Ward", SR, "Consumable", cost=125,
                   menu=[shop["Consumables"]],
                   capacities=dict(Consume=["Places an invisible ward with "
                   "1100 Vision Sight and 1000 range Magical Sight (can see "
                   "invisible units). Lasts 3 minutes."]))
total_biscuit_of_rejuvenation = Item("Total Biscuit of Rejuvenation",
                                     COMMON, "Consumable",
                                     capacities=dict(Consume=["Restores 80 "
                                     "health and 50 mana over 10 seconds."]))

# Basic items

amplifying_tome = Item("Amplifying Tome", COMMON, "Basic", cost=435,
                       menu=[shop["Magic"]["Ability_Power"]], ability_power=20)
bf_sword = Item("B.F. Sword", COMMON, "Basic", cost=1550,
                menu=[shop["Attack"]["Damage"]], attack_damage=45)
blasting_wand = Item("Blasting Wand", COMMON, "Basic", cost=860,
                     menu=[shop["Magic"]["Ability_Power"]], ability_power=40)
boots_of_speed = Item("Boots of Speed", COMMON, "Basic", cost=325,
                      menu=[shop["Movement"]],
                      capacities=dict(Passive=["Unique - Enhanced Movement: "
                      "+25 movement speed"]), movement_speed=25)
brawler_s_gloves = Item("Brawler's Gloves", COMMON, "Basic", cost=400,
                        menu=[shop["Attack"]["Critical_Strike"]],
                        critical_strike_chance=0.08)
chain_vest = Item("Chain Vest", COMMON, "Basic", cost=720,
                  menu=[shop["Defense"]["Armor"]], armor=40)
cloak_of_agility = Item("Cloak of Agility", COMMON, "Basic", cost=730,
                        menu=[shop["Attack"]["Critical_Strike"]],
                        critical_strike_chance=0.15)
cloth_armor = Item("Cloth Armor", COMMON, "Basic", cost=300,
                   menu=[shop["Defense"]["Armor"]], armor=15)
dagger= Item("Dagger", COMMON, "Basic", cost=400,
             menu=[shop["Attack"]["Attack_Speed"]], attack_speed=0.12)
doran_s_blade = Item("Doran's Blade", SR + TT + HA, "Basic", cost=475,
                     menu=[shop["Attack"]["Damage"],
                     shop["Defense"]["Health"]],
                     capacities=dict(Passive=["Your basic attacks restore 5 "
                     "health each time they hit an enemy."]), health=80,
                     attack_damage=10)
doran_s_ring = Item("Doran's Ring", SR + TT + HA, "Basic", cost=400,
                    menu=[shop["Defense"]["Health"],
                    shop["Magic"]["Ability_Power"],
                    shop["Magic"]["Mana_Regen"]],
                    capacities=dict(Passive=["Restores 4 mana when you kill an"
                    " enemy unit."]), ability_power=15, health=60,
                    mana_regeneration=3)
doran_s_shield = Item("Doran's Shield", COMMON, "Basic", cost=440,
                      menu=[shop["Defense"]["Health"],
                      shop["Defense"]["Health_Regen"]],
                      capacities=dict(Passive=["Unique: Blocks 8 damage from "
                      "champion basic attacks."]), health=100,
                      health_regeneration=10)
faerie_charm = Item("Faerie Charm", COMMON, "Basic", cost=180,
                    menu=[shop["Magic"]["Mana_Regen"]], mana_regeneration=3)
giant_s_belt = Item("Giant's Belt", COMMON, "Basic", cost=1000,
                    menu=[shop["Defense"]["Health"]], health=380)
hunter_s_machete = Item("Hunter's Machete", SR + TT + HA, "Basic", cost=300,
                        capacities=dict(Passive=["Unique Passive - Butcher: "
                        "Damage dealt to monsters increased by 10%.",
                        "Unique Passive - Maim: Your basic attacks "
                        "deal 10 bonus magic damage to monsters."]))
long_sword = Item("Long Sword", COMMON, "Basic", cost=400,
                  menu=[shop["Attack"]["Damage"]], attack_damage=10)
needlessly_large_rod = Item("Needlessly Large Rod", SR + HA, "Basic",
                            cost=1600, menu=[shop["Magic"]["Ability_Power"]],
                            ability_power=80)
negatron_cloak = Item("Negatron Cloak", COMMON, "Basic", cost=720,
                      menu=[shop["Defense"]["Magic_Resist"]],
                      magic_resistance=40)
null_magic_mantle = Item("Null-Magic Mantle", COMMON, "Basic", cost=400,
                         menu=[shop["Defense"]["Magic_Resist"]],
                         magic_resistance=20)
pickaxe = Item("Pickaxe", COMMON, "Basic", cost=875,
               menu=[shop["Attack"]["Damage"]], attack_damage=25)
prospector_s_blade = Item("Prospector's Blade", CS, "Basic", cost=950,
                          menu=[shop["Defense"]["Health"],
                          shop["Attack"]["Damage"],
                          shop["Attack"]["Life_Steal"]],
                          capacities=dict(Passive=["Unique - Prospector: +200 "
                          "health (does not stack with other Prospector items"
                          ")."]), health=200, attack_damage=20,
                          life_steal=0.05)
prospector_s_ring = Item("Prospector's Ring", CS, "Basic", cost=950,
                         menu=[shop["Defense"]["Health"],
                         shop["Magic"]["Ability_Power"],
                         shop["Magic"]["Mana_Regen"]],
                         capacities=dict(Passive=["Unique - Prospector: +200 "
                         "health (does not stack with other Prospector items"
                         ")."]), health=200, ability_power=40,
                         mana_regeneration=10)
recurve_bow = Item("Recurve Bow", COMMON, "Basic", cost=900,
                   menu=[shop["Attack"]["Attack_Speed"]], attack_speed=0.3)
rejuvenation_bead = Item("Rejuvenation Bead", COMMON, "Basic", cost=180,
                         menu=[shop["Defense"]["Health_Regen"]],
                         health_regeneration=5)
ruby_crystal = Item("Ruby Crystal", COMMON, "Basic", cost=475,
                    menu=[shop["Defense"]["Health"]], health=180)
sapphire_crystal = Item("Sapphire Crystal", COMMON, "Basic", cost=400,
                        menu=[shop["Magic"]["Mana"]], mana=200)
bonetooth_necklace = Item("Bonetooth Necklace", COMMON, "Basic", cost=800,
                          menu=[shop["Attack"]["Damage"],
                          shop["Magic"]["Cooldown_Reduction"],
                          shop["Movement"]], capacities=dict(Passive=["Unique:"
                          " +2 attack damage per level", "Rengar collects "
                          "trophies when killing Champions, and gains bonus "
                          "effects based on how many trophies he has. Kills "
                          "and assists grant 1 trophy, and 1 trophy is lost on"
                          " death.\n\t3 Trophies:\n\t\t+10 armor penetration"
                          "\n\t\t+5% cooldown reduction\n\t6 Trophies:\n\t\t"
                          "+25 movement speed\n\t9 Trophies:\n\t\tRengar's "
                          "leap gains 150 bonus range\n\t14 Trophies:\n\t\t"
                          "Thrill of the Hunt's duration is increased by 3 "
                          "seconds. Additionally, Rengar's next ability used "
                          "after activating Thrill of the Hunt generates 1 "
                          "bonus Ferocity\nKilling or assisting in killing "
                          "Kha'Zix after the \"The Hunt Is On !\" event has "
                          "started will upgrade this into the Head of Kha'Zix,"
                          " permanently gaining the effects of all 14 "
                          "trophies."]), attack_damage=5)
hex_core = Item("Hex Core", COMMON, "Basic", capacities=dict(Passive=["Grants "
                "Viktor +3 ability power per level"]))

# Advanced items

abyssal_scepter = Item("Abyssal Scepter", COMMON, "Advanced", cost=980,
                       menu=[shop["Defense"]["Magic_Resist"],
                       shop["Magic"]["Ability_Power"]], recipe=[blasting_wand,
                       negatron_cloak], capacities=dict(Aura=["Unique: Reduces"
                       " the magic resist of nearby enemies by 20 (700 "
                       "range)."]), ability_power=70, magic_resistance=45)
avarice_blade = Item("Avarice Blade", COMMON, "Advanced", cost=400,
                     menu=[shop["Attack"]["Critical_Strike"]],
                     recipe=[brawler_s_gloves],
                     capacities=dict(Passive=["Unique - Avarice: Gain an "
                     "additional +3 gold every 10 seconds", "Unique - Greed: "
                     "Gain an additional 2 gold every kill."]),
                     critical_strike_chance=0.1)
berserker_s_greaves = Item("Berserker's Greaves", COMMON, "Advanced", cost=175,
                           menu=[shop["Attack"]["Attack_Speed"],
                           shop["Movement"]], recipe=[boots_of_speed, dagger],
                           capacities=dict(Passive=["Unique - Enhanced "
                           "Movement: +45 movement speed"]), movement_speed=45,
                           attack_speed=0.2)
boots_of_mobility = Item("Boots of Mobility", COMMON, "Advanced", cost=675,
                         menu=[shop["Movement"]], recipe=[boots_of_speed],
                         capacities=dict(Passive=["Unique - Enhanced Movement:"
                         " +45 movement speed. Increases to +105 movement "
                         "speed when out of combat for 5 seconds."]),
                         movement_speed=45)
boots_of_swiftness = Item("Boots of Swiftness", COMMON, "Advanced", cost=675,
                          menu=[shop["Movement"]], recipe=[boots_of_speed],
                          capacities=dict(Passive=["Unique - Enhanced "
                          "Movement: +60 movement speed.", "Unique - Slow "
                          "Resist: Movement slowing effects are reduced by "
                          "25%."]), movement_speed=60)
the_brutalizer = Item("The Brutalizer", COMMON, "Advanced", cost=537,
                      menu=[shop["Attack"]["Damage"],
                      shop["Magic"]["Cooldown_Reduction"]],
                      recipe=[long_sword, long_sword],
                      capacities=dict(Passive=["Unique: +10% cooldown "
                      "reduction", "Unique: +10 armor penetration"]),
                      attack_damage=25, cooldown_reduction=0.1,
                      flat_armor_penetration=10)
catalyst_the_protector = Item("Catalyst the Protector", COMMON, "Advanced",
                              cost=325, menu=[shop["Defense"]["Health"],
                              shop["Magic"]["Mana"]], recipe=[ruby_crystal,
                              sapphire_crystal],
                              capacities=dict(Passive=["Unique Passive - "
                              "Valor's Reward: On leveling up, restores 150 "
                              "health and 200 mana over 8 seconds."]),
                              health=200, mana=300)
chalice_of_harmony = Item("Chalice of Harmony", COMMON, "Advanced", cost=120,
                          menu=[shop["Defense"]["Magic_Resist"],
                          shop["Magic"]["Mana_Regen"]],
                          recipe=[faerie_charm, faerie_charm,
                          null_magic_mantle], capacities=dict(Passive=["Unique"
                          " Passive - Mana Font: Increases your mana "
                          "regeneration by 1% per 1% mana you are missing."]),
                          magic_resistance=25, mana_regeneration=7)
emblem_of_valor = Item("Emblem of Valor", COMMON, "Advanced", cost=170,
                       menu=[shop["Defense"]["Armor"],
                       shop["Defense"]["Health_Regen"]], recipe=[cloth_armor,
                       rejuvenation_bead], capacities=dict(Aura=["Unique - "
                       "Valor: Nearby allied champions gain +7 health regen "
                       "per 5 seconds."]), armor=20)
fiendish_codex = Item("Fiendish Codex", COMMON, "Advanced", cost=385,
                      menu=[shop["Magic"]["Ability_Power"],
                      shop["Magic"]["Cooldown_Reduction"]],
                      recipe=[amplifying_tome],
                      capacities=dict(Passive=["Unique: +10% cooldown "
                      "reduction"]), ability_power=30, cooldown_reduction=0.1)
frozen_mallet = Item("Frozen Mallet", COMMON, "Advanced", cost=950,
                     menu=[shop["Attack"]["Damage"],
                     shop["Defense"]["Health"]], recipe=[ruby_crystal, pickaxe,
                     giant_s_belt], capacities=dict(Passive=["Unique - Icy: "
                     "Your basic attacks slow your target's Movement Speed by "
                     "40% for 1.5 seconds (30% slow for ranged attacks)."]),
                     health=700, attack_damage=30)
glacial_shroud = Item("Glacial Shroud", COMMON, "Advanced", cost=230,
                      menu=[shop["Defense"]["Armor"],
                      shop["Magic"]["Cooldown_Reduction"],
                      shop["Magic"]["Mana"]], recipe=[sapphire_crystal,
                      chain_vest], capacities=dict(Passive=["Unique: +10% "
                      "cooldown reduction"]), armor=45, mana=300,
                      cooldown_reduction=0.1)
guardian_angel = Item("Guardian Angel", SR + CS, "Advanced", cost=1310,
                      menu=[shop["Defense"]["Armor"],
                      shop["Defense"]["Magic_Resist"]], recipe=[negatron_cloak,
                      chain_vest], capacities=dict(Passive=["Unique: Revives "
                      "your champion upon death, restoring 30% of your "
                      "maximum health and mana after 4 seconds of stasis. "
                      "5 minutes cooldown."]), armor=50, magic_resistance=40)