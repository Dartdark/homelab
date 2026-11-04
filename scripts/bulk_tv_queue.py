import subprocess
import os
import urllib.request
import urllib.parse
import http.cookiejar
import json
import time
import sys

sys.stdout.reconfigure(line_buffering=True)

TARGET_SHOWS = [
    ("Drake & Josh (All Seasons)", ["Drake and Josh Complete", "Drake and Josh", "Drake & Josh"]),
    ("iCarly (All Seasons)", ["iCarly Complete", "iCarly Season 1", "iCarly"]),
    ("Victorious (All Seasons)", ["Victorious Complete", "Victorious Season", "Victorious"]),
    ("Adventure Time (All Seasons)", ["Adventure Time Complete", "Adventure Time Seasons 1", "Adventure Time"]),
    ("Regular Show (All Seasons)", ["Regular Show Complete", "Regular Show Seasons", "Regular Show"]),
    ("SpongeBob SquarePants (All Seasons)", ["SpongeBob SquarePants Complete", "SpongeBob Complete", "SpongeBob SquarePants"]),
    ("Avatar: The Last Airbender (Complete 2005)", ["Avatar The Last Airbender 2005 Complete", "Avatar The Last Airbender Complete", "Avatar The Last Airbender Seasons 1 to 3"]),
    ("South Park (All Seasons)", ["South Park Complete", "South Park Season 1", "South Park"]),
    ("Invincible (All Seasons)", ["Invincible Complete", "Invincible S01 S02", "Invincible 2021 Complete"]),
    ("Money Heist / La Casa de Papel (Complete)", ["Money Heist Complete", "La Casa de Papel Complete", "Money Heist"]),
    ("Sherlock (Complete BBC)", ["Sherlock Complete", "Sherlock BBC Complete", "Sherlock Seasons 1-4"]),
    ("House M.D. (Complete 8 Seasons)", ["House MD Complete", "House M.D. Complete", "House Complete Series"])
]

def search_nova2(query):
    # Check if running inside container or on host
    if os.path.exists('/config/qBittorrent/nova3/nova2.py'):
        cmd = ['python3', '/config/qBittorrent/nova3/nova2.py', 'piratebay', 'all', query]
    else:
        cmd = ['docker', 'exec', 'qbittorrent', 'python3', '/config/qBittorrent/nova3/nova2.py', 'piratebay', 'all', query]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore', timeout=25)
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
                if seeds < 1:
                    continue
                nl = name.lower()
                # filter out low quality or non-video
                if 'sample' in nl or 'trailer' in nl:
                    continue
                score = seeds
                if 'complete' in nl:
                    score += 1000
                if 'season' in nl or 's01' in nl:
                    score += 400
                if '1080p' in nl:
                    score += 800
                elif '720p' in nl:
                    score += 500
                if 'bluray' in nl or 'web-dl' in nl or 'webrip' in nl:
                    score += 300
                candidates.append((score, seeds, size_gb, name, parts[0]))
        candidates.sort(key=lambda x: x[0], reverse=True)
        return candidates
    except Exception as e:
        print(f"Error executing nova2 for {query}: {e}")
        return []

def add_to_qbittorrent(magnet, category="shows", savepath="/shows"):
    url = "http://localhost:8080/api/v2/torrents/add"
    data = urllib.parse.urlencode({
        "urls": magnet,
        "category": category,
        "savepath": savepath
    }).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status == 200 or resp.read().decode("utf-8") == "Ok."
    except Exception as e:
        print(f"Error adding torrent: {e}")
        return False

def get_existing_torrents():
    url = "http://localhost:8080/api/v2/torrents/info"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return [t.get("name", "").lower() for t in data]
    except Exception as e:
        print(f"Error checking torrents: {e}")
        return []

def main():
    print("==================================================")
    print("      HOMELAB BULK TV SHOW DOWNLOAD QUEUE         ")
    print("==================================================")
    existing = get_existing_torrents()
    print(f"Currently active/existing torrents in client: {len(existing)}")
    
    queued_count = 0
    skipped_count = 0
    
    for display_name, queries in TARGET_SHOWS:
        print(f"\nSearching for: {display_name}...")
        
        # Check if already present
        clean_name = display_name.split('(')[0].strip().lower()
        already_have = any(clean_name in t for t in existing)
        if already_have:
            print(f"  ? Already queued or downloaded! Skipping.")
            skipped_count += 1
            continue
            
        found = False
        for q in queries:
            results = search_nova2(q)
            if results:
                # pick top result
                score, seeds, size_gb, name, magnet = results[0]
                print(f"  ? Found match via '{q}':")
                print(f"     Title: {name}")
                print(f"     Seeds: {seeds} | Size: {size_gb} GB | Score: {score}")
                
                success = add_to_qbittorrent(magnet, category="shows", savepath="/shows")
                if success:
                    print("     ?? Successfully added to /shows download queue!")
                    queued_count += 1
                    found = True
                    break
                else:
                    print("     ? Failed to add to qBittorrent.")
            else:
                time.sleep(1)
                
        if not found:
            print(f"  ⚠️ No healthy torrents with seeds found on first pass for {display_name}.")
            
    print("\n==================================================")
    print(f"SUMMARY: {queued_count} new shows queued | {skipped_count} already active.")
    print("==================================================")

if __name__ == "__main__":
    main()
