from langchain_text_splitters import RecursiveCharacterTextSplitter

text = '''
Whiterun is a major city in the center of Skyrim, and the capital of Whiterun Hold. Its central location makes it the province's major commercial hub, as well as a crucial strategic point in the Civil War between the Imperial Legion loyalists and Stormcloak rebels, as control of Whiterun Hold grants access to all surrounding lands. Whiterun is initially nominally aligned with the Empire, but Jarl Balgruuf the Greater seems to care more about the people of Whiterun than either side of the conflict, rendering the hold effectively neutral.

Whiterun comprises three districts arranged in tiers and connected by stairways. The Plains District is the lowest and contains the city's marketplace and shops, inns, a few homes, and the city gates. The Wind District is the main residential area; it features the Temple of Kynareth, Jorrvaskr, the ancient mead hall and headquarters of the Companions, and the Skyforge, worked by the greatest blacksmith in Skyrim, Eorlund Gray-Mane. The Cloud District is dominated by the government seat Dragonsreach and its dungeon, and is the highest point in Whiterun. Local businesses and services include the smithy and weapons shop Warmaiden's, the tavern and hunting supply store The Drunken Huntsman, Belethor's General Goods, the alchemy shop Arcadia's Cauldron, and The Bannered Mare inn. The jarl's court wizard Farengar Secret-Fire has spells and enchanting supplies for sale and can teach you the basics of enchanting.
'''

splitter = RecursiveCharacterTextSplitter(
    chunk_size=250,
    chunk_overlap=35
)

chunks = splitter.split_text(text)
print(chunks[:5])