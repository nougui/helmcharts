# helmcharts

A chart for Librespeed. Depends on librespeed chart and adds ingress and backup secrets.

## Install

```bash
helm upgrade --install librespeed .\ --namespace librespeed --create-namespace
```

## Uninstall

```bash
helm uninstall librespeed --namespace librespeed
```
