# helmcharts

A chart for Wireguard. Wireguard Vpn with a dashboard.

## Install

```bash
helm upgrade --install wireguard .\ --namespace wireguard --create-namespace
```

## Uninstall

```bash
helm uninstall wireguard --namespace wireguard
```
