# helmcharts

A chart for Squid. A Proxy server.

## Install

```bash
helm install squid .\ --namespace squid --create-namespace
```

## Upgrade

```bash
helm upgrade squid .\ --namespace squid
```

## Uninstall

```bash
helm uninstall squid --namespace squid
```

## Delete Namespace

```bash
kubectl delete namespace squid
```