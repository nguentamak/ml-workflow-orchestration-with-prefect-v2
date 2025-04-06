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


Processus complet pour déployer un flow
Démarrer le serveur Prefect (si ce n'est pas déjà fait) :

bash
Copy
prefect server start
Créer un work pool (si nécessaire) :

bash
Copy
prefect work-pool create "default-agent-pool" --type process
Démarrer un worker :

bash
Copy
prefect worker start -p default-agent-pool
Déployer votre flow (comme dans votre exemple initial) :

python
Copy
flow.from_source(
    source="https://github.com/nguentamak/ml-workflow-orchestration-with-prefect-v2.git",
    entrypoint="main.py:ml_workflow",
).deploy(
    name="ml_workflow_bank_churn",
    work_pool_name="default-agent-pool",
    schedule={"cron": "0 * * * *"},  # Toutes les heures
