#Mario Pauldon 
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash, session
import re
from sentence_transformers import SentenceTransformer, util
from data import fashion_articles 

# Initialize the SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

app = Flask(__name__)
#
app.secret_key = "supersecretkey" 

data = {
    "1": {
        "id": "1",
        "image": "https://lsco.scene7.com/is/image/lsco/299450063-front-gstk?fmt=webp&qlt=70&resMode=sharp2&fit=crop,1&op_usm=0.6,0.6,8&wid=232&hei=232",
        "item_name": "Classic Denim Jacket",
        "brand": "Levi's",
        "category": "Outerwear",
        "style": "Casual",
        "price": "$89.99",
        "color": "Light Blue",
        "material": "100% Cotton",
        "description": "A timeless light-wash denim jacket, perfect for layering in cool weather.",
        "similar_items": ["2", "5"]
    },
    "2": {
        "id": "2",
        "image": "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcSlgUGDmuFwBfsoPMj8matK9Ex6JFLMmo8puou_WJNW9uw1AxPaYz9_dJpMUNzPVK3azvOfdHy4U0Fw3O85G4E33V3jLwwg3Hh1w92sOoZfylfR2XvlRw&usqp=CAc",
        "item_name": "Black Leather Biker Jacket",
        "brand": "AllSaints",
        "category": "top",
        "style": "Edgy",
        "price": "$420.00",
        "color": "Black",
        "material": "Genuine Leather",
        "description": "Sleek and rebellious, this fitted biker jacket adds edge to any look.",
        "similar_items": ["1", "3"]
    },
    "3": {
        "id": "3",
        "image": "https://static.zara.net/assets/public/d54b/fcf1/4d5d4368875e/70770542224b/06962031330-e2/06962031330-e2.jpg?ts=1745580410439&w=1024",
        "item_name": "Flowy Summer Dress",
        "brand": "Zara",
        "category": "Dress",
        "style": "Bohemian",
        "price": "$49.90",
        "color": "White Floral",
        "material": "Viscose Blend",
        "description": "Lightweight and flowy dress with floral patterns, ideal for summer outings.",
        "similar_items": ["4", "7"]
    },
    "4": {
        "id": "4",
        "image": "https://image.uniqlo.com/UQ/ST3/WesternCommon/imagesgoods/455957/sub/goods_455957_sub14_3x4.jpg?width=400",
        "item_name": "Breezy Linen Shirt",
        "brand": "Uniqlo",
        "category": "Top",
        "style": "Minimalist",
        "price": "$29.90",
        "color": "Ivory",
        "material": "Linen",
        "description": "Relaxed fit shirt made from breathable linen, perfect for warmer days.",
        "similar_items": ["3", "6"]
    },
    "5": {
        "id": "5",
        "image": "https://media.everlane.com/images/c_fill,w_750,ar_4:5,q_auto:best:sensitive,dpr_2.0,f_auto/i/cbc4c153_1dc1/mens-essential-organic-crew-uniform-white",
        "item_name": "Basic White Tee",
        "brand": "Everlane",
        "category": "Top",
        "style": "Essential",
        "price": "$25.00",
        "color": "White",
        "material": "Organic Cotton",
        "description": "The classic crew neck t-shirt, perfect for everyday wear or layering.",
        "similar_items": ["1", "4"]
    },
    "6": {
        "id": "6",
        "image": "https://cdn.shopify.com/s/files/1/2185/2813/files/W51208R_02125_b1_s1_a1_1_m76_750x.jpg?v=1709685746",
        "item_name": "High-Waisted Trousers",
        "brand": "COS",
        "category": "Bottom",
        "style": "Chic",
        "price": "$89.00",
        "color": "Charcoal Grey",
        "material": "Wool Blend",
        "description": "Tailored trousers with a modern silhouette for a polished look.",
        "similar_items": ["4", "7"]
    },
    "7": {
        "id": "7",
        "image": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcStwub8bb0cbSOMigLoLeFQDRYf6x9hFXYeF45qWqHn31hAoUaIlDD9Oeliokwuozu5rX8odII&usqp=CAc",
        "item_name": "Relaxed Fit Jeans",
        "brand": "ASOS",
        "category": "Bottom",
        "style": "Streetwear",
        "price": "$45.00",
        "color": "Blue",
        "material": "Denim",
        "description": "Relaxed blue jeans with vintage wash and straight-leg fit.",
        "similar_items": ["3", "6"]
    },
    "8": {
        "id": "8",
        "image": "https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/7d82b564-abb2-4140-94fa-6f5625d98bdf/NIKE+V5+RNR.png",
        "item_name": "Classic White Sneakers",
        "brand": "Nike",
        "category": "Shoes",
        "style": "Casual",
        "price": "$75.00",
        "color": "White",
        "material": "Leather Upper",
        "description": "Versatile white sneakers designed for comfort and everyday wear.",
        "similar_items": ["9", "11"]
    },
    "9": {
        "id": "9",
        "image": "https://cdn.media.amplience.net/i/drmartens/27149001.80?$smart1024$&fmt=auto",
        "item_name": "Chunky Platform Boots",
        "brand": "Dr. Martens",
        "category": "Shoes",
        "style": "Edgy",
        "price": "$180.00",
        "color": "Black",
        "material": "Genuine Leather",
        "description": "Bold platform boots perfect for making a statement.",
        "similar_items": ["8", "10"]
    },
    "10": {
        "id": "10",
        "image": "https://www.stevemadden.com/cdn/shop/files/STEVEMADDEN_SHOES_JYPSEY_TAN-LEATHER_01.jpg",
        "item_name": "Strappy Nude Heels",
        "brand": "Steve Madden",
        "category": "Shoes",
        "style": "Elegant",
        "price": "$95.00",
        "color": "Nude",
        "material": "Synthetic Leather",
        "description": "Delicate strappy heels ideal for weddings and formal events.",
        "similar_items": ["9", "12"]
    },
    "11": {
        "id": "11",
        "image": "https://assets.adidas.com/images/h_2000,f_auto,q_auto,fl_lossy,c_fill,g_auto/959c50a4907640b4b7fd2db73f05dc4d_9366/Adizero_Boston_12_Shoes_Grey_JI4472_HM1.jpg",
        "item_name": "Sporty Running Shoes",
        "brand": "Adidas",
        "category": "Shoes",
        "style": "Sporty",
        "price": "$110.00",
        "color": "Grey/Neon",
        "material": "Mesh",
        "description": "Lightweight and breathable shoes designed for running and training.",
        "similar_items": ["8", "12"]
    },
    "12": {
        "id": "12",
        "image": "https://wholesale.baggu.com/_next/image?url=https%3A%2F%2Fcdn.shopify.com%2Fs%2Ffiles%2F1%2F1892%2F2397%2Ffiles%2F8a6e46ead1e489db3c798d04fc94822d49dec4b1-3200x4000.jpg%3Fv%3D1741217043&w=828&q=75",
        "item_name": "Canvas Tote Bag",
        "brand": "Baggu",
        "category": "Accessories",
        "style": "Minimalist",
        "price": "$45.00",
        "color": "Natural",
        "material": "Recycled Canvas",
        "description": "Durable and eco-friendly tote bag perfect for daily errands.",
        "similar_items": ["10", "13"]
    },
    "13": {
        "id": "13",
        "image": "https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcR5iz-0fj0ZjV1dKWxA1kUcWSP5NLE8EyXUS1LEUYzqA5Y5C6SoYlulNcnkagjACMqgp0OxIJ3XCEo5F3hC2AtPiuBvYbL4c3TRHpIECUKQQUgDivtP8ok&usqp=CAc",
        "item_name": "Gold Hoop Earrings",
        "brand": "Mejuri",
        "category": "Accessories",
        "style": "Chic",
        "price": "$75.00",
        "color": "Gold",
        "material": "14k Gold Vermeil",
        "description": "Simple yet elegant hoop earrings that elevate any outfit.",
        "similar_items": ["12", "14"]
    },
    "14": {
        "id": "14",
        "image": "https://www.quay.com/cdn/shop/files/Quay_Nightfall_BlackSmokePol_Front_f66c0674-3c32-4244-9adc-09dfa1797f80.jpg?v=1721424372&width=2000",
        "item_name": "Oversized Sunglasses",
        "brand": "Quay Australia",
        "category": "Accessories",
        "style": "Trendy",
        "price": "$65.00",
        "color": "Black",
        "material": "Acetate",
        "description": "Bold oversized sunglasses for a glamorous touch.",
        "similar_items": ["13", "15"]
    },
    "15": {
        "id": "15",
        "image": "https://coach.scene7.com/is/image/Coach/cv935_svmpl_a0?$desktopProduct$",
        "item_name": "Leather Crossbody Bag",
        "brand": "Coach",
        "category": "Accessories",
        "style": "Classic",
        "price": "$250.00",
        "color": "Brown",
        "material": "Pebbled Leather",
        "description": "Compact crossbody bag with timeless design and premium leather.",
        "similar_items": ["12", "14"]
    }
}


# Precompute description embeddings for all fashion items
item_embeddings = {}
for item_id, item in data.items():
    desc = item.get("description", "") + " " + item.get("style", "") + " " + item.get("category", "")
    item_embeddings[item_id] = model.encode(desc, convert_to_tensor=True)


# route for articles
@app.route('/articles')
def articles():
    return render_template('articles.html', items=fashion_articles)

# route for find_outfit
@app.route('/find_outfit')
def find_outfit():
    return render_template('find_outfit.html')

# route for favorites
@app.route('/favorites')
def favorites():
    favorites = session.get('favorites', [])
    favorite_items = [data[company_id] for company_id in favorites if company_id in data]
    return render_template('favorites.html', items=favorite_items)

# Add to favorites
@app.route('/add_to_favorites/<company_id>', methods=['POST'])
def add_to_favorites(company_id):
    favorites = session.get('favorites', [])

    if company_id in favorites:
        favorites.remove(company_id)
        flash('Item removed from favorites!', 'info')
    else:
        favorites.append(company_id)
        flash('Item added to favorites!', 'success')

    session['favorites'] = favorites  # Update session
    return redirect(url_for('company_page', company_id=company_id))

# remove from favorites
@app.route('/remove_from_favorites/<company_id>', methods=['POST'])
def remove_from_favorites(company_id):
    favorites = session.get('favorites', [])

    if company_id in favorites:
        favorites.remove(company_id)
        flash('Item removed from favorites!', 'info')
    else:
        flash('Item not found in favorites!', 'warning')

    session['favorites'] = favorites
    return redirect(url_for('favorites'))

# Home route 
@app.route('/')
def home():
    # Convert prices to floats for sorting
    for item in data.values():
        price = item["price"]
        if isinstance(price, str):
            price = float(price.replace("$", "").replace(",", ""))
        item["price"] = price
        
    lowest_price_items = sorted(data.values(), key=lambda x: x["price"])[:3]
    return render_template('home_page.html', companies=lowest_price_items)

@app.route('/search')
def search():
    query = request.args.get('query', '').strip().lower()
    filter_type = request.args.get('filter', '').strip().lower()
    filter_value = request.args.get('value', '').strip().lower()
    
    if filter_type and filter_value:
        results = [
            item for item in data.values()
            if item.get(filter_type, '').lower() == filter_value
        ]
        return render_template('search_results.html', query=f"{filter_type.title()}: {filter_value.title()}", results=results, result_count=len(results))
    if query:
        query_embedding = model.encode(query, convert_to_tensor=True)

        similarity_scores = []
        for item_id, embedding in item_embeddings.items():
            score = util.cos_sim(query_embedding, embedding).item()
            similarity_scores.append((item_id, score))
            
        similarity_scores.sort(key=lambda x: x[1], reverse=True)
        top_matches = [data[item_id] for item_id, score in similarity_scores[:10]]

        return render_template('search_results.html', query=query, results=top_matches, result_count=len(top_matches))
    # If nothing is given
    return render_template('search_results.html', query="", results=[], result_count=0)



# Autocomplete
@app.route('/autocomplete')
def autocomplete():
    search_term = request.args.get("term", "").lower()
    suggestions = [item["item_name"] for item in data.values() if search_term in item["item_name"].lower()]
    return jsonify(suggestions)

@app.route('/view/<company_id>')
def company_page(company_id):
    company = data.get(company_id)
    if not company:
        return "Item not found", 404
    return render_template('company_details.html', company=company)


if __name__ == '__main__':
    app.run(debug=True, port=5001)