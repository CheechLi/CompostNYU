import random

greens = ["fruits/vegetables", "coffee grounds", "eggshells", "grass clippings", "leaves", "tea bags", "weeds", "yard trimmings", "flowers"]
browns = ["cardboard", "newspaper", "organic paper", "paper straw", "wood chips", "sawdust", "hay", "egg cartons", "toilet paper rolls"]
not_allowed = ["dairy", "meat", "bones", "fish", "grease", "oil", "glossy paper", "pet waste", "weeds with seeds", "diseased plants", "inorganic material"]

def getChoices():
    return random.sample(greens + browns + not_allowed, 10)