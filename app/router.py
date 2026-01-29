from semantic_router import Route, RouteLayer
from semantic_router.encoders import HuggingFaceEncoder

encoder = HuggingFaceEncoder(
    name="sentence-transformers/all-mpnet-base-v2"

)

faq = Route(
    name="faq",
    utterances=[
        "What is the return policy?",
        "What is your refund policy?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "Do you offer international shipping?",
        "What is your policy on defective products?"
    ]
)

product_search = Route(
    name="product_search",
    utterances=[
        "I want to buy nike shoes with discount",
        "Shoes under 3000 rupees",
        "Formal shoes in size 9",
        "Puma shoes on sale",
        "Price of puma running shoes",
        "Pink puma shoes between 1000 and 5000"
    ]
)

router = RouteLayer(
    routes=[faq, product_search],
    encoder=encoder
)

if __name__ == "__main__":
    print(router("What is your policy on defective product?").name)
    print(router("Pink Puma shoes in price range 5000 to 1000").name)
