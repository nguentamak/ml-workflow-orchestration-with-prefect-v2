# ml-workflow-orchestration-with-prefect-v2

Solution Complète
Démarrer le serveur Prefect (dans un terminal séparé)

powershell
Copy
prefect server start
Laissez ce terminal ouvert - le serveur doit rester actif.

Vérifier que le serveur est accessible

powershell
Copy
curl http://127.0.0.1:4200/api/health
➔ Doit retourner {"status":"OK"}

Configurer l'URL de l'API (dans le terminal où vous exécutez votre script)

powershell
Copy
$env:PREFECT_API_URL="http://127.0.0.1:4200/api"
Exécuter à nouveau votre script

powershell
Copy
python .\main.py