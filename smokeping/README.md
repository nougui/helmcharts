# helmcharts

A chart for Smokeping. Depends on smokeping chart and adds ingress and backup secrets.

## Install

```bash
helm upgrade --install smokeping .\ --namespace smokeping --create-namespace
```

## Uninstall

```bash
helm uninstall smokeping --namespace smokeping
```
