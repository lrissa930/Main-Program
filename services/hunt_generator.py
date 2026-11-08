import random
def generate_hunt(area, habitat):

    if habitat == "Coastal":
        objectives = [
            {
                "title": "Find a Piece of Driftwood",
                "description":
                "Look for driftwood resting on the beach.",
                "image": "coastal_driftwood.png"
            },
            {
                "title": "Find a Coastal Plant",
                "description":
                "Look for a plant growing near the beach or along the trail.",
                "image": "coastal_plant.png"
            },
            {
                "title": "Observe a Shorebird",
                "description": 
                "From a safe distance, watch a bird along the beach.",
                "image": "coastal_shorebird.png"
            },
            {
                "title": "Find an Interesting Shell",
                "description":
                "Look for a shell along the beach and notice its shape, pattern, and texture.",
                "image": "coastal_shell.jpg"
            },
            {
                "title": "Observe a Tide Pool",
                "description":
                "Look carefully into a tide pool without touching or disturbing it.",
                "image": "coastal_tidepool.jpg"
            },
            {
                "title": "Find Seaweed",
                "description":
                "Look for seaweed/kelp washed ashore.",
                "image": "coastal_kelp.jpg"
            },
            {
                "title": "Listen to Ocean Sounds",
                "description":
                "Pause for a moment and listen to the waves, wind, and wildlife around you.",
                "image": "coastal_waves.jpg"    
            },
            {
                "title": "Find a Coastal Rock Formation",
                "description": 
                "Look for rocks shaped by wind and water over time.",
                "image": "coastal_rocks.jpg"
            },
            {
                "title": "Observe an Insect",
                "description":
                "Watch for insects visiting coastal flowers or resting on plants.",
                "image": "coastal_insect.jpg"
            },
            {
                "title": "Spot Signs of the Tide",
                "description":
                "Look for a line of seaweed, shells, or debris that shows how high the water recently reached.",
                "image": "coastal_tideline.jpg"
            }
        ]
        return random.sample(objectives, 5)

    elif habitat == "Forest":
        objectives = [
            {
                "title": "Find a Fallen Log",
                "description":
                "Look for a fallen tree trunk or branch on the forest floor.",
                "image": "forest_fallenlog.jpg"
            },
            {
                "title": "Observe a Bird in a Tree",
                "description":
                "Watch a bird from a distance and notice how it moves through the branches.",
                "image": "forest_bird.jpg"
            },
            {
                "title": "Find Moss",
                "description": 
                "Look for moss growing on a tree, rock, or log.",
                "image": "forest_moss.jpg"
            },
            {
                "title": "Find an Interesting Leaf",
                "description": 
                "Study the shape, color, and texture of a leaf.",
                "image": "forest_leaf.jpg"
            },
            {
                "title": "Spot a Mushroom",
                "description":
                "Look for a mushroom or other fungus growing on a log, tree, or forest floor without touching it.",
                "image": "forest_mushroom.jpg"
            },
            {
                "title": "Listen for Birdsong",
                "description":
                "Pause quietly and listen for forest sounds.",
                "image": "forest_sounds.jpg"
            },
            {
                "title": "Find a Tree with Unique Bark",
                "description":
                "Compare bark patterns and textures.",
                "image": "forest_bark.jpg"
            },
            {
                "title": "Observe a Forest Insect",
                "description":
                "Watch an insect as it moves across a log or leaf.",
                "image": "forest_insect.jpg"
            },
            {
                "title": "Find Animal Evidence",
                "description":
                "Look for tracks, feathers, nests, or other signs of wildlife.",
                "image": "forest_tracks.jpg"
            },
            {
                "title": "Look up at the Canopy",
                "description":
                "Notice how tree branches create layers above you.",
                "image": "forest_canopy.jpg"
            }
        ]
        return random.sample(objectives, 5)
    
    elif habitat == "Grassland":
        objectives = [
            {
                "title": "Find a Tall Grass",
                "description":
                "Notice how the grasses bend and move in the wind.",
                "image": "grassland_tallgrass.jpg"
            },
            {
                "title": "Observe a Wildflower",
                "description":
                "Look closely at a flower's colors and petals.",
                "image": "grassland_wildflower.jpg"
            },
            {
                "title": "Watch an Insect",
                "description":
                "Observe a bee or butterfly visiting flowers.",
                "image": "grassland_insect.jpg"
            },
            {
                "title": "Find a Seed Head",
                "description":
                "Look for grass seeds and think about how they spread.",
                "image": "grassland_seedhead.jpg"
            },
            {
                "title": "Observe Clouds",
                "description":
                "Grasslands offer wide-open views. Watch the clouds move across the sky.",
                "image": "grassland_sky.jpg"
            },
            {
                "title": "Spot a Bird",
                "description":
                "Look for birds flying overhead or perched nearby.",
                "image": "grassland_bird.jpg"
            },
            {
                "title": "Find a Patch of Vegetation",
                "description":
                "Compare one area of plants to another.",
                "image": "grassland_vegetation.jpg"
            },
            {
                "title": "Look for Animal Tracks",
                "description":
                "Search for footprints along dirt paths.",
                "image": "grassland_tracks.jpg"
            },
            {
                "title": "Feel the Wind",
                "description":
                "Notice how the wind changes the movement of plants around you.",
                "image": "grassland_wind.jpg"
            },
            {
                "title": "Look for Movement in the Grass",
                "description":
                "Stand quietly and watch the grass around you for movement from birds, animals, or insects.",
                "image": "grassland_movement.jpg"
            }
        ]
        return random.sample(objectives, 5)

    elif habitat == "Wetlands":
        objectives = [
            {
                "title": "Observe Still Water",
                "description":
                "Notice reflections and movement on the water's surface.",
                "image": "wetlands_pond.jpg"
            },
            {
                "title": "Find Reeds or Cattails",
                "description":
                "Observe plants growing near the water.",
                "image": "wetlands_cattail.jpg"
            },
            {
                "title": "Look for a DragonFly",
                "description":
                "Watch how dragonflies patrol above the water.",
                "image": "wetlands_dragonfly.jpg"
            },
            {
                "title": "Observe a Water Bird",
                "description": 
                "Watch a bird standing or feeding near the water.",
                "image": "wetlands_bird.jpg"
            },
            {
                "title": "Find Floating Plants",
                "description":
                "Look for plants growing on the water surface.",
                "image": "wetlands_lilypad.jpg"
            },
            {
                "title": "Listen for Frog Calls",
                "description":
                "Pause quietly and listen for frogs if conditions are right.",
                "image": "wetlands_frog.jpg"
            },
            {
                "title": "Observe Ripples",
                "description":
                "Watch for ripples caused by wind, fish, or insects.",
                "image": "wetlands_waterripple.jpg"
            },
            {
                "title": "Find a Wetland Insect",
                "description":
                "Look for insects resting on plants or near the water.",
                "image": "wetlands_insect.jpg"
            },
            {
                "title": "Spot an Amphibian",
                "description":
                "If you see a frog, salamander, or tadpole, watch it quietly from a distance.",
                "image": "wetlands_amphibian.jpg"
            },
            {
                "title": "Look for Animal Tracks Near Water",
                "description":
                "Search muddy areas for signs of wildlife activity.",
                "image": "wetlands_tracks.jpg"
            }
        ]
        return random.sample(objectives, 5)

    elif habitat == "Desert":
        objectives = [
            {
                "title": "Find a Desert Plant",
                "description":
                "Observe how desert plants store water and survive harsh conditions.",
                "image": "desert_plant.jpg"
            },
            {
                "title": "Observe a Rock Formation",
                "description":
                "Notice the colors, textures, and shapes created by weathering.",
                "image": "desert_rocks.jpg"
            },
            {
                "title": "Find Animal Tracks",
                "description":
                "Look for tracks left in sand or loose soil.",
                "image": "desert_tracks.jpg"
            },
            {
                "title": "Observe Desert Wildflowers",
                "description":
                "Look for flowers adapted to dry environments.",
                "image": "desert_flower.jpg"
            },
            {
                "title": "Find a Plant with Small Leaves",
                "description":
                "Notice adaptations that help conserve water.",
                "image": "desert_shrub.jpg"
            },
            {
                "title": "Observe the Sky",
                "description":
                "Notice visibility, clouds, and light in the open landscape.",
                "image": "desert_sky.jpg"
            },
            {
                "title": "Observe a Desert Animal",
                "description":
                "Watch a lizard, bird, or other desert animal from a distance.",
                "image": "desert_lizard.jpg"
            },
            {
                "title": "Find Patterns in Sand",
                "description":
                "Look for wind-created textures and shapes.",
                "image": "desert_sandpattern.jpg"
            },
            {
                "title": "Observe Desert Insects",
                "description":
                "Watch how insects move between plants and rocks.",
                "image": "desert_insect.jpg"
            },
            {
                "title": "Look for a Nurse Plant",
                "description":
                "Find a larger plant providing shade or shelter for smaller plants nearby.",
                "image": "desert_nurseplant.jpg"
            }
        ]
        return random.sample(objectives, 5)