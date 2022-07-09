# helmcharts

A chart for Reflector. Depends on reflectors chart and adds ingress and backup secrets.

## Install

```bash
helm upgrade --install reflector .\ --namespace reflector --create-namespace
```

## Uninstall

```bash
helm uninstall reflector --namespace reflector
```
