# helmcharts

A chart for Adguard. Depends on adguard chart and adds ingress and backup secrets.

## Install

```bash
helm install adguard .\ --namespace adguard --create-namespace
```

## Upgrade

```bash
helm upgrade adguard .\ --namespace adguard
```

## Uninstall

```bash
helm uninstall adguard --namespace adguard
```

## Delete Namespace

```bash
kubectl delete namespace adguard
```