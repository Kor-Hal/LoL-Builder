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
b_f_sword = Item("B.F. Sword", COMMON, "Basic", cost=1550,
                menu=[shop["Attack"]["Damage"]], attack_damage=45)
blasting_wand = Item("Blasting Wand", COMMON, "Basic", cost=860,
                     menu=[shop["Magic"]["Ability_Power"]], ability_power=40)
boots_of_speed = Item("Boots of Speed", COMMON, "Basic", cost=325,
                      menu=[shop["Movement"]],
                      capacities=dict(Passive=["Unique - Enhanced Movement: "
                      "+25 movement speed"]), flat_movement_speed=25)
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
the_hex_core = Item("Hex Core", COMMON, "Basic",
                    capacities=dict(Passive=["Grants Viktor +3 ability power "
                    "per level"]))

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
                           "Movement: +45 movement speed"]),
                           flat_movement_speed=45, attack_speed=0.2)
boots_of_mobility = Item("Boots of Mobility", COMMON, "Advanced", cost=675,
                         menu=[shop["Movement"]], recipe=[boots_of_speed],
                         capacities=dict(Passive=["Unique - Enhanced Movement:"
                         " +45 movement speed. Increases to +105 movement "
                         "speed when out of combat for 5 seconds."]),
                         flat_movement_speed=45)
boots_of_swiftness = Item("Boots of Swiftness", COMMON, "Advanced", cost=675,
                          menu=[shop["Movement"]], recipe=[boots_of_speed],
                          capacities=dict(Passive=["Unique - Enhanced "
                          "Movement: +60 movement speed.", "Unique - Slow "
                          "Resist: Movement slowing effects are reduced by "
                          "25%."]), flat_movement_speed=60)
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
guardian_s_horn = Item("Guardian's Horn", HA, "Advanced", cost=370,
                       menu=[shop["Defense"]["Health"],
                       shop["Defense"]["Health_Regen"]],
                       recipe=[rejuvenation_bead, ruby_crystal],
                       capacities=dict(Passive=["Unique: Nearby enemy spell "
                       "casts reduce the cooldown of Battle Cry by 1 second."],
                       Active=["Unique - Battle Cry: Gain 30% movement speed, "
                       "20 armor and 20 magic resistance for 3 seconds. 25 "
                       "seconds cooldown."]), health=180,
                       health_regeneration=12)
guinsoo_s_rageblade = Item("Guinsoo's Rageblade", COMMON, "Advanced", cost=865,
                           menu=[shop["Attack"]["Damage"],
                           shop["Attack"]["Attack_Speed"],
                           shop["Magic"]["Ability_Power"]],
                           recipe=[pickaxe, blasting_wand],
                           capacities=dict(Passive=["Passive: Your basic "
                           "attacks or spellcasts grant you 4% attack speed "
                           "and 4 ability power for 8 seconds. This bonus "
                           "stacks up to 8 times.", "Unique Passive: Falling "
                           "below 50% health grants you 20% attack speed, "
                           "10% life steal and 10% spell vamp until you exit "
                           "combat. 30 seconds cooldown."]), ability_power=40,
                           attack_damage=30)
haunting_guise = Item("Haunting Guise", COMMON, "Advanced", cost=575,
                      menu=[shop["Defense"]["Health"],
                      shop["Magic"]["Ability_Power"]], recipe=[ruby_crystal,
                      amplifying_tome], capacities=dict(Passive=["Unique "
                      "Passive - Eyes of Pain: +15 magic penetration"]),
                      flat_magic_penetration=15, ability_power=25, health=200)
hexdrinker = Item("Hexdrinker", COMMON, "Advanced", cost=550,
                  menu=[shop["Attack"]["Damage"],
                  shop["Defense"]["Magic_Resist"]], recipe=[long_sword,
                  null_magic_mantle], capacities=dict(Passive=["Unique - "
                  "Lifeline: Upon taking magic damage that would reduce "
                  "health below 30%, grants a shield that absorbs 250 magic "
                  "damage for 5 seconds (90 second cooldown)."]),
                  attack_damage=25, magic_resistance=25)
hextech_revolver = Item("Hextech Revolver", COMMON, "Advanced", cost=330,
                        menu=[shop["Magic"]["Ability_Power"]],
                        recipe=[amplifying_tome, amplifying_tome],
                        capacities=dict(Passive=["Unique: +12% spell vamp"]),
                        spell_vamp=0.12, ability_power=40)
infinity_edge = Item("Infinity Edge", COMMON, "Advanced", cost=645,
                     menu=[shop["Attack"]["Critical_Strike"],
                     shop["Attack"]["Damage"]], recipe=[b_f_sword, pickaxe,
                     cloak_of_agility], capacities=dict(Passive=["Unique: +50%"
                     " critical strike damage."]), critical_strike_damage=0.5,
                     attack_damage=70, critical_strike_chance=0.25)
ionian_boots_of_lucidity = Item("Ionian Boots of Lucidity", COMMON, "Advanced",
                                cost=675, menu=[shop["Movement"],
                                shop["Magic"]["Cooldown_Reduction"]],
                                recipe=[boots_of_speed],
                                capacities=dict(Passive=["Unique: +15% "
                                "cooldown reduction","Unique - Enhanced "
                                "Movement: +45 movement speed"]),
                                cooldown_reduction=0.15,
                                flat_movement_speed=45)
kage_s_lucky_pick = Item("Kage's Lucky Pick", COMMON, "Advanced", cost=330,
                         menu=[shop["Magic"]["Ability_Power"]],
                         recipe=[amplifying_tome],
                         capacities=dict(Passive=["Unique - Lucky Shadow: Gain"
                         " +4 additional gold every 10 seconds."]),
                         ability_power=25)
kindlegem = Item("Kindlegem", COMMON, "Advanced", cost=375,
                 menu=[shop["Defense"]["Health"],
                 shop["Magic"]["Cooldown_Reduction"]], recipe=[ruby_crystal],
                 capacities=dict(Passive=["Unique: +10% cooldown reduction"]),
                 cooldown_reduction=0.1, health=200)
last_whisper = Item("Last Whisper", COMMON, "Advanced", cost=1025,
                    menu=[shop["Attack"]["Damage"]], recipe=[long_sword,
                    pickaxe], capacities=dict(Passive=["Unique: +35% armor "
                    "penetration"]), perc_armor_penetration = 0.35,
                    attack_damage=40)
madred_s_razors = Item("Madred's Razor", SR, "Advanced", cost=100,
                       menu=[shop["Attack"]["Damage"],
                       shop["Defense"]["Armor"]], recipe=[cloth_armor,
                       hunter_s_machete], capacities=dict(Passive=["Unique - "
                       "Maim: Your basic attacks against monsters deal 60 "
                       "bonus magic damage."]), armor=25)
mana_manipulator = Item("Mana Manipulator", COMMON, "Advanced", cost=120,
                        menu=[shop["Magic"]["Mana_Regen"]],
                        recipe=[faerie_charm],
                        capacities=dict(Passive=["Unique Aura - Mana Warp: "
                        "Nearby allied champions gain +5 mana regeneration per"
                        " 5 seconds. (1100 range)"]))
mejai_s_soulstealer = Item("Mejai's Soulstealer", SR, "Advanced", cost=800,
                           menu=[shop["Magic"]["Ability_Power"]],
                           recipe=[amplifying_tome],
                           capacities=dict(Passive=["Unique: Your champion "
                           "gains 8 ability power per stack, receiving 2 "
                           "stacks for a kill or 1 stack for an assist. This "
                           "effect can stack 20 times ; you lose a third of "
                           "your stacks if you die. At 20 stacks, your "
                           "champion gains 15% cooldown reduction."]),
                           ability_power=20)
mercury_s_treads = Item("Mercury's Treads", COMMON, "Advanced", cost=475,
                        menu=[shop["Defense"]["Magic_Resist"],
                        shop["Movement"]], recipe=[boots_of_speed,
                        null_magic_mantle], capacities=dict(Passive=["Unique "
                        "- Enhanced Movement: +45 movement speed", "Unique - "
                        "Tenacity: The duration of stuns, slows, taunts, fears"
                        ", silences, blinds and immobilizes are reduced by "
                        "35%."]), flat_movement_speed=45, magic_resistance=25)
ninja_tabi = Item("Ninja Tabi", COMMON, "Advanced", cost=375,
                  menu=[shop["Defense"]["Armor"], shop["Movement"]],
                  recipe=[boots_of_speed, cloth_armor],
                  capacities=dict(Passive=["Unique - Enhanced Movement: +45 "
                  "movement speed.", "Unique: Blocks 10% of the damage from "
                  "basic attacks."]), flat_movement_speed=45, armor=25)
overlord_s_bloodmail = Item("Overlord's Bloodmail", TT, "Advanced", cost=980,
                            menu=[shop["Defense"]["Health"]],
                            recipe=[ruby_crystal, giant_s_belt],
                            capacities=dict(Passive=["Unique Passive: On kill "
                            "or assist, gain 200 health over 5 seconds."]),
                            health=850)
phage = Item("Phage", COMMON, "Advanced", cost=475,
             menu=[shop["Attack"]["Damage"], shop["Defense"]["Health"]],
             recipe=[ruby_crystal, long_sword],
             capacities=dict(Passive=["Unique - Rage: Basic attacks grant 20 "
             "movement speed for 2 seconds on hit. Minion, monster and "
             "champion kills grant 60 movement speed for 2 seconds. The "
             "movement speed bonus is halved for ranged champions."]),
             health=200, attack_damage=20)
philosopher_s_stone = Item("Philosopher's Stone", COMMON, "Advanced", cost=340,
                           menu=[shop["Defense"]["Health_Regen"],
                           shop["Magic"]["Mana_Regen"]], recipe=[faerie_charm,
                           rejuvenation_bead],
                           capacities=dict(Passive=["Unique - Transmute: Gain "
                           "+5 additional gold every 10 seconds."]),
                           health_regeneration=7, mana_regeneration=9)
quicksilver_sash = Item("Quicksilver Sash", COMMON, "Advanced", cost=830,
                        menu=[shop["Defense"]["Magic_Resist"]],
                        recipe=[negatron_cloak],
                        capacities=dict(Passive=["Unique - Quicksilver: "
                        "Removes all debuffs from your champion. 90 seconds "
                        "cooldown."]), magic_resistance=45)
rabadon_s_deathcap = Item("Rabadon's Deathcap", SR + HA, "Advanced", cost=840,
                          menu=[shop["Magic"]["Ability_Power"]],
                          recipe=[blasting_wand, needlessly_large_rod],
                          capacities=dict(Passive=["Unique: +30% ability "
                          "power"]), ability_power=120)
runaan_s_hurricane = Item("Runaan's Hurricane", COMMON, "Advanced", cost=700,
                          menu=[shop["Attack"]["Attack_Speed"]],
                          recipe=[recurve_bow, dagger, dagger],
                          capacities=dict(Passive=["Ranged only", "Unique "
                          "Passive: Your basic attacks fire minor bolts at 2 "
                          "nearby targets, each dealing 10 + 50% of your "
                          "attack damage and applying on-hit effects."]),
                          attack_speed=0.7)
rylai_s_crystal_scepter = Item("Rylai's Crystal Scepter", COMMON, "Advanced",
                               cost=605, menu=[shop["Defense"]["Health"],
                               shop["Magic"]["Ability_Power"]],
                               recipe=[amplifying_tome, blasting_wand,
                               giant_s_belt], capacities=dict(Passive=["Unique"
                               ": Dealing spell damage slows the target's "
                               "movement speed by 35% for 1.5 seconds (15% "
                               "for multi-target and damage-over-time "
                               "spells)."]), ability_power=80, health=500)
seeker_s_armguard = Item("Seeker's Armguard", COMMON, "Advanced", cost=125,
                         menu=[shop["Defense"]["Armor"],
                         shop["Magic"]["Ability_Power"]],
                         recipe=[amplifying_tome, cloth_armor, cloth_armor],
                         capacities=dict(Passive=["Unique: Killing a unit "
                         "grants 0.5 bonus armor and ability power. This "
                         "bonus stacks up to 30 times."]),
                         armor=30, ability_power=20)
sheen = Item("Sheen", COMMON, "Advanced", cost=365,
             menu=[shop["Magic"]["Ability_Power"], shop["Magic"]["Mana"]],
             recipe=[sapphire_crystal, amplifying_tome],
             capacities=dict(Passive=["Unique - Spellblade: On cast, for 10 "
             "seconds, your next standard attack deals additional physical "
             "damage equal to 100% of your base attack damage. 2 seconds "
             "cooldown."]), ability_power=25, mana=200)
sightstone = Item("Sightstone", SR, "Advanced", cost=475,
                  menu=[shop["Defense"]["Health"], shop["Consumables"]],
                  recipe=[ruby_crystal], capacities=dict(Passive=["Unique: "
                  "Ward Refresh - Starts with 4 charges and refill each time "
                  "you return to the shop."], Active=["Unique: Ghost Ward - "
                  "Consumes a charge to place a Ghost Ward. You may have a "
                  "maximum of 2 wards from this item at once."]), health=180)
sorcerer_s_shoes = Item("Sorcerer's Shoes", COMMON, "Advanced", cost=775,
                        menu=[shop["Movement"]], recipe=[boots_of_speed],
                        capacities=dict(Passive=["Unique - Enhanced Movement: "
                        "+45 movement speed."]), flat_movement_speed=45,
                        flat_magic_penetration=15)
spectre_s_cowl = Item("Spectre's Cowl", COMMON, "Advanced", cost=205,
                      menu=[shop["Defense"]["Health"],
                      shop["Defense"]["Magic_Resist"]], recipe=[negatron_cloak,
                      ruby_crystal], capacities=dict(Passive=["Unique: Grants "
                      "15 health regen for 10 seconds after taking damage from"
                      " an enemy champion."]), health=200, magic_resistance=45)
spirit_stone = Item("Spirit Stone", SR + TT + HA, "Advanced", cost=40,
                    menu=[shop["Defense"]["Health_Regen"],
                    shop["Magic"]["Mana_Regen"]], recipe=[hunter_s_machete,
                    faerie_charm, rejuvenation_bead],
                    capacities=dict(Passive=["Unique Passive - Butcher: "
                    "Damage dealt to monsters incresed by 20%.", "Unique "
                    "Passive - Maim: Your basic attacks against monsters deal "
                    "10 bonus magic damage."]), health_regeneration=14,
                    mana_regeneration=7)
stinger = Item("Stinger", COMMON, "Advanced", cost=450,
               menu=[shop["Attack"]["Attack_Speed"]], recipe=[dagger, dagger],
               capacities=dict(Passive=["Unique: +10% cooldown reduction"]),
               attack_speed=0.4)
sunfire_cape = Item("Sunfire Cape", COMMON, "Advanced", cost=930,
                    menu=[shop["Defense"]["Armor"], shop["Defense"]["Health"]],
                    recipe=[chain_vest, giant_s_belt],
                    capacities=dict(Passive=["Unique passive: Deals 40 magic "
                    "damage per second to nearby enemies (400 range)."]),
                    armor=45, health=450)
sword_of_the_divine = Item("Sword of the Divine", COMMON, "Advanced", cost=850,
                           menu=[shop["Attack"]["Attack_Speed"],
                           shop["Attack"]["Critical_Strike"]],
                           recipe=[recurve_bow, dagger],
                           capacities=dict(Passive=["Passive: This item does "
                           "not grant any attack speed while on cooldown. "
                           "Champion kills reduce the current cooldown by "
                           "50%."], Active=["Unique: You gain 100% attack "
                           "speed and 100% critical strike for 3 seconds or "
                           "3 critical strikes - 60 seconds cooldown."]),
                           attack_speed=0.45)
sword_of_the_occult = Item("Sword of the Occult", SR, "Advanced", cost=800,
                           menu=[shop["Attack"]["Damage"]],
                           recipe=[long_sword],
                           capacities=dict(Passive=["Unique: Your champion "
                           "gains +5 damage per stack, receiving 2 stacks for "
                           "a kill or 1 stack for an assist. This effect can "
                           "stack 20 times ; you lose a third of your stacks "
                           "if you die. At 20 stacks, your champion gains "
                           "+15% movement speed."]), attack_damage=10)
tear_of_the_goddess = Item("Tear of the Goddess", SR + TT + HA, "Advanced",
                           cost=120, menu=[shop["Magic"]["Mana"],
                           shop["Magic"]["Mana_Regen"]], recipe=[faerie_charm,
                           sapphire_crystal],
                           capacities=dict(Passive=["Unique - Mana Charge: "
                           "Grants +4 maximum Mana (max +750 Mana) for each "
                           "spell cast and Mana expenditure (occurs up to 2 "
                           "times every 8 seconds)."]), mana=250,
                           mana_regeneration=7)
thornmail = Item("Thornmail", SR + CS + HA, "Advanced", cost=1180,
                 menu=[shop["Defense"]["Armor"]], recipe=[cloth_armor,
                 chain_vest], capacities=dict(Passive=["Unique: On being hit "
                 "by basic attacks, returns 30% of damage, before any "
                 "reductions such as armor, as magic damage."]), armor=100)
tiamat = Item("Tiamat", COMMON, "Advanced", cost=265,
              menu=[shop["Attack"]["Damage"], shop["Defense"]["Health_Regen"]],
              recipe=[pickaxe, long_sword, rejuvenation_bead,
              rejuvenation_bead], capacities=dict(Passive=["Melee Only",
              "Unique - Cleave: Your attacks deal physical damage up to 60% "
              "of your Attack Damage to units around your target (185 range), "
              "decaying down to 20% near the edge (385 range)."],
              Active=["Unique - Crescent: Deals physical damage up to 100% of "
              "your Attack Damage to units around you, decaying down to 60% "
              "near the edge (400 range). 10 seconds cooldown"]),
              attack_damage=40, health_regeneration=15)
vampiric_scepter= Item("Vampiric Scepter", COMMON, "Advanced", cost=400,
                       menu=[shop["Attack"]["Damage"],
                       shop["Attack"]["Life_Steal"]], recipe=[long_sword],
                       attack_damage=10, life_steal=0.1)
void_staff = Item("Void Staff", COMMON, "Advanced", cost=1000,
                  menu=[shop["Magic"]["Ability_Power"]],
                  recipe=[amplifying_tome, blasting_wand],
                  capacities=dict(Passive=["Unique: Magic damage ignores 35% "
                  "of the target's Magic Resist (applies before magic "
                  "penetration)"]), perc_magic_penetration=0.35,
                  ability_power=70)
warden_s_mail = Item("Warden's Mail", COMMON, "Advanced", cost=400,
                     menu=[shop["Defense"]["Armor"]], recipe=[cloth_armor,
                     cloth_armor], capacities=dict(Passive=["Unique - Cold "
                     "Steel: If you are hit by a basic attack, you slow the "
                     "attacker's attack speed by 15% for 1 second."]),
                     armor=50)
warmog_s_armor = Item("Warmog's Armor", SR, "Advanced", cost=995,
                      menu=[shop["Defense"]["Health"],
                      shop["Defense"]["Health_Regen"]], recipe=[giant_s_belt,
                      ruby_crystal, rejuvenation_bead, rejuvenation_bead],
                      capacities=dict(Passive=["Unique Passive: You gain "
                      "health regeneration equal to 1% of your maximum "
                      "health."]), health=1000)
wit_s_end = Item("Wit's End", COMMON, "Advanced", cost=700,
                 menu=[shop["Attack"]["Attack_Speed"],
                 shop["Defense"]["Magic_Resist"]], recipe=[recurve_bow,
                 null_magic_mantle, dagger],
                 capacities=dict(Passive=["Unique: Basic attacks deal 42 "
                 "bonus magic damage on hit.", "Unique: Basic attacks increase"
                 " your magic resistance by 5 for 5 seconds and reduce the "
                 "target's magic resistance by 5 on hit (stacks up to 5 "
                 "times)."]), attack_speed=0.42, magic_resistance=25)
zeal = Item("Zeal", COMMON, "Advanced", cost=375,
            menu=[shop["Attack"]["Attack_Speed"],
            shop["Attack"]["Critical_Strike"], shop["Movement"]],
            recipe=[dagger, brawler_s_gloves], attack_speed=0.18,
            critical_strike_chance=0.1, perc_movement_speed=0.5)
augment_power = Item("Augment: Power", COMMON, "Advanced", cost=1000,
                     recipe=[the_hex_core], capacities=dict(Passive=["The "
                     "item now grants Viktor +3 ability power per level, "
                     "+220 health and +6 health regeneration per 5 seconds. "
                     "Also, Power Transfer increases Viktor's movement speed "
                     "by 30% for 3 seconds."]), health=220,
                     health_regeneration=6)
augment_gravity = Item("Augment: Gravity", COMMON, "Advanced", cost=1000,
                       recipe=[the_hex_core], capacities=dict(Passive=["The "
                       "item now grants Viktor +3 ability power per level, "
                       "+200 mana, +10% cooldown reduction and +5 mana "
                       "regeneration per 5 seconds. Also, Gravity Field's cast"
                       " range is increased by 30%."]), mana=200,
                       cooldown_reduction=0.1, mana_regeneration=5)
augment_death = Item("Augment: Death", COMMON, "Advanced", cost=1000,
                     recipe=[the_hex_core], capacities=dict(Passive=["The "
                     "item now grants Viktor +3 ability power per level and "
                     "+45 ability power. Also, Death Ray sets fire to enemies,"
                     " dealing 30% additional magic damage over 4 seconds."]),
                     ability_power=45)
head_of_kha_zix = Item("Head of Kha'Zix", COMMON, "Advanced",
                       recipe=[bonetooth_necklace],
                       capacities=dict(Passive=["+2 attack damage per level",
                       "+10 armor penetration", "+5% cooldown reduction",
                       "+25 movement speed", "Rengar's leap gains 150 bonus "
                       "range", "Thrill of the Hunt's duration is increased "
                       "by 3 seconds. Additionally, Rengar's next ability "
                       "used after activating Thrill of the Hunt generates "
                       "1 bonus Ferocity."]), flat_armor_penetration=10,
                       cooldown_reduction=0.05, flat_movement_speed=25)

# Legendary items

aegis_of_the_legion = Item("Aegis of the Legion", COMMON, "Legendary",
                           cost=375, menu=[shop["Defense"]["Armor"],
                           shop["Defense"]["Health"],
                           shop["Defense"]["Health_Regen"],
                           shop["Defense"]["Magic_Resist"]],
                           recipe=[emblem_of_valor, ruby_crystal,
                           null_magic_mantle], capacities=dict(Aura=["Unique "
                           "- Legion: Nearby allied champions gain +20 magic "
                           "resist and +10 health regen per 5 seconds (1100 "
                           "range)."]), health=200, armor=20)
archangel_s_staff = Item("Archangel's Staff", SR + TT + HA, "Legendary",
                         cost=1140, menu=[shop["Magic"]["Ability_Power"],
                         shop["Magic"]["Mana"], shop["Magic"]["Mana_Regen"]],
                         recipe=[tear_of_the_goddess, blasting_wand],
                         capacities=dict(Passive=["Unique Passive - Insight: "
                         "Gain ability power equal to 3% of your maximum "
                         "mana.", "Unique Passive - Mana Charge: Grants +8 "
                         "maximum Mana (max +750 Mana) for each spell cast "
                         "and Mana expenditure (occurs up to 2 times every 8 "
                         "seconds).", "Transforms into Seraph's Embrace at "
                         "+750 Mana."]), mana=250, ability_power=60,
                         mana_regeneration=10)
athene_s_unholy_grail = Item("Athene's Unholy Grail", COMMON, "Legendary",
                             cost=900, menu=[shop["Defense"]["Magic_Resist"],
                             shop["Magic"]["Ability_Power"],
                             shop["Magic"]["Mana_Regen"],
                             shop["Magic"]["Cooldown_Reduction"]],
                             recipe=[fiendish_codex, chalice_of_harmony],
                             capacities=dict(Passive=["Unique - Mana Font: "
                             "Increases your mana regeneration by 1% per 1% "
                             "mana you are missing.", "Unique: Restores 12% "
                             "of your max mana on kill or assist."]),
                             ability_power=60, magic_resistance=40,
                             mana_regeneration=15, cooldown_reduction=0.2)
atma_s_impaler = Item("Atma's Impaler", COMMON, "Legendary", cost=780,
                      menu=[shop["Attack"]["Critical_Strike"],
                      shop["Defense"]["Armor"]], recipe=[chain_vest,
                      avarice_blade], capacities=dict(Passive=["Unique: You "
                      "gain attack damage equal to 1.5% of your maximum "
                      "health."]), armor=45, critical_strike_chance=0.15)
banner_of_command = Item("Banner of Command", COMMON, "Legendary", cost=890,
                         menu=[shop["Defense"]["Armor"],
                         shop["Defense"]["Health_Regen"],
                         shop["Magic"]["Ability_Power"]],
                         recipe=[fiendish_codex, emblem_of_valor],
                         capacities=dict(Aura=["Unique - Valor: Nearby allies "
                         "gain 10 health regen per 5 seconds and nearby "
                         "allied minions have 15% increased attack damage and "
                         "ability power."], Active=["Unique - Promote: "
                         "Transforms a nearby siege minion to a more "
                         "powerful unit. You gain all the gold this unit "
                         "earns. 180 seconds cooldown."]), ability_power=40,
                         armor=30, cooldown_reduction=0.1)
banshee_s_veil = Item("Banshee's Veil", SR + TT + HA, "Legendary", cost=875,
                      menu=[shop["Defense"]["Health"],
                      shop["Defense"]["Magic_Resist"]], recipe=[ruby_crystal,
                      spectre_s_cowl], capacities=dict(Passive=["Unique: "
                      "Grants a spell shield that blocks the next enemy "
                      "ability. This shield refreshes after no damage is taken"
                      " from enemy champions for 25 seconds.", "Unique: Grants"
                      " 45 health regen for up to 10 seconds after taking "
                      "damage from an enemy champion or when the spell shield "
                      "breaks."]), health=450, magic_resistance=55)
bilgewater_cutlass = Item("Bilgewater Cutlass", COMMON, "Legendary", cost=200,
                          menu=[shop["Attack"]["Damage"],
                          shop["Attack"]["Life_Steal"]], recipe=[long_sword,
                          vampiric_scepter], capacities=dict(Active=["Unique "
                          "Active: Deals 100 magic damage and slows the target"
                          " enemy champion's movement speed by 25% for 2 "
                          "seconds. 90 seconds cooldown. 450 range."]),
                          attack_damage=25, life_steal=0.12)
the_black_cleaver = Item("The Black Cleaver", COMMON, "Legendary", cost=1188,
                         menu=[shop["Attack"]["Damage"],
                         shop["Magic"]["Cooldown_Reduction"],
                         shop["Defense"]["Health"]], recipe=[the_brutalizer,
                         ruby_crystal], capacities=dict(Passive=["Unique: +10 "
                         "armor penetration", "Dealing physical damage to an "
                         "enemy champion reduces their armor by 5% for 4 "
                         "seconds. This effect stacks up to 5 times."]),
                         health=200, attack_damage=50, cooldown_reduction=0.1,
                         flat_armor_penetration=10)
blackfire_torch = Item("Blackfire Torch", TT + CS, "Legendary", cost=720,
                       menu=[shop["Defense"]["Health"],
                       shop["Magic"]["Ability_Power"],
                       shop["Magic"]["Cooldown_Reduction"]],
                       recipe=[blasting_wand, fiendish_codex],
                       capacities=dict(Active=["Unique: Deals 20% of target "
                       "champion's maximum Health in magic damage over 6 "
                       "seconds and increases all subsequent magic damage "
                       "taken by target by 20% (60 seconds cooldown)"]),
                       ability_power=80, cooldown_reduction=0.1)
the_bloodthirster = Item("The Bloodthirster", SR, "Legendary", cost=850,
                         menu=[shop["Attack"]["Damage"],
                         shop["Attack"]["Life_Steal"]], recipe=[b_f_sword,
                         vampiric_scepter], capacities=dict(Passive=["Gains "
                         "1 stack per kill, up to a maximum of 30. Each stack "
                         "grants +1 attack damage and +0.2% life steal (max: "
                         "+30 attack damage and +6% life steal). Half of the "
                         "current stacks are lost upon death."]),
                         attack_damage=70, life_steal=0.12)
deathfire_grasp = Item("Deathfire Grasp", SR + HA, "Legendary", cost=680,
                       menu=[shop["Magic"]["Ability_Power"],
                       shop["Magic"]["Cooldown_Reduction"]],
                       recipe=[needlessly_large_rod, fiendish_codex],
                       capacities=dict(Active=["Unique: Deals 15% of target "
                       "champion's maximum health in magic damage and "
                       "applies the debuff, Doom. Doom amplifies all magic "
                       "damage that champion takes by 20% for 4 seconds. 60 "
                       "seconds cooldown (750 range)."]), ability_power=120,
                       cooldown_reduction=0.1)
eleisa_s_miracle = Item("Eleisa's Miracle", COMMON, "Legendary", cost=400,
                        menu=[shop["Defense"]["Health_Regen"],
                        shop["Magic"]["Mana_Regen"]],
                        recipe=[philosopher_s_stone],
                        capacities=dict(Passive=["Unique Passive - Aid: Your "
                        "Summoner Heal, Clarity and Clairvoyance cooldowns are"
                        " reduced by 25", "Unique Passive - Eleisa's Blessing:"
                        " If you gain 3 levels with this item, you gain all "
                        "the effects permanently and this item is consumed."]),
                        health_regeneration=10, mana_regeneration=15)
entropy = Item("Entropy", CS + HA, "Legendary", cost=600,
               menu=[shop["Attack"]["Damage"], shop["Defense"]["Health"]],
               recipe=[phage, b_f_sword], capacities=dict(Passive=["Unique "
               "Passive - Rage: Basic attacks grant 20 movement speed for 2 "
               "seconds on hit. Minion, monster and champion kills grant 60 "
               "movement speed for 2 seconds."], Active=["Unique: For 5 "
               "seconds, your attacks reduce your target's movement speed by "
               "30% and deal 80 true damage over 2.5 seconds. 60 seconds "
               "cooldown."]), attack_damage=70, health=275)
executuoner_s_calling = Item("Executioner's Calling", COMMON, "Legendary",
                             cost=700, menu=[shop["Attack"]["Critical_Strike"],
                             shop["Attack"]["Damage"]], recipe=[avarice_blade,
                             long_sword], capacities=dict(Passive=["Unique: "
                             "Your basic attacks inflict Grievous Wounds on "
                             "enemy champions for 1.5 seconds."]),
                             attack_damage=25, critical_strike_chance=0.2)
frozen_heart = Item("Frozen Heart", COMMON, "Legendary", cost=550,
                    menu=[shop["Defense"]["Armor"],
                    shop["Magic"]["Cooldown_Reduction"],
                    shop["Magic"]["Mana"]], recipe=[warden_s_mail,
                    glacial_shroud], capacities=dict(Passive=["Unique: "
                    "Reduces the attack speed of nearby enemies by 20%. (700 "
                    "range)"]), armor=95, mana=400, cooldown_reduction=0.2)
grez_s_spectral_lantern = Item("Grez's Spectral Lantern", TT + CS + HA,
                               "Legendary", cost=150,
                               menu=[shop["Attack"]["Damage"],
                               shop["Defense"]["Armor"]], recipe=[cloth_armor,
                               vampiric_scepter],
                               capacities=dict(Passive=["Unique: Your basic "
                               "attacks against minions have a 20% chance to "
                               "deal 200 bonus magic damage."],
                               Active=["Unique: A stealth-detecting mist "
                               "grants vision in the target area for 10 "
                               "seconds. 60 seconds cooldown (1000 range, "
                               "375 AOE estimate)."]), attack_damage=20,
                               armor=20, life_steal=0.12)
hextech_sweeper = Item("Hextech Sweeper", TT + CS + HA, "Legendary", cost=200,
                       menu=[shop["Magic"]["Ability_Power"],
                       shop["Movement"]], recipe=[amplifying_tome,
                       amplifying_tome, kindlegem],
                       capacities=dict(Passive=["Unique: +10% cooldown "
                       "reduction", "Unique: +10% movement speed",
                       "Unique - Trap Detection: Nearby stealthed enemy "
                       "traps are revealed"], Active=["Unique: Covers an area "
                       "with stealth-detecting mist for 10 seconds, granting "
                       "vision of units which pass through it for 6 seconds. "
                       "60 seconds cooldown (1000 range, 375 AOE estimate)."]),
                       cooldown_reduction=0.1, perc_movement_speed=0.1,
                       ability_power=50, health=300)
iceborn_gauntlet = Item("Iceborn Gauntlet", COMMON, "Legendary", cost=700,
                        menu=[shop["Defense"]["Armor"],
                        shop["Magic"]["Ability_Power"],
                        shop["Magic"]["Cooldown_Reduction"],
                        shop["Magic"]["Mana"]], recipe=[sheen, glacial_shroud],
                        capacities=dict(Passive=["Unique Passive - Spellblade:"
                        " After using an ability, your next basic attack deals"
                        " bonus physical damage equal to 125% of your base "
                        "attack damage to surrounding enemies and creates a "
                        "field for 2 seconds that slows enemies inside by 30% "
                        "(2 seconds cooldown)."]), ability_power=30, mana=500,
                        armor=70, cooldown_reduction=0.1)
liandry_s_torment = Item("Liandry's Torment", COMMON, "Legendary", cost=980,
                         menu=[shop["Defense"]["Health"],
                         shop["Magic"]["Ability_Power"]],
                         recipe=[haunting_guise, amplifying_tome],
                         capacities=dict(Passive=["Unique Passive - Eyes of "
                         "Pain: +15 magic penetration", "Unique Passive: "
                         "Dealing spell damage applies a damage-over-time "
                         "effect that deals bonus magic damage equal to 2% "
                         "of the target's current Health per second for 3 "
                         "seconds. This bonus damage is doubled against "
                         "movement-impaired units and capped at 100 damage "
                         "per second vs monsters."]),
                         flat_magic_penetration=15, ability_power=50,
                         health=300)
lich_bane = Item("Lich Bane", COMMON, "Legendary", cost=940,
                 menu=[shop["Magic"]["Ability_Power"], shop["Magic"]["Mana"],
                 shop["Movement"]], recipe=[sheen, blasting_wand],
                 capacities=dict(Passive=["Unique - Spellblade: After using "
                 "an ability, your next basic attack deals bonus magic "
                 "damage equal to 50 + 75% of your ability power. 2 seconds "
                 "cooldown."]), ability_power=80, mana=250,
                 perc_movement_speed=0.05)
manamune = Item("Manamune", SR + TT + HA, "Legendary", cost=1000,
                menu=[shop["Attack"]["Damage"], shop["Magic"]["Mana"],
                shop["Magic"]["Mana_Regen"]], recipe=[tear_of_the_goddess,
                long_sword], capacities=dict(Passive=["Unique Passive - Awe: "
                "Gain attack damage equal to 2% of your maximum mana.",
                "Unique Passive - Mana Charge: Grants +4 maximum Mana (max "
                "+750 Mana) for each basic attack, spell cast and Mana "
                "expenditure (occurs up to 2 times every 8 seconds).",
                "Transforms into Muramana at +750 Mana."]),
                mana=250, attack_damage=20, mana_regeneration=7)
maw_of_malmortius = Item("Maw of Malmortius", COMMON, "Legendary", cost=975,
                         menu=[shop["Defense"]["Magic_Resist"],
                         shop["Attack"]["Damage"]], recipe=[hexdrinker,
                         pickaxe], capacities=dict(Passive=["Unique: Grants "
                         "+1 attack damage for every 2% of missing health, "
                         "capped at 35 Attack Damage.", "Unique - Lifeline: "
                         "Upon taking magic damage that would reduce health "
                         "below 30%, grants a shield that absorbs 400 magic "
                         "damage for 5 seconds (90 seconds cooldown)."]),
                         attack_damage=60, magic_resistance=40)
mercurial_scimitar = Item("Mercurial Scimitar", SR, "Legendary", cost=600,
                          menu=[shop["Defense"]["Magic_Resist"],
                          shop["Attack"]["Damage"], shop["Movement"]],
                          capacities=dict(Active=["Unique Active - "
                          "Quicksilver: Removes all debuffs from your "
                          "champion. Melee champions also gain +50% movement "
                          "speed for 1 second. 90 seconds cooldown."]),
                          attack_damage=60, magic_resistance=45)
mikael_s_crucible = Item("Mikael's Crucible", SR, "Legendary", cost=920,
                         menu=[shop["Defense"]["Health_Regen"],
                         shop["Defense"]["Magic_Resist"],
                         shop["Magic"]["Mana_Regen"]],
                         recipe=[philosopher_s_stone, chalice_of_harmony],
                         capacities=dict(Passive=["Unique Passive - Mana Font:"
                         " Increases your Mana Regen by 1% per 1% Mana you "
                         "are missing."], Active=["Unique Active: Removes all "
                         "stuns, roots, taunts, fears, silences and slows on "
                         "an allied champion and heals for 150 + 10% of the "
                         "target's maximum health (180 seconds cooldown)."]),
                         health_regeneration=7, magic_resistance=40,
                         mana_regeneration=18)
morellonomicon = Item("Morellonomicon", COMMON, "Legendary", cost=435,
                      menu=[shop["Magic"]["Ability_Power"],
                      shop["Magic"]["Cooldown_Reduction"],
                      shop["Magic"]["Mana_Regen"]], recipe=[fiendish_codex,
                      kage_s_lucky_pick, faerie_charm],
                      capacities=dict(Passive=["Unique: Dealing magic damage "
                      "to an enemy champion below 40% health inflicts "
                      "Grevious Wounds to them for 4 seconds."]),
                      ability_power=75, mana_regeneration=12,
                      cooldown_reduction=0.2)
nashor_s_tooth = Item("Nashor's Tooth", COMMON, "Legendary", cost=850,
                      menu=[shop["Attack"]["Attack_Speed"],
                      shop["Magic"]["Ability_Power"],
                      shop["Magic"]["Cooldown_Reduction"]], recipe=[stinger,
                      fiendish_codex], capacities=dict(Passive=["Unique: +20% "
                      "Cooldown Reduction", "Unique: Basic attacks deal 15 + "
                      "15% AP bonus magic damage on hit"]),
                      cooldown_reduction=0.2, attack_speed=0.5,
                      ability_power=60)
odyn_s_veil = Item("Odyn's Veil", CS, "Legendary", cost=600,
                   menu=[shop["Defense"]["Health"],
                   shop["Defense"]["Magic_Resist"], shop["Magic"]["Mana"]],
                   recipe=[negatron_cloak, catalyst_the_protector],
                   capacities=dict(Passive=["Unique: Reduces and stores 10% of"
                   " the magic damage dealt to your champion."],
                   Active=["Unique: Deals 200 + (stored magic)[max: 400] to "
                   "nearby enemy units. 90 second cooldown (525 range "
                   "estimate)."]), health=350, magic_resistance=50, mana=350)
ohmwrecker = Item("Ohmwrecker", SR + TT, "Legendary", cost=800,
                  menu=[shop["Defense"]["Health"],
                  shop["Magic"]["Ability_Power"]], recipe=[ruby_crystal,
                  blasting_wand, philosopher_s_stone],
                  capacities=dict(Active=["Unique Active: Prevents the "
                  "closest enemy tower from attacking for 2.5 seconds (120 "
                  "seconds cooldown). This effect cannot be used against the "
                  "same tower more than once every 7.5 seconds."]),
                  health=350, ability_power=50, health_regeneration=15,
                  mana_regeneration=15)
phantom_dancer = Item("Phantom Dancer", COMMON, "Legendary", cost=495,
                      menu=[shop["Attack"]["Attack_Speed"],
                      shop["Attack"]["Critical_Strike"], shop["Movement"]],
                      recipe=[cloak_of_agility, zeal, dagger],
                      capacities=dict(Passive=["Unique: Your champion ignores "
                      "unit collision."]), attack_speed=0.5,
                      critical_strike_chance=0.3, perc_movement_speed=0.05)
randuin_s_omen = Item("Randuin's Omen", COMMON, "Legendary", cost=1000,
                      menu=[shop["Defense"]["Armor"],
                      shop["Defense"]["Health"]], recipe=[giant_s_belt,
                      warden_s_mail], capacities=dict(Passive=["Unique Passive"
                      " - Cold Steel: When hit by basic attacks, reduces the "
                      "attacker's attack speed by 15% and movement speed by "
                      "10% for 1 second."], Active=["Unique Active: Slows the "
                      "movement speed of nearby enemy units by 35% for 2 ("
                      "+0.5% armor)(+0.5% magic resistance) seconds. 60 "
                      "seconds cooldown (500 range)."]), health=500, armor=70)
ravenous_hydra = Item("Ravenous Hydra", COMMON, "Legendary", cost=600,
                      menu=[shop["Attack"]["Damage"],
                      shop["Attack"]["Life_Steal"],
                      shop["Defense"]["Health_Regen"]], recipe=[tiamat,
                      vampiric_scepter], capacities=dict(Passive=["Melee only",
                      "Passive: Damage dealt by this item benefits from life "
                      "steal.", "Unique Passive - Cleave: Your attacks deal up"
                      " to 60% of your Attack Damage to units around your "
                      "target as physical damage (185 range), decaying down to"
                      " 20% near the edge (385 range)."], Active=["Unique "
                      "Active - Crescent: Deals up to 100% of your Attack "
                      "Damage to units around you as physical damage, "
                      "decaying down to 60% near the edge. 10 seconds "
                      "cooldown (400 range)."]), attack_damage=75,
                      health_regeneration=15, life_steal=0.12)
rod_of_ages = Item("Rod of Ages", SR + TT + HA, "Legendary", cost=740,
                   menu=[shop["Defense"]["Health"],
                   shop["Magic"]["Ability_Power"], shop["Magic"]["Mana"]],
                   recipe=[catalyst_the_protector, blasting_wand],
                   capacities=dict(Passive=["Passive: This item gains 20 "
                   "health, 20 mana and 2 ability power every minute, up to "
                   "10 times.", "Unique Passive: Valor's Reward: On leveling "
                   "up, restores 150 health and 200 mana over 8 seconds."]),
                   health=450, mana=450, ability_power=60)
ruby_sightstone = Item("Ruby Sightstone", SR, "Legendary", cost=125,
                       menu=[shop["Defense"]["Health"], shop["Consumables"]],
                       recipe=[sightstone, ruby_crystal],
                       capacities=dict(Passive=["Unique Passive: Ward "
                       "Refresh - Starts with 5 charges and refills each time "
                       "you visit the shop."], Active=["Unique Active: Ghost "
                       "Ward - Consumes a charge to place an invisible Ghost "
                       "Ward that reveals the surrounding area for 3 minutes. "
                       "You may have a maximum of 3 wards placed from this "
                       "item at once. 1 second cooldown."]), health=360)
sanguine_blade = Item("Sanguine Blade", TT + CS + HA, "Legendary", cost=500,
                      menu=[shop["Attack"]["Damage"],
                      shop["Attack"]["Life_Steal"]], recipe=[pickaxe,
                      vampiric_scepter], capacities=dict(Passive=["Unique: "
                      "Your basic attacks grant +6 attack damage and +1% "
                      "life steal for 4 seconds (maximum 5 stacks)."]),
                      attack_damage=50, life_steal=0.15)
shard_of_true_ice = Item("Shard of True Ice", SR, "Legendary", cost=535,
                         menu=[shop["Magic"]["Ability_Power"],
                         shop["Magic"]["Mana_Regen"]],
                         recipe=[kage_s_lucky_pick, mana_manipulator],
                         capacities=dict(Aura=["Unique Aura: Mana Warp - "
                         "Nearby allied champions gain 5 mana regen per 5 "
                         "seconds."], Passive=["Unique passive: Lucky Shadow "
                         "- Gain an additional 4 gold every 10 seconds."],
                         Active=["Unique Active: Surrounds an ally with a "
                         "blizzard for 4 seconds that slows nearby enemy "
                         "movement speed by 30%. 60 seconds cooldown."]),
                         ability_power=45)
shurelya_s_reverie = Item("Shurelya's Reverie", COMMON, "Legendary", cost=550,
                          menu=[shop["Defense"]["Health"],
                          shop["Defense"]["Health_Regen"],
                          shop["Magic"]["Cooldown_Reduction"],
                          shop["Magic"]["Mana_Regen"], shop["Movement"]],
                          recipe=[kindlegem, philosopher_s_stone],
                          capacities=dict(Passive=["+10% cooldown reduction"],
                          Active=["Unique: Nearby allies gain 40% movement "
                          "speed for 3 seconds (60 seconds cooldown)(600 "
                          "range)."]), cooldown_reduction=0.1, health=250,
                          health_regeneration=10, mana_regeneration=10)
spirit_of_the_ancient_golem = Item("Spirit of the Ancient Golem", SR + TT + HA,
                                   "Legendary", cost=450,
                                   menu=[shop["Defense"]["Health"],
                                   shop["Defense"]["Health_Regen"],
                                   shop["Defense"]["Tenacity"],
                                   shop["Magic"]["Mana_Regen"],
                                   shop["Magic"]["Cooldown_Reduction"]],
                                   recipe=[spirit_stone, kindlegem],
                                   capacities=dict(Passive=["Unique Passive - "
                                   "Butcher: Damage dealt to monsters "
                                   "increased by 30%.", "Unique Passive - "
                                   "Tenacity: The duration of stuns, slows, "
                                   "taunts, fears, silences, blinds and "
                                   "immobilizes are reduced by 35%."]),
                                   health=500, health_regeneration=14,
                                   mana_regeneration=7, cooldown_reduction=0.1)
spirit_of_the_elder_lizard = Item("Spirit of the Elder Lizard", SR + TT + HA,
                                  "Legendary", cost=500,
                                  menu=[shop["Attack"]["Damage"],
                                  shop["Defense"]["Health_Regen"],
                                  shop["Magic"]["Mana_Regen"]],
                                  recipe=[spirit_stone, long_sword,
                                  long_sword],
                                  capacities=dict(Passive=["Unique Passive - "
                                  "Butcher: Damage dealt to monsters increased"
                                  " by 30%.", "Unique Passive - Incinerate: "
                                  "Basic attacks and spells that do not "
                                  "inflict damage-over-time deal 4 + (2 * "
                                  "level) bonus true damage over 3 seconds on "
                                  "hit."]), attack_damage=35,
                                  health_regeneration=14, mana_regeneration=7,
                                  cooldown_reduction=0.1)
spirit_of_the_spectral_wraith = Item("Spirit of the Spectral Wraith", SR + TT +
                                     HA, "Legendary", cost=100,
                                     menu=[shop["Magic"]["Ability_Power"],
                                     shop["Magic"]["Cooldown_Reduction"],
                                     shop["Magic"]["Spell_Vamp"],
                                     shop["Magic"]["Mana_Regen"]],
                                     recipe=[spirit_stone, hextech_revolver],
                                     capacities=dict(Passive=["Unique Passive:"
                                     " +20% spell vamp", "Unique Passive - "
                                     "Butcher: Damage dealt to monsters "
                                     "increased by 30%.", "Unique Passive: "
                                     "Reduces the cooldown on Smite by 20%."]),
                                     spell_vamp=0.2, ability_power=40,
                                     mana_regeneration=10,
                                     cooldown_reduction=0.1)
spirit_visage = Item("Spirit Visage", COMMON, "Legendary", cost=500,
                     menu=[shop["Defense"]["Health"],
                     shop["Defense"]["Magic_Resist"],
                     shop["Magic"]["Cooldown_Reduction"]], recipe=[kindlegem,
                     spectre_s_cowl], capacities=dict(Passive=["Unique: "
                     "Increases your self-healing, health regen, life steal "
                     "and spell vamp by 20%"]), health=400,
                     magic_resistance=55, cooldown_reduction=0.2,
                     health_regeneration=20)
statikk_shiv = Item("Statikk Shiv", COMMON, "Legendary", cost=525,
                    menu=[shop["Attack"]["Critical_Strike"],
                    shop["Attack"]["Attack_Speed"], shop["Movement"]],
                    recipe=[zeal, avarice_blade],
                    capacities=dict(Passive=["Unique Passive: Moving and "
                    "attacking builds Static Charges. At 100 charges, your "
                    "next attack expends the charges to deal 100 magic "
                    "damage to up to 4 targets. This damage can critically "
                    "strike."]), attack_speed=0.4, critical_strike_chance=0.2,
                    perc_movement_speed=0.06)
trinity_force = Item("Trinity Force", COMMON, "Legendary", cost=3,
                     menu=[shop["Attack"]["Critical_Strike"],
                     shop["Attack"]["Attack_Speed"],
                     shop["Movement"]], recipe=[zeal, sheen, phage],
                     capacities=dict(Passive=["Unique Passive - Rage: Basic "
                     "attacks grant 20 movement speed for 2 seconds on hit. "
                     "Minion, monster and champion kills grant 60 movement "
                     "speed for 2 seconds. The movement speed bonus is halved "
                     "for ranged champions.", "Unique Passive - Spellblade: "
                     "After using an ability, your next basic attack deals "
                     "bonus damage equal to 200% of your base attack damage "
                     "as physical damage (2 second cooldown)."]),
                     ability_power=30, attack_damage=30, attack_speed=0.3,
                     critical_strike_chance=0.1, health=250, mana=200,
                     perc_movement_speed=0.08)
twin_shadows = Item("Twin Shadows", SR + TT, "Legendary", cost=735,
                    menu=[shop["Defense"]["Magic_Resist"],
                    shop["Magic"]["Ability_Power"], shop["Movement"]],
                    recipe=[kage_s_lucky_pick, null_magic_mantle],
                    capacities=dict(Active=["Unique Active - Hunt: Summons "
                    "2 invulnerable ghosts for 6 seconds to seek the 2 nearest"
                    " enemy champions. If they touch an enemy champion, they "
                    "slow their movement speed by 40% and reveal them for 2.5 "
                    "seconds. 120 seconds cooldown."]), ability_power=40,
                    magic_resistance=40, perc_movement_speed=0.06)
will_of_the_ancients = Item("Will of the Ancients", COMMON, "Legendary",
                            cost=585, menu=[shop["Magic"]["Ability_Power"]],
                            recipe=[hextech_revolver, kage_s_lucky_pick],
                            capacities=dict(Aura=["Unique: Nearby allied "
                            "champions gain +30 ability power and +20% spell "
                            "vamp (1100 range)."]), ability_power=50)
wriggle_s_lantern = Item("Wriggle's Lantern", SR, "Legendary", cost=500,
                         menu=[shop["Attack"]["Damage"],
                         shop["Attack"]["Life_Steal"],
                         shop["Defense"]["Armor"]], recipe=[madred_s_razors,
                         vampiric_scepter], capacities=dict(Passive=["Unique "
                         "Passive - Maim: Basic attacks deal 100 bonus magic "
                         "damage to monsters on hit."], Active=["Unique: "
                         "Places a Sight Ward at target location that lasts "
                         "for 90 seconds. 90 seconds cooldown (600 cast "
                         "range)."]), armor=25, attack_damage=25,
                         life_steal=0.15)
wooglet_s_witchcap = Item("Wooglet's Witchcap", TT + CS, "Legendary",
                          cost=1045, menu=[shop["Magic"]["Ability_Power"],
                          shop["Defense"]["Armor"]], recipe=[seeker_s_armguard,
                          blasting_wand, amplifying_tome],
                          capacities=dict(Passive=["Unique: +25% ability "
                          "power"], Active=["Unique: Places your champion into"
                          " stasis for 2.5 seconds, rendering you invulnerable"
                          " and untargetable but unable to take any action. 90"
                          " seconds cooldown."]), ability_power=100, armor=45)
youmuu_s_ghostblade = Item("Youmuu's Ghostblade", COMMON, "Legendary",
                           cost=563, menu=[shop["Attack"]["Attack_Speed"],
                           shop["Attack"]["Critical_Strike"],
                           shop["Attack"]["Damage"],
                           shop["Magic"]["Cooldown_Reduction"],
                           shop["Movement"]], recipe=[avarice_blade,
                           the_brutalizer], capacities=dict(Passive=["Unique: "
                           "+20 armor penetration"], Active=["Unique: Gain "
                           "+40% attack speed and +20% movement speed for 6 "
                           "seconds (4 seconds for ranged champions). 45 "
                           "seconds cooldown."]), flat_armor_penetration=20,
                           attack_damage=30, critical_strike_chance=0.15,
                           cooldown_reduction=0.1)
zeke_s_herald = Item("Zeke's Herald", COMMON, "Legendary", cost=900,
                     menu=[shop["Attack"]["Damage"],
                     shop["Attack"]["Life_Steal"],
                     shop["Defense"]["Health"],
                     shop["Magic"]["Cooldown_Reduction"]],
                     recipe=[kindlegem, vampiric_scepter],
                     capacities=dict(Aura=["Unique: Nearby allied champions "
                     "gain +20 attack damage and +10% life steal (1100 "
                     "range)."]), health=250, cooldown_reduction=0.2)
zephyr = Item("Zephyr", SR, "Legendary", cost=725,
              menu=[shop["Attack"]["Damage"], shop["Attack"]["Attack_Speed"],
              shop["Magic"]["Cooldown_Reduction"], shop["Movement"]],
              recipe=[stinger, pickaxe], capacities=dict(Passive=["Unique "
              "Passive - Tenacity: The duration of stuns, slows, taunts, fears"
              ", silences, blinds and immobilizes are reduced by 35%."]),
              attack_damage=25, attack_speed=0.5, perc_movement_speed=0.1,
              cooldown_reduction=0.1)
zhonya_s_hourglass = Item("Zhonya's Hourglass", SR + HA, "Legendary", cost=500,
                          menu=[shop["Magic"]["Ability_Power"],
                          shop["Defense"]["Armor"]], recipe=[seeker_s_armguard,
                          needlessly_large_rod],
                          capacities=dict(Active=["Unique Active - Stasis: "
                          "Champion becomes invulnerable and untargetable for "
                          "2.5 seconds, but is unable to move, attack, cast "
                          "spells, or use items during this time (90 seconds "
                          "cooldown)."]), ability_power=120, armor=50)

# Mythical items

blade_of_the_ruined_king = Item("Blade of the Ruined King", COMMON, "Mythical",
                                cost=1000, menu=[shop["Attack"]["Damage"],
                                shop["Attack"]["Attack_Speed"],
                                shop["Attack"]["Life_Steal"]],
                                recipe=[bilgewater_cutlass, dagger, dagger],
                                capacities=dict(Passive=["Unique: Your attacks"
                                " deal 5% of the target's current health in "
                                "physical damage (60 max vs minions and "
                                "monsters)."], Active=["Unique: Drains target "
                                "champion, dealing 15% of the champion's "
                                "maximum health in physical damage and healing"
                                " you for the damage dealt. Additionally you "
                                "steal 30% of their movement speed for 3 "
                                "seconds. 90 seconds cooldown (450 range)."]),
                                attack_damage=25, life_steal=0.15,
                                attack_speed=0.4)
hextech_gunblade = Item("Hextech Gunblade", COMMON, "Mythical", cost=800,
                        menu=[shop["Attack"]["Damage"],
                        shop["Attack"]["Life_Steal"],
                        shop["Magic"]["Ability_Power"]],
                        recipe=[hextech_revolver, bilgewater_cutlass],
                        capacities=dict(Passive=["Unique: +20% spell vamp",
                        "Unique - Reload: Your basic attacks and single target"
                        " spells against champions reduce the cooldown of this"
                        " item by 3 seconds."], Active=["Unique Active: Deals "
                        "150 + 40% of your ability power as magic damage and "
                        "slows the target champion's movement speed by 40% for"
                        " 2 seconds. 60 seconds cooldown (700 range)."]),
                        attack_damage=45, ability_power=65, life_steal=0.12)
locket_of_the_iron_solari = Item("Locket of the Iron Solari", COMMON,
                                 "Mythical", cost=600,
                                 menu=[shop["Defense"]["Health"],
                                 shop["Defense"]["Armor"],
                                 shop["Defense"]["Health_Regen"],
                                 shop["Defense"]["Magic_Resist"],
                                 shop["Magic"]["Cooldown_Reduction"]],
                                 recipe=[aegis_of_the_legion],
                                 capacities=dict(Aura=["Unique - Legion: "
                                 "Nearby allied champions gain +20 magic "
                                 "resist and +10 health regen per 5 seconds "
                                 "(1100 range)."], Active=["Unique: Shield "
                                 "yourself and nearby allied champions for 5 "
                                 "seconds, absorbing up to 50 (+10 per level) "
                                 "damage. 60 second cooldown (600 range)."]),
                                 health=300, armor=20, cooldown_reduction=0.1)
muramana = Item("Muramana", SR + TT + HA, "Mythical", recipe=[manamune],
                capacities=dict(Passive=["Unique Passive - Awe: Gain attack "
                "damage equal to 2% of your maximum mana."], Active=["Toggle: "
                "Single target spells and attacks (on hit) consume 3% of "
                "current Mana to deal bonus physical damage equal to twice the"
                " amount of Mana consumed."]), mana=1000, attack_damage=20,
                mana_regeneration=7)
seraph_s_embrace = Item("Seraph's Embrace", COMMON, "Mythical",
                        recipe=[archangel_s_staff],
                        capacities=dict(Passive=["Unique Passive - Insight: "
                        "Gain ability power equal to 3% of your maximum "
                        "mana."], Active=["Unique Active - Mana Shield: Drains"
                        " 20% of your current mana to shield yourself for an "
                        "equal amount plus 150 for 3 seconds (120 seconds "
                        "cooldown)."]), mana=1000, ability_power=60,
                        mana_regeneration=10)
the_lightbringer = Item("The Lightbringer", TT + CS + HA, "Mythical", cost=300,
                        menu=[shop["Defense"]["Armor"],
                        shop["Attack"]["Damage"],
                        shop["Attack"]["Life_Steal"]], recipe=[pickaxe,
                        grez_s_spectral_lantern],
                        capacities=dict(Passive=["Unique - Vanquish: Basic "
                        "attacks have a 20% chance to deal 100 bonus magic "
                        "damage. Effect doubled for non-champions.", "Unique "
                        "- Trap Detection: Nearby stealthed enemy traps are "
                        "revealed."], Active=["Unique: Covers a target area "
                        "in a stealth-detecting mist that grants vision for "
                        "10 seconds. 60 seconds cooldown."]), attack_damage=50,
                        armor=20, life_steal=0.12)
