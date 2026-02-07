# 🤝 Contribuer au Template Cookiecutter ADK

Merci de contribuer à l'amélioration de la structure de nos Agents IA ! Ce template est le socle de nos projets Python chez Effinity.

## 📋 Comment proposer des changements ?

1. **Ouvrez une Issue** pour discuter de la modification souhaitée.
2. **Forkez** le repository.
3. Créez une branche de fonctionnalité (`git checkout -b feature/amelioration-template`).
4. Effectuez vos tests (voir section ci-dessous).
5. Soumettez une **Pull Request**.

---

## 🏗️ Structure du Template

* `{{cookiecutter.project_slug}}/` : Contient le code source qui sera généré.
* `hooks/post_gen_project.py` : Script Python exécuté immédiatement après la génération (installation `uv`, configuration venv).
* `cookiecutter.json` : Définition des variables de saisie.

## 🧪 Comment tester vos modifications ?

Avant de soumettre une modification, vous devez vérifier que le template génère toujours un projet fonctionnel.

1. **Générer un projet de test :**
   ```bash
   uv tool run cookiecutter . --no-input