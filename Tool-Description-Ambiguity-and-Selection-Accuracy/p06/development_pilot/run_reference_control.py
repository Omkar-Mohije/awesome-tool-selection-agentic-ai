"""Download hash-locked upstream sources and run CPU controls. Standard library only."""
import argparse
import hashlib
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache', type=Path, default=Path('/tmp/p06_reference_sources'))
    parser.add_argument('--output', type=Path, default=Path('reference_replay_results.json'))
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    lock = json.loads((here/'reference_control/source_lock.json').read_text())
    for relative, expected in lock['source_sha256'].items():
        dest = args.cache/relative
        if dest.exists() and hashlib.sha256(dest.read_bytes()).hexdigest() == expected:
            continue
        url = ('https://raw.githubusercontent.com/ShishirPatil/gorilla/'
               + lock['upstream_commit'] + '/berkeley-function-call-leaderboard/' + relative)
        with urllib.request.urlopen(url, timeout=60) as response:
            content = response.read()
        assert hashlib.sha256(content).hexdigest() == expected, relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(content)
    subprocess.run([sys.executable, str(here/'reference_replay.py'),
                    '--source-root', str(args.cache), '--output', str(args.output)], check=True)

if __name__ == '__main__':
    main()
