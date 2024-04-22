# FlaskIntroduction

This repo has been updated to work with `Python v3.8` and up.

## How To Run
1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:
```
$ .\env\Scripts\activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Finally start the web server:
```
$ (env) python app.py
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```

## Contributing

Since this is a repository for a tutorial, the code should remain the same as the code that was shown in the tutorial. Any pull requests that don't address security flaws or fixes for language updates will be automatically closed. Style changes, adding libraries, etc are not valid changes for submitting a pull request.


## Tests
Voici une explication de chaque fonction de test dans le fichier `pytest` en format Markdown :

---

### Explications des Fonctions de Test

#### `test_index_get(client)`
Ce test vérifie le comportement de la route d'index lorsqu'elle est accédée avec une requête GET. Il confirme deux points principaux :
- **Code de Statut** : Assure que le code de statut de la réponse est `200`, ce qui indique que la page se charge avec succès sans erreurs de serveur.
- **Vérification du Contenu** : Vérifie que du contenu spécifique, comme le mot "Tasks", est présent dans les données de réponse. Cela permet de s'assurer que le modèle HTML correct est rendu. (Vous devrez peut-être ajuster le mot-clé en fonction du contenu réel de votre HTML).

#### `test_index_post(client)`
Ce test évalue le comportement de la route d'index sur une requête POST, spécifiquement en testant la fonctionnalité d'ajout d'une nouvelle tâche :
- **Opération Post** : Simule l'envoi d'une requête POST avec le contenu de la tâche ('Test task') pour voir si la tâche est correctement ajoutée.
- **Code de Statut et Redirection** : Vérifie que le code de statut de la réponse est `200` après une redirection, confirmant que l'utilisateur est redirigé vers la page d'index.
- **Vérification du Contenu** : Assure que le contenu de la nouvelle tâche ajoutée ('Test task') apparaît dans le contenu de la page, confirmant que la tâche a été ajoutée avec succès.

#### `test_task_delete(client)`
Cette fonction teste la suppression d'une tâche :
- **Préparation** : Insère une tâche fictive dans la base de données pour établir un état connu.
- **Opération de Suppression** : Envoie une requête GET à la route de suppression et suit les redirections pour simuler un utilisateur cliquant sur un lien de suppression.
- **Code de Statut et Redirection** : Confirme que le code de statut de la réponse est `200` après l'opération, indiquant une suppression réussie et une redirection.
- **Vérification du Contenu** : Assure que le contenu de la tâche supprimée n'est plus présent dans les données de réponse, vérifiant ainsi que la tâche a bien été supprimée.

#### `test_task_update_get(client)`
Ce test vérifie la fonctionnalité de mise à jour lors d'une requête GET :
- **Préparation** : Ajoute une tâche de test à la base de données pour garantir qu'il y a du contenu à mettre à jour.
- **Opération Get** : Récupère la page de mise à jour pour la tâche spécifique.
- **Code de Statut** : Vérifie une réponse `200`, indiquant que la page est accessible.
- **Vérification du Contenu** : Vérifie que le contenu de la tâche avant la mise à jour ('Contenu initial') est présent dans les données de réponse, s'assurant que la bonne tâche est chargée pour la mise à jour.

#### `test_task_update_post(client)`
Cette fonction teste la mise à jour d'une tâche via une requête POST :
- **Préparation** : Crée une tâche fictive avec un contenu initial ('Avant la mise à jour').
- **Opération Post** : Envoie une requête POST à la route de mise à jour avec un nouveau contenu ('Après la mise à jour').
- **Code de Statut et Redirection** : Assure que le code de statut est `200` après une redirection, confirmant que la mise à jour de la tâche a réussi et que la page redirige comme prévu.
- **Vérification du Contenu** : Vérifie que le contenu mis à jour ('Après la mise à jour') est présent et que le contenu original ('Avant la mise à jour') est absent, vérifiant que le contenu de la tâche a été mis à jour correctement.

---

Ces tests visent à couvrir les opérations CRUD de base dans une application Flask, en s'assurant que chaque partie de l'application se comporte comme prévu dans des conditions de test. Des ajustements peuvent être nécessaires en fonction des détails de mise en œuvre réels et du contenu HTML de votre application.