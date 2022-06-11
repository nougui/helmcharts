# helmcharts

A chart for Paperless ngx. The document management system.

## Install

```bash
helm install paperless .\ --namespace paperless --create-namespace
```

## Upgrade

```bash
helm upgrade paperless .\ --namespace paperless      
```

## Uninstall

```bash
helm uninstall paperless --namespace paperless
```

## Delete Namespace

```bash
kubectl delete namespace paperless
```