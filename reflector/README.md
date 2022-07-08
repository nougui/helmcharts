# helmcharts

A chart for Reflector. Depends on reflectors chart and adds ingress and backup secrets.

## Install

```bash
helm install reflector .\ --namespace reflector --create-namespace
```

## Upgrade

```bash
helm upgrade reflector .\ --namespace reflector
```

## Uninstall

```bash
helm uninstall reflector --namespace reflector
```

## Delete Namespace

```bash
kubectl delete namespace reflector
```