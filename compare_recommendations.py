from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

# Compute average similarity: calculates the cosine of the angle between the two vectors
def average_similarity(item_texts, query_embedding):
    embeddings = [model.encode(text, convert_to_tensor=True) for text in item_texts]
    return sum(util.cos_sim(query_embedding, emb).item() for emb in embeddings) / len(embeddings)


# Us only the first 10 words from the itemas discritpions or tittle to reduce bias 
test_data = {
    "outfit for a casual brunch in spring": {
        "your_app": [
            "Lightweight and flowy dress with floral patterns, ideal for summer outings",
            "A timeless light-wash denim jacket, perfect for layering in cool",
            "Tailored trousers with a modern silhouette for a polished look"
        ],
        "amazon": [
            "The mens shorts and tshirt set made with high quality",
            "Mandonce 2 Piece Outfits for Women Crew Neck Short Sleeve ",
            "kaimimei Casual 2 Piece Outfit for Women - Linen Long Sleeve"
        ],
        "H&M": [
            "Set with a T-shirt in cotton jersey and sweatshorts in",
            "Set with a T-shirt in cotton jersey and sweatshorts in",
            "Set with a T-shirt and shorts in waffled cotton jersey. T-shirt"
        ],
        "ZARA": [
            "Relaxed fit jacket made of cotton fabric. Lapel collar and ",
            "Relaxed fit shirt. Spread collar and short sleeves. Side vents",
            "Relaxed fit shirt made of fabric with matching raised appliqués"
        ]
    },
    "comfy cozy outfit for rainy day": {
        "your_app": [
            "A timeless light-wash denim jacket, perfect for layering in cool",
            "Lightweight and flowy dress with floral patterns, ideal for summer outings",
            "Relaxed fit shirt made from breathable linen, perfect for warmer"
        ],
        "amazon": [
            "Tanming Sweater Sets Women 2 Piece Lounge Sets Short Sleeve Knit ",
            "PRETTYGARDEN Women's 2 Piece Ribbed Tracksuit Outfits Off Shoulder Long ",
            "LILLUSORY Womens Cardigan Pants Sets 2 Piece Slouchy Sweater Loungewear"
        ],
        "H&M": [
            "Set with a T-shirt in cotton jersey and sweatshorts in",
            "Set with a T-shirt in cotton jersey and sweatshorts in",
            "Set, with a T-shirt and shorts in waffled cotton jersey. T-shirt"
        ],
        "ZARA": [
            "Relaxed fit hoodie. Hooded collar and long sleeves. Front kangaroo ",
            "Relaxed fit hoodie. Hooded collar and long sleeves. Front kangaroo ",
            "Boxy fit hoodie. Hooded collar and long sleeves. Front kangaroo" 
        ]
    },
    "edgy streetwear with dark colors": {
        "your_app": [
            "Sleek and rebellious, this fitted biker jacket adds edge to",
            "Bold platform boots perfect for making a statement",
            "Relaxed blue jeans with vintage wash and straight-leg fit"
        ],
        "amazon": [
            "SOLY HUX Women's Off The Shoulder Tops Graphic Tees Y2k",
            "Men's Graphic Tees Shirt Unisex Cotton Oversized T-Shirt Short Sleeve",
            "SOLY HUX Men's T-Shirt Y2K Graphic Tees Short Sleeve"
        ],
        "H&M": [
            "Set with a T-shirt and shorts in waffled cotton jersey.",
            "Set with a T-shirt in cotton jersey and sweatshorts in",
            "Set with a shirt and shorts in soft, lightweight cotton"
        ],
        "ZARA": [
            "Relaxed fit T-shirt made of cotton fabric. Round neck and",
            "Relaxed fit hoodie. Adjustable hood and long sleeves. Kangaroo pocket",
            "Relaxed fit pants made of flowy modal blend fabric. Adjustable"
        ]
    },
    "white dress for a summer wedding": {
        "your_app": [
            "Lightweight and flowy dress with floral patterns, ideal for summer ",
            "Delicate strappy heels ideal for weddings and formal events",
            "Versatile white sneakers designed for comfort and everyday wear"
        ],
        "amazon": [
            "VIMPUNEC 2024 Womens Summer Wedding Guest Formal Dresses Cocktail Halter",
            "QACOHU Summer Dresses for Women V Neck Ruffle Short Sleeve",
            "DRESSTELLS Women's Cocktail Party Dress, Formal Wedding Guest High Low"
        ],
        "H&M": [
            "Sleeveless, ankle-length dress in crinkled satin with a slight sheen. ",
            "Comfortable, sleeveless dress in soft cotton jersey with a printed ",
            "Short, sleeveless A-line dress in airy, woven cotton with eyelet "
        ],
        "ZARA": [
            "Sleeveless midi dress with a crossover V-neck. Features a metallic",
            "Slim fit shirt made of fabric that minimizes the need",
            "Relaxed fit shirt made of linen fabric. Lapel collar with"
        ]
    },
    "a business casual look": {
        "your_app": [
            "Tailored trousers with a modern silhouette for a polished look",
            "Relaxed blue jeans with vintage wash and straight-leg fit",
            "A timeless light-wash denim jacket, perfect for layering in cool"
        ],
        "amazon": [
            "Blooming Jelly Womens Summer Tank Tops Business Casual Outfits Satin ",
            "LILLUSORY Summer Vest Tops for Women 2025 Striped Sweater Vests ",
            "Lee Women's Ultra Lux Comfort with Flex Motion Trouser Pant"
        ],
        "H&M": [
            "Loafers with a moccasin seam at front. Lining and insoles",
            "Loafer mules in leather with rounded toes and a penny",
            "Classic loafers with a moccasin seam at front and decorative"
        ],
        "ZARA": [
           "Regular fit blazer. Notched lapel collar and long sleeves with",
           "Long sleeve blazer with lapel collar. False front flap pockets",
           "Open front blazer with lapel collar and shoulder pads. Below-the-elbow "
        ]
    },
    "sporty gym-ready outfit": {
        "your_app": [
            "Tailored trousers with a modern silhouette for a polished look",
            "Relaxed blue jeans with vintage wash and straight-leg fit",
            "The classic crew neck t-shirt, perfect for everyday wear or "  
        ],
        "amazon": [
            "Women 2 Piece Outfits Summer Sweatsuits Biker Short Workout Jogger ",
            "Casual Workout Two Piece Outfits for Women Short Sleeve Crop",
            "Women Workout Sets 2 Piece - Seamless Yoga Leggings and Cross-Strap"
        ],
        "H&M": [
            "Set with a T-shirt in cotton jersey and sweatshorts in",
            "Set with a T-shirt in cotton jersey and sweatshorts in",
            "Set with a T-shirt and shorts in waffled cotton jersey. T-shirt"
        ],
        "ZARA": [
            "Slim fit pants made of lightweight 4-way stretch technical fabric",
            "Regular fit pants made of cotton with brushed interior. Adjustable",
            "T-shirt made of lightweight, technical stretch fabric with structure"
        ]
    },
     "winter-ready puffer and boots": {
        "your_app": [
           "Bold platform boots perfect for making a statement",
           "Versatile white sneakers designed for comfort and everyday wear",
           " Lightweight and breathable shoes designed for running and training"
        ],
        "amazon": [
            "Women's Nylon Mid-Calf Winter Snow Boot | Outdoor Cold Weather Faux",
            "These lace-up puffer boots have a padded insole with high-quality memory",
            "These pull on puffer boots are half lined in shearling"
        ],
        "H&M": [
           "Lightweight, slim-fit puffer jacket in quilted, woven fabric with a",
           "Puffer jacket in woven, quilted, water-repellent fabric designed for",
           "Puffer jacket in woven, quilted, water-repellent fabric designed for"
        ],
        "ZARA": [
            "Technical jumpsuit with water and wind resistant fabric. Designed with",
            "RECCO TECHNOLOGY WATER RESISTANT AND WIND PROTECTION JUMPSUIT SKI COLLECTION",
            "Technical jumpsuit with water and wind resistant fabric. Thermal insulation "  
        ]
    },
    "accessories for a bold night out": {
        "your_app": [
           "Bold oversized sunglasses for a glamorous touch",
           "Simple yet elegant hoop earrings that elevate any outfit",
           "Compact crossbody bag with timeless design and premium leather"
        ],
        "amazon": [
          "Rave Leg Wrap for Women - EDC Festival Outfit Elastic Non-Slip Straps", 
          "Black Sponge Bump It Up Volume Hair Base Fluffy Bump",
          "Single Gold Tooth Clover Four-Leaf Hip Hop Grillz for Men"
        ],
        "H&M": [
            "We couldnt find any results. Try again using another wor"
            "We couldnt find any results. Try again using another word",
            "We couldnt find any results. Try again using another word"
        ],
        "ZARA": [
            "Necklace with different sized rhinestone appliqués. Lobster clasp closure",
            "Pack of two contrasting metal charms",
            "Neck flowers with thin cord "
          ]
    },
    "minimalist all-black outfit": {
        "your_app": [
           "Tailored trousers with a modern silhouette for a polished look",
           "Relaxed fit shirt made from breathable linen, perfect for warmer days",
           "A timeless light-wash denim jacket, perfect for layering in cool"
        ],
        "amazon": [
           "Women 2 Piece Outfits Summer Sweatsuits Biker Short Workout Jogger",
           "Women's Sexy 2 Piece Outfits Sweatsuits Half Zip Tracksuit Long",
           "Sneakers Barefoot Shoes for Womens Mens Minimalist Trail Running Hiking"
        ],
        "H&M": [
           "Set with a T-shirt and shorts in waffled cotton jersey",
           "Set with a shirt and pants in soft, ribbed cotton",
           "Set in cotton with sweatshirt in lightweight fabric and leggings"
        ],
        
        "ZARA": [
            "Jumpsuit with a lapel collar and short sleeves. Front pockets ",
            "Sleeveless round neck jumpsuit. Skirt-style front detail. Front buttons",
            "Mid-rise straight-leg pants with front pockets and faux welt back pockets"
        ]
    },
    "festival-ready boho style": {
        "your_app": [
           "Tailored trousers with a modern silhouette for a polished look",
           "The classic crew neck t-shirt, perfect for everyday wear or layering",
           " Compact crossbody bag with timeless design and premium leather"
        ],
        
        "amazon": [
           "Western Cowgirl Fringe Top - Country Concert Outfits Festival Tassel Hem",
           "Romper Dresses for Women - Boho Rompers for Women, Whimsical Clothes",
           "Western Cowgirl Fringe Top for Women - Country Concert Outfits Festival"
        ],
        
        "H&M": [
           "We couldnt find any results. Try again using another word.",
           "We couldnt find any results. Try again using another word.",
           "We couldnt find any results. Try again using another word."
        ],
        
        "ZARA": [
            "Relaxed fit t-shirt made of textured piqué fabric. Round neck ",
            "PAISLEY PRINT BANDANA", 
            "Baggy fit denim shorts made of cotton denim. Five pockets"
        ]
    }
}

# Runs comparisons
for prompt, sources in test_data.items():
    query_emb = model.encode(prompt, convert_to_tensor=True)

    your_score = average_similarity(sources["your_app"], query_emb)
    amz_score = average_similarity(sources["amazon"], query_emb)
    hm_score = average_similarity(sources["H&M"], query_emb)
    zara_score = average_similarity(sources["ZARA"], query_emb)
    
    print(f"\nPrompt: {prompt}")
    print(f" Your App Similarity:     {your_score:.4f}")
    print(f" Amazon Platform Score: {amz_score:.4f}")
    print(f" H&M Platform Score:      {hm_score:.4f}")
    print(f" ZARA Platform Score:      {zara_score:.4f}")
