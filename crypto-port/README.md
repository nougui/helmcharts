# helmcharts

Install

```bash
helm --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" install crypto-port .\ --namespace crypto-port --create-namespace
```

Upgrade

```bash
helm --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" upgrade crypto-port .\ --namespace crypto-port
```

Uninstall

```bash
helm --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" uninstall crypto-port --namespace crypto-port
```

Delete Namespace

```bash
kubectl --kubeconfig "C:\coding\secret\kubeconfigs\oracle-cluster-config" delete namespace crypto-port
```