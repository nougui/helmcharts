# helmcharts

A chart for Smokeping. Depends on smokeping chart and adds ingress and backup secrets.

## Install

```bash
helm install smokeping .\ --namespace smokeping --create-namespace
```

## Upgrade

```bash
helm upgrade smokeping .\ --namespace smokeping
```

## Uninstall

```bash
helm uninstall smokeping --namespace smokeping
```

## Delete Namespace

```bash
kubectl delete namespace smokeping
```