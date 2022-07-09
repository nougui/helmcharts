# helmcharts

A chart for Adguard. Depends on adguard chart and adds ingress and backup secrets.

## Install

```bash
helm upgrade --install adguard .\ --namespace adguard --create-namespace
```

## Uninstall

```bash
helm uninstall adguard --namespace adguard
```
