# helmcharts

A chart for Vaultwarden. Password Manager.

## Install

```bash
helm install vaultwarden .\ --namespace vaultwarden --create-namespace
```

## Upgrade

```bash
helm upgrade vaultwarden .\ --namespace vaultwarden      
```

## Uninstall

```bash
helm uninstall vaultwarden --namespace vaultwarden
```

## Delete Namespace

```bash
kubectl delete namespace vaultwarden
```