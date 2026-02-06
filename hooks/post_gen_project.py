import subprocess
import shutil


def setup_with_uv():
    print("\n--- Configuration avec UV (Vitesse maximale) ---")

    # 1. Vérifier si uv est installé
    uv_path = shutil.which("uv")

    if not uv_path:
        print("❌ 'uv' n'est pas installé sur cette machine.")
        print(
            "👉 Installez-le avec : "
            "curl -LsSf https://astral.sh/uv/install.sh | sh"
        )
        return False

    try:
        # 2. Création de l'environnement virtuel avec uv
        print("⚡ Création du .venv...")
        subprocess.run([uv_path, "venv"], check=True)

        # 3. Installation des dépendances avec uv
        # uv détecte automatiquement le .venv dans le dossier courant
        print("⚡ Installation des dépendances (Google Auth & ADK)...")
        subprocess.run([uv_path, "pip", "install", "-r",
                        "requirements.txt"], check=True)

        print("✅ Projet configuré avec succès grâce à uv.")
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la configuration avec uv : {e}")
        return False


if __name__ == "__main__":
    success = setup_with_uv()
    if success:
        print(
            "\n🚀 Votre agent ADK est prêt dans le dossier : "
            "{{ cookiecutter.project_slug }}"
        )
        print(
            "💻 Pour commencer : cd {{ cookiecutter.project_slug }} "
            "&& source .venv/bin/activate"
        )
