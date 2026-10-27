import sys
import time
import statistics
import requests

port = sys.argv[1] if len(sys.argv) > 1 else '8100'
URL = f'http://127.0.0.1:{port}/invocations'

CORPS = {'dataframe_records': [{'montant': 8500.0, 'anciennete': 3,
                                 'freq_24h': 9, 'nuit': 1}]}

# 1. Test initial
try:
    r = requests.post(URL, json=CORPS, timeout=10)
    print('reponse initiale :', r.status_code, r.json())
except Exception as e:
    print(f"Erreur lors de la requête initiale : {e}")
    sys.exit(1)

# 2. Échauffement (Warm-up)
print("Échauffement en cours...")
for _ in range(10):
    try:
        requests.post(URL, json=CORPS, timeout=10)
    except Exception:
        pass

# 3. Mesure de la latence (200 appels)
print("Mesure des 200 appels...")
lat = []
success_count = 0
start_total = time.perf_counter()

for _ in range(200):
    t = time.perf_counter()
    try:
        r = requests.post(URL, json=CORPS, timeout=10)
        if r.status_code == 200:
            success_count += 1
            lat.append((time.perf_counter() - t) * 1000)
    except requests.exceptions.RequestException:
        pass

end_total = time.perf_counter()
total_time = end_total - start_total

# 4. Affichage des résultats
if lat:
    throughput = success_count / total_time
    print(f'\n--- Résultats pour le port {port} ---')
    print(f'Succès : {success_count}/200 requêtes')
    print(f'Médiane : {statistics.median(lat):.1f} ms')
    print(f'P95     : {statistics.quantiles(lat, n=20)[18]:.1f} ms')
    print(f'Débit   : {throughput:.1f} req/sec')
else:
    print("Aucune requête n'a pu aboutir.")
