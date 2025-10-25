import json
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os
import urllib.parse

class JSONConfigEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("TROCKII Potions - Custom Potion Recipes [TP_OverrideRecipesJson]")
        self.root.geometry("800x600")
        
        # Default data
        self.default_items = {
            "Strength Potion": "Blueprint'/TrockiiPotions/Items/Basic_Potions/PrimalItemResource_StrengthPotion.PrimalItemResource_StrengthPotion'",
            "Agility Potion": "Blueprint'/TrockiiPotions/Items/Basic_Potions/PrimalItemResource_AgilityPotion.PrimalItemResource_AgilityPotion'",
            "Intelligence Potion": "Blueprint'/TrockiiPotions/Items/Basic_Potions/PrimalItemResource_IntelligencePotion.PrimalItemResource_IntelligencePotion'",
            
            "Damage Potion": "Blueprint'/TrockiiPotions/Items/Strength_Potions/PrimalItemConsumable_DamagePotion.PrimalItemConsumable_DamagePotion'",
            "Fortitude Potion": "Blueprint'/TrockiiPotions/Items/Strength_Potions/PrimalItemConsumable_FortitudePotion.PrimalItemConsumable_FortitudePotion'",
            "25% Health Potion": "Blueprint'/TrockiiPotions/Items/Strength_Potions/PrimalItemConsumable_Increment25Health.PrimalItemConsumable_Increment25Health'",
            "50% Health Potion": "Blueprint'/TrockiiPotions/Items/Strength_Potions/PrimalItemConsumable_Increment50Health.PrimalItemConsumable_Increment50Health'",
            "100% Health Potion": "Blueprint'/TrockiiPotions/Items/Strength_Potions/PrimalItemConsumable_FullHealth.PrimalItemConsumable_FullHealth'",
            "Buff Health Potion": "Blueprint'/TrockiiPotions/Items/Strength_Potions/PrimalItemConsumable_BuffHP.PrimalItemConsumable_BuffHP'",
            "Harvest Potion": "Blueprint'/TrockiiPotions/Items/Strength_Potions/PrimalItemConsumable_HarvestPotion.PrimalItemConsumable_HarvestPotion'",
            "Weight Potion 2X": "Blueprint'/TrockiiPotions/Items/Strength_Potions/PrimalItemConsumable_X2WeightPotion.PrimalItemConsumable_X2WeightPotion'",
            "Weight Potion 5X": "Blueprint'/TrockiiPotions/Items/Strength_Potions/PrimalItemConsumable_X5WeightPotion.PrimalItemConsumable_X5WeightPotion'",
            "Weight Potion 10X": "Blueprint'/TrockiiPotions/Items/Strength_Potions/PrimalItemConsumable_X10WeightPotion.PrimalItemConsumable_X10WeightPotion'",
            "Mutation Potion": "Blueprint'/TrockiiPotions/Items/Strength_Potions/PrimalItemConsumable_MutationPotion.PrimalItemConsumable_MutationPotion'",
            "Maturation Stop Potion": "Blueprint'/TrockiiPotions/Items/Strength_Potions/PrimalItemConsumable_AgeStopPotion.PrimalItemConsumable_AgeStopPotion'",
            "Skill Tree Potion": "Blueprint'/TrockiiPotions/Items/Strength_Potions/PrimalItemConsumable_SkillPointPotion.PrimalItemConsumable_SkillPointPotion'",
            
            "Fly Potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_FlyPotion.PrimalItemConsumable_FlyPotion'",
            "Invisible Potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_BuffInvisiblePotion.PrimalItemConsumable_BuffInvisiblePotion'",
            "Hazard Shield Potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_BuffHazardShield.PrimalItemConsumable_BuffHazardShield'",
            "Buff Stamina Potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_BuffStamina.PrimalItemConsumable_BuffStamina'",
            "100% Stamina Potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_FullStamina.PrimalItemConsumable_FullStamina'",
            "Lesser Speed Potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_SpeedPotionX3.PrimalItemConsumable_SpeedPotionX3'",
            "Speed Potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_SpeedPotion.PrimalItemConsumable_SpeedPotion'",
            "Aquatic Speed Potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_SpeedPotionUnderwather.PrimalItemConsumable_SpeedPotionUnderwather'",
            "Breathing potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_BreathingPotion.PrimalItemConsumable_BreathingPotion'",
            "Sedative Potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_SedativePotion.PrimalItemConsumable_SedativePotion'",
            "Stimulant Potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_StimulantPotion.PrimalItemConsumable_StimulantPotion'",
            "Food Potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_FoodPotion.PrimalItemConsumable_FoodPotion'",
            "Night Vision Potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_NightVisionPotion.PrimalItemConsumable_NightVisionPotion'",
            "Predator Vision Potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_OwlVisionPotion.PrimalItemConsumable_OwlVisionPotion'",
            "XRay Vision Potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_ScoutVisionPotion.PrimalItemConsumable_ScoutVisionPotion'",
            "Spy Potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_SpyPotion.PrimalItemConsumable_SpyPotion'",
            "Adaptive Crafting Potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_BuffCraftPotionV2.PrimalItemConsumable_BuffCraftPotionV2'",
            "Crafting Potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_BuffCraftPotion.PrimalItemConsumable_BuffCraftPotion'",
            "Hairs Potion": "Blueprint'/TrockiiPotions/Items/Agility_Potions/PrimalItemConsumable_HairPotion.PrimalItemConsumable_HairPotion'",
            
            "Bosses Potion": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_BossesPotion.PrimalItemConsumable_BossesPotion'",
            "Loot Potion": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_LioPotion.PrimalItemConsumable_LioPotion'",
            "Tame Potion": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_TamePotion.PrimalItemConsumable_TamePotion'",
            "GrowUp Potion": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_AdultPotion.PrimalItemConsumable_AdultPotion'",
            "50% Reset Mating Potion": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_50ResetMating.PrimalItemConsumable_50ResetMating'",
            "Reset Mating Potion": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_ResetMating.PrimalItemConsumable_ResetMating'",
            "Allow Breeding Potion": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_AllowBreeding.PrimalItemConsumable_AllowBreeding'",
            "Assign Gender Potion": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_AssignGender.PrimalItemConsumable_AssignGender'",
            "Gender Change Potion": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_GenderChange.PrimalItemConsumable_GenderChange'",
            "Color Potion": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_ColorPotion.PrimalItemConsumable_ColorPotion'",
            "Random Trait Potion": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_RandomTraitPotion.PrimalItemConsumable_RandomTraitPotion'",
            "Random Trait 3 Potion": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_RandomTrait3TPotion.PrimalItemConsumable_RandomTrait3TPotion'",
            "Imprint Potion": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_100ImprintPotion.PrimalItemConsumable_100ImprintPotion'",
            "Imprint Potion +100": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_Inc100ImprintPotion.PrimalItemConsumable_Inc100ImprintPotion'",
            "Imprint Potion 500": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_500ImprintPotion.PrimalItemConsumable_500ImprintPotion'",
            "Imprint Owner Potion": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_ImprintOwnerPotion.PrimalItemConsumable_ImprintOwnerPotion'",
            "2x Experience Potion": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_X2ExpPotion.PrimalItemConsumable_X2ExpPotion'",
            "4x Experience Potion": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_X4ExpPotion.PrimalItemConsumable_X4ExpPotion'",
            "MAX Experience Potion": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_MaxExpPotion.PrimalItemConsumable_MaxExpPotion'",
            "Notes Potion": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_NotesPotion.PrimalItemConsumable_NotesPotion'",
            
            "Dino Potion of Health +10": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_IncrementBaseHp.PrimalItemConsumable_IncrementBaseHp'",
            "Dino Potion of Damage +10": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_IncrementBaseDamage.PrimalItemConsumable_IncrementBaseDamage'",
            "Dino Potion of Stamina +10": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_IncrementBaseStamina.PrimalItemConsumable_IncrementBaseStamina'",
            "Dino Potion of Food +10": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_IncrementBaseFood.PrimalItemConsumable_IncrementBaseFood'",
            "Dino Potion of Weight +10": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_IncrementBaseWeight.PrimalItemConsumable_IncrementBaseWeight'",
            "Dino Potion of Oxygen +10": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_IncrementBaseOxygen.PrimalItemConsumable_IncrementBaseOxygen'",
            "Dino Potion of Craft +10": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_IncrementBaseCraft.PrimalItemConsumable_IncrementBaseCraft'",
            
            "Dino Antidote": "Blueprint'/TrockiiPotions/Items/Intelligence_Potions/PrimalItemConsumable_DinoAntidot.PrimalItemConsumable_DinoAntidot'",
            "Dwarf Ale": "Blueprint'/TrockiiPotions/Items/Strength_Potions/PrimalItemConsumable_DwarfAle.PrimalItemConsumable_DwarfAle'",
            "Elven Ale": "Blueprint'/TrockiiPotions/Items/Strength_Potions/PrimalItemConsumable_ElvenAle.PrimalItemConsumable_ElvenAle'",
            "Mindwipe Tonic: Player Stats": "Blueprint'/TrockiiPotions/Items/PrimeBrews/PrimalItemConsumable_TPPlayerStatslMindWipe.PrimalItemConsumable_TPPlayerStatslMindWipe'",
            "Mindwipe Tonic: Engrams": "Blueprint'/TrockiiPotions/Items/PrimeBrews/PrimalItemConsumable_TPEngramsMindWipe.PrimalItemConsumable_TPEngramsMindWipe'",
            "Mindwipe Tonic: Skill Tree": "Blueprint'/TrockiiPotions/Items/PrimeBrews/PrimalItemConsumable_TPSkillTreeMindWipe.PrimalItemConsumable_TPSkillTreeMindWipe'",
            "Mindwipe Tonic: Dino Stats": "Blueprint'/TrockiiPotions/Items/PrimeBrews/PrimalItemConsumable_TPDinoMindWipe.PrimalItemConsumable_TPDinoMindWipe'",


            "Aquatic Mushroom": "Blueprint'/Game/Aberration/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Mushroom_Aquatic.PrimalItemConsumable_Mushroom_Aquatic'",
            "Ascerbic Mushroom": "Blueprint'/Game/Aberration/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Mushroom_Ascerbic.PrimalItemConsumable_Mushroom_Ascerbic'",
            "Auric Mushroom": "Blueprint'/Game/Aberration/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Mushroom_Auric.PrimalItemConsumable_Mushroom_Auric'",
            "Mushroom Brew": "Blueprint'/Game/Aberration/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Soup_MushroomSoup.PrimalItemConsumable_Soup_MushroomSoup'",
            "Aggeravic Mushroom": "Blueprint'/Game/Aberration/CoreBlueprints/Items/Consumables/PrimalItemResource_CommonMushroom.PrimalItemResource_CommonMushroom'",
            "Nameless Venom": "Blueprint'/Game/Aberration/CoreBlueprints/Resources/PrimalItemConsumable_NamelessVenom.PrimalItemConsumable_NamelessVenom'",
            "Element Ore": "Blueprint'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_ElementOre.PrimalItemResource_ElementOre'",
            "Fungal Wood": "Blueprint'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_FungalWood.PrimalItemResource_FungalWood'",
            "Congealed Gas Ball": "Blueprint'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_Gas.PrimalItemResource_Gas'",
            "Blue Gem": "Blueprint'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_Gem_BioLum.PrimalItemResource_Gem_BioLum'",
            "Red Gem": "Blueprint'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_Gem_Element.PrimalItemResource_Gem_Element'",
            "Green Gem": "Blueprint'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_Gem_Fertile.PrimalItemResource_Gem_Fertile'",
            "Reaper Pheromone Gland": "Blueprint'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_XenomorphPheromoneGland.PrimalItemResource_XenomorphPheromoneGland'",
            "Plant Species Z Fruit": "Blueprint'/Game/Aberration/WeaponPlantSpeciesZ/PrimalItem_PlantSpeciesZ_Grenade.PrimalItem_PlantSpeciesZ_Grenade'",
            "Plant Species Z Seed": "Blueprint'/Game/Aberration/WeaponPlantSpeciesZ/PrimalItemConsumable_Seed_PlantSpeciesZ.PrimalItemConsumable_Seed_PlantSpeciesZ'",
            "Archelon Algae": "Blueprint'/Game/ASA/Dinos/Archelon/Dinos/Consumables/PrimalItemConsumable_Veggie_TurtleAlgae_ASA.PrimalItemConsumable_Veggie_TurtleAlgae_ASA'",
            "Algae Sushi": "Blueprint'/Game/ASA/Dinos/Archelon/Dinos/Consumables/PrimalItemConsumableEatable_Sushi_ASA.PrimalItemConsumableEatable_Sushi_ASA'",
            "Hemoglobin Cocktail": "Blueprint'/Game/ASA/Dinos/Ceratosaurus/Dinos/Cocktail/PrimalItemConsumable_HemogoblinCocktail_ASA.PrimalItemConsumable_HemogoblinCocktail_ASA'",
            "Blue Crystalized Sap": "Blueprint'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_BlueSap.PrimalItemResource_BlueSap'",
            "Condensed Gas": "Blueprint'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_CondensedGas.PrimalItemResource_CondensedGas'",
            "Corrupted Nodule": "Blueprint'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_CorruptedPolymer.PrimalItemResource_CorruptedPolymer'",
            "Corrupted Wood": "Blueprint'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_CorruptedWood.PrimalItemResource_CorruptedWood'",
            "Element Dust": "Blueprint'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_ElementDust.PrimalItemResource_ElementDust'",
            "Fragmented Green Gem": "Blueprint'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_FracturedGem.PrimalItemResource_FracturedGem'",
            "Red Crystalized Sap": "Blueprint'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_RedSap.PrimalItemResource_RedSap'",
            "Scrap Metal": "Blueprint'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_ScrapMetal.PrimalItemResource_ScrapMetal'",
            "Scrap Metal Ingot": "Blueprint'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_ScrapMetalIngot.PrimalItemResource_ScrapMetalIngot'",
            "Silicate": "Blueprint'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_Silicate.PrimalItemResource_Silicate'",
            "Snow Owl Pellet": "Blueprint'/Game/Extinction/Dinos/Owl/Pellet/PrimalItemConsumable_OwlPellet.PrimalItemConsumable_OwlPellet'",
            "Lesser Antidote": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/BaseBPs/PrimalItemConsumable_CureLow.PrimalItemConsumable_CureLow'",
            "Wyvern Milk": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/BaseBPs/PrimalItemConsumable_WyvernMilk.PrimalItemConsumable_WyvernMilk'",
            "Mindwipe Tonic": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/BaseBPs/PrimalItemConsumableRespecSoup.PrimalItemConsumableRespecSoup'",
            "Soap": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/BaseBPs/PrimalItemConsumableSoap.PrimalItemConsumableSoap'",
            "Beer Jar": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_BeerJar.PrimalItemConsumable_BeerJar'",
            "Beer Jar Alt": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_BeerJarAlt.PrimalItemConsumable_BeerJarAlt'",
            "Amarberry": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Berry_Amarberry.PrimalItemConsumable_Berry_Amarberry'",
            "Azulberry": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Berry_Azulberry.PrimalItemConsumable_Berry_Azulberry'",
            "Cianberry": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Berry_Cianberry.PrimalItemConsumable_Berry_Cianberry'",
            "Magenberry": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Berry_Magenberry.PrimalItemConsumable_Berry_Magenberry'",
            "Mejoberry": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Berry_Mejoberry.PrimalItemConsumable_Berry_Mejoberry'",
            "Narcoberry": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Berry_Narcoberry.PrimalItemConsumable_Berry_Narcoberry'",
            "Stimberry": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Berry_Stimberry.PrimalItemConsumable_Berry_Stimberry'",
            "Tintoberry": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Berry_Tintoberry.PrimalItemConsumable_Berry_Tintoberry'",
            "Verdberry": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Berry_Verdberry.PrimalItemConsumable_Berry_Verdberry'",
            "Blood Pack": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_BloodPack.PrimalItemConsumable_BloodPack'",
            "Bug Repellant": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_BugRepellant.PrimalItemConsumable_BugRepellant'",
            "Cactus Broth": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_CactusBuffSoup.PrimalItemConsumable_CactusBuffSoup'",
            "Canteen": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_CanteenCraftable.PrimalItemConsumable_CanteenCraftable'",
            "Canteen (Filled)": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_CanteenRefill.PrimalItemConsumable_CanteenRefill'",
            "Cooked Lamb Chop": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_CookedLambChop.PrimalItemConsumable_CookedLambChop'",
            "Cooked Meat": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_CookedMeat.PrimalItemConsumable_CookedMeat'",
            "Cooked Fish Meat": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_CookedMeat_Fish.PrimalItemConsumable_CookedMeat_Fish'",
            "Cooked Meat Jerky": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_CookedMeat_Jerky.PrimalItemConsumable_CookedMeat_Jerky'",
            "Cooked Prime Meat": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_CookedPrimeMeat.PrimalItemConsumable_CookedPrimeMeat'",
            "Cooked Prime Fish Meat": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_CookedPrimeMeat_Fish.PrimalItemConsumable_CookedPrimeMeat_Fish'",
            "Prime Meat Jerky": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_CookedPrimeMeat_Jerky.PrimalItemConsumable_CookedPrimeMeat_Jerky'",
            "Fertilizer": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Fertilizer_Compost.PrimalItemConsumable_Fertilizer_Compost'",
            "Medical Brew": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_HealSoup.PrimalItemConsumable_HealSoup'",
            "Honey": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Honey.PrimalItemConsumable_Honey'",
            "Bio Toxin": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_JellyVenom.PrimalItemConsumable_JellyVenom'",
            "Superior Kibble": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Kibble_Base_Large.PrimalItemConsumable_Kibble_Base_Large'",
            "Regular Kibble": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Kibble_Base_Medium.PrimalItemConsumable_Kibble_Base_Medium'",
            "Simple Kibble": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Kibble_Base_Small.PrimalItemConsumable_Kibble_Base_Small'",
            "Extraordinary Kibble": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Kibble_Base_Special.PrimalItemConsumable_Kibble_Base_Special'",
            "Exceptional Kibble": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Kibble_Base_XLarge.PrimalItemConsumable_Kibble_Base_XLarge'",
            "Basic Kibble": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Kibble_Base_XSmall.PrimalItemConsumable_Kibble_Base_XSmall'",
            "Narcotic": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Narcotic.PrimalItemConsumable_Narcotic'",
            "Raw Meat": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_RawMeat.PrimalItemConsumable_RawMeat'",
            "Raw Fish Meat": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_RawMeat_Fish.PrimalItemConsumable_RawMeat_Fish'",
            "Raw Mutton": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_RawMutton.PrimalItemConsumable_RawMutton'",
            "Raw Prime Meat": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_RawPrimeMeat.PrimalItemConsumable_RawPrimeMeat'",
            "Raw Prime Fish Meat": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_RawPrimeMeat_Fish.PrimalItemConsumable_RawPrimeMeat_Fish'",
            "Battle Tartare": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Soup_BattleTartare.PrimalItemConsumable_Soup_BattleTartare'",
            "Calien Soup": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Soup_CalienSoup.PrimalItemConsumable_Soup_CalienSoup'",
            "Enduro Stew": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Soup_EnduroStew.PrimalItemConsumable_Soup_EnduroStew'",
            "Focal Chili": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Soup_FocalChili.PrimalItemConsumable_Soup_FocalChili'",
            "Fria Curry": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Soup_FriaCurry.PrimalItemConsumable_Soup_FriaCurry'",
            "Lazarus Chowder": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Soup_LazarusChowder.PrimalItemConsumable_Soup_LazarusChowder'",
            "Shadow Steak Saute": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Soup_ShadowSteak.PrimalItemConsumable_Soup_ShadowSteak'",
            "Spoiled Meat": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_SpoiledMeat.PrimalItemConsumable_SpoiledMeat'",
            "Energy Brew": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_StaminaSoup.PrimalItemConsumable_StaminaSoup'",
            "Stimulant": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Stimulant.PrimalItemConsumable_Stimulant'",
            "Sweet Vegetable Cake": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_SweetVeggieCake.PrimalItemConsumable_SweetVeggieCake'",
            "Broth of Enlightenment": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_TheHorn.PrimalItemConsumable_TheHorn'",
            "Citronal": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Veggie_Citronal.PrimalItemConsumable_Veggie_Citronal'",
            "Longrass": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Veggie_Longrass.PrimalItemConsumable_Veggie_Longrass'",
            "Rockarrot": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Veggie_Rockarrot.PrimalItemConsumable_Veggie_Rockarrot'",
            "Savoroot": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Veggie_Savoroot.PrimalItemConsumable_Veggie_Savoroot'",
            "Amarberry Seed": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/Seeds/PrimalItemConsumable_Seed_Amarberry.PrimalItemConsumable_Seed_Amarberry'",
            "Azulberry Seed": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/Seeds/PrimalItemConsumable_Seed_Azulberry.PrimalItemConsumable_Seed_Azulberry'",
            "Any Berry Seed": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/Seeds/PrimalItemConsumable_Seed_BaseBerry.PrimalItemConsumable_Seed_BaseBerry'",
            "Cianberry Seed": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/Seeds/PrimalItemConsumable_Seed_Cianberry.PrimalItemConsumable_Seed_Cianberry'",
            "Citronal Seed": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/Seeds/PrimalItemConsumable_Seed_Citronal.PrimalItemConsumable_Seed_Citronal'",
            "Plant Species X Seed": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/Seeds/PrimalItemConsumable_Seed_DefensePlant.PrimalItemConsumable_Seed_DefensePlant'",
            "Longrass Seed": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/Seeds/PrimalItemConsumable_Seed_Longrass.PrimalItemConsumable_Seed_Longrass'",
            "Magenberry Seed": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/Seeds/PrimalItemConsumable_Seed_Magenberry.PrimalItemConsumable_Seed_Magenberry'",
            "Mejoberry Seed": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/Seeds/PrimalItemConsumable_Seed_Mejoberry.PrimalItemConsumable_Seed_Mejoberry'",
            "Narcoberry Seed": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/Seeds/PrimalItemConsumable_Seed_Narcoberry.PrimalItemConsumable_Seed_Narcoberry'",
            "Rockarrot Seed": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/Seeds/PrimalItemConsumable_Seed_Rockarrot.PrimalItemConsumable_Seed_Rockarrot'",
            "Savoroot Seed": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/Seeds/PrimalItemConsumable_Seed_Savoroot.PrimalItemConsumable_Seed_Savoroot'",
            "Stimberry Seed": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/Seeds/PrimalItemConsumable_Seed_Stimberry.PrimalItemConsumable_Seed_Stimberry'",
            "Berry Bush Seed": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/Seeds/PrimalItemConsumable_Seed_Test.PrimalItemConsumable_Seed_Test'",
            "Tintoberry Seed": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/Seeds/PrimalItemConsumable_Seed_Tintoberry.PrimalItemConsumable_Seed_Tintoberry'",
            "Verdberry Seed": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/Seeds/PrimalItemConsumable_Seed_Verdberry.PrimalItemConsumable_Seed_Verdberry'",
            "Plant Species X": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TurretPlant.PrimalItemStructure_TurretPlant'",
            "Flashlight Attachment": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/WeaponAttachments/PrimalItemWeaponAttachment_Flashlight.PrimalItemWeaponAttachment_Flashlight'",
            "Ammonite Bile": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_AmmoniteBlood.PrimalItemResource_AmmoniteBlood'",
            "Angler Gel": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_AnglerGel.PrimalItemResource_AnglerGel'",
            "Beer": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Beer.PrimalItemResource_Beer'",
            "Black Pearl": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_BlackPearl.PrimalItemResource_BlackPearl'",
            "Charcoal": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Charcoal.PrimalItemResource_Charcoal'",
            "Chitin": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Chitin.PrimalItemResource_Chitin'",
            "Cementing Paste": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_ChitinPaste.PrimalItemResource_ChitinPaste'",
            "Crystal": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Crystal.PrimalItemResource_Crystal'",
            "Electronics": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Electronics.PrimalItemResource_Electronics'",
            "Element": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Element.PrimalItemResource_Element'",
            "Element Shard": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_ElementShard.PrimalItemResource_ElementShard'",
            "Fiber": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Fibers.PrimalItemResource_Fibers'",
            "Flint": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Flint.PrimalItemResource_Flint'",
            "Gasoline": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Gasoline.PrimalItemResource_Gasoline'",
            "Gunpowder": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Gunpowder.PrimalItemResource_Gunpowder'",
            "Human Hair": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Hair.PrimalItemResource_Hair'",
            "Hide": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Hide.PrimalItemResource_Hide'",
            "Woolly Rhino Horn": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Horn.PrimalItemResource_Horn'",
            "Keratin": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Keratin.PrimalItemResource_Keratin'",
            "Leech Blood": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_LeechBlood.PrimalItemResource_LeechBlood'",
            "Metal": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Metal.PrimalItemResource_Metal'",
            "Metal Ingot": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_MetalIngot.PrimalItemResource_MetalIngot'",
            "Obsidian": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Obsidian.PrimalItemResource_Obsidian'",
            "Oil": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Oil.PrimalItemResource_Oil'",
            "Pelt": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Pelt.PrimalItemResource_Pelt'",
            "Polymer": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Polymer.PrimalItemResource_Polymer'",
            "Organic Polymer": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Polymer_Organic.PrimalItemResource_Polymer_Organic'",
            "Rare Flower": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_RareFlower.PrimalItemResource_RareFlower'",
            "Rare Mushroom": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_RareMushroom.PrimalItemResource_RareMushroom'",
            "Sap": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Sap.PrimalItemResource_Sap'",
            "Silica Pearls": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Silicon.PrimalItemResource_Silicon'",
            "Sparkpowder": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Sparkpowder.PrimalItemResource_Sparkpowder'",
            "Stone": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Stone.PrimalItemResource_Stone'",
            "Absorbent Substrate": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_SubstrateAbsorbent.PrimalItemResource_SubstrateAbsorbent'",
            "Thatch": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Thatch.PrimalItemResource_Thatch'",
            "Wood": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Wood.PrimalItemResource_Wood'",
            "Wool": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Wool.PrimalItemResource_Wool'",
            "Smoke Grenade": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_GasGrenade.PrimalItem_GasGrenade'",
            "Poison Grenade": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_PoisonGrenade.PrimalItem_PoisonGrenade'",
            "Tek Grenade": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_TekGrenade.PrimalItem_TekGrenade'",
            "Grenade": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponGrenade.PrimalItem_WeaponGrenade'",
            "Advanced Bullet": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_AdvancedBullet.PrimalItemAmmo_AdvancedBullet'",
            "Advanced Rifle Bullet": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_AdvancedRifleBullet.PrimalItemAmmo_AdvancedRifleBullet'",
            "Advanced Sniper Bullet": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_AdvancedSniperBullet.PrimalItemAmmo_AdvancedSniperBullet'",
            "Pheromone Dart": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_AggroTranqDart.PrimalItemAmmo_AggroTranqDart'",
            "Flame Arrow": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_ArrowFlame.PrimalItemAmmo_ArrowFlame'",
            "Stone Arrow": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_ArrowStone.PrimalItemAmmo_ArrowStone'",
            "Tranquilizer Arrow": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_ArrowTranq.PrimalItemAmmo_ArrowTranq'",
            "Spear Bolt": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_BallistaArrow.PrimalItemAmmo_BallistaArrow'",
            "Boulder": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_Boulder.PrimalItemAmmo_Boulder'",
            "Cannon Ball": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_CannonBall.PrimalItemAmmo_CannonBall'",
            "Chain Bola": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_ChainBola.PrimalItemAmmo_ChainBola'",
            "Metal Arrow": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_CompoundBowArrow.PrimalItemAmmo_CompoundBowArrow'",
            "Grappling Hook": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_GrapplingHook.PrimalItemAmmo_GrapplingHook'",
            "Shocking Tranquilizer Dart": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_RefinedTranqDart.PrimalItemAmmo_RefinedTranqDart'",
            "Rocket Propelled Grenade": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_Rocket.PrimalItemAmmo_Rocket'",
            "Simple Bullet": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_SimpleBullet.PrimalItemAmmo_SimpleBullet'",
            "Simple Rifle Ammo": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_SimpleRifleBullet.PrimalItemAmmo_SimpleRifleBullet'",
            "Simple Shotgun Ammo": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_SimpleShotgunBullet.PrimalItemAmmo_SimpleShotgunBullet'",
            "Tranquilizer Dart": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_TranqDart.PrimalItemAmmo_TranqDart'",
            "Tranq Spear Bolt": "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_TranqSpearBolt.PrimalItemAmmo_TranqSpearBolt'",
            "Achatina Paste": "Blueprint'/Game/PrimalEarth/Dinos/Achatina/PrimalItemResource_SnailPaste.PrimalItemResource_SnailPaste'",
            "Rhyniognatha Pheromone": "Blueprint'/Game/PrimalEarth/Dinos/Rhyniognatha/Impregnation/PrimalItemConsumableEatable_RhynioPheromone.PrimalItemConsumableEatable_RhynioPheromone'",
            "Resin": "Blueprint'/Game/PrimalEarth/Dinos/Rhyniognatha/Resin/PrimalItemResource_Resin.PrimalItemResource_Resin'",
            "Squid Oil": "Blueprint'/Game/PrimalEarth/Dinos/Tusoteuthis/PrimalItemResource_SquidOil.PrimalItemResource_SquidOil'",
            "Bingleberry Soup": "Blueprint'/Game/PrimalEarth/Test/PrimalItemConsumable_BerrySoup.PrimalItemConsumable_BerrySoup'",
            "Cactus Sap": "Blueprint'/Game/ScorchedEarth/CoreBlueprints/Consumables/PrimalItemConsumable_CactusSap.PrimalItemConsumable_CactusSap'",
            "Clay": "Blueprint'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_Clay.PrimalItemResource_Clay'",
            "Preserving Salt": "Blueprint'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_PreservingSalt.PrimalItemResource_PreservingSalt'",
            "Propellant": "Blueprint'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_Propellant.PrimalItemResource_Propellant'",
            "Raw Salt": "Blueprint'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_RawSalt.PrimalItemResource_RawSalt'",
            "Sand": "Blueprint'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_Sand.PrimalItemResource_Sand'",
            "Silk": "Blueprint'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_Silk.PrimalItemResource_Silk'",
            "Sulfur": "Blueprint'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_Sulfur.PrimalItemResource_Sulfur'",
            "Deathworm Horn": "Blueprint'/Game/ScorchedEarth/Dinos/Deathworm/PrimalItemResource_KeratinSpike.PrimalItemResource_KeratinSpike'",
            "Flamethrower Ammo": "Blueprint'/Game/ScorchedEarth/WeaponFlamethrower/PrimalItemAmmo_Flamethrower.PrimalItemAmmo_Flamethrower'",
            "Plant Species Y Seed": "Blueprint'/Game/ScorchedEarth/WeaponPlantSpeciesY/PrimalItemConsumable_Seed_PlantSpeciesY.PrimalItemConsumable_Seed_PlantSpeciesY'",
            "Plant Species Y Trap": "Blueprint'/Game/ScorchedEarth/WeaponPlantSpeciesY/PrimalItemStructure_PlantSpeciesYTrap.PrimalItemStructure_PlantSpeciesYTrap'"
        }
        
        self.default_potions = {
            "PrimalItemResource_StrengthPotion_C": "Potion of Strength",
            "PrimalItemResource_AgilityPotion_C": "Potion of Agility", 
            "PrimalItemResource_IntelligencePotion_C": "Potion of Intellect",
            "PrimalItemConsumable_DamagePotion_C": "Damage Potion",
            "PrimalItemConsumable_FortitudePotion_C": "Fortitude Potion",
            "PrimalItemConsumable_Increment25Health_C": "25% Health Potion",
            "PrimalItemConsumable_Increment50Health_C": "50% Health Potion",
            "PrimalItemConsumable_FullHealth_C": "100% Health Potion",
            "PrimalItemConsumable_BuffHealthPotion_C": "Buff Health Potion",
            "PrimalItemConsumable_HarvestPotion_C": "Harvest Potion",
            "PrimalItemConsumable_X2WeightPotion_C": "Weight Potion 2X",
            "PrimalItemConsumable_X5WeightPotion_C": "Weight Potion 5X",
            "PrimalItemConsumable_X10WeightPotion_C": "Weight Potion 10X",
            "PrimalItemConsumable_MutationPotion_C": "Mutation Potion",
            "PrimalItemConsumable_AgeStopPotion_C": "Maturation Stop Potion",
            "PrimalItemConsumable_SkillPointPotion_C": "Skill Tree Potion",
            "PrimalItemConsumable_FlyPotion_C": "Fly Potion",
            "PrimalItemConsumable_BuffInvisiblePotion_C": "Invisible Potion",
            "PrimalItemConsumable_BuffHazardShield_C": "Hazard Shield Potion",
            "PrimalItemConsumable_BuffStamina_C": "Buff Stamina Potion",
            "PrimalItemConsumable_FullStamina_C": "100% Stamina Potion",
            "PrimalItemConsumable_SpeedPotionX3_C": "Lesser Speed Potion",
            "PrimalItemConsumable_SpeedPotion_C": "Speed Potion",
            "PrimalItemConsumable_SpeedPotionUnderwather_C": "Aquatic Speed Potion",
            "PrimalItemConsumable_BreathingPotion_C": "Breathing potion",
            "PrimalItemConsumable_SedativePotion_C": "Sedative Potion",
            "PrimalItemConsumable_StimulantPotion_C": "Stimulant Potion",
            "PrimalItemConsumable_FoodPotion_C": "Food Potion",
            "PrimalItemConsumable_NightVisionPotion_C": "Night Vision Potion",
            "PrimalItemConsumable_OwlVisionPotion_C": "Predator Vision Potion",
            "PrimalItemConsumable_ScoutVisionPotion_C": "XRay Vision Potion",
            "PrimalItemConsumable_SpyPotion_C": "Spy Potion",
            "PrimalItemConsumable_BuffCraftPotionV2_C": "Adaptive Crafting Potion",
            "PrimalItemConsumable_BuffCraftPotion_C": "Crafting Potion",
            "PrimalItemConsumable_HairPotion_C": "Hairs Potion",
            "PrimalItemConsumable_BossesPotion_C": "Bosses Potion",
            "PrimalItemConsumable_LioPotion_C": "Loot Potion",
            "PrimalItemConsumable_TamePotion_C": "Tame Potion",
            "PrimalItemConsumable_AdultPotion_C": "GrowUp Potion",
            "PrimalItemConsumable_50ResetMating_C": "50% Reset Mating Potion",
            "PrimalItemConsumable_ResetMating_C": "Reset Mating Potion",
            "PrimalItemConsumable_AllowBreeding_C": "Allow Breeding Potion",
            "PrimalItemConsumable_AssignGender_C": "Assign Gender Potion",
            "PrimalItemConsumable_GenderChange_C": "Gender Change Potion",
            "PrimalItemConsumable_ColorPotion_C": "Color Potion",
            "PrimalItemConsumable_RandomTraitPotion_C": "Random Trait Potion",
            "PrimalItemConsumable_RandomTrait3TPotion_C": "Random Trait 3 Potion",
            "PrimalItemConsumable_100ImprintPotion_C": "Imprint Potion",
            "PrimalItemConsumable_Inc100ImprintPotion_C": "Imprint Potion +100",
            "PrimalItemConsumable_500ImprintPotion_C": "Imprint Potion 500",
            "PrimalItemConsumable_ImprintOwnerPotion_C": "Imprint Owner Potion",
            "PrimalItemConsumable_X2ExpPotion_C": "2x Experience Potion",
            "PrimalItemConsumable_X4ExpPotion_C": "4x Experience Potion",
            "PrimalItemConsumable_MaxExpPotion_C": "MAX Experience Potion",
            "PrimalItemConsumable_NotesPotion_C": "Notes Potion",
            "PrimalItemConsumable_IncrementBaseHp_C": "Dino Potion of Health +10",
            "PrimalItemConsumable_IncrementBaseDamage_C": "Dino Potion of Damage +10",
            "PrimalItemConsumable_IncrementBaseStamina_C": "Dino Potion of Stamina +10",
            "PrimalItemConsumable_IncrementBaseFood_C": "Dino Potion of Food +10",
            "PrimalItemConsumable_IncrementBaseWeight_C": "Dino Potion of Weight +10",
            "PrimalItemConsumable_IncrementBaseOxygen_C": "Dino Potion of Oxygen +10",
            "PrimalItemConsumable_IncrementBaseCraft_C": "Dino Potion of Craft +10",
            "PrimalItemConsumable_DinoAntidot_C": "Dino Antidote",
            "PrimalItemConsumable_DwarfAle_C": "Dwarf Ale",
            "PrimalItemConsumable_ElvenAle_C": "Elven Ale",
            "PrimalItemConsumable_TPPlayerStatslMindWipe_C": "Mindwipe Tonic: Player Stats",
            "PrimalItemConsumable_TPEngramsMindWipe_C": "Mindwipe Tonic: Engrams",
            "PrimalItemConsumable_TPSkillTreeMindWipe_C": "Mindwipe Tonic: Skill Tree",
            "PrimalItemConsumable_TPDinoMindWipe_C": "Mindwipe Tonic: Dino Stats"
        }
        
        
        self.config_data = {
            "CustomPotionRecipes": {}
        }
        
        # Variable to store currently selected potion
        self.current_potion_id = None

        self.load_data()
        self.create_widgets()

        # Add this line to ensure JSON views are updated after initialization
        self.update_json_views()
        
    def load_data(self):
        """Load data from files or use default values"""
        try:
            if os.path.exists("items.json"):
                with open("items.json", "r", encoding="utf-8") as f:
                    self.default_items = json.load(f)
        except:
            pass
            
        try:
            if os.path.exists("potions.json"):
                with open("potions.json", "r", encoding="utf-8") as f:
                    self.default_potions = json.load(f)
        except:
            pass
            
        try:
            if os.path.exists("config.json"):
                with open("config.json", "r", encoding="utf-8") as f:
                    self.config_data = json.load(f)
                # Add this line to update JSON views after loading config
                self.update_json_views()
        except:
            pass
    
    def save_data(self):
        """Save all data to files"""
        try:
            with open("items.json", "w", encoding="utf-8") as f:
                json.dump(self.default_items, f, indent=2, ensure_ascii=False)
                
            with open("potions.json", "w", encoding="utf-8") as f:
                json.dump(self.default_potions, f, indent=2, ensure_ascii=False)
                
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(self.config_data, f, indent=2, ensure_ascii=False)
                
            # Auto-update JSON views
            self.update_json_views()
                
            messagebox.showinfo("Success", "Data saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error while saving: {str(e)}")
    
    def create_widgets(self):
        """Create interface"""
        # Create tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Main tab - recipe editing
        self.main_frame = ttk.Frame(notebook)
        notebook.add(self.main_frame, text="Potion Recipes")
        
        # Items editing tab
        self.items_frame = ttk.Frame(notebook)
        notebook.add(self.items_frame, text="Ark Items List")
        
        # Potions editing tab
        self.potions_frame = ttk.Frame(notebook)
        notebook.add(self.potions_frame, text="Potions List")
        
        # New tab - readable JSON
        self.compressed_json_frame = ttk.Frame(notebook)
        notebook.add(self.compressed_json_frame, text="Readable JSON")
        
        # New tab - JSON in URL format
        self.url_json_frame = ttk.Frame(notebook)
        notebook.add(self.url_json_frame, text="JSON in URL")
        
        self.setup_main_tab()
        self.setup_items_tab()
        self.setup_potions_tab()
        self.setup_compressed_json_tab()
        self.setup_url_json_tab()
        
        # Button panel
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(button_frame, text="Save All Data", command=self.save_data).pack(side=tk.RIGHT, padx=5)
        ttk.Button(button_frame, text="Load JSON", command=self.load_json).pack(side=tk.RIGHT, padx=5)
        ttk.Button(button_frame, text="Export JSON", command=self.export_json).pack(side=tk.RIGHT, padx=5)
    
    def setup_compressed_json_tab(self):
        """Setup readable JSON tab"""
        # Header
        ttk.Label(self.compressed_json_frame, text="Readable JSON Config", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Text field for JSON with scrollbar
        json_frame = ttk.Frame(self.compressed_json_frame)
        json_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Scrollbar for text field
        json_scrollbar = ttk.Scrollbar(json_frame)
        json_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.compressed_json_text = tk.Text(json_frame, yscrollcommand=json_scrollbar.set, 
                                       wrap=tk.WORD, font=('Consolas', 10), state='disabled')
        self.compressed_json_text.pack(fill=tk.BOTH, expand=True)
        json_scrollbar.config(command=self.compressed_json_text.yview)
        
        # Buttons
        button_frame = ttk.Frame(self.compressed_json_frame)
        button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(button_frame, text="Copy to Clipboard", command=self.copy_compressed_json).pack(side=tk.LEFT, padx=5)

    def setup_url_json_tab(self):
        """Setup JSON in URL format tab"""
        # Header
        ttk.Label(self.url_json_frame, text="Compressed JSON in URL Format", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Text field for URL with scrollbar
        url_frame = ttk.Frame(self.url_json_frame)
        url_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Scrollbar for text field
        url_scrollbar = ttk.Scrollbar(url_frame)
        url_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.url_json_text = tk.Text(url_frame, yscrollcommand=url_scrollbar.set, 
                                wrap=tk.WORD, font=('Consolas', 10), state='disabled')
        self.url_json_text.pack(fill=tk.BOTH, expand=True)
        url_scrollbar.config(command=self.url_json_text.yview)
        
        # Buttons
        button_frame = ttk.Frame(self.url_json_frame)
        button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(button_frame, text="Copy to Clipboard", command=self.copy_url_json).pack(side=tk.LEFT, padx=5)

    def update_compressed_json_view(self):
        """Update readable JSON view"""
        try:
            # Beautiful formatted JSON with indentation
            formatted_json = json.dumps(self.config_data, indent=2, ensure_ascii=False)
            
            # Temporarily enable editing to update content
            self.compressed_json_text.config(state='normal')
            self.compressed_json_text.delete(1.0, tk.END)
            self.compressed_json_text.insert(1.0, formatted_json)
            self.compressed_json_text.config(state='disabled')
        except Exception as e:
            self.compressed_json_text.config(state='normal')
            self.compressed_json_text.delete(1.0, tk.END)
            self.compressed_json_text.insert(1.0, f"Error creating JSON: {str(e)}")
            self.compressed_json_text.config(state='disabled')

    def update_url_json_view(self):
        """Update JSON in URL format view"""
        try:
            import urllib.parse
            # Compressed JSON without spaces for URL
            compressed_json = json.dumps(self.config_data, separators=(',', ':'), ensure_ascii=False)
            url_encoded_json = urllib.parse.quote(compressed_json)
            
            # Temporarily enable editing to update content
            self.url_json_text.config(state='normal')
            self.url_json_text.delete(1.0, tk.END)
            self.url_json_text.insert(1.0, url_encoded_json)
            self.url_json_text.config(state='disabled')
        except Exception as e:
            self.url_json_text.config(state='normal')
            self.url_json_text.delete(1.0, tk.END)
            self.url_json_text.insert(1.0, f"Error creating URL JSON: {str(e)}")
            self.url_json_text.config(state='disabled')

    def update_json_views(self):
        """Update all JSON views"""
        self.update_compressed_json_view()
        self.update_url_json_view()

    def copy_compressed_json(self):
        """Copy compressed JSON to clipboard"""
        # Temporarily enable to get content
        self.compressed_json_text.config(state='normal')
        compressed_json = self.compressed_json_text.get(1.0, tk.END).strip()
        self.compressed_json_text.config(state='disabled')
        
        if compressed_json:
            self.root.clipboard_clear()
            self.root.clipboard_append(compressed_json)
            messagebox.showinfo("Success", "Compressed JSON copied to clipboard")

    def copy_url_json(self):
        """Copy URL JSON to clipboard"""
        # Temporarily enable to get content
        self.url_json_text.config(state='normal')
        url_json = self.url_json_text.get(1.0, tk.END).strip()
        self.url_json_text.config(state='disabled')
        
        if url_json:
            self.root.clipboard_clear()
            self.root.clipboard_append(url_json)
            messagebox.showinfo("Success", "URL JSON copied to clipboard")

    def setup_main_tab(self):
        """Setup main recipe editing tab"""
        # Left part - potions list
        left_frame = ttk.LabelFrame(self.main_frame, text="Potions")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add scrollbar for potions list
        potions_scrollbar = ttk.Scrollbar(left_frame)
        potions_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.potions_listbox = tk.Listbox(left_frame, yscrollcommand=potions_scrollbar.set)
        self.potions_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        potions_scrollbar.config(command=self.potions_listbox.yview)
        self.potions_listbox.bind('<<ListboxSelect>>', self.on_potion_select)
        
        # Buttons for potions
        potion_buttons = ttk.Frame(left_frame)
        potion_buttons.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(potion_buttons, text="Add Potion", command=self.add_potion_to_config).pack(side=tk.LEFT, padx=2)
        ttk.Button(potion_buttons, text="Remove Potion", command=self.remove_potion_from_config).pack(side=tk.LEFT, padx=2)
        
        # Right part - selected potion recipe
        right_frame = ttk.LabelFrame(self.main_frame, text="Potion Recipe")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Recipe items list with scrollbar
        self.recipe_frame = ttk.Frame(right_frame)
        self.recipe_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        recipe_scrollbar = ttk.Scrollbar(self.recipe_frame)
        recipe_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.recipe_listbox = tk.Listbox(self.recipe_frame, yscrollcommand=recipe_scrollbar.set)
        self.recipe_listbox.pack(fill=tk.BOTH, expand=True)
        recipe_scrollbar.config(command=self.recipe_listbox.yview)
        
        # Buttons for recipe
        recipe_buttons = ttk.Frame(right_frame)
        recipe_buttons.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(recipe_buttons, text="Add Item", command=self.add_item_to_recipe).pack(side=tk.LEFT, padx=2)
        ttk.Button(recipe_buttons, text="Remove Item", command=self.remove_item_from_recipe).pack(side=tk.LEFT, padx=2)
        ttk.Button(recipe_buttons, text="Edit Quantity", command=self.edit_quantity).pack(side=tk.LEFT, padx=2)
        
        self.update_potions_list()

    def setup_items_tab(self):
        """Setup items editing tab"""
        # Items list
        items_list_frame = ttk.LabelFrame(self.items_frame, text="Items List")
        items_list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add scrollbar for items list
        items_scrollbar = ttk.Scrollbar(items_list_frame)
        items_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.items_listbox = tk.Listbox(items_list_frame, yscrollcommand=items_scrollbar.set)
        self.items_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        items_scrollbar.config(command=self.items_listbox.yview)
        
        # Buttons for items
        items_buttons = ttk.Frame(items_list_frame)
        items_buttons.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(items_buttons, text="Add Item", command=self.add_item).pack(side=tk.LEFT, padx=2)
        ttk.Button(items_buttons, text="Edit Item", command=self.edit_item).pack(side=tk.LEFT, padx=2)
        ttk.Button(items_buttons, text="Delete Item", command=self.delete_item).pack(side=tk.LEFT, padx=2)
        
        self.update_items_list()

    def setup_potions_tab(self):
        """Setup potions editing tab"""
        # Potions list
        potions_list_frame = ttk.LabelFrame(self.potions_frame, text="Potions List")
        potions_list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add scrollbar for potions list
        potions_edit_scrollbar = ttk.Scrollbar(potions_list_frame)
        potions_edit_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.potions_edit_listbox = tk.Listbox(potions_list_frame, yscrollcommand=potions_edit_scrollbar.set)
        self.potions_edit_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        potions_edit_scrollbar.config(command=self.potions_edit_listbox.yview)
        
        # Buttons for potions
        potions_buttons = ttk.Frame(potions_list_frame)
        potions_buttons.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(potions_buttons, text="Add Potion", command=self.add_potion).pack(side=tk.LEFT, padx=2)
        ttk.Button(potions_buttons, text="Edit Potion", command=self.edit_potion).pack(side=tk.LEFT, padx=2)
        ttk.Button(potions_buttons, text="Delete Potion", command=self.delete_potion).pack(side=tk.LEFT, padx=2)
        
        self.update_potions_edit_list()
    
    def update_items_list(self):
        """Update items list"""
        self.items_listbox.delete(0, tk.END)
        for item_name, item_class in self.default_items.items():
            self.items_listbox.insert(tk.END, f"{item_name} -> {item_class}")
    
    def update_potions_list(self):
        """Update potions list in main tab"""
        self.potions_listbox.delete(0, tk.END)
        for potion_id in self.config_data["CustomPotionRecipes"]:
            display_name = self.default_potions.get(potion_id, potion_id)
            self.potions_listbox.insert(tk.END, f"{potion_id} ({display_name})")
    
    def update_potions_edit_list(self):
        """Update potions list in editing tab"""
        self.potions_edit_listbox.delete(0, tk.END)
        for potion_id, potion_name in self.default_potions.items():
            # Swap order: name first, then ID
            self.potions_edit_listbox.insert(tk.END, f"{potion_name} -> {potion_id}")
    
    def update_recipe_list(self, potion_id):
        """Update recipe list"""
        self.recipe_listbox.delete(0, tk.END)
        if potion_id in self.config_data["CustomPotionRecipes"]:
            recipe = self.config_data["CustomPotionRecipes"][potion_id]["RequiredItems"]
            for item in recipe:
                item_class = item["ItemClass"]
                quantity = item["Quantity"]
                # Find display name for item
                display_name = next((name for name, cls in self.default_items.items() if cls == item_class), item_class)
                self.recipe_listbox.insert(tk.END, f"{display_name} x{quantity}")
    
    def on_potion_select(self, event):
        """Handle potion selection"""
        selection = self.potions_listbox.curselection()
        if selection:
            potion_text = self.potions_listbox.get(selection[0])
            self.current_potion_id = potion_text.split(" (")[0]  # Save current potion ID
            potion_id = potion_text.split(" (")[0]
            self.update_recipe_list(potion_id)
    
    def add_item(self):
        """Add new item"""
        name = simpledialog.askstring("Add Item", "Enter item name:")
        if name:
            class_path = simpledialog.askstring("Add Item", "Enter ItemClass path:")
            if class_path:
                self.default_items[name] = class_path
                self.update_items_list()
    
    def edit_item(self):
        """Edit item"""
        selection = self.items_listbox.curselection()
        if selection:
            item_text = self.items_listbox.get(selection[0])
            # Format: "Name -> path"
            old_name = item_text.split(" -> ")[0]  # Get first part (name)
            
            new_name = simpledialog.askstring("Edit Item", "Enter new name:", initialvalue=old_name)
            if new_name:
                new_class = simpledialog.askstring("Edit Item", "Enter new ItemClass:", 
                                                initialvalue=self.default_items[old_name])
                if new_class:
                    if old_name != new_name:
                        del self.default_items[old_name]
                    self.default_items[new_name] = new_class
                    self.update_items_list()
    
    def delete_item(self):
        """Delete item"""
        selection = self.items_listbox.curselection()
        if selection:
            item_text = self.items_listbox.get(selection[0])
            # Format: "Name -> path"
            item_name = item_text.split(" -> ")[0]  # Get first part (name)
            if messagebox.askyesno("Delete Item", f"Delete item '{item_name}'?"):
                del self.default_items[item_name]
                self.update_items_list()
    
    def add_potion(self):
        """Add new potion"""
        potion_id = simpledialog.askstring("Add Potion", "Enter potion ID (e.g.: PrimalItemResource_StrengthPotion_C):")
        if potion_id:
            potion_name = simpledialog.askstring("Add Potion", "Enter display name:")
            if potion_name:
                self.default_potions[potion_id] = potion_name
                self.update_potions_edit_list()
                self.update_potions_list()
    
    def edit_potion(self):
        """Edit potion"""
        selection = self.potions_edit_listbox.curselection()
        if selection:
            potion_text = self.potions_edit_listbox.get(selection[0])
            # Format: "Name -> ID"
            old_id = potion_text.split(" -> ")[1]  # Get second part (ID)
            
            new_id = simpledialog.askstring("Edit Potion", "Enter new ID:", initialvalue=old_id)
            if new_id:
                new_name = simpledialog.askstring("Edit Potion", "Enter new name:", 
                                                initialvalue=self.default_potions[old_id])
                if new_name:
                    if old_id != new_id:
                        del self.default_potions[old_id]
                        # Update recipe if exists
                        if old_id in self.config_data["CustomPotionRecipes"]:
                            self.config_data["CustomPotionRecipes"][new_id] = self.config_data["CustomPotionRecipes"][old_id]
                            del self.config_data["CustomPotionRecipes"][old_id]
                    
                    self.default_potions[new_id] = new_name
                    self.update_potions_edit_list()
                    self.update_potions_list()

    def delete_potion(self):
        """Delete potion"""
        selection = self.potions_edit_listbox.curselection()
        if selection:
            potion_text = self.potions_edit_listbox.get(selection[0])
            # Format: "Name -> ID"
            potion_id = potion_text.split(" -> ")[1]  # Get second part (ID)
            if messagebox.askyesno("Delete Potion", f"Delete potion '{potion_id}'?"):
                del self.default_potions[potion_id]
                if potion_id in self.config_data["CustomPotionRecipes"]:
                    del self.config_data["CustomPotionRecipes"][potion_id]
                self.update_potions_edit_list()
                self.update_potions_list()
    
    def add_potion_to_config(self):
        """Add potion to config for recipe editing"""
        if not self.default_potions:
            messagebox.showwarning("Warning", "First add potions in 'Potions' tab")
            return
            
        potion_list = list(self.default_potions.keys())
        # For potions show both name and ID
        selection_dialog = SelectionDialog(self.root, "Select Potion", potion_list, self.default_potions, show_path=True)
        self.root.wait_window(selection_dialog.dialog)
        
        if selection_dialog.result:
            potion_id = selection_dialog.result
            if potion_id not in self.config_data["CustomPotionRecipes"]:
                self.config_data["CustomPotionRecipes"][potion_id] = {"RequiredItems": []}
                self.update_potions_list()
                self.update_json_views()
    
    def remove_potion_from_config(self):
        """Remove potion from config"""
        if not self.current_potion_id:
            messagebox.showwarning("Warning", "First select a potion")
            return
            
        if messagebox.askyesno("Delete Potion", f"Delete recipe for '{self.current_potion_id}'?"):
            del self.config_data["CustomPotionRecipes"][self.current_potion_id]
            self.current_potion_id = None  # Reset current potion
            self.update_potions_list()
            self.recipe_listbox.delete(0, tk.END)
            self.update_json_views()
    
    def add_item_to_recipe(self):
        """Add item to recipe"""
        if not self.current_potion_id:
            messagebox.showwarning("Warning", "First select a potion")
            return
            
        if not self.default_items:
            messagebox.showwarning("Warning", "First add items in 'Items' tab")
            return
            
        item_list = list(self.default_items.keys())
        # For items show only names
        selection_dialog = SelectionDialog(self.root, "Select Item", item_list, {}, show_path=False, is_items=True)
        self.root.wait_window(selection_dialog.dialog)
        
        if selection_dialog.result:
            item_name = selection_dialog.result
            quantity = simpledialog.askinteger("Quantity", "Enter quantity:", 
                                            initialvalue=1, minvalue=1,
                                            parent=self.root)
            if quantity:
                item_class = self.default_items[item_name]
                new_item = {"ItemClass": item_class, "Quantity": quantity}
                
                if self.current_potion_id not in self.config_data["CustomPotionRecipes"]:
                    self.config_data["CustomPotionRecipes"][self.current_potion_id] = {"RequiredItems": []}
                
                self.config_data["CustomPotionRecipes"][self.current_potion_id]["RequiredItems"].append(new_item)
                self.update_recipe_list(self.current_potion_id)
                self.update_json_views()
        
    def remove_item_from_recipe(self):
        """Remove item from recipe"""
        selection_item = self.recipe_listbox.curselection()
        
        if not selection_item:
            messagebox.showwarning("Warning", "First select an item in the recipe to remove")
            return
            
        if not self.current_potion_id:
            messagebox.showwarning("Warning", "First select a potion")
            return
            
        item_index = selection_item[0]
        self.config_data["CustomPotionRecipes"][self.current_potion_id]["RequiredItems"].pop(item_index)
        self.update_recipe_list(self.current_potion_id)
        self.update_json_views()

    def edit_quantity(self):
        """Edit item quantity in recipe"""
        selection_item = self.recipe_listbox.curselection()
        
        if not selection_item:
            messagebox.showwarning("Warning", "First select an item in the recipe to edit quantity")
            return
            
        if not self.current_potion_id:
            messagebox.showwarning("Warning", "First select a potion")
            return
            
        item_index = selection_item[0]
        current_quantity = self.config_data["CustomPotionRecipes"][self.current_potion_id]["RequiredItems"][item_index]["Quantity"]
        
        new_quantity = simpledialog.askinteger("Quantity", "Enter new quantity:", 
                                            initialvalue=current_quantity, minvalue=1,
                                            parent=self.root)
        if new_quantity:
            self.config_data["CustomPotionRecipes"][self.current_potion_id]["RequiredItems"][item_index]["Quantity"] = new_quantity
            self.update_recipe_list(self.current_potion_id)
            self.update_json_views()
    
    def load_json(self):
        """Load JSON file"""
        from tkinter import filedialog
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if filename:
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    loaded_data = json.load(f)
                
                if "CustomPotionRecipes" in loaded_data:
                    self.config_data = loaded_data
                    self.update_potions_list()
                    # Auto-update JSON views
                    self.update_json_views()
                    messagebox.showinfo("Success", "JSON file loaded successfully!")
                else:
                    messagebox.showerror("Error", "Invalid JSON file format")
            except Exception as e:
                messagebox.showerror("Error", f"Error while loading: {str(e)}")
    
    def export_json(self):
        """Export JSON file"""
        from tkinter import filedialog
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filename:
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(self.config_data, f, indent=2, ensure_ascii=False)
                messagebox.showinfo("Success", "JSON file exported successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error while exporting: {str(e)}")


class SelectionDialog:
    """Dialog for selecting element from list"""
    def __init__(self, parent, title, items, display_dict, show_path=False, is_items=False):
        self.dialog = tk.Toplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("500x400")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        self.result = None
        self.all_items = items  # Save all elements
        self.display_dict = display_dict
        self.show_path = show_path
        self.is_items = is_items
        
        ttk.Label(self.dialog, text=title).pack(padx=10, pady=5)
        
        # Search bar
        search_frame = ttk.Frame(self.dialog)
        search_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(search_frame, text="Search:").pack(side=tk.LEFT, padx=(0, 5))
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        search_entry.bind('<KeyRelease>', self.on_search)
        
        # Add scrollbar for selection dialog
        list_frame = ttk.Frame(self.dialog)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, font=('Arial', 10))
        self.listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)
        
        # Fill list with all elements
        self.filtered_items = self.all_items[:]
        self.update_listbox()
        
        button_frame = ttk.Frame(self.dialog)
        button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(button_frame, text="Select", command=self.on_select).pack(side=tk.RIGHT, padx=5)
        ttk.Button(button_frame, text="Cancel", command=self.dialog.destroy).pack(side=tk.RIGHT, padx=5)
        
        self.listbox.bind('<Double-Button-1>', lambda e: self.on_select())
        # Focus on search field when opening
        search_entry.focus_set()
    
    def on_search(self, event):
        """Handle search"""
        search_text = self.search_var.get().lower()
        
        if self.is_items:
            # For items: search by names
            self.filtered_items = [item for item in self.all_items if search_text in item.lower()]
        else:
            # For potions: search by names from display_dict
            self.filtered_items = []
            for item_id in self.all_items:
                display_name = self.display_dict.get(item_id, item_id)
                if search_text in display_name.lower() or search_text in item_id.lower():
                    self.filtered_items.append(item_id)
        
        self.update_listbox()
    
    def update_listbox(self):
        """Update list with filter"""
        self.listbox.delete(0, tk.END)
        
        if self.is_items:
            # For items: just sort filtered names
            sorted_items = sorted(self.filtered_items)
            for item_name in sorted_items:
                self.listbox.insert(tk.END, item_name)
        else:
            # For potions: create list for sorting by name
            sorted_items = []
            for item_id in self.filtered_items:
                display_name = self.display_dict.get(item_id, item_id)
                sorted_items.append((display_name, item_id))
            
            # Sort by name
            sorted_items.sort(key=lambda x: x[0])
            
            for display_name, item_id in sorted_items:
                if self.show_path:
                    # For potions: name -> ID
                    self.listbox.insert(tk.END, f"{display_name} -> {item_id}")
                else:
                    # For other cases: only name
                    self.listbox.insert(tk.END, f"{display_name}")
    
    def on_select(self):
        """Handle element selection"""
        selection = self.listbox.curselection()
        if selection:
            if self.is_items:
                # For items: just get selected name
                self.result = self.listbox.get(selection[0])
            elif self.show_path:
                # For potions: format "Name -> ID", get ID
                selected_text = self.listbox.get(selection[0])
                self.result = selected_text.split(" -> ")[1]
            else:
                # For other cases: find ID by name
                selected_display_name = self.listbox.get(selection[0])
                for item_id, display_name in self.display_dict.items():
                    if display_name == selected_display_name:
                        self.result = item_id
                        break
            self.dialog.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = JSONConfigEditor(root)
    root.mainloop()