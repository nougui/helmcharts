# helmcharts

A chart for Kubernetes Dashboard. Admin user is created by chart.

## Install

```bash
helm install kubernetes-dashboard ".\"
```

## Upgrade

```bash
helm upgrade kubernetes-dashboard ".\"
```

## Uninstall

```bash
helm uninstall kubernetes-dashboard
```

## Delete Namespace

```bash
kubectl delete namespace kubernetes-dashboard
```