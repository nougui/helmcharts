# helmcharts

A chart for Librespeed. Depends on librespeed chart and adds ingress and backup secrets.

## Install

```bash
helm install librespeed .\ --namespace librespeed --create-namespace
```

## Upgrade

```bash
helm upgrade librespeed .\ --namespace librespeed
```

## Uninstall

```bash
helm uninstall librespeed --namespace librespeed
```

## Delete Namespace

```bash
kubectl delete namespace librespeed
```