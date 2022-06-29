# helmcharts

A chart for Wikijs. Depends on wikijs chart and adds ingress and backup secrets.

## Install

```bash
helm install wikijs .\ --namespace wikijs --create-namespace
```

## Upgrade

```bash
helm upgrade wikijs .\ --namespace wikijs
```

## Uninstall

```bash
helm uninstall wikijs --namespace wikijs
```

## Delete Namespace

```bash
kubectl delete namespace wikijs
```