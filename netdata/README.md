# helmcharts

A chart for Netdata. Depends on netdatas chart and adds ingress and backup secrets.

## Install

```bash
helm upgrade --install netdata .\ --namespace netdata --create-namespace
```

## Uninstall

```bash
helm uninstall netdata --namespace netdata
```
