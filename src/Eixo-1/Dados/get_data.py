import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import threading

API_KEY = "88793d5aa9f58ed4781762c6b39e633a"
BASE_URL = "https://api.themoviedb.org/3"

# Usamos uma Session global para reaproveitar conexões
session = requests.Session()

def get_movie_details(movie_id):
    """Busca detalhes de um único filme."""
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": API_KEY, "language": "pt-BR"}
    try:
        resp = session.get(url, params=params, timeout=10)
        if resp.status_code == 200:
            details = resp.json()
            return {
                "title": details.get("title"),
                "release_date": details.get("release_date"),
                "vote_average": details.get("vote_average"),
                "budget": details.get("budget"),
                "vote_count": details.get( 'vote_count' ),
                "revenue": details.get("revenue"),
                "runtime": details.get("runtime"),
                "production_country": ", ".join([c['name'] for c in details.get('production_countries', [])]),
                "genres": ", ".join([g['name'] for g in details.get('genres', [])]),
            }
    except Exception as e:
        print(f"Erro no ID {movie_id}: {e}")
    return None

def get_movie_data(start_year, end_year):
    all_movies = []
    
    for year in range(start_year, end_year + 1):
        print(f"Buscando ano: {year}...")
        page = 1
        
        while page <= 50: # TMDB limita discover a 500 páginas, mas você usou 50
            discover_url = f"{BASE_URL}/discover/movie"
            params = {
                "api_key": API_KEY,
                "primary_release_year": year,
                "page": page,
                "sort_by": "popularity.desc"
            }
            
            response = session.get(discover_url, params=params)
            data = response.json()
            results = data.get("results", [])
            
            if not results:
                break

            # Extraímos os IDs dos filmes da página atual
            movie_ids = [m.get("id") for m in results]

            # --- A MÁGICA ACONTECE AQUI ---
            # Disparamos até 20 requisições simultâneas para pegar os detalhes
            with ThreadPoolExecutor(max_workers=20) as executor:
                details_list = list(executor.map(get_movie_details, movie_ids))
            
            # Filtramos resultados nulos e adicionamos o ano
            for detail in details_list:
                if detail:
                    detail["release_year"] = year
                    all_movies.append(detail)

            if page >= data.get("total_pages", 1):
                break
            page += 1

    return all_movies

# Execução
lista_filmes = get_movie_data(1950, 2025)
df = pd.DataFrame(lista_filmes)
df.to_csv("filmes_tmdb_veloz.csv", index=False, encoding='utf-8-sig')
print(f"Concluído! {len(df)} filmes salvos.")
