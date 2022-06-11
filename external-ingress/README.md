# helmcharts

A chart for External Ingress. Useful for reverse proxying outside resources.

## Install

```bash
helm install external-ingress .\ --namespace external-ingress --create-namespace
```

## Upgrade

```bash
helm upgrade external-ingress .\ --namespace external-ingress      
```

## Uninstall

```bash
helm uninstall external-ingress --namespace external-ingress
```

## Delete Namespace

```bash
kubectl delete namespace external-ingress
```