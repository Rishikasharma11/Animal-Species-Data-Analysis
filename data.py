import pandas as pd
import numpy as np

data = pd.DataFrame({
    'Animal_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32],
    
    'Species': ['Elephant', 'Lion', 'Panda', 'Giraffe', 'Tiger', 'Kangaroo', 'Koala', 'Penguin', 'Gorilla', 'Polar Bear', 'Wolf', 'Cheetah', 'Rhino', 'Zebra', 'Orangutan', 'Bald Eagle', 'Sloth', 'Crocodile', 'Blue Whale', 'Flamingo', 'Lemur', 'Eagle', 'Shark', 'Turtle', 'Ostrich', 'Dolphin', 'Bat', 'Deer', 'Camel', 'Leopard', 'Hippo', 'Antelope'],
    
    'Habitat': ['Savanna', 'Grassland', 'Forest', 'Savanna', 'Forest', 'Desert', 'Forest', 'Coastal', 'Forest', 'Arctic', 'Forest', 'Grassland', 'Savanna', 'Savanna', 'Rainforest', 'Forest', 'Rainforest', 'Wetlands', 'Ocean', 'Wetlands', 'Rainforest', 'Mountains', 'Ocean', 'Ocean', 'Grassland', 'Ocean', 'Cave', 'Forest', 'Desert', 'Forest', 'Wetlands', 'Savanna'],
    
    'Weight (kg)': [5400, 190, 100, 800, 220, 85, 15, 35, 160, 450, 50, 70, 2300, 380, 70, 6, 4, 500, 150000, 3, 3.5, 7, 1000, 300, 100, 200, 0.03, 90, 600, 80, 1500, 80],
    
    'Present Age (years)': [25, 10, 5, 12, 8, 6, 4, 9, 20, 15, 6, 5, 20, 10, 35, 14, 8, 30, 90, 20, 6, 12, 30, 50, 15, 12, 5, 10, 20, 7, 30, 8],
    
    'Conservation_Status': ['Vulnerable', 'Vulnerable', 'Endangered', 'Vulnerable', 'Endangered', 'Least Concern', 'Vulnerable', 'Near Threatened', 'Critically Endangered', 'Vulnerable', 'Least Concern', 'Vulnerable', 'Critically Endangered', 'Least Concern', 'Critically Endangered', 'Least Concern', 'Vulnerable', 'Least Concern', 'Endangered', 'Least Concern', 'Endangered', 'Least Concern', 'Vulnerable', 'Endangered', 'Least Concern', 'Least Concern', 'Least Concern', 'Least Concern', 'Vulnerable', 'Least Concern', 'Vulnerable', 'Least Concern'],
    
    'Lifespan (years)': [60, 15, 20, 25, 20, 12, 13, 20, 40, 25, 13, 12, 40, 20, 40, 20, 30, 70, 90, 30, 20, 15, 70, 100, 40, 40, 10, 15, 40, 15, 40, 12],

    'Category': ['Herbivore', 'Carnivore', 'Herbivore', 'Herbivore', 'Carnivore', 'Herbivore', 'Herbivore', 'Carnivore', 'Omnivore', 'Carnivore', 'Carnivore', 'Carnivore', 'Herbivore', 'Herbivore', 'Omnivore', 'Carnivore', 'Herbivore', 'Carnivore', 'Carnivore', 'Omnivore', 'Omnivore', 'Carnivore', 'Carnivore', 'Herbivore', 'Omnivore', 'Carnivore', 'Omnivore', 'Herbivore', 'Herbivore', 'Carnivore', 'Omnivore', 'Herbivore'],

    'Top_Speed (km/h)': [40, 80, 20, 60, 65, 71, 30, 6, 40, 56, 65, 110, 55, 65, 40, 160, 0.27, 24, 48, 6, 12, 160, 56, 2, 70, 60, 100, 80, 65, 58, 40, 90],

    'Population_in_the_Wild': [415000, 20000, 1864, 117000, 3900, 50000, 80000, 1200000, 1000, 26000, 300000, 7100, 27500, 750000, 10000, 70000, 1500, 2000000, 10000, 19000, 2000, 100000, 1000000, 2300000, 50000, 600000, 450000, 2000000, 35000, 180000, 130000, 550000],

    'Endemic_Regions': ['Africa', 'Africa', 'China', 'Africa', 'Asia', 'Australia', 'Australia', 'Antarctica', 'Africa', 'Arctic', 'North America', 'Africa', 'Africa', 'Africa', 'Asia', 'North America', 'South America', 'Africa', 'Global', 'South America', 'Madagascar', 'Global', 'Global', 'Global', 'Africa', 'Global', 'Global', 'Global', 'Africa', 'Africa', 'Africa', 'Africa'],

    'Human_Interaction': ['Low', 'Medium', 'Medium', 'Low', 'Medium', 'Low', 'Low', 'High', 'Medium', 'Medium', 'Low', 'Medium', 'Low', 'Medium', 'Medium', 'Medium', 'Low', 'Low', 'Low', 'Medium', 'Medium', 'Low', 'Low', 'Low', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'Medium']

})

print(data.to_string)

import pandas as pd
import numpy as np

data = pd.DataFrame({
    'Animal_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32],
    
    'Species': ['Elephant', 'Lion', 'Panda', 'Giraffe', 'Tiger', 'Kangaroo', 'Koala', 'Penguin', 'Gorilla', 'Polar Bear', 'Wolf', 'Cheetah', 'Rhino', 'Zebra', 'Orangutan', 'Bald Eagle', 'Sloth', 'Crocodile', 'Blue Whale', 'Flamingo', 'Lemur', 'Eagle', 'Shark', 'Turtle', 'Ostrich', 'Dolphin', 'Bat', 'Deer', 'Camel', 'Leopard', 'Hippo', 'Antelope'],
    
    'Habitat': ['Savanna', 'Grassland', 'Forest', 'Savanna', 'Forest', 'Desert', 'Forest', 'Coastal', 'Forest', 'Arctic', 'Forest', 'Grassland', 'Savanna', 'Savanna', 'Rainforest', 'Forest', 'Rainforest', 'Wetlands', 'Ocean', 'Wetlands', 'Rainforest', 'Mountains', 'Ocean', 'Ocean', 'Grassland', 'Ocean', 'Cave', 'Forest', 'Desert', 'Forest', 'Wetlands', 'Savanna'],
    
    'Weight (kg)': [5400, 190, 100, 800, 220, 85, 15, 35, 160, 450, 50, 70, 2300, 380, 70, 6, 4, 500, 150000, 3, 3.5, 7, 1000, 300, 100, 200, 0.03, 90, 600, 80, 1500, 80],
    
    'Present Age (years)': [25, 10, 5, 12, 8, 6, 4, 9, 20, 15, 6, 5, 20, 10, 35, 14, 8, 30, 90, 20, 6, 12, 30, 50, 15, 12, 5, 10, 20, 7, 30, 8],
    
    'Conservation_Status': ['Vulnerable', 'Vulnerable', 'Endangered', 'Vulnerable', 'Endangered', 'Least Concern', 'Vulnerable', 'Near Threatened', 'Critically Endangered', 'Vulnerable', 'Least Concern', 'Vulnerable', 'Critically Endangered', 'Least Concern', 'Critically Endangered', 'Least Concern', 'Vulnerable', 'Least Concern', 'Endangered', 'Least Concern', 'Endangered', 'Least Concern', 'Vulnerable', 'Endangered', 'Least Concern', 'Least Concern', 'Least Concern', 'Least Concern', 'Vulnerable', 'Least Concern', 'Vulnerable', 'Least Concern'],
    
    'Lifespan (years)': [60, 15, 20, 25, 20, 12, 13, 20, 40, 25, 13, 12, 40, 20, 40, 20, 30, 70, 90, 30, 20, 15, 70, 100, 40, 40, 10, 15, 40, 15, 40, 12],

    'Category': ['Herbivore', 'Carnivore', 'Herbivore', 'Herbivore', 'Carnivore', 'Herbivore', 'Herbivore', 'Carnivore', 'Omnivore', 'Carnivore', 'Carnivore', 'Carnivore', 'Herbivore', 'Herbivore', 'Omnivore', 'Carnivore', 'Herbivore', 'Carnivore', 'Carnivore', 'Omnivore', 'Omnivore', 'Carnivore', 'Carnivore', 'Herbivore', 'Omnivore', 'Carnivore', 'Omnivore', 'Herbivore', 'Herbivore', 'Carnivore', 'Omnivore', 'Herbivore'],

    'Top_Speed (km/h)': [40, 80, 20, 60, 65, 71, 30, 6, 40, 56, 65, 110, 55, 65, 40, 160, 0.27, 24, 48, 6, 12, 160, 56, 2, 70, 60, 100, 80, 65, 58, 40, 90],

    'Population_in_the_Wild': [415000, 20000, 1864, 117000, 3900, 50000, 80000, 1200000, 1000, 26000, 300000, 7100, 27500, 750000, 10000, 70000, 1500, 2000000, 10000, 19000, 2000, 100000, 1000000, 2300000, 50000, 600000, 450000, 2000000, 35000, 180000, 130000, 550000],

    'Endemic_Regions': ['Africa', 'Africa', 'China', 'Africa', 'Asia', 'Australia', 'Australia', 'Antarctica', 'Africa', 'Arctic', 'North America', 'Africa', 'Africa', 'Africa', 'Asia', 'North America', 'South America', 'Africa', 'Global', 'South America', 'Madagascar', 'Global', 'Global', 'Global', 'Africa', 'Global', 'Global', 'Global', 'Africa', 'Africa', 'Africa', 'Africa'],

    'Human_Interaction': ['Low', 'Medium', 'Medium', 'Low', 'Medium', 'Low', 'Low', 'High', 'Medium', 'Medium', 'Low', 'Medium', 'Low', 'Medium', 'Medium', 'Medium', 'Low', 'Low', 'Low', 'Medium', 'Medium', 'Low', 'Low', 'Low', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'Medium']

})

print(data.to_string)

# --------------------------------------Endemic_Regions----------------------------------------------------------------
# User input for species find in different regions
species_found = input("Enter the region to find species (Africa, Global, South America, Asia, North America, Australia, China, Antarctica, Arctic, Madagascar) : ").capitalize() 

if species_found in ['Africa', 'Global', 'South America', 'Asia', 'North America', 'Australia', 'China', 'Antarctica', 'Arctic', 'Madagascar']:
    species_found_in_region = data.loc[data['Endemic_Regions'] == species_found, ['Species']]
   
    if not species_found_in_region.empty:
        print(f"\nSpecies found in {species_found}:\n", species_found_in_region)
    else:
        print(f"\nNo species found in {species_found}.")

else:
    print("\nInvalid input! Please enter a valid region from the list.")


# --------------------------------------------Human_Interaction-----------------------------------------------
# User input for human interaction level
interaction_level = input("Enter the human interaction level (High, Medium, Low): ").capitalize()

# Animals based on the user's input
if interaction_level in ['High', 'Medium', 'Low']:
    interactive_animals = data.loc[data['Human_Interaction'] == interaction_level, ['Species']]
    print(f"\nAnimals with {interaction_level} human interaction: \n", interactive_animals)
else:
    print("\nInvalid input! Please enter High, Medium, or Low.")

