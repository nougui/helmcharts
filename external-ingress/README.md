# helmcharts

A chart for External Ingress. Useful for reverse proxying outside resources.

## Install

```bash
helm upgrade --install external-ingress .\ --namespace external-ingress --create-namespace
```

## Uninstall

```bash
helm uninstall external-ingress --namespace external-ingress
```
