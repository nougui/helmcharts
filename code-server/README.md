# helmcharts

A chart for Code-server. Password Manager.

## Install

```bash
helm install code-server .\ --namespace code-server --create-namespace
```

## Upgrade

```bash
helm upgrade code-server .\ --namespace code-server      
```

## Uninstall

```bash
helm uninstall code-server --namespace code-server
```

## Delete Namespace

```bash
kubectl delete namespace code-server
```