# helmcharts

A chart for Longhorn. Depends on longhorns chart and adds ingress and backup secrets.

## Install

```bash
helm upgrade --install longhorn .\ --namespace longhorn-system --create-namespace
```

## Uninstall

```bash
helm uninstall longhorn --namespace longhorn-system
```
