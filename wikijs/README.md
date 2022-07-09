# helmcharts

A chart for Wikijs. Depends on wikijs chart and adds ingress and backup secrets.

## Install

```bash
helm upgrade --install wikijs .\ --namespace wikijs --create-namespace
```

## Uninstall

```bash
helm uninstall wikijs --namespace wikijs
```
