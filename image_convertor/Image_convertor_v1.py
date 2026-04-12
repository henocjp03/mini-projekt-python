import cv2
import os

def convert_to_sketch(image_path, output_path):
    """
    Convertit une image en sketch (effet crayon).
    """
    if not os.path.exists(image_path):
        print(f"Erreur : L'image '{image_path}' n'existe pas.")
        return

    image = cv2.imread(image_path)
    if image is None:
        print(f"Erreur : Impossible de lire l'image '{image_path}'.")
        return

    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_img = cv2.bitwise_not(grey_img)
    blur = cv2.GaussianBlur(inverted_img, (21, 21), 0)
    inverted_blur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_img, inverted_blur, scale=256.0)

    cv2.imwrite(output_path, sketch)
    print(f"Image convertie et sauvegardée dans '{output_path}'.")

# Demander les chemins à l'utilisateur
image_input = input("Entrez le chemin de l'image d'entrée (ex: Burger.jpg) : ")
image_output = input("Entrez le chemin de l'image de sortie (ex: sketch.jpg) : ")

convert_to_sketch(image_input, image_output)
