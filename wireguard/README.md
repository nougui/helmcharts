# helmcharts

A chart for Wireguard. Wireguard Vpn with a dashboard.

## Install

```bash
helm install wireguard .\ --namespace wireguard --create-namespace
```

## Upgrade

```bash
helm upgrade wireguard .\ --namespace wireguard      
```

## Uninstall

```bash
helm uninstall wireguard --namespace wireguard
```

## Delete Namespace

```bash
kubectl delete namespace wireguard
```