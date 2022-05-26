# helmcharts

Install

```bash
helm --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" install vaultwarden .\ --namespace vaultwarden --create-namespace
```

Upgrade

```bash
helm --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" upgrade vaultwarden .\ --namespace vaultwarden      
```

Uninstall

```bash
helm --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" uninstall vaultwarden --namespace vaultwarden
```

Delete Namespace

```bash
kubectl --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" delete namespace vaultwarden
```