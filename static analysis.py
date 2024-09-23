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

# Species with the maximum lifespan
max_lifespan = data['Lifespan (years)'].max()
animal_with_max_lifespan = data.loc[data['Lifespan (years)'] == max_lifespan, ('Species','Lifespan (years)')]
print("Animal with maximum lifespan in years: \n", animal_with_max_lifespan, "\n")

# Species with the minimum lifespan
min_lifespan = data['Lifespan (years)'].min()
animal_with_min_lifespan = data.loc[data["Lifespan (years)"] == min_lifespan, ('Species','Lifespan (years)')]
print("Animal with shortest lifespan in years: \n", animal_with_min_lifespan, "\n")

# Average lifespan of Animals
avg_count_of_lifespan = data['Lifespan (years)'].mean()
print("Average Lifespan of Animals:", avg_count_of_lifespan, "\n")

# Maximum weight of Species
max_weight = data['Weight (kg)'].max()
animal_with_max_weight = data.loc[data['Weight (kg)'] == max_weight, ('Species', 'Weight (kg)')]
print("Animal with maximum weight: \n", animal_with_max_weight, "\n")

# Minimum weight of species
min_weight = data['Weight (kg)'].min()
animal_with_min_weight = data.loc[data['Weight (kg)'] == min_weight, ('Species', 'Weight (kg)')]
print("Animal with minimum weight: \n", animal_with_min_weight, "\n")

# Maximum age of animal
max_age = data['Present Age (years)'].max()
animal_with_max_age = data.loc[data['Present Age (years)'] == max_age, ['Species', 'Present Age (years)']]
print("Animal with maximum age: \n", animal_with_max_age, "\n")

# Minimum age of animal
min_age = data['Present Age (years)'].min()  
animal_with_min_age = data.loc[data['Present Age (years)'] == min_age, ['Species', 'Present Age (years)']]  
print("Animal with minimum age: \n", animal_with_min_age, "\n")

# Habitat count
habitat_count = data['Habitat'].value_counts()
print("Habitat count of Animals: \n", habitat_count, "\n")

# Animal lives in forest
animal_lives_in_forest = data.loc[data['Habitat'] == 'Forest', ('Species', 'Habitat')]
print("Animal lives in forest: \n", animal_lives_in_forest, "\n")

# Animal lives in Savanna
animal_lives_in_savanna = data.loc[data['Habitat'] == 'Savanna', ('Species', 'Habitat')]
print("Animal lives in Savanna: \n", animal_lives_in_savanna, "\n")

# Animal lives in Ocean
animal_lives_in_ocean = data.loc[data['Habitat'] == 'Ocean', ('Species', 'Habitat')]
print("Animal lives in Ocean: \n", animal_lives_in_ocean, "\n")

# Animal lives in Grassland
animal_lives_in_grassland = data.loc[data['Habitat'] == 'Grassland', ('Species', 'Habitat')]
print("Animal lives in Grassland: \n", animal_lives_in_grassland, "\n")

# Animal lives in Desert
animal_lives_in_desert = data.loc[data['Habitat'] == 'Desert', ('Species', 'Habitat')]
print("Animal lives in Desert: \n", animal_lives_in_desert, "\n")

# Animal lives in Arctic
animal_lives_in_arctic = data.loc[data['Habitat'] == 'Arctic', ('Species', 'Habitat')]
print("Animal lives in Arctic: \n", animal_lives_in_arctic, "\n")

# Animal lives in Coastal
animal_lives_in_coastal = data.loc[data['Habitat'] == 'Coastal', ('Species', 'Habitat')]
print("Animal lives in Coastal: \n", animal_lives_in_coastal, "\n")

# Animal lives in Mountains
animal_lives_in_mountains = data.loc[data['Habitat'] == 'Mountains', ('Species', 'Habitat')]
print("Animal lives in Mountains: \n", animal_lives_in_mountains, "\n")

# Animal lives in Cave
animal_lives_in_cave = data.loc[data['Habitat'] == 'Cave', ('Species', 'Habitat')]
print("Animal lives in Cave: \n", animal_lives_in_cave, "\n")

# Conservation_Status count
conservation_status_count = data['Conservation_Status'].value_counts()
print("Conservation Status of Species: \n", conservation_status_count, "\n")

# Vulnerable animals
vulnerable_animals = data.loc[data['Conservation_Status'] == 'Vulnerable', ('Species', 'Conservation_Status')]
print("Vulnerable Animals: \n",vulnerable_animals, "\n")

# Least Concern animals
least_concern_animals = data.loc[data['Conservation_Status'] == 'Least Concern', ('Species', 'Conservation_Status')]
print("Least Concern Animals: \n", least_concern_animals, "\n")

# Endangered animals
endangered_animals = data.loc[data['Conservation_Status'] == 'Endangered', ('Species', 'Conservation_Status')]
print("Endangered Animals: \n", endangered_animals, "\n")

# Critically Endangered animals
critically_endangered_animals = data.loc[data['Conservation_Status'] == 'Critically Endangered', ('Species', 'Conservation_Status')]
print("Critically Endangered Animals: \n", critically_endangered_animals, "\n")

# Mean weight
mean_weight_of_animals = data['Weight (kg)'].mean()
print(f"Mean weight of animals: {mean_weight_of_animals:.2f}", "\n")

# Median weight
median_weight_of_animals = data['Weight (kg)'].median()
print("Median weight of animals: \n", median_weight_of_animals, "\n")

# Mode weight
mode_weight_of_animals = data['Weight (kg)'].mode()
print("Mode weight of animals: \n", mode_weight_of_animals, "\n")

# Mean of age
mean_age_of_animals = data['Present Age (years)'].mean()
print(f"Mean weight of animals: {mean_age_of_animals:.2f}", "\n")

# Median of age
median_age_of_animals = data['Present Age (years)'].median()
print(f"Median weight of animals: {median_age_of_animals:2f}", "\n")

# Mode of age
mode_age_of_animals = data['Present Age (years)'].mode()
print("Mode weight of animals:", mode_age_of_animals, "\n")

# category wise value count of animal 
categories_of_animals = data["Category"].value_counts()
print("Categorywise value count of animal: \n", categories_of_animals)

# Total Carnivore animals
total_carnivore_animal = data.loc[data['Category'] == 'Carnivore', ('Species', 'Category')]
print("Total Carnivores animals: \n", total_carnivore_animal)

# Total Herbivore animals
total_herbivore_animal = data.loc[data['Category'] == 'Herbivore', ('Species', 'Category')]
print("Total Herbivores animals: \n", total_herbivore_animal)

# Total Herbivore animals
total_omnivore_animal = data.loc[data['Category'] == 'Omnivore', ('Species', 'Category')]
print("Total Omnivore animals: \n", total_omnivore_animal)

# Fastest running animal and speed
fastest_running_speed = data['Top_Speed (km/h)'].max()  
fastest_running_animal = data.loc[data['Top_Speed (km/h)'] == fastest_running_speed, ('Species', 'Top_Speed (km/h)')] 
print("Fastest running animal: \n", fastest_running_animal)

# Slowest running animal and speed
slowest_running_speed = data['Top_Speed (km/h)'].min()
slowest_running_animal = data.loc[data['Top_Speed (km/h)'] == slowest_running_speed, ('Species', 'Top_Speed (km/h)')]
print("Slowest running animal: \n", slowest_running_animal)

# Maximum population of species
max_population = data['Population_in_the_Wild'].max()
max_population_of_species = data.loc[data['Population_in_the_Wild'] == max_population, ('Species', 'Population_in_the_Wild')]
print("Most commonly found species: \n", max_population_of_species)


# Minimum population of species
min_population = data['Population_in_the_Wild'].min()
min_population_of_species = data.loc[data['Population_in_the_Wild'] == min_population, ('Species', 'Population_in_the_Wild')]
print("Most rarely found species: \n", min_population_of_species)

# Endemic_Regions value counts
endemic_regions = data['Endemic_Regions'].value_counts()
print("Value counts of Endemic Reguons of Species: \n", endemic_regions)

# Species found in Africa
species_found_in_africa = data.loc[data['Endemic_Regions'] == 'Africa', ('Species', 'Endemic_Regions')]
print("Species found in Africa: \n", species_found_in_africa)

# Species found in Global
species_found_in_global = data.loc[data['Endemic_Regions'] == 'Global', ('Species', 'Endemic_Regions')]
print("Species found in Global: \n", species_found_in_global)

# Species found in South America
species_found_in_south_merica = data.loc[data['Endemic_Regions'] == 'South America', ('Species', 'Endemic_Regions')]
print("Species found in South America: \n", species_found_in_global)

# Species found in Asia
species_found_in_asia = data.loc[data['Endemic_Regions'] == 'Asia', ('Species', 'Endemic_Regions')]
print("Species found in Asia: \n", species_found_in_asia)

# Species found in North America
species_found_in_north_america = data.loc[data['Endemic_Regions'] == 'North America', ('Species', 'Endemic_Regions')]
print("Species found in North America: \n", species_found_in_north_america)

# Human Interaction value counts
human_interaction = data['Human_Interaction'].value_counts()
print("Value counts of Human INteraction: \n", human_interaction)

# Most human interactive animal
most_human_interactive_animal = data.loc[data['Human_Interaction'] == 'High', ('Species')]
print("Most human interactive species: \n", most_human_interactive_animal)

# Least human interactive animal
least_human_interactive_animal = data.loc[data['Human_Interaction'] == 'Low', ('Species')]
print("Least human interactive species: \n", least_human_interactive_animal)

# Medium human interactive animal
medium_human_interactive_animal = data.loc[data['Human_Interaction'] == 'Medium', ('Species')]
print("Least human interactive species: \n", medium_human_interactive_animal)
