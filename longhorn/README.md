# helmcharts

Install

```bash
helm --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" install longhorn .\ --namespace longhorn-system --create-namespace
```

Upgrade

```bash
helm --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" upgrade longhorn .\ --namespace longhorn-system
```

Uninstall

```bash
helm --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" uninstall longhorn --namespace longhorn-system
```

Delete Namespace

```bash
kubectl --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" delete namespace longhorn
```