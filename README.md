# 🛰️ EPICS GPS/NTP/PTP Time Server for Raspberry Pi 3

This project configures a Raspberry Pi 3 as a Stratum-1 NTP server and software-timestamped PTP node using a Quectel L80-M39 GPS module on a Dragino LoRaWAN GPS HAT. It also deploys an EPICS P4P (pvAccess) Python server to expose GPS and timing health PVs.

## 📦 Features

- PPS via GPIO4 and NMEA via UART (/dev/serial0)
- gpsd + chrony for Stratum-1 NTP (PPS locked to NMEA)
- linuxptp (ptp4l) for IEEE-1588 PTP with software timestamping
- EPICS P4P server with minimal PV mode:
  - `TIMING:GPS:CONTACT` — True if GPS is producing usable fix + PPS
  - `TIMING:TIME:ACCURATE` — True if chrony is locked to satellite time
  - `TIMING:STATUS` — Synthesized status string (e.g., "OK", "NO_FIX")

## 🛠️ Setup

### 1. Inventory

Edit `inventory.ini` with your Pi's IP and SSH credentials.

```ini
[timing_pi]
192.168.42.42 ansible_user=pi ansible_port=22 ansible_ssh_private_key_file=~/.ssh/id_rsa

Make a roles based site.yml file to run your installation.
