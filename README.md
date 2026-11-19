# Oracle VM network status demo

This Flask app renders `templates/index.html` and runs Cisco IOS status
commands through Netmiko. Router credentials are read from environment
variables; do not put passwords in Python files or commit them to GitHub.

## Install

Run these commands in the project folder. If you already created `venv` with
`python -m venv venv`, skip the creation command and activate it.

### Windows PowerShell

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Linux in the Oracle VM

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

## Configure and run

Set these variables in the same terminal that will run the app. Use the
reachable router address and credentials from your lab instructions.

### Windows PowerShell

```powershell
$env:NET_HOST = "192.168.10.37"
$env:NET_PORT = "32770"
$env:NET_SECRET = "your-enable-secret"
$env:APP_HOST = "127.0.0.1"
python api.py
```

### Linux in the Oracle VM

```bash
export NET_HOST="192.168.10.37"
export NET_PORT="32770"
export NET_SECRET="your-enable-secret"
export APP_HOST="0.0.0.0"
python api.py
```

Open `http://127.0.0.1:5000` in Chrome when running on the same computer. When
running inside the VM, open `http://<VM-IP>:5000` from the host computer. Find
the VM address with `ip address` on Linux. The VM's network mode must allow the
host to reach it, and TCP port 5000 must be allowed by the VM firewall. Keep the
demo on a trusted host-only lab network; do not expose Flask's development
server to the public internet.

The page runs `show version`, `show ip interface brief`, and `show running-config`.
The configuration output may contain sensitive information; keep the app on a
trusted lab network and do not publish captured router output or credentials.
The starter follows the existing script's Telnet connection type; Telnet sends
credentials without encryption, so use it only on an isolated lab network. If
your lab router supports SSH, use its assigned SSH device type instead.
The EVE-NG Telnet port connects directly to the router console, so it does not
use `NET_USER` or `NET_PASS`. Set `NET_SECRET` to the router's enable secret.

## GitHub and screenshot

Before publishing, confirm `.env` and virtual-environment folders are not
included in the GitHub upload. Run the app, open the page in Chrome, click
**Connect to router**, then take a screenshot of the rendered page for the
assignment.
