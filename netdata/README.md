# helmcharts

A chart for Netdata. Depends on netdatas chart and adds ingress and backup secrets.

## Install

```bash
helm install netdata .\ --namespace netdata --create-namespace
```

## Upgrade

```bash
helm upgrade netdata .\ --namespace netdata
```

## Uninstall

```bash
helm uninstall netdata --namespace netdata
```

## Delete Namespace

```bash
kubectl delete namespace netdata
```