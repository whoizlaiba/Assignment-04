# Question 2: Favorite Animal Response

def share_favorite_animal():
    print("== Question 2: Agreement Bot ==")
    fav_animal = input("What's your favorite animal? ").strip().lower()
    print(f"Hey! Mine too — I love {fav_animal}s!")

if __name__ == '__main__':
    share_favorite_animal()
