from datasets import load_dataset
import json

review_dataset = load_dataset(
    "McAuley-Lab/Amazon-Reviews-2023", "raw_review_Appliances", trust_remote_code=True, streaming=True, split="full"
)
meta_dataset = load_dataset(
    "McAuley-Lab/Amazon-Reviews-2023", "raw_meta_Appliances", trust_remote_code=True, streaming=True, split="full"
)

processed_data = []
meta_dataset = meta_dataset.shuffle()
meta_iterable = iter(meta_dataset)

for i in range(10):
    meta = next(meta_iterable)
    print("getting reviews for", meta["title"])
    review_with_asin = review_dataset.filter(
        lambda review: review["parent_asin"] == meta["parent_asin"]
    )
    reviews = list(review_with_asin.take(5))
    processed_data.append(
        {
            "item name": meta["title"],
            "item description": " ".join(meta["features"]),
            "reviews": [{"stars": review["rating"], "content": f"Title: {review['title']}, Text: {review['text']}"} for review in reviews],
        }
    )

with open("real_dataset.json", "w") as out_file:
    json.dump(processed_data, out_file, indent=4)
