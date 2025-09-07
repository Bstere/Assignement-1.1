from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.

print("Preview of first 3 products:")
for item in products[:3]:
    print(item)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = []  # <-- create the list FIRST

response = ""
while response != "N":
    print("Input a preference:")
    preference = input().strip()
    # Add the customer preference to the list
    if preference:  # ignore empty entries
        customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()

print("\nYou entered (raw list):", customer_preferences)

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.

customer_tags = set(tag.strip().lower() for tag in customer_preferences)
print("De-duplicated preferences (set):", customer_tags)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

for p in products:
    converted_products.append({
        "id": p.get("id"),
        "name": p.get("name"),
        # convert the product's tag list into a set
        "tags": set(t.strip().lower() for t in p.get("tags", []))
    })

print("\nConverted products (first 2 shown):")
for item in converted_products[:2]:
    print(item)


# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags & customer_tags)



# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    results = []
    for p in products:
        score = count_matches(p["tags"], customer_tags)
        if score > 0:
            results.append({"name": p["name"], "match_count": score})
    results.sort(key=lambda x: x["match_count"], reverse=True)
    return results




# TODO: Step 7 - Call your function and print the results

recommendations = recommend_products(converted_products, customer_tags)

print("\nRecommended products:")
if not recommendations:
    print("No matches found.")
else:
    for r in recommendations:
        print(f"- {r['name']} | matches: {r['match_count']}")





# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?
