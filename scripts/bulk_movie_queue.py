import subprocess
import urllib.request
import urllib.parse
import http.cookiejar
import json
import time
import sys

sys.stdout.reconfigure(line_buffering=True)

# List of all requested movies with primary and fallback search queries
TARGET_MOVIES = [
    ("Aladdin (2019) [Will Smith Live Action]", ["Aladdin 2019", "Aladdin 2019 1080p"]),
    ("Obsessed (2009) [Beyonce]", ["Obsessed 2009", "Obsessed 2009 1080p"]),
    ("Coraline (2009)", ["Coraline 2009", "Coraline 1080p"]),
    ("The Nightmare Before Christmas (1993)", ["Nightmare Before Christmas", "Nightmare Before Christmas 1993"]),
    
    # Spider-Man Trilogy (Sam Raimi)
    ("Spider-Man (2002) [Raimi]", ["Spider-Man 2002", "Spider-Man 2002 1080p"]),
    ("Spider-Man 2 (2004) [Raimi]", ["Spider-Man 2 2004", "Spider-Man 2 2004 1080p"]),
    ("Spider-Man 3 (2007) [Raimi]", ["Spider-Man 3 2007", "Spider-Man 3 2007 1080p"]),
    
    # The Amazing Spider-Man (Andrew Garfield)
    ("The Amazing Spider-Man (2012) [Garfield]", ["Amazing Spider-Man 2012", "The Amazing Spider-Man 2012"]),
    ("The Amazing Spider-Man 2 (2014) [Garfield]", ["Amazing Spider-Man 2 2014", "The Amazing Spider-Man 2 2014"]),
    
    # Spider-Man (Tom Holland)
    ("Spider-Man: Homecoming (2017) [Holland]", ["Spider-Man Homecoming 2017", "Homecoming 2017 1080p"]),
    ("Spider-Man: Far From Home (2019) [Holland]", ["Spider-Man Far From Home 2019", "Far From Home 2019 1080p"]),
    ("Spider-Man: No Way Home (2021) [Holland]", ["Spider-Man No Way Home 2021", "No Way Home 2021 1080p"]),
    ("Captain America: Civil War (2016) [Holland Debut]", ["Captain America Civil War 2016", "Civil War 2016 1080p"]),
    
    # Dune 1 & 2
    ("Dune: Part One (2021)", ["Dune 2021", "Dune 2021 1080p"]),
    ("Dune: Part Two (2024)", ["Dune Part Two 2024", "Dune 2 2024 1080p"]),
    
    # Michael
    ("Michael (1996) [Travolta]", ["Michael 1996", "Michael 1996 1080p"]),
    
    # Top Gun & Top Gun Maverick
    ("Top Gun (1986)", ["Top Gun 1986", "Top Gun 1986 1080p"]),
    ("Top Gun: Maverick (2022)", ["Top Gun Maverick 2022", "Top Gun Maverick 1080p"]),
    
    # Avengers
    ("The Avengers (2012)", ["The Avengers 2012", "Avengers 2012 1080p"]),
    ("Avengers: Age of Ultron (2015)", ["Avengers Age of Ultron 2015", "Age of Ultron 2015 1080p"]),
    ("Avengers: Infinity War (2018)", ["Avengers Infinity War 2018", "Infinity War 2018 1080p"]),
    ("Avengers: Endgame (2019)", ["Avengers Endgame 2019", "Endgame 2019 1080p"]),
    
    # Rocky 1-5
    ("Rocky (1976)", ["Rocky 1976", "Rocky 1976 1080p"]),
    ("Rocky II (1979)", ["Rocky II 1979", "Rocky 2 1979 1080p"]),
    ("Rocky III (1982)", ["Rocky III 1982", "Rocky 3 1982 1080p"]),
    ("Rocky IV (1985)", ["Rocky IV 1985", "Rocky 4 1985 1080p"]),
    ("Rocky V (1990)", ["Rocky V 1990", "Rocky 5 1990 1080p"]),
    
    # Deadpool & Wolverine
    ("Deadpool & Wolverine (2024)", ["Deadpool Wolverine 2024", "Deadpool and Wolverine 2024"]),
    
    # John Wick 1-4
    ("John Wick (2014)", ["John Wick 2014", "John Wick 2014 1080p"]),
    ("John Wick: Chapter 2 (2017)", ["John Wick Chapter 2 2017", "John Wick 2 2017"]),
    ("John Wick: Chapter 3 - Parabellum (2019)", ["John Wick Chapter 3 2019", "John Wick 3 2019"]),
    ("John Wick: Chapter 4 (2023)", ["John Wick Chapter 4 2023", "John Wick 4 2023"]),
    
    # Guardians of the Galaxy 1-3
    ("Guardians of the Galaxy (2014)", ["Guardians of the Galaxy 2014", "Guardians of the Galaxy 2014 1080p"]),
    ("Guardians of the Galaxy Vol. 2 (2017)", ["Guardians of the Galaxy Vol 2 2017", "Guardians of the Galaxy 2 2017"]),
    ("Guardians of the Galaxy Vol. 3 (2023)", ["Guardians of the Galaxy Vol 3 2023", "Guardians of the Galaxy 3 2023"]),
    
    # Fast & Furious Series
    ("The Fast and the Furious (2001)", ["Fast and the Furious 2001", "The Fast and the Furious 2001"]),
    ("2 Fast 2 Furious (2003)", ["2 Fast 2 Furious 2003", "2 Fast 2 Furious 1080p"]),
    ("The Fast and the Furious: Tokyo Drift (2006)", ["Tokyo Drift 2006", "Fast and Furious Tokyo Drift 2006"]),
    ("Fast & Furious (2009)", ["Fast & Furious 2009", "Fast and Furious 4 2009"]),
    ("Fast Five (2011)", ["Fast Five 2011", "Fast Five 2011 1080p"]),
    ("Fast & Furious 6 (2013)", ["Fast and Furious 6 2013", "Fast & Furious 6 2013"]),
    ("Furious 7 (2015)", ["Furious 7 2015", "Fast and Furious 7 2015"]),
    ("The Fate of the Furious (2017)", ["Fate of the Furious 2017", "Fast and Furious 8 2017"]),
    ("Fast & Furious Presents: Hobbs & Shaw (2019)", ["Hobbs and Shaw 2019", "Hobbs & Shaw 2019"]),
    ("F9: The Fast Saga (2021)", ["F9 The Fast Saga 2021", "Fast and Furious 9 2021"]),
    ("Fast X (2023)", ["Fast X 2023", "Fast and Furious 10 2023"]),
    
    # Bad Boys 1-4
    ("Bad Boys (1995)", ["Bad Boys 1995", "Bad Boys 1995 1080p"]),
    ("Bad Boys II (2003)", ["Bad Boys II 2003", "Bad Boys 2 2003"]),
    ("Bad Boys for Life (2020)", ["Bad Boys for Life 2020", "Bad Boys 3 2020"]),
    ("Bad Boys: Ride or Die (2024)", ["Bad Boys Ride or Die 2024", "Bad Boys 4 2024"]),
    
    # Disney / Family
    ("Moana (2016)", ["Moana 2016", "Moana 2016 1080p"]),
    ("Monsters, Inc. (2001)", ["Monsters Inc 2001", "Monsters Inc 2001 1080p"]),
    ("Willy Wonka & the Chocolate Factory (1971) [Gene Wilder]", ["Willy Wonka Chocolate Factory 1971", "Willy Wonka 1971 1080p"]),
    ("Finding Nemo (2003)", ["Finding Nemo 2003", "Finding Nemo 2003 1080p"]),
    
    # Equalizer 1-3
    ("The Equalizer (2014)", ["The Equalizer 2014", "Equalizer 2014 1080p"]),
    ("The Equalizer 2 (2018)", ["The Equalizer 2 2018", "Equalizer 2 2018 1080p"]),
    ("The Equalizer 3 (2023)", ["The Equalizer 3 2023", "Equalizer 3 2023 1080p"])
]

def search_nova2(query):
    cmd = ['docker', 'exec', 'qbittorrent', 'python3', '/config/qBittorrent/nova3/nova2.py', 'piratebay', 'all', query]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore', timeout=20)
        candidates = []
        for line in res.stdout.splitlines():
            parts = line.strip().split('|')
            if len(parts) >= 4 and parts[0].startswith('magnet:'):
                name = urllib.parse.unquote(parts[1])
                try:
                    size_gb = round(int(parts[2]) / (1024**3), 2)
                    seeds = int(parts[3])
                except:
                    continue
                if seeds < 5:
                    continue
                nl = name.lower()
                # filter out low quality cams/screeners
                if 'camrip' in nl or 'telesync' in nl or 'hdts' in nl or 'hdcam' in nl:
                    continue
                # scoring
                score = seeds
                if '1080p' in nl:
                    score += 1500
                elif '720p' in nl:
                    score += 500
                if 'bluray' in nl or 'bdrip' in nl:
                    score += 600
                elif 'web-dl' in nl or 'webrip' in nl:
                    score += 400
                if size_gb > 20:
                    score -= 800  # prioritize fast downloading ~1.5 to 8 GB releases
                elif size_gb < 0.6:
                    score -= 500  # avoid low-bitrate rips
                candidates.append((score, seeds, size_gb, name, parts[0]))
        candidates.sort(key=lambda x: x[0], reverse=True)
        return candidates
    except Exception as e:
        print(f"Error executing nova2 for {query}: {e}")
        return []

def add_torrent(opener, magnet):
    add_url = 'http://localhost:8080/api/v2/torrents/add'
    form_data = urllib.parse.urlencode({
        'urls': magnet,
        'savepath': '/movies',
        'category': 'movies',
        'paused': 'false'
    }).encode()
    req = urllib.request.Request(add_url, data=form_data, headers={'Referer': 'http://localhost:8080'})
    try:
        with opener.open(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            return data.get('success_count', 0) > 0 or len(data.get('added_torrent_ids', [])) > 0
    except Exception as e:
        return False

def get_existing_torrents(opener):
    try:
        with opener.open('http://localhost:8080/api/v2/torrents/info') as resp:
            torrents = json.loads(resp.read().decode())
            return [t['name'].lower() for t in torrents]
    except:
        return []

def main():
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    login_url = 'http://localhost:8080/api/v2/auth/login'
    data = urllib.parse.urlencode({'username': 'admin', 'password': 'sUIvWnHGx'}).encode()
    opener.open(urllib.request.Request(login_url, data=data, headers={'Referer': 'http://localhost:8080'}))
    print("Logged into qBittorrent WebAPI successfully.")

    existing_names = get_existing_torrents(opener)
    print(f"Current torrents in qBittorrent: {len(existing_names)}")

    success_count = 0
    results_summary = []

    print(f"\nProcessing {len(TARGET_MOVIES)} requested movie titles...\n")

    for display_title, queries in TARGET_MOVIES:
        print(f"==> Searching: {display_title}...")
        found = False
        for q in queries:
            candidates = search_nova2(q)
            if candidates:
                best = candidates[0]
                # Check if already in client
                magnet = best[4]
                name = best[3]
                size_gb = best[2]
                seeds = best[1]
                
                added = add_torrent(opener, magnet)
                if added:
                    print(f"    [QUEUED] {name} ({size_gb} GB | {seeds} seeds)")
                    results_summary.append((display_title, name, size_gb, seeds, "QUEUED"))
                    success_count += 1
                else:
                    print(f"    [ALREADY ACTIVE OR FAILED] {name}")
                    results_summary.append((display_title, name, size_gb, seeds, "ALREADY ACTIVE"))
                found = True
                break
            time.sleep(0.5)
            
        if not found:
            print(f"    [NOT FOUND] No high-speed release found for: {display_title}")
            results_summary.append((display_title, "N/A", 0, 0, "NOT FOUND"))

    print("\n" + "="*70)
    print(f"SUMMARY: Successfully queued {success_count} / {len(TARGET_MOVIES)} movies into qBittorrent (/movies)")
    print("="*70)

if __name__ == '__main__':
    main()
