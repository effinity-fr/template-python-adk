# 🍪 Cookiecutter Python ADK

Ce template permet de générer instantanément un projet Python standardisé pour le framework **ADK (Agent Development Kit)**.

## 🚀 Utilisation rapide

Si vous avez déjà configuré votre environnement avec notre [dev-toolkit](https://www.google.com/search?q=https://github.com/effinity-fr/dev-toolkit), lancez simplement :

```bash
uv tool run cookiecutter https://github.com/effinity-fr/cookiecutter-python-adk

```

## 📝 Variables du template

Lors de la génération, vous devrez renseigner les champs suivants :

| Variable | Description | Valeur par défaut |
| --- | --- | --- |
| `project_name` | Le nom lisible de votre agent. | `Mon Agent IA` |
| `project_slug` | Le nom du dossier et du package (généré automatiquement). | `mon_agent_ia` |
| `ai_model` | Le modèle Gemini à utiliser par défaut. | `gemini-2.0-flash` |
| `description` | Une brève description de la mission de l'agent. | `Un agent IA basé sur ADK` |


## 🛠️ Installation après génération

```bash
cd mon_agent_ia && source .venv/bin/activate
```