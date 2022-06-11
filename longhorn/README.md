# helmcharts

A chart for Longhorn. Depends on longhorns chart and adds ingress and backup secrets.

## Install

```bash
helm install longhorn .\ --namespace longhorn-system --create-namespace
```

## Upgrade

```bash
helm upgrade longhorn .\ --namespace longhorn-system
```

## Uninstall

```bash
helm uninstall longhorn --namespace longhorn-system
```

## Delete Namespace

```bash
kubectl delete namespace longhorn
```