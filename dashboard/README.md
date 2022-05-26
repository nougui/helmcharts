# helmcharts

Install

```bash
helm --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" install kubernetes-dashboard ".\"
```

Upgrade

```bash
helm --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" upgrade kubernetes-dashboard ".\"
```

Uninstall

```bash
helm --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" uninstall kubernetes-dashboard
```

Delete Namespace

```bash
kubectl --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" delete namespace kubernetes-dashboard
```