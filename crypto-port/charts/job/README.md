# crypto port job

A sub chart of Crypto Portfolio application. Corresponds to job system.

## Install

```bash
helm install crypto-port .\ --namespace crypto-port --create-namespace
```

## Upgrade

```bash
helm upgrade crypto-port .\ --namespace crypto-port
```

## Uninstall

```bash
helm uninstall crypto-port --namespace crypto-port
```

## Delete Namespace

```bash
kubectl delete namespace crypto-port
```