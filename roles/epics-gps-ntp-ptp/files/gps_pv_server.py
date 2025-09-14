#!/usr/bin/env python3
import json
import time
from p4p.server import Server, StaticProvider
from p4p.nt import NTScalar

CONFIG_PATH = '/etc/epics-p4p/config.json'
AUTOSAVE_PATH = '/var/lib/epics-p4p/autosave.json'

def load_config():
    config = {}
    try:
        with open(CONFIG_PATH, 'r') as f:
            config = json.load(f)
        if os.path.exists(AUTOSAVE_PATH):
            with open(AUTOSAVE_PATH, 'r') as f:
                config.update(json.load(f))
    except Exception:
        pass
    return config

def main():
    config = load_config()
    prefix = config.get("pv_prefix", "CLF-TIMING")
    minimal = config.get("minimal_pvs", True)

    provider = StaticProvider("")
    server = Server(providers=[provider])

    if minimal:
        provider.add(f"{prefix}:GPS:CONTACT", NTScalar('b').wrap({'value': False}))
        provider.add(f"{prefix}:TIME:ACCURATE", NTScalar('b').wrap({'value': False}))
        provider.add(f"{prefix}:STATUS", NTScalar('s').wrap({'value': "UNKNOWN"}))

    try:
        while True:
            # Simulated logic — replace with real checks
            contact = True
            accurate = True
            status = "OK" if contact and accurate else "NO_LOCK" if contact else "NO_GPS"

            provider.update(f"{prefix}:GPS:CONTACT", {'value': contact})
            provider.update(f"{prefix}:TIME:ACCURATE", {'value': accurate})
            provider.update(f"{prefix}:STATUS", {'value': status})

            time.sleep(config.get("publish_period_s", 1.0))
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()

