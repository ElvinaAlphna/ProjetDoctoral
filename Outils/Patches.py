#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Alphna Kemoe
#
# Created:     29-06-2023
# Copyright:   (c) Alphna Kemoe 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from PIL import Image
import os

# Définir le chemin du dossier vers les images à traiter
chemin_vers_images = "C:/Users/Alphna Kemoe/Desktop/segmantation_semantique/Annotations/Input/Image_3"

# Définir le chemin du dossier vers les patchs (imagettes)
chemin_dossier_patches = "C:/Users/Alphna Kemoe/Desktop/segmantation_semantique/Annotations/Patch"

# Dossier des images reconstituées
chemin_dossier_fusionne = "C:/Users/Alphna Kemoe/Desktop/segmantation_semantique/Annotations/Output"

# Définir la taille des imagettes
patch_size = 224

# Definir la taille de l'image d'orignine
img_size = (9995, 12297)
def create_patch(img_size,patch_size):
    # Pour chaque image dans le dossier
    for nom_image in os.listdir(chemin_vers_images):
        # Vérifier si l'élément est bien un fichier image
        if nom_image.lower().endswith(".jpg"): # or nom_image.lower().endswith('.tif'):
            # Ouvrir l'image originale
            img = Image.open(os.path.join(chemin_vers_images, nom_image))
            # Calculer le nombre de patches nécessaires
            num_patches_wide = img_size[0] // patch_size
            num_patches_high = img_size[1] // patch_size

            # Créer un dossier pour stocker les patches découpés
            chemin_vers_dossier_patches = os.path.join(chemin_dossier_patches, f"{os.path.splitext(nom_image)[0]}_patches")
            if not os.path.exists(chemin_vers_dossier_patches):
                os.makedirs(chemin_vers_dossier_patches)

            # Découper l'image en patches et les enregistrer dans le dossier
            for i in range(num_patches_high):
                for j in range(num_patches_wide):
                    box = (j*patch_size, i*patch_size, (j+1)*patch_size, (i+1)*patch_size)
                    patch = img.crop(box)
                    patch.save(os.path.join(chemin_vers_dossier_patches, f"patch_{i}_{j}.jpg"))


def merge_patch(img_size,patch_size):
     num_patches_wide = img_size[0] // patch_size
     num_patches_high = img_size[1] // patch_size
     # Reconstituer l'image originale à partir des patches
     new_img = Image.new('RGB', img_size)
     for dir in os.listdir(chemin_dossier_patches):
         nom_image = dir.split('_patches')[0]
         for i in range(num_patches_high):
            for j in range(num_patches_wide):
                chemin_vers_dossier_patches = os.path.join(chemin_dossier_patches, f"{os.path.splitext(nom_image)[0]}_patches")
                patch = Image.open(os.path.join(chemin_vers_dossier_patches, f"patch_{i}_{j}.jpg"))
                print(os.path.join(chemin_vers_dossier_patches, f"patch_{i}_{j}.jpg"))
                box = (j*patch_size, i*patch_size)
                new_img.paste(patch, box)
         # Enregistrer l'image reconstituée
         new_nom_image = os.path.join(chemin_dossier_fusionne, f"{os.path.splitext(nom_image)[0]}.jpg")
         new_img.save(new_nom_image)


print("On commence")

create_patch(img_size, patch_size)
print("Terminer")
