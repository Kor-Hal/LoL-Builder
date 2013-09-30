# -*-coding:utf-8 -*
from packages.basics.rune import Rune

# Defining the runes
# Variable names :
#   1st part = l, n or g (Lesser, Normal or Greater)
#   2nd part = mark, seal, glyph or quintessence
#   3rd part = rune's name (can be shortened, like "ap" for "ability power",
#              as long as it is easily understandable)

# Ability Power
l_mark_ap = Rune("Lesser", "Mark", "Ability Power", "Secondary", 30, None,
            ability_power=0.33)
n_mark_ap = Rune("Normal", "Mark", "Ability Power", "Secondary", 165, None,
            ability_power=0.46)
g_mark_ap = Rune("Greater", "Mark", "Ability Power", "Secondary", 410, None,
            ability_power=0.59)
l_seal_ap = Rune("Lesser", "Seal", "Ability Power", "Secondary", 30, None,
            ability_power=0.33)
n_seal_ap = Rune("Normal", "Seal", "Ability Power", "Secondary", 165, None,
            ability_power=0.46)
g_seal_ap = Rune("Greater", "Seal", "Ability Power", "Secondary", 410, None,
            ability_power=0.59)
l_glyph_ap = Rune("Lesser", "Glyph", "Ability Power", "Primary", 30, None,
             ability_power=0.66)
n_glyph_ap = Rune("Normal", "Glyph", "Ability Power", "Primary", 165, None,
             ability_power=0.92)
g_glyph_ap = Rune("Greater", "Glyph", "Ability Power", "Primary", 410, None,
             ability_power=1.19)
l_quintessence_ap = Rune("Lesser", "Quintessence", "Ability Power", "Primary",
                    80, None, ability_power=2.75)
n_quintessence_ap = Rune("Normal", "Quintessence", "Ability Power", "Primary",
                    410, None, ability_power=3.85)
g_quintessence_ap = Rune("Greater", "Quintessence", "Ability Power", "Primary",
                    1025, None, ability_power=4.95)

# Armor
l_mark_armor = Rune("Lesser", "Mark", "Armor", "Secondary", 15, None,
               armor=0.51)
n_mark_armor = Rune("Normal", "Mark", "Armor", "Secondary", 80, None,
               armor=0.71)
g_mark_armor = Rune("Greater", "Mark", "Armor", "Secondary", 205, None,
               armor=0.91)
l_seal_armor = Rune("Lesser", "Seal", "Armor", "Primary", 15, None, armor=0.78)
n_seal_armor = Rune("Normal", "Seal", "Armor", "Primary", 80, None, armor=1.09)
g_seal_armor = Rune("Greater", "Seal", "Armor", "Primary", 205, None,
               armor=1.41)
l_glyph_armor = Rune("Lesser", "Glyph", "Armor", "Secondary", 15, None,
                armor=0.39)
n_glyph_armor = Rune("Normal", "Glyph", "Armor", "Secondary", 80, None,
                armor=0.55)
g_glyph_armor = Rune("Greater", "Glyph", "Armor", "Secondary", 205, None,
                armor=0.7)
l_quintessence_armor = Rune("Lesser", "Quintessence", "Armor", "Primary", 80,
                       None, armor=2.37)
n_quintessence_armor = Rune("Normal", "Quintessence", "Armor", "Primary", 410,
                       None, armor=3.32)
g_quintessence_armor = Rune("Greater", "Quintessence", "Armor", "Primary",
                       1025, None, armor=4.26)

# Armor Penetration
l_mark_armor_penetration = Rune("Lesser", "Mark", "Armor Penetration",
                           "Primary", 30, None, flat_armor_penetration=0.72)
n_mark_armor_penetration = Rune("Normal", "Mark", "Armor Penetration",
                           "Primary", 165, None, flat_armor_penetration=1)
g_mark_armor_penetration = Rune("Greater", "Mark", "Armor Penetration",
                           "Primary", 410, None, flat_armor_penetration=1.28)
l_quintessence_armor_penetration = Rune("Lesser", "Quintessence",
                                   "Armor Penetration", "Secondary", 80, None,
                                   flat_armor_penetration=1.42)
n_quintessence_armor_penetration = Rune("Normal", "Quintessence",
                                   "Armor Penetration", "Secondary", 410, None,
                                   flat_armor_penetration=1.99)
g_quintessence_armor_penetration = Rune("Greater", "Quintessence",
                                   "Armor Penetration", "Secondary", 1025,
                                   None, flat_armor_penetration=2.56)

# Attack Damage
l_mark_attack_damage = Rune("Lesser", "Mark", "Attack Damage", "Primary",
                       15, None, attack_damage=0.53)
n_mark_attack_damage = Rune("Normal", "Mark", "Attack Damage", "Primary",
                       80, None, attack_damage=0.74)
g_mark_attack_damage = Rune("Greater", "Mark", "Attack Damage", "Primary",
                       205, None, attack_damage=0.95)
l_seal_attack_damage = Rune("Lesser", "Seal", "Attack Damage", "Secondary",
                       15, None, attack_damage=0.24)
n_seal_attack_damage = Rune("Normal", "Seal", "Attack Damage", "Secondary",
                       80, None, attack_damage=0.33)
g_seal_attack_damage = Rune("Greater", "Seal", "Attack Damage", "Secondary",
                       205, None, attack_damage=0.43)
l_glyph_attack_damage = Rune("Lesser", "Glyph", "Attack Damage", "Secondary",
                        15, None, attack_damage=0.16)
n_glyph_attack_damage = Rune("Normal", "Glyph", "Attack Damage", "Secondary",
                        80, None, attack_damage=0.22)
g_glyph_attack_damage = Rune("Greater", "Glyph", "Attack Damage", "Secondary",
                        205, None, attack_damage=0.28)
l_quintessence_attack_damage = Rune("Lesser", "Quintessence", "Attack Damage",
                               "Secondary", 80, None, attack_damage=1.25)
n_quintessence_attack_damage = Rune("Normal", "Quintessence", "Attack Damage",
                               "Secondary", 410, None, attack_damage=1.75)
g_quintessence_attack_damage = Rune("Greater", "Quintessence", "Attack Damage",
                               "Secondary", 1025, None, attack_damage=2.25)

# Attack Speed
l_mark_attack_speed = Rune("Lesser", "Mark", "Attack Speed", "Primary",
                      30, None, attack_speed=0.0094)
n_mark_attack_speed = Rune("Normal", "Mark", "Attack Speed", "Primary",
                      165, None, attack_speed=0.0132)
g_mark_attack_speed = Rune("Greater", "Mark", "Attack Speed", "Primary",
                      410, None, attack_speed=0.017)
l_seal_attack_speed = Rune("Lesser", "Seal", "Attack Speed", "Secondary",
                      30, None, attack_speed=0.0042)
n_seal_attack_speed = Rune("Normal", "Seal", "Attack Speed", "Secondary",
                      165, None, attack_speed=0.0059)
g_seal_attack_speed = Rune("Greater", "Seal", "Attack Speed", "Secondary",
                      410, None, attack_speed=0.0076)
l_glyph_attack_speed = Rune("Lesser", "Glyph", "Attack Speed", "Secondary",
                       30, None, attack_speed=0.0035)
n_glyph_attack_speed = Rune("Normal", "Glyph", "Attack Speed", "Secondary",
                       165, None, attack_speed=0.005)
g_glyph_attack_speed = Rune("Greater", "Glyph", "Attack Speed", "Secondary",
                       410, None, attack_speed=0.0064)
l_quintessence_attack_speed = Rune("Lesser", "Quintessence", "Attack Speed",
                              "Secondary", 80, None, attack_speed=0.0189)
n_quintessence_attack_speed = Rune("Normal", "Quintessence", "Attack Speed",
                              "Secondary", 410, None, attack_speed=0.0264)
g_quintessence_attack_speed = Rune("Greater", "Quintessence", "Attack Speed",
                              "Secondary", 1025, None, attack_speed=0.034)

# Cooldown Reduction
l_mark_cooldown_reduction = Rune("Lesser", "Mark", "Cooldown Reduction",
                            "Secondary", 30, None, cooldown_reduction=0.0011)
n_mark_cooldown_reduction = Rune("Normal", "Mark", "Cooldown Reduction",
                            "Secondary", 165, None, cooldown_reduction=0.0016)
g_mark_cooldown_reduction = Rune("Greater", "Mark", "Cooldown Reduction",
                            "Secondary", 410, None, cooldown_reduction=0.002)
l_seal_cooldown_reduction = Rune("Lesser", "Seal", "Cooldown Reduction",
                            "Secondary", 30, None, cooldown_reduction=0.002)
n_seal_cooldown_reduction = Rune("Normal", "Seal", "Cooldown Reduction",
                            "Secondary", 165, None, cooldown_reduction=0.0029)
g_seal_cooldown_reduction = Rune("Greater", "Seal", "Cooldown Reduction",
                            "Secondary", 410, None, cooldown_reduction=0.0036)
l_glyph_cooldown_reduction = Rune("Lesser", "Glyph", "Cooldown Reduction",
                             "Primary", 65, None, cooldown_reduction=0.0047)
n_glyph_cooldown_reduction = Rune("Normal", "Glyph", "Cooldown Reduction",
                             "Primary", 330, None, cooldown_reduction=0.0067)
g_glyph_cooldown_reduction = Rune("Greater", "Glyph", "Cooldown Reduction",
                             "Primary", 820, None, cooldown_reduction=0.0083)
l_quintessence_cooldown_reduction = Rune("Lesser", "Quintessence",
                                    "Cooldown Reduction", "Secondary",
                                    165, None, cooldown_reduction=0.0093)
n_quintessence_cooldown_reduction = Rune("Normal", "Quintessence",
                                    "Cooldown Reduction", "Secondary",
                                    820, None, cooldown_reduction=0.0133)
g_quintessence_cooldown_reduction = Rune("Greater", "Quintessence",
                                    "Cooldown Reduction", "Secondary",
                                    2050, None, cooldown_reduction=0.0167)

# Critical Chance
l_mark_critical_strike_chance = Rune("Lesser", "Mark", "Critical Chance",
                                "Primary", 30, None,
                                critical_strike_chance=0.0052)
n_mark_critical_strike_chance = Rune("Normal", "Mark", "Critical Chance",
                                "Primary", 165, None,
                                critical_strike_chance=0.0072)
g_mark_critical_strike_chance = Rune("Greater", "Mark", "Critical Chance",
                                "Primary", 410, None,
                                critical_strike_chance=0.0093)
l_seal_critical_strike_chance = Rune("Lesser", "Seal", "Critical Chance",
                                "Secondary", 30, None,
                                critical_strike_chance=0.0023)
n_seal_critical_strike_chance = Rune("Normal", "Seal", "Critical Chance",
                                "Secondary", 165, None,
                                critical_strike_chance=0.0032)
g_seal_critical_strike_chance = Rune("Greater", "Seal", "Critical Chance",
                                "Secondary", 410, None,
                                critical_strike_chance=0.0042)
l_glyph_critical_strike_chance = Rune("Lesser", "Glyph", "Critical Chance",
                                 "Secondary", 30, None,
                                 critical_strike_chance=0.0015)
n_glyph_critical_strike_chance = Rune("Normal", "Glyph", "Critical Chance",
                                 "Secondary", 165, None,
                                 critical_strike_chance=0.0022)
g_glyph_critical_strike_chance = Rune("Greater", "Glyph", "Critical Chance",
                                 "Secondary", 410, None,
                                 critical_strike_chance=0.0028)
l_quintessence_critical_strike_chance = Rune("Lesser", "Quintessence",
                                        "Critical Chance", "Secondary",
                                        80, None,
                                        critical_strike_chance=0.0103)
n_quintessence_critical_strike_chance = Rune("Normal", "Quintessence",
                                        "Critical Chance", "Secondary",
                                        410, None,
                                        critical_strike_chance=0.0144)
g_quintessence_critical_strike_chance = Rune("Greater", "Quintessence",
                                        "Critical Chance", "Secondary",
                                        1025, None,
                                        critical_strike_chance=0.0186)

# Critical Damage
l_mark_critical_strike_damage = Rune("Lesser", "Mark", "Critical Damage",
                                "Primary", 65, None,
                                critical_strike_damage=0.0124)
n_mark_critical_strike_damage = Rune("Normal", "Mark", "Critical Damage",
                                "Primary", 330, None,
                                critical_strike_damage=0.0174)
g_mark_critical_strike_damage = Rune("Greater", "Mark", "Critical Damage",
                                "Primary", 820, None,
                                critical_strike_damage=0.0223)
l_seal_critical_strike_damage = Rune("Lesser", "Seal", "Critical Damage",
                                "Secondary", 65, None,
                                critical_strike_damage=0.0043)
n_seal_critical_strike_damage = Rune("Normal", "Seal", "Critical Damage",
                                "Secondary", 330, None,
                                critical_strike_damage=0.0061)
g_seal_critical_strike_damage = Rune("Greater", "Seal", "Critical Damage",
                                "Secondary", 820, None,
                                critical_strike_damage=0.0078)
l_glyph_critical_strike_damage = Rune("Lesser", "Glyph", "Critical Damage",
                                 "Secondary", 65, None,
                                 critical_strike_damage=0.0031)
n_glyph_critical_strike_damage = Rune("Normal", "Glyph", "Critical Damage",
                                 "Secondary", 330, None,
                                 critical_strike_damage=0.0043)
g_glyph_critical_strike_damage = Rune("Greater", "Glyph", "Critical Damage",
                                 "Secondary", 820, None,
                                 critical_strike_damage=0.0056)
l_quintessence_critical_strike_damage = Rune("Lesser", "Quintessence",
                                        "Critical Damage", "Secondary",
                                        80, None,
                                        critical_strike_damage=0.0248)
n_quintessence_critical_strike_damage = Rune("Normal", "Quintessence",
                                        "Critical Damage", "Secondary",
                                        410, None,
                                        critical_strike_damage=0.0347)
g_quintessence_critical_strike_damage = Rune("Greater", "Quintessence",
                                        "Critical Damage", "Secondary",
                                        1025, None,
                                        critical_strike_damage=0.0446)

# Energy
g_glyph_energy = Rune("Greater", "Glyph", "Energy", "Primary",
                 820, None, energy=2.2)
g_quintessence_energy = Rune("Greater", "Quintessence", "Energy", "Primary",
                        1025, None, energy=5.4)

# Energy Regeneration
g_seal_energy_regeneration = Rune("Greater", "Seal", "Energy Regeneration",
                             "Primary", 820, None, energy_regeneration=0.63)
g_quintessence_energy_regeneration = Rune("Greater", "Quintessence",
                                     "Energy Regeneration", "Primary",
                                     2050, None, energy_regeneration=1.575)

# Experience
g_quintessence_experience = Rune("Greater", "Quintessence", "Experience",
                            "Primary", 2050, None, experience=0.02)

# Gold (Gold / 10 sec)
g_seal_gold = Rune("Greater", "Seal", "Gold", "Primary", 410, None, gold=0.25)
g_quintessence_gold = Rune("Greater", "Quintessence", "Gold", "Primary",
                      515, None, gold=1)

# Health
l_mark_health = Rune("Lesser", "Mark", "Health", "Secondary",
                30, None, health=1.93)
n_mark_health = Rune("Normal", "Mark", "Health", "Secondary",
                165, None, health=2.7)
g_mark_health = Rune("Greater", "Mark", "Health", "Secondary",
                410, None, health=3.47)
l_seal_health = Rune("Lesser", "Seal", "Health", "Primary",
                65, None, health=2.97)
n_seal_health = Rune("Normal", "Seal", "Health", "Primary",
                330, None, health=4.16)
g_seal_health = Rune("Greater", "Seal", "Health", "Primary",
                820, None, health=5.35)
l_glyph_health = Rune("Lesser", "Glyph", "Health", "Secondary",
                 30, None, health=1.49)
n_glyph_health = Rune("Normal", "Glyph", "Health", "Secondary",
                 165, None, health=2.08)
g_glyph_health = Rune("Greater", "Glyph", "Health", "Secondary",
                 410, None, health=2.67)
l_quintessence_health = Rune("Lesser", "Quintessence", "Health", "Primary",
                        165, None, health=14.5)
n_quintessence_health = Rune("Normal", "Quintessence", "Health", "Primary",
                        820, None, health=20)
g_quintessence_health = Rune("Greater", "Quintessence", "Health", "Primary",
                        2050, None, health=26)

# Health Regeneration (Health Regen / 5 sec)
l_seal_health_regeneration = Rune("Lesser", "Seal", "Health Regeneration",
                             "Primary", 65, None, health_regeneration=0.24)
n_seal_health_regeneration = Rune("Normal", "Seal", "Health Regeneration",
                             "Primary", 330, None, health_regeneration=0.34)
g_seal_health_regeneration = Rune("Greater", "Seal", "Health Regeneration",
                             "Primary", 820, None, health_regeneration=0.43)
l_glyph_health_regeneration = Rune("Lesser", "Glyph", "Health Regeneration",
                              "Secondary", 65, None, health_regeneration=0.15)
n_glyph_health_regeneration = Rune("Normal", "Glyph", "Health Regeneration",
                              "Secondary", 330, None, health_regeneration=0.21)
g_glyph_health_regeneration = Rune("Greater", "Glyph", "Health Regeneration",
                              "Secondary", 820, None, health_regeneration=0.27)
l_quintessence_health_regeneration = Rune("Lesser", "Quintessence",
                                     "Health Regeneration", "Primary",
                                     165, None, health_regeneration=1.5)
n_quintessence_health_regeneration = Rune("Normal", "Quintessence",
                                     "Health Regeneration", "Primary",
                                     820, None, health_regeneration=2.1)
g_quintessence_health_regeneration = Rune("Greater", "Quintessence",
                                     "Health Regeneration", "Primary",
                                     2050, None, health_regeneration=2.7)

# Hybrid Penetration (Armor Penetration / Magic Penetration)
l_mark_hybrid_penetration = Rune("Lesser", "Mark", "Hybrid Penetration",
                            "Primary", 65, None, flat_armor_penetration=0.5,
                            flat_magic_penetration=0.34)
n_mark_hybrid_penetration = Rune("Normal", "Mark", "Hybrid Penetration",
                            "Primary", 330, None, flat_armor_penetration=0.7,
                            flat_magic_penetration=0.48)
g_mark_hybrid_penetration = Rune("Greater", "Mark", "Hybrid Penetration",
                            "Primary", 820, None, flat_armor_penetration=0.9,
                            flat_magic_penetration=0.62)
l_quintessence_hybrid_penetration = Rune("Lesser", "Quintessence",
                                    "Hybrid Penetration", "Secondary",
                                    165, None, flat_armor_penetration=0.99,
                                    flat_magic_penetration=0.78)
n_quintessence_hybrid_penetration = Rune("Normal", "Quintessence",
                                    "Hybrid Penetration", "Secondary",
                                    820, None, flat_armor_penetration=1.39,
                                    flat_magic_penetration=1.09)
g_quintessence_hybrid_penetration = Rune("Greater", "Quintessence",
                                    "Hybrid Penetration", "Secondary",
                                    2050, None, flat_armor_penetration=1.79,
                                    flat_magic_penetration=1.4)

# Life Steal
l_quintessence_life_steal = Rune("Lesser", "Quintessence", "Life Steal",
                            "Primary", 165, None, life_steal=0.0112)
n_quintessence_life_steal = Rune("Normal", "Quintessence", "Life Steal",
                            "Primary", 820, None, life_steal=0.0156)
g_quintessence_life_steal = Rune("Greater", "Quintessence", "Life Steal",
                            "Primary", 2050, None, life_steal=0.02)

# Magic Penetration
l_mark_magic_penetration = Rune("Lesser", "Mark", "Magic Penetration",
                           "Primary", 30, None, flat_magic_penetration=0.49)
n_mark_magic_penetration = Rune("Normal", "Mark", "Magic Penetration",
                           "Primary", 165, None, flat_magic_penetration=0.68)
g_mark_magic_penetration = Rune("Greater", "Mark", "Magic Penetration",
                           "Primary", 410, None, flat_magic_penetration=0.87)
l_glyph_magic_penetration = Rune("Lesser", "Glyph", "Magic Penetration",
                            "Secondary", 30, None, flat_magic_penetration=0.35)
n_glyph_magic_penetration = Rune("Normal", "Glyph", "Magic Penetration",
                            "Secondary", 165, None,
                            flat_magic_penetration=0.49)
g_glyph_magic_penetration = Rune("Greater", "Glyph", "Magic Penetration",
                            "Secondary", 410, None,
                            flat_magic_penetration=0.63)
l_quintessence_magic_penetration = Rune("Lesser", "Quintessence",
                                   "Magic Penetration", "Secondary",
                                   80, None, flat_magic_penetration=1.11)
n_quintessence_magic_penetration = Rune("Normal", "Quintessence",
                                   "Magic Penetration", "Secondary",
                                   410, None, flat_magic_penetration=1.56)
g_quintessence_magic_penetration = Rune("Greater", "Quintessence",
                                   "Magic Penetration", "Secondary",
                                   1025, None, flat_magic_penetration=2.01)

# Magic Resist
l_mark_magic_resist = Rune("Lesser", "Mark", "Magic Resist", "Secondary",
                      15, None, magic_resistance=0.43)
n_mark_magic_resist = Rune("Normal", "Mark", "Magic Resist", "Secondary",
                      80, None, magic_resistance=0.6)
g_mark_magic_resist = Rune("Greater", "Mark", "Magic Resist", "Secondary",
                      205, None, magic_resistance=0.77)
l_seal_magic_resist = Rune("Lesser", "Seal", "Magic Resist", "Secondary",
                      15, None, magic_resistance=0.41)
n_seal_magic_resist = Rune("Normal", "Seal", "Magic Resist", "Secondary",
                      80, None, magic_resistance=0.58)
g_seal_magic_resist = Rune("Greater", "Seal", "Magic Resist", "Secondary",
                      205, None, magic_resistance=0.74)
l_glyph_magic_resist = Rune("Lesser", "Glyph", "Magic Resist", "Primary",
                       15, None, magic_resistance=0.74)
n_glyph_magic_resist = Rune("Normal", "Glyph", "Magic Resist", "Primary",
                       80, None, magic_resistance=1.04)
g_glyph_magic_resist = Rune("Greater", "Glyph", "Magic Resist", "Primary",
                       205, None, magic_resistance=1.34)
l_quintessence_magic_resist = Rune("Lesser", "Quintessence", "Magic Resist",
                              "Secondary", 80, None, magic_resistance=2.22)
n_quintessence_magic_resist = Rune("Normal", "Quintessence", "Magic Resist",
                              "Secondary", 410, None, magic_resistance=3.11)
g_quintessence_magic_resist = Rune("Greater", "Quintessence", "Magic Resist",
                              "Secondary", 1025, None, magic_resistance=4)

# Mana
l_mark_mana = Rune("Lesser", "Mark", "Mana", "Secondary", 30, None, mana=3.28)
n_mark_mana = Rune("Normal", "Mark", "Mana", "Secondary", 165, None, mana=4.59)
g_mark_mana = Rune("Greater", "Mark", "Mana", "Secondary",
              410, None, mana=5.91)
l_seal_mana = Rune("Lesser", "Seal", "Mana", "Secondary", 30, None, mana=3.83)
n_seal_mana = Rune("Normal", "Seal", "Mana", "Secondary", 165, None, mana=5.36)
g_seal_mana = Rune("Greater", "Seal", "Mana", "Secondary",
              410, None, mana=6.89)
l_glyph_mana = Rune("Lesser", "Glyph", "Mana", "Primary", 30, None, mana=6.25)
n_glyph_mana = Rune("Normal", "Glyph", "Mana", "Primary",
               165, None, mana=8.75)
g_glyph_mana = Rune("Greater", "Glyph", "Mana", "Primary",
               410, None,mana=11.25)
l_quintessence_mana = Rune("Lesser", "Quintessence", "Mana", "Primary",
                      80, None, mana=20.83)
n_quintessence_mana = Rune("Normal", "Quintessence", "Mana", "Primary",
                      410, None, mana=29.17)
g_quintessence_mana = Rune("Greater", "Quintessence", "Mana", "Primary",
                      1025, None, mana=37.5)

# Mana Regeneration (Mana regen / 5 sec)
l_mark_mana_regeneration = Rune("Lesser", "Mark", "Mana Regeneration",
                           "Secondary", 15, None, mana_regeneration=0.15)
n_mark_mana_regeneration = Rune("Normal", "Mark", "Mana Regeneration",
                           "Secondary", 80, None, mana_regeneration=0.2)
g_mark_mana_regeneration = Rune("Greater", "Mark", "Mana Regeneration",
                           "Secondary", 205, None, mana_regeneration=0.26)
l_seal_mana_regeneration = Rune("Lesser", "Seal", "Mana Regeneration",
                           "Primary", 15, None, mana_regeneration=0.23)
n_seal_mana_regeneration = Rune("Normal", "Seal", "Mana Regeneration",
                           "Primary", 80, None, mana_regeneration=0.32)
g_seal_mana_regeneration = Rune("Greater", "Seal", "Mana Regeneration",
                           "Primary", 205, None, mana_regeneration=0.41)
l_glyph_mana_regeneration = Rune("Lesser", "Glyph", "Mana Regeneration",
                            "Secondary", 30, None, mana_regeneration=0.17)
n_glyph_mana_regeneration = Rune("Normal", "Glyph", "Mana Regeneration",
                            "Secondary", 165, None, mana_regeneration=0.24)
g_glyph_mana_regeneration = Rune("Greater", "Glyph", "Mana Regeneration",
                            "Secondary", 410, None, mana_regeneration=0.31)
l_quintessence_mana_regeneration = Rune("Lesser", "Quintessence",
                                   "Mana Regeneration", "Primary",
                                   80, None, mana_regeneration=0.69)
n_quintessence_mana_regeneration = Rune("Normal", "Quintessence",
                                   "Mana Regeneration", "Primary",
                                   410, None, mana_regeneration=0.97)
g_quintessence_mana_regeneration = Rune("Greater", "Quintessence",
                                   "Mana Regeneration", "Primary",
                                   1025, None, mana_regeneration=1.25)

# Movement Speed
l_quintessence_movement_speed = Rune("Lesser", "Quintessence",
                                "Movement Speed", "Primary",
                                165, None, movement_speed=0.0083)
n_quintessence_movement_speed = Rune("Normal", "Quintessence",
                                "Movement Speed", "Primary",
                                820, None, movement_speed=0.0117)
g_quintessence_movement_speed = Rune("Greater", "Quintessence",
                                "Movement Speed", "Primary",
                                2050, None, movement_speed=0.015)

# Percent Health
l_seal_percent_health = Rune("Lesser", "Seal", "Percent Health", "Primary",
                        65, None, percent_health=0.0028)
n_seal_percent_health = Rune("Normal", "Seal", "Percent Health", "Primary",
                        330, None, percent_health=0.0039)
g_seal_percent_health = Rune("Greater", "Seal", "Percent Health", "Primary",
                        820, None, percent_health=0.005)
l_quintessence_percent_health = Rune("Lesser", "Quintessence",
                                "Percent Health", "Primary",
                                165, None, percent_health=0.0084)
n_quintessence_percent_health = Rune("Normal", "Quintessence",
                                "Percent Health", "Primary",
                                820, None, percent_health=0.0117)
g_quintessence_percent_health = Rune("Greater", "Quintessence",
                                "Percent Health", "Primary",
                                2050, None, percent_health=0.015)

# Revival (Reduction of time dead)
g_quintessence_revival = Rune("Greater", "Quintessence", "Revival", "Primary",
                         1025, None, revival=0.05)

# Scaling Ability Power (Ability Power per level)
l_mark_scaling_ability_power = Rune("Lesser", "Mark", "Scaling Ability Power",
                               "Secondary", 30, None,
                               scaling_ability_power=0.06)
n_mark_scaling_ability_power = Rune("Normal", "Mark", "Scaling Ability Power",
                               "Secondary", 165, None,
                               scaling_ability_power=0.08)
g_mark_scaling_ability_power = Rune("Greater", "Mark", "Scaling Ability Power",
                               "Secondary", 410, None,
                               scaling_ability_power=0.1)
l_seal_scaling_ability_power = Rune("Lesser", "Seal", "Scaling Ability Power",
                               "Secondary", 30, None,
                               scaling_ability_power=0.06)
n_seal_scaling_ability_power = Rune("Normal", "Seal", "Scaling Ability Power",
                               "Secondary", 165, None,
                               scaling_ability_power=0.08)
g_seal_scaling_ability_power = Rune("Greater", "Seal", "Scaling Ability Power",
                               "Secondary", 410, None,
                               scaling_ability_power=0.1)
l_glyph_scaling_ability_power = Rune("Lesser", "Glyph",
                                "Scaling Ability Power", "Primary",
                                30, None, scaling_ability_power=0.1)
n_glyph_scaling_ability_power = Rune("Normal", "Glyph",
                                "Scaling Ability Power", "Primary",
                                165, None, scaling_ability_power=0.13)
g_glyph_scaling_ability_power = Rune("Greater", "Glyph",
                                "Scaling Ability Power", "Primary",
                                410, None, scaling_ability_power=0.17)
l_quintessence_scaling_ability_power = Rune("Lesser", "Quintessence",
                                       "Scaling Ability Power", "Secondary",
                                       80, None, scaling_ability_power=0.24)
n_quintessence_scaling_ability_power = Rune("Normal", "Quintessence",
                                       "Scaling Ability Power", "Secondary",
                                       410, None, scaling_ability_power=0.34)
g_quintessence_scaling_ability_power = Rune("Greater", "Quintessence",
                                       "Scaling Ability Power", "Secondary",
                                       1025, None, scaling_ability_power=0.43)

# Scaling Armor (Armor per level)
l_seal_scaling_armor = Rune("Lesser", "Seal", "Scaling Armor", "Primary", 30,
                       None, scaling_armor=0.08)
n_seal_scaling_armor = Rune("Normal", "Seal", "Scaling Armor", "Primary", 165,
                       None, scaling_armor=0.12)
g_seal_scaling_armor = Rune("Greater", "Seal", "Scaling Armor", "Primary", 410,
                       None, scaling_armor=0.15)
l_quintessence_scaling_armor = Rune("Lesser", "Quintessence", "Scaling Armor",
                               "Secondary", 80, None, scaling_armor=0.21)
n_quintessence_scaling_armor = Rune("Normal", "Quintessence", "Scaling Armor",
                               "Secondary", 410, None, scaling_armor=0.29)
g_quintessence_scaling_armor = Rune("Greater", "Quintessence", "Scaling Armor",
                               "Secondary", 1025, None, scaling_armor=0.38)

# Scaling Attack Damage (Attack Damage per level)
l_mark_scaling_attack_damage = Rune("Lesser", "Mark", "Scaling Attack Damage",
                               "Primary", 30, None, scaling_attack_damage=0.08)
n_mark_scaling_attack_damage = Rune("Normal", "Mark", "Scaling Attack Damage",
                               "Primary", 165, None, scaling_attack_damage=0.1)
g_mark_scaling_attack_damage = Rune("Greater", "Mark", "Scaling Attack Damage",
                               "Primary", 410, None,
                               scaling_attack_damage=0.13)
l_seal_scaling_attack_damage = Rune("Lesser", "Seal", "Scaling Attack Damage",
                               "Secondary", 15, None,
                               scaling_attack_damage=0.03)
n_seal_scaling_attack_damage = Rune("Normal", "Seal", "Scaling Attack Damage",
                               "Secondary", 80, None,
                               scaling_attack_damage=0.05)
g_seal_scaling_attack_damage = Rune("Greater", "Seal", "Scaling Attack Damage",
                               "Secondary", 205, None,
                               scaling_attack_damage=0.06)
l_glyph_scaling_attack_damage = Rune("Lesser", "Glyph",
                                "Scaling Attack Damage", "Secondary",
                                15, None, scaling_attack_damage=0.02)
n_glyph_scaling_attack_damage = Rune("Normal", "Glyph",
                                "Scaling Attack Damage", "Secondary",
                                80, None, scaling_attack_damage=0.03)
g_glyph_scaling_attack_damage = Rune("Greater", "Glyph",
                                "Scaling Attack Damage", "Secondary",
                                205, None, scaling_attack_damage=0.04)
l_quintessence_scaling_attack_damage = Rune("Lesser", "Quintessence",
                                       "Scaling Attack Damage", "Secondary",
                                       40, None, scaling_attack_damage=0.14)
n_quintessence_scaling_attack_damage = Rune("Normal", "Quintessence",
                                       "Scaling Attack Damage", "Secondary",
                                       205, None, scaling_attack_damage=0.19)
g_quintessence_scaling_attack_damage = Rune("Greater", "Quintessence",
                                       "Scaling Attack Damage", "Secondary",
                                       515, None, scaling_attack_damage=0.25)

# Scaling Cooldown Reduction (Cooldown Reduction per level)
l_glyph_scaling_cooldown_reduction = Rune("Lesser", "Glyph",
                                     "Scaling Cooldown Reduction", "Primary",
                                     30, None,
                                     scaling_cooldown_reduction=0.0004)
n_glyph_scaling_cooldown_reduction = Rune("Normal", "Glyph",
                                     "Scaling Cooldown Reduction", "Primary",
                                     165, None,
                                     scaling_cooldown_reduction=0.0005)
g_glyph_scaling_cooldown_reduction = Rune("Greater", "Glyph",
                                     "Scaling Cooldown Reduction", "Primary",
                                     410, None,
                                     scaling_cooldown_reduction=0.0006)
l_quintessence_scaling_cooldown_reduction = Rune("Lesser", "Quintessence",
                                            "Scaling Cooldown Reduction",
                                            "Secondary", 80, None,
                                            scaling_cooldown_reduction=0.0008)
n_quintessence_scaling_cooldown_reduction = Rune("Normal", "Quintessence",
                                            "Scaling Cooldown Reduction",
                                            "Secondary", 410, None,
                                            scaling_cooldown_reduction=0.0011)
g_quintessence_scaling_cooldown_reduction = Rune("Greater", "Quintessence",
                                            "Scaling Cooldown Reduction",
                                            "Secondary", 1025, None,
                                            scaling_cooldown_reduction=0.0014)

# Scaling Energy (Energy per level)
g_glyph_scaling_energy = Rune("Greater", "Glyph", "Scaling Energy", "Primary",
                         820, None, scaling_energy=0.161)

# Scaling Energy Regeneration (Energy Regen / 5 sec per level)
g_seal_scaling_energy_regeneration = Rune("Greater", "Seal",
                                     "Scaling Energy Regeneration",
                                     "Secondary", 820, None,
                                     scaling_energy_regeneration=0.064)

# Scaling Health (Health per level)
l_mark_scaling_health = Rune("Lesser", "Mark", "Scaling Health", "Secondary",
                        65, None, scaling_health=0.3)
n_mark_scaling_health = Rune("Normal", "Mark", "Scaling Health", "Secondary",
                        330, None, scaling_health=0.42)
g_mark_scaling_health = Rune("Greater", "Mark", "Scaling Health", "Secondary",
                        820, None, scaling_health=0.54)
l_seal_scaling_health = Rune("Lesser", "Seal", "Scaling Health", "Primary", 30,
                        None, scaling_health=0.6)
n_seal_scaling_health = Rune("Normal", "Seal", "Scaling Health", "Primary",
                        165, None, scaling_health=0.84)
g_seal_scaling_health = Rune("Greater", "Seal", "Scaling Health", "Primary",
                        410, None, scaling_health=1.08)
l_glyph_scaling_health = Rune("Lesser", "Glyph", "Scaling Health", "Secondary",
                         65, None, scaling_health=0.3)
n_glyph_scaling_health = Rune("Normal", "Glyph", "Scaling Health",
                         "Secondary", 330, None, scaling_health=0.42)
g_glyph_scaling_health = Rune("Greater", "Glyph", "Scaling Health",
                         "Secondary", 820, None, scaling_health=0.54)
l_quintessence_scaling_health = Rune("Lesser", "Quintessence",
                                "Scaling Health", "Secondary", 165, None,
                                scaling_health=1.5)
n_quintessence_scaling_health = Rune("Normal", "Quintessence",
                                "Scaling Health", "Secondary", 820, None,
                                scaling_health=2.1)
g_quintessence_scaling_health = Rune("Greater", "Quintessence",
                                "Scaling Health", "Secondary", 2050, None,
                                scaling_health=2.7)

# Scaling Health Regeneration (Health Regen / 5 sec per level)
l_seal_scaling_health_regeneration = Rune("Lesser", "Seal",
                                     "Scaling Health Regeneration", "Primary",
                                     30, None,
                                     scaling_health_regeneration=0.06)
n_seal_scaling_health_regeneration = Rune("Normal", "Seal",
                                     "Scaling Health Regeneration", "Primary",
                                     165, None,
                                     scaling_health_regeneration=0.09)
g_seal_scaling_health_regeneration = Rune("Greater", "Seal",
                                     "Scaling Health Regeneration", "Primary",
                                     410, None,
                                     scaling_health_regeneration=0.11)
l_quintessence_scaling_health_regeneration = Rune("Lesser", "Quintessence",
                                             "Scaling Health Regeneration",
                                             "Primary", 165, None,
                                             scaling_health_regeneration=0.16)
n_quintessence_scaling_health_regeneration = Rune("Normal", "Quintessence",
                                             "Scaling Health Regeneration",
                                             "Primary", 820, None,
                                             scaling_health_regeneration=0.22)
g_quintessence_scaling_health_regeneration = Rune("Greater", "Quintessence",
                                             "Scaling Health Regeneration",
                                             "Primary", 2050, None,
                                             scaling_health_regeneration=0.28)

# Scaling Magic Resist (Magic Resist per level)
l_mark_scaling_magic_resist = Rune("Lesser", "Mark", "Scaling Magic Resist",
                              "Secondary", 15, None,
                              scaling_magic_resistance=0.04)
n_mark_scaling_magic_resist = Rune("Normal", "Mark", "Scaling Magic Resist",
                              "Secondary", 80, None,
                              scaling_magic_resistance=0.06)
g_mark_scaling_magic_resist = Rune("Greater", "Mark", "Scaling Magic Resist",
                              "Secondary", 205, None,
                              scaling_magic_resistance=0.07)
l_seal_scaling_magic_resist = Rune("Lesser", "Seal", "Scaling Magic Resist",
                              "Secondary", 30, None,
                              scaling_magic_resistance=0.05)
n_seal_scaling_magic_resist = Rune("Normal", "Seal", "Scaling Magic Resist",
                              "Secondary", 165, None,
                              scaling_magic_resistance=0.08)
g_seal_scaling_magic_resist = Rune("Greater", "Seal", "Scaling Magic Resist",
                              "Secondary", 410, None,
                              scaling_magic_resistance=0.1)
l_glyph_scaling_magic_resist = Rune("Lesser", "Glyph", "Scaling Magic Resist",
                               "Primary", 15, None,
                               scaling_magic_resistance=0.08)
n_glyph_scaling_magic_resist = Rune("Normal", "Glyph", "Scaling Magic Resist",
                               "Primary", 80, None,
                               scaling_magic_resistance=0.12)
g_glyph_scaling_magic_resist = Rune("Greater", "Glyph", "Scaling Magic Resist",
                               "Primary", 205, None,
                               scaling_magic_resistance=0.15)
l_quintessence_scaling_magic_resist = Rune("Lesser", "Quintessence",
                                      "Scaling Magic Resist", "Secondary", 80,
                                      None, scaling_magic_resistance=0.21)
n_quintessence_scaling_magic_resist = Rune("Normal", "Quintessence",
                                      "Scaling Magic Resist", "Secondary", 410,
                                      None, scaling_magic_resistance=0.29)
g_quintessence_scaling_magic_resist = Rune("Greater", "Quintessence",
                                      "Scaling Magic Resist", "Secondary",
                                      1025, None,
                                      scaling_magic_resistance=0.37)

# Scaling Mana (Mana per level)
l_mark_scaling_mana = Rune("Lesser", "Mark", "Scaling Mana", "Secondary", 30,
                      None, scaling_mana=0.65)
n_mark_scaling_mana = Rune("Normal", "Mark", "Scaling Mana", "Secondary", 165,
                      None, scaling_mana=0.91)
g_mark_scaling_mana = Rune("Greater", "Mark", "Scaling Mana", "Secondary", 410,
                      None, scaling_mana=1.17)
l_seal_scaling_mana = Rune("Lesser", "Seal", "Scaling Mana", "Secondary", 30,
                      None, scaling_mana=0.65)
n_seal_scaling_mana = Rune("Normal", "Seal", "Scaling Mana", "Secondary", 165,
                      None, scaling_mana=0.91)
g_seal_scaling_mana = Rune("Greater", "Seal", "Scaling Mana", "Secondary", 410,
                      None, scaling_mana=1.17)
l_glyph_scaling_mana = Rune("Lesser", "Glyph", "Scaling Mana", "Primary", 30,
                       None, scaling_mana=0.79)
n_glyph_scaling_mana = Rune("Normal", "Glyph", "Scaling Mana", "Primary", 165,
                       None, scaling_mana=1.1)
g_glyph_scaling_mana = Rune("Greater", "Glyph", "Scaling Mana", "Primary", 410,
                       None, scaling_mana=1.42)
l_quintessence_scaling_mana = Rune("Lesser", "Quintessence", "Scaling Mana",
                              "Secondary", 40, None, scaling_mana=2.31)
n_quintessence_scaling_mana = Rune("Normal", "Quintessence", "Scaling Mana",
                              "Secondary", 205, None, scaling_mana=3.24)
g_quintessence_scaling_mana = Rune("Greater", "Quintessence", "Scaling Mana",
                              "Secondary", 515, None, scaling_mana=4.17)

# Scaling Mana Regeneration (Mana regen / 5 sec per level)
l_seal_scaling_mana_regeneration = Rune("Lesser", "Seal",
                                   "Scaling Mana Regeneration", "Primary", 15,
                                   None, scaling_mana_regeneration=0.036)
n_seal_scaling_mana_regeneration = Rune("Normal", "Seal",
                                   "Scaling Mana Regeneration", "Primary", 80,
                                   None, scaling_mana_regeneration=0.05)
g_seal_scaling_mana_regeneration = Rune("Greater", "Seal",
                                   "Scaling Mana Regeneration", "Primary", 205,
                                   None, scaling_mana_regeneration=0.065)
l_glyph_scaling_mana_regeneration = Rune("Lesser", "Glyph",
                                    "Scaling Mana Regeneration", "Secondary",
                                    15, None, scaling_mana_regeneration=0.03)
n_glyph_scaling_mana_regeneration = Rune("Normal", "Glyph",
                                    "Scaling Mana Regeneration", "Secondary",
                                    80, None, scaling_mana_regeneration=0.04)
g_glyph_scaling_mana_regeneration = Rune("Greater", "Glyph",
                                    "Scaling Mana Regeneration", "Secondary",
                                    205, None, scaling_mana_regeneration=0.055)
l_quintessence_scaling_mana_regeneration = Rune("Lesser", "Quintessence",
                                           "Scaling Mana Regeneration",
                                           "Primary", 80, None,
                                           scaling_mana_regeneration=0.14)
n_quintessence_scaling_mana_regeneration = Rune("Normal", "Quintessence",
                                           "Scaling Mana Regeneration",
                                           "Primary", 410, None,
                                           scaling_mana_regeneration=0.19)
g_quintessence_scaling_mana_regeneration = Rune("Greater", "Quintessence",
                                           "Scaling Mana Regeneration",
                                           "Primary", 1025, None,
                                           scaling_mana_regeneration=0.24)

# Spell Vamp
l_quintessence_spell_vamp = Rune("Lesser", "Quintessence", "Spell Vamp",
                            "Primary", 165, None, spell_vamp=0.0112)
n_quintessence_spell_vamp = Rune("Normal", "Quintessence", "Spell Vamp",
                            "Primary", 820, None, spell_vamp=0.0156)
g_quintessence_spell_vamp = Rune("Greater", "Quintessence", "Spell Vamp",
                            "Primary", 2050, None, spell_vamp=0.02)