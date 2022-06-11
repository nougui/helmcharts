# crypto port coingecko

A sub chart of Crypto Portfolio application. Corresponds to coingecko system.

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