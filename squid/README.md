# helmcharts

Install

```bash
helm --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" install squid .\ --namespace squid --create-namespace
```

Upgrade

```bash
helm --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" upgrade squid .\ --namespace squid
```

Uninstall

```bash
helm --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" uninstall squid --namespace squid
```

Delete Namespace

```bash
kubectl --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" delete namespace squid
```